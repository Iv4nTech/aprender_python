"""
================================================================================
 THREADING EN PYTHON
 Ejecutar: python3 introduccion.py
================================================================================
"""

import threading
import time


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA: I/O BLOQUEANTE EN SERIE
# ============================================================================
seccion("1. El problema: I/O bloqueante en serie")

# Caso real: una herramienta de monitorización tiene que comprobar el estado
# de 5 servicios (peticiones de red). Simulamos cada petición con sleep().
urls_a_monitorizar = [
    "api.pagos.com",
    "api.usuarios.com",
    "api.inventario.com",
    "api.envios.com",
    "api.notificaciones.com",
]


def comprobar_servicio(url: str, latencia: float) -> None:
    time.sleep(latencia)
    print(f"  [{url}] respondió en {latencia:.1f}s")


inicio = time.perf_counter()
for url in urls_a_monitorizar:
    comprobar_servicio(url, 0.3)
duracion_serie = time.perf_counter() - inicio
print(f"  Total en serie: {duracion_serie:.2f}s")

# El problema: cada comprobación espera a que termine la anterior aunque
# ninguna dependa de la otra. Con 5 servicios de 0.3s cada uno, la herramienta
# tarda 1.5s en dar un solo vistazo al sistema. Con 50 servicios reales,
# serían 15s de nada más que esperar red, uno detrás de otro.


# ============================================================================
# 2. LA SOLUCIÓN: Thread BÁSICO
# ============================================================================
seccion("2. La solución: Thread básico")

hilos = [
    threading.Thread(target=comprobar_servicio, args=(url, 0.3))
    for url in urls_a_monitorizar
]

inicio = time.perf_counter()
for hilo in hilos:
    hilo.start()
for hilo in hilos:
    hilo.join()
duracion_paralelo = time.perf_counter() - inicio
print(f"  Total en paralelo: {duracion_paralelo:.2f}s (antes {duracion_serie:.2f}s)")

# start() lanza el hilo y sigue ejecutando el bucle sin esperar a que acabe.
# join() sí bloquea hasta que ese hilo concreto termine. Al arrancar los 5
# hilos primero y hacer join() después, el tiempo total pasa a ser el de la
# tarea MÁS LENTA, no la suma de todas. El orden en que se imprime cada línea
# arriba no está garantizado: depende de qué hilo termine antes, no del
# orden en que se lanzaron.


# ============================================================================
# 3. HILO COMO SUBCLASE
# ============================================================================
seccion("3. Hilo como subclase")

# Cuándo tiene sentido: cuando el hilo necesita guardar SU PROPIO estado
# (contadores, resultados acumulados) en vez de solo ejecutar una función
# suelta. Caso real: un monitor de logs que necesita recordar cuántos
# errores ha visto para decidir si dispara una alerta.
class MonitorDeLogs(threading.Thread):
    def __init__(self, nombre_fichero: str, lineas: list[str]) -> None:
        super().__init__()
        self.nombre_fichero = nombre_fichero
        self.lineas = lineas
        self.errores_encontrados = 0

    def run(self) -> None:
        for linea in self.lineas:
            time.sleep(0.05)
            if "ERROR" in linea:
                self.errores_encontrados += 1


log_pagos = [
    "INFO pago procesado",
    "ERROR timeout con pasarela",
    "INFO pago procesado",
    "ERROR tarjeta rechazada",
]
monitor = MonitorDeLogs("pagos.log", log_pagos)
monitor.start()
monitor.join()
print(f"  '{monitor.nombre_fichero}': {monitor.errores_encontrados} errores encontrados")

# Solo se sobreescriben __init__ (para añadir estado propio, llamando
# siempre a super().__init__()) y run() (el código que ejecuta el hilo).
# Nunca se sobreescribe start() ni join(): son los que gestiona threading
# internamente para arrancar y esperar el hilo real del sistema operativo.


# ============================================================================
# 4. DAEMON THREADS
# ============================================================================
seccion("4. Daemon threads")

# Caso real: un hilo de heartbeat que manda un ping a un servidor cada
# poco tiempo mientras el programa principal hace su trabajo. Si ese hilo
# fuera normal, el programa nunca podría cerrarse porque el heartbeat no
# termina nunca por sí solo.
def heartbeat() -> None:
    contador = 0
    while True:
        contador += 1
        time.sleep(0.2)


hilo_heartbeat = threading.Thread(target=heartbeat, daemon=True)
hilo_heartbeat.start()
print(f"  hilo_heartbeat.daemon = {hilo_heartbeat.daemon}")
print("  Programa principal trabajando 0.5s...")
time.sleep(0.5)
print("  Programa principal termina; el heartbeat se corta con él, sin bloquear el cierre")

# Aviso importante: un daemon thread se mata en seco cuando el programa
# principal acaba, no se le da la oportunidad de terminar su iteración
# actual. Si ese hilo tuviera un fichero abierto o una transacción a medio
# hacer, se pierde sin limpiar. Para un cierre ordenado hay que coordinarlo
# explícitamente con un Event (sección 8), no confiar en daemon=True para
# nada que necesite liberar recursos.


# ============================================================================
# 5. RACE CONDITION Y POR QUÉ IMPORTA
# ============================================================================
seccion("5. Race condition y por qué importa")

# Caso real: un contador de peticiones procesadas compartido por varios
# hilos trabajadores. 10 hilos, 1.000 incrementos cada uno: el resultado
# esperado es 10.000 exacto.

# --- 5.1 La versión ingenua: "en mi máquina funciona" -----------------
# contador_inseguro += 1 NO es atómico: por debajo son tres pasos (leer el
# valor, sumar 1, guardar el valor). Para que se pierda un incremento, el
# planificador tiene que interrumpir a un hilo justo entre el "leer" y el
# "guardar" de otro. Esa ventana dura nanosegundos, así que en una máquina
# de desarrollo, con pocos hilos y un bucle que no hace I/O, es fácil que
# el bug NUNCA se manifieste en cientos de ejecuciones de prueba.
contador_ingenuo = 0


def incrementar_ingenuo(veces: int) -> None:
    global contador_ingenuo
    for _ in range(veces):
        contador_ingenuo += 1  # el mismo código que escribirías sin pensarlo


hilos_ingenuos = [threading.Thread(target=incrementar_ingenuo, args=(1_000,)) for _ in range(10)]
for hilo in hilos_ingenuos:
    hilo.start()
for hilo in hilos_ingenuos:
    hilo.join()

print(f"  Versión ingenua  — Esperado: 10000 — Obtenido: {contador_ingenuo}")
if contador_ingenuo == 10_000:
    print("  Ha dado el resultado correcto... por pura suerte de scheduling, NO porque el código sea correcto")

# ¿Por qué "sale bien" aquí? CPython solo cede el control de un hilo a otro
# cuando expira un intervalo de tiempo (sys.getswitchinterval(), 5ms por
# defecto) o cuando el hilo hace algo que libera el GIL explícitamente
# (I/O, sleep). Sumar 1 a un entero tarda del orden de decenas de
# nanosegundos: con 10 hilos y 1.000 iteraciones cada uno, es estadísticamente
# improbable que el reloj de 5ms interrumpa a un hilo justo en el
# nanosegundo malo. El bug SIGUE ahí (la operación sigue sin ser atómica),
# simplemente la ventana de fallo es tan estrecha que rara vez se cruza.
#
# En producción esa probabilidad deja de ser insignificante: más hilos
# compitiendo por el mismo dato, más peticiones por segundo, procesos que
# llevan corriendo días (no segundos), hardware con más núcleos, pausas del
# recolector de basura que ceden el GIL en momentos impredecibles... todo
# eso multiplica las oportunidades de que la interrupción caiga justo en
# medio del "leer, sumar, guardar". El resultado: un contador de métricas,
# un saldo de cuenta o un stock de inventario que "en local siempre
# cuadraba" empieza a descuadrarse en producción, de forma esporádica e
# irreproducible — el peor tipo de bug para depurar.


# --- 5.2 Forzando la interrupción: hacer visible el bug real ----------
# Para dejar de fiarse de la suerte del scheduler, se puede forzar
# explícitamente el cambio de contexto entre el "leer" y el "guardar",
# separándolos y cediendo el control con sleep(0) en medio. Esto no
# introduce un bug nuevo: expone exactamente el mismo bug de la versión
# ingenua, solo que ahora la ventana de fallo se cruza en CADA iteración
# en lugar de una vez entre un millón.
contador_inseguro = 0


def incrementar_inseguro(veces: int) -> None:
    global contador_inseguro
    for _ in range(veces):
        temporal = contador_inseguro
        time.sleep(0)  # cede el GIL a otro hilo justo aquí, a propósito
        contador_inseguro = temporal + 1


hilos_inseguros = [threading.Thread(target=incrementar_inseguro, args=(1_000,)) for _ in range(10)]
for hilo in hilos_inseguros:
    hilo.start()
for hilo in hilos_inseguros:
    hilo.join()

print(f"  Versión forzada  — Esperado: 10000 — Obtenido: {contador_inseguro}")
if contador_inseguro != 10_000:
    print("  Bug reproducido de forma determinista: se han perdido incrementos")

# Cuantos más hilos compitan por el mismo dato, más veces coincide esa
# ventana y peor es el desfase. Este es exactamente el tipo de bug que en
# producción aparece "a veces", es casi imposible de reproducir en local
# sin forzarlo así, y hace que las métricas de un sistema no cuadren. La
# lección no es "si funciona en mis pruebas, es seguro": es que cualquier
# dato compartido y modificado por varios hilos necesita protección
# explícita (sección 6), se haya manifestado el bug en tu máquina o no.


# ============================================================================
# 6. Lock — PROTEGER RECURSOS COMPARTIDOS
# ============================================================================
seccion("6. Lock: proteger recursos compartidos")

contador_seguro = 0
lock_contador = threading.Lock()


def incrementar_seguro(veces: int) -> None:
    global contador_seguro
    for _ in range(veces):
        with lock_contador:
            temporal = contador_seguro
            time.sleep(0)  # el mismo punto de fuga que en la sección 5...
            contador_seguro = temporal + 1  # ...pero ahora dentro del lock


hilos_seguros = [threading.Thread(target=incrementar_seguro, args=(1_000,)) for _ in range(10)]
for hilo in hilos_seguros:
    hilo.start()
for hilo in hilos_seguros:
    hilo.join()

print(f"  Esperado: 10000 — Obtenido: {contador_seguro}")

# with lock_contador: adquiere el lock antes de entrar y lo libera al salir
# (incluso si hay una excepción), igual que with open(...) con un fichero.
# Mientras un hilo tiene el lock, cualquier otro hilo que intente adquirirlo
# se queda esperando: eso convierte "leer, sumar, guardar" en una operación
# efectivamente atómica. Desde Python 3.13, Lock es una clase real (antes
# era una función de fábrica que devolvía un objeto interno), lo que
# permite comprobaciones como isinstance(lock_contador, threading.Lock).
print(f"  isinstance(lock_contador, threading.Lock) = {isinstance(lock_contador, threading.Lock)}")


# ============================================================================
# 7. RLock — LOCK REENTRANTE
# ============================================================================
seccion("7. RLock: lock reentrante")

# Caso real: una clase de inventario donde un método público (reservar)
# necesita llamar a otro método interno (descontar_stock) que también
# protege el mismo dato compartido. Con un Lock normal, el propio hilo se
# bloquearía a sí mismo al intentar adquirir un lock que ya tiene.
class Inventario:
    def __init__(self, stock_inicial: int) -> None:
        self.stock = stock_inicial
        self._lock = threading.RLock()

    def reservar(self, cantidad: int) -> bool:
        with self._lock:
            if self.stock < cantidad:
                return False
            self._descontar_stock(cantidad)
            return True

    def _descontar_stock(self, cantidad: int) -> None:
        with self._lock:  # mismo hilo, mismo lock: con Lock normal, deadlock
            self.stock -= cantidad


inventario = Inventario(stock_inicial=10)
print(f"  reservar(3) -> {inventario.reservar(3)} (stock restante: {inventario.stock})")
print(f"  RLock.locked() (nuevo en 3.14): {inventario._lock.locked()}")

# Un RLock lleva la cuenta de cuántas veces lo ha adquirido EL MISMO hilo y
# solo lo libera de verdad cuando ese hilo lo suelta el mismo número de
# veces. Un Lock normal no distingue quién lo pide: si el hilo que ya lo
# tiene vuelve a pedirlo, se queda esperando a sí mismo para siempre.


# ============================================================================
# 8. Event — COMUNICACIÓN ENTRE HILOS
# ============================================================================
seccion("8. Event: comunicación entre hilos")

# Caso real: un hilo trabajador no debe empezar a procesar pedidos hasta
# que la conexión a base de datos esté lista. En vez de sondear en un bucle
# (time.sleep(0.1) comprobando una variable una y otra vez), espera a una
# señal explícita.
base_de_datos_lista = threading.Event()


def trabajador_pedidos() -> None:
    print("  [trabajador] esperando a que la base de datos esté lista...")
    base_de_datos_lista.wait()
    print("  [trabajador] señal recibida, empiezo a procesar pedidos")


hilo_trabajador = threading.Thread(target=trabajador_pedidos)
hilo_trabajador.start()
time.sleep(0.3)  # simula el tiempo que tarda la "conexión" en establecerse
print("  [main] base de datos conectada, doy la señal")
base_de_datos_lista.set()
hilo_trabajador.join()

# wait() bloquea el hilo hasta que otro hilo llama a set(). Pero una vez
# señalado, un Event se queda señalado para siempre: si el mismo trabajador
# tuviera que esperar una SEGUNDA señal (el siguiente lote de pedidos, no
# solo "la base de datos ya está lista" una vez), wait() devolvería el
# control al instante sin esperar nada, porque el Event nunca ha vuelto a
# "no señalado". clear() es justo eso: reinicia el Event para poder
# reutilizarlo en un ciclo.

# Caso real: el mismo trabajador de pedidos, una vez conectado, no procesa
# un único pedido y termina — se queda vivo esperando LOTES sucesivos que
# van llegando, uno detrás de otro, cada uno con su propia señal.
lote_listo = threading.Event()
lote_procesado = threading.Event()
lote_procesado.set()  # al principio el productor puede preparar el primer lote
lote_actual = {"pedidos": None}
lotes_de_pedidos = [["PED-1", "PED-2"], ["PED-3"], ["PED-4", "PED-5", "PED-6"]]


def trabajador_lotes() -> None:
    for _ in lotes_de_pedidos:
        lote_listo.wait()
        print(f"  [trabajador] procesando lote: {lote_actual['pedidos']}")
        lote_listo.clear()  # vuelve a "no señalado": listo para esperar el próximo lote
        lote_procesado.set()  # avisa al productor de que ya puede preparar el siguiente


hilo_trabajador_lotes = threading.Thread(target=trabajador_lotes)
hilo_trabajador_lotes.start()

for pedidos_lote in lotes_de_pedidos:
    lote_procesado.wait()
    lote_procesado.clear()
    lote_actual["pedidos"] = pedidos_lote
    time.sleep(0.1)  # simula que montar el lote lleva su tiempo
    print(f"  [main] lote listo: {pedidos_lote}")
    lote_listo.set()

hilo_trabajador_lotes.join()

# Sin el clear() de dentro de trabajador_lotes, la segunda vuelta del bucle
# vería lote_listo todavía "señalado" desde la vuelta anterior y wait() no
# esperaría nada: procesaría el mismo lote otra vez (o peor, un lote
# incompleto si el productor todavía no ha terminado de montarlo). clear()
# es lo que obliga a esperar de verdad a la señal SIGUIENTE en cada vuelta.


# ============================================================================
# 9. Semaphore — LIMITAR CONCURRENCIA
# ============================================================================
seccion("9. Semaphore: limitar concurrencia")

# Caso real: un pool de conexiones a base de datos solo admite 3 conexiones
# simultáneas. Si 10 hilos intentan conectarse a la vez sin control, la
# base de datos rechaza las peticiones de más o se satura.
pool_conexiones = threading.BoundedSemaphore(3)
conexiones_activas = 0
lock_contador_conexiones = threading.Lock()


def usar_conexion(id_hilo: int) -> None:
    global conexiones_activas
    with pool_conexiones:
        with lock_contador_conexiones:
            conexiones_activas += 1
            print(f"  hilo-{id_hilo} conecta    (activas: {conexiones_activas})")
        time.sleep(0.15)
        with lock_contador_conexiones:
            conexiones_activas -= 1
            print(f"  hilo-{id_hilo} desconecta (activas: {conexiones_activas})")


hilos_conexion = [threading.Thread(target=usar_conexion, args=(i,)) for i in range(10)]
for hilo in hilos_conexion:
    hilo.start()
for hilo in hilos_conexion:
    hilo.join()

# BoundedSemaphore(3) deja pasar como máximo a 3 hilos a la vez dentro del
# "with"; el resto se queda esperando a que alguno salga. A diferencia de
# Semaphore, BoundedSemaphore lanza ValueError si se libera más veces de
# las que se ha adquirido, lo que detecta bugs de "liberar de más" en vez
# de esconderlos.


# ============================================================================
# 10. threading.local — DATOS PRIVADOS POR HILO
# ============================================================================
seccion("10. threading.local: datos privados por hilo")

# Caso real: un servidor web donde cada hilo atiende una petición distinta
# y necesita su propio user_id e idioma sin que se mezclen con los de otra
# petición que se está atendiendo en paralelo en otro hilo.
contexto_peticion = threading.local()


def atender_peticion(user_id: str, idioma: str) -> None:
    contexto_peticion.user_id = user_id
    contexto_peticion.idioma = idioma
    time.sleep(0.1)
    print(f"  hilo atendiendo user_id={contexto_peticion.user_id} idioma={contexto_peticion.idioma}")


hilos_peticiones = [
    threading.Thread(target=atender_peticion, args=(f"user-{i}", idioma))
    for i, idioma in enumerate(["es", "en", "fr"])
]
for hilo in hilos_peticiones:
    hilo.start()
for hilo in hilos_peticiones:
    hilo.join()

# Aunque contexto_peticion es UNA sola variable compartida por todos los
# hilos, cada hilo ve su propia copia de sus atributos: escribir
# contexto_peticion.user_id en un hilo no toca el valor que ve otro hilo.
# threading.local() resuelve exactamente el problema que en la sección 5
# rompía el contador: aquí no hace falta lock porque no hay dato compartido
# de verdad, cada hilo tiene el suyo.


# ============================================================================
# 11. GIL Y CUÁNDO USAR HILOS VS PROCESOS
# ============================================================================
seccion("11. GIL y cuándo usar hilos vs procesos")

print("""
  El GIL (Global Interpreter Lock) permite que solo un hilo ejecute bytecode
  Python a la vez dentro de un mismo proceso, en el build estándar de
  Python 3.14. Pero durante una operación de I/O (red, disco, esperar una
  respuesta de base de datos), el hilo LIBERA el GIL mientras espera, así
  que otros hilos pueden avanzar. Por eso todos los ejemplos de este fichero
  (sleep simulando red) sí se benefician de threading.

    Tipo de tarea                          Herramienta recomendada
    --------------------------------------  ------------------------------
    I/O-bound (red, disco, BD, APIs)        threading
    CPU-bound (cálculo, compresión, ML)     multiprocessing /
                                             concurrent.futures.ProcessPoolExecutor

  Para CPU-bound, varios hilos Python no aceleran nada porque el GIL sigue
  bloqueando a los demás mientras uno calcula: solo se ejecuta bytecode de
  un hilo cada vez. multiprocessing usa procesos separados, cada uno con su
  propio intérprete y su propio GIL, y ahí sí hay paralelismo real en CPU.

  Nota al margen: desde Python 3.13 existe un build experimental
  "free-threaded" (PEP 703) que puede compilarse sin GIL, pero no es el
  build por defecto en 3.14 y sigue considerándose experimental.
""")


seccion("FIN — ya conoces threading al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
