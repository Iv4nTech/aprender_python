"""
================================================================================
 EJERCICIOS: THREADING EN PYTHON
 Casos reales — de fácil a experto
 Ejecutar: python3 ejercicios.py
================================================================================

Completa cada ejercicio donde encuentres "..." y descomenta los print()
para comprobar el resultado.
================================================================================
"""

import threading
import time


def seccion(titulo: str) -> None:
    """Pequeño helper para imprimir cabeceras y que la salida sea legible."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# EJERCICIO 1 — FÁCIL — Descargas en paralelo
# ============================================================================
seccion("EJERCICIO 1 — FÁCIL — Descargas en paralelo")

# Una herramienta de backups necesita descargar 3 ficheros. Descargarlos uno
# a uno desperdicia tiempo esperando red que no depende entre ficheros.


def descargar_archivo(url: str, delay: float) -> None:
    time.sleep(delay)
    print(f"  descargado: {url}")


urls = [("informe.pdf", 0.3), ("foto.png", 0.2), ("backup.zip", 0.4)]

# Crea un Thread por cada (url, delay) de 'urls', arráncalos todos y luego
# haz join() a todos. Mide el tiempo con time.perf_counter() antes y después
# y comprueba que tarda menos que la suma de los delays (0.9s).
...

# inicio = time.perf_counter()
# ... (crear, start y join de los hilos)
# duracion = time.perf_counter() - inicio
# print(f"Duración: {duracion:.2f}s (suma en serie sería 0.90s)")


# ============================================================================
# EJERCICIO 2 — FÁCIL — MonitorEstado como subclase de Thread
# ============================================================================
seccion("EJERCICIO 2 — FÁCIL — MonitorEstado como subclase de Thread")

# Un servicio de salud hace ping a un servidor varias veces y necesita
# recordar cuántos intentos ha hecho.


# Crea MonitorEstado(threading.Thread) con __init__(self, iteraciones: int)
# que guarde self.intentos = 0, y run() que por cada iteración duerma 0.05s
# e incremente self.intentos en 1
class MonitorEstado(threading.Thread):
    ...

# monitor = MonitorEstado(3)
# monitor.start()
# monitor.join()
# print(f"Intentos realizados: {monitor.intentos}")

# Resultado esperado: Intentos realizados: 3


# ============================================================================
# EJERCICIO 3 — FÁCIL — Heartbeat con daemon thread
# ============================================================================
seccion("EJERCICIO 3 — FÁCIL — Heartbeat con daemon thread")

# Un hilo de heartbeat manda "ping" cada 0.5s en segundo plano. El programa
# principal solo necesita vivir 1.5s y no debe esperar a que el heartbeat
# termine por su cuenta (nunca termina solo).


def hilo_daemon_heartbeat() -> None:
    # Sigue vivo para siempre (nunca termina por sí solo, es la esencia de
    # un daemon), pero deja de imprimir tras unos pocos pings para no
    # ensuciar la salida de los ejercicios siguientes con "ping" sueltos.
    pings_visibles = 3
    iteracion = 0
    while True:
        if iteracion < pings_visibles:
            print("  ping")
        time.sleep(0.5)
        iteracion += 1


# Crea el hilo con target=hilo_daemon_heartbeat y daemon=True, arráncalo,
# deja dormir al hilo principal 1.5s e imprime que el programa termina
...

# print("Programa principal termina sin esperar al heartbeat")


# ============================================================================
# EJERCICIO 4 — MEDIO — ContadorSeguro con Lock
# ============================================================================
seccion("EJERCICIO 4 — MEDIO — ContadorSeguro con Lock")

# Un contador de peticiones procesadas, compartido por 5 hilos que
# incrementan 500 veces cada uno. Sin protección, el resultado final no
# sería fiable.


# Crea ContadorSeguro con self.valor = 0 y self._lock = threading.Lock().
# Añade incrementar(self) que suma 1 a self.valor protegido por el lock.
class ContadorSeguro:
    ...

# contador = ContadorSeguro()
# def trabajo():
#     for _ in range(500):
#         contador.incrementar()
# hilos = [threading.Thread(target=trabajo) for _ in range(5)]
# for h in hilos: h.start()
# for h in hilos: h.join()
# print(f"Valor final: {contador.valor}")

# Resultado esperado: Valor final: 2500


# ============================================================================
# EJERCICIO 5 — MEDIO — Cola de tareas con Event
# ============================================================================
seccion("EJERCICIO 5 — MEDIO — Cola de tareas con Event")

# Un hilo productor llena una lista de tareas y avisa con un Event cuando
# está lista. Un hilo consumidor debe esperar esa señal antes de procesar,
# para no leer una lista a medio llenar.

tareas = []
tareas_listas = threading.Event()


def cola_tareas_con_event() -> None:
    # Productor: añade "tarea-1", "tarea-2", "tarea-3" a 'tareas' (con un
    # pequeño sleep entre cada una) y al terminar llama a tareas_listas.set()
    ...


def consumidor_tareas() -> None:
    # Consumidor: espera con tareas_listas.wait() y luego imprime 'tareas'
    ...

# hilo_productor = threading.Thread(target=cola_tareas_con_event)
# hilo_consumidor = threading.Thread(target=consumidor_tareas)
# hilo_consumidor.start()
# hilo_productor.start()
# hilo_productor.join()
# hilo_consumidor.join()

# Resultado esperado: el consumidor imprime la lista completa de 3 tareas,
# nunca una lista vacía o a medias


# ============================================================================
# EJERCICIO 6 — MEDIO — PoolConexiones con BoundedSemaphore
# ============================================================================
seccion("EJERCICIO 6 — MEDIO — PoolConexiones con BoundedSemaphore")

# Una base de datos solo admite 2 conexiones simultáneas. 6 hilos intentan
# conectarse a la vez: hay que garantizar que nunca hay más de 2 dentro.


# Crea PoolConexiones con self._semaforo = threading.BoundedSemaphore(2) y
# un método conectar(self, id_hilo) que, dentro del semáforo, imprima
# "hilo-{id_hilo} entra", duerma 0.1s e imprima "hilo-{id_hilo} sale"
class PoolConexiones:
    ...

# pool = PoolConexiones()
# hilos = [threading.Thread(target=pool.conectar, args=(i,)) for i in range(6)]
# for h in hilos: h.start()
# for h in hilos: h.join()


# ============================================================================
# EJERCICIO 7 — AVANZADO — GestorCache con RLock
# ============================================================================
seccion("EJERCICIO 7 — AVANZADO — GestorCache con RLock")

# Un método público obtener() llama internamente a _cargar() si la clave no
# está en caché, y ambos métodos protegen el mismo diccionario compartido
# con el mismo lock. Con un Lock normal, esto sería un deadlock.


# Crea GestorCache con self._cache = {}, self._lock = threading.RLock().
# obtener(self, clave): dentro del lock, si la clave no está en self._cache
# llama a self._cargar(clave); devuelve self._cache[clave]
# _cargar(self, clave): dentro del (mismo) lock, simula una carga lenta
# (time.sleep(0.05)) y guarda self._cache[clave] = f"valor-de-{clave}"
class GestorCache:
    ...

# cache = GestorCache()
# print(cache.obtener("usuario:42"))
# print(cache.obtener("usuario:42"))  # segunda vez: ya está en caché

# Resultado esperado ambas líneas: valor-de-usuario:42


# ============================================================================
# EJERCICIO 8 — AVANZADO — ContextoPeticion con threading.local
# ============================================================================
seccion("EJERCICIO 8 — AVANZADO — ContextoPeticion con threading.local")

# Un servidor simplificado atiende 4 peticiones en paralelo, cada una en su
# propio hilo. Cada petición necesita su propio usuario_id e idioma, sin
# que se mezclen con los de las peticiones que se atienden en paralelo.

contexto = threading.local()


def atender(usuario_id: str, idioma: str) -> None:
    # Guarda usuario_id e idioma en 'contexto', duerme 0.05s e imprime
    # ambos valores leídos de 'contexto' (deben ser los mismos que se
    # guardaron en ESTE hilo, no los de otro)
    ...

# peticiones = [("u1", "es"), ("u2", "en"), ("u3", "fr"), ("u4", "de")]
# hilos = [threading.Thread(target=atender, args=p) for p in peticiones]
# for h in hilos: h.start()
# for h in hilos: h.join()


# ============================================================================
# EJERCICIO 9 — AVANZADO — Pipeline de dos etapas con Event
# ============================================================================
seccion("EJERCICIO 9 — AVANZADO — Pipeline de dos etapas con Event")

# Hilo A genera números del 1 al 5. Hilo B los consume y calcula su
# cuadrado. Se sincronizan con dos Event (sin usar queue): "dato_listo"
# avisa a B de que hay un número nuevo, "dato_procesado" avisa a A de que
# ya puede generar el siguiente.

dato_listo = threading.Event()
dato_procesado = threading.Event()
dato_procesado.set()  # al principio, A puede generar el primer dato
dato_compartido = {"valor": None, "fin": False}
lock_dato = threading.Lock()


def pipeline_generador() -> None:
    # Para cada número del 1 al 5: espera dato_procesado, límpialo, guarda
    # el número en dato_compartido["valor"] (protegido por lock_dato) y
    # marca dato_listo. Al terminar los 5, espera dato_procesado una vez
    # más, marca dato_compartido["fin"] = True y marca dato_listo.
    ...


def pipeline_consumidor() -> None:
    # En bucle: espera dato_listo, límpialo; si dato_compartido["fin"] es
    # True, termina el bucle; si no, imprime el cuadrado del valor y marca
    # dato_procesado
    ...

# hilo_a = threading.Thread(target=pipeline_generador)
# hilo_b = threading.Thread(target=pipeline_consumidor)
# hilo_a.start()
# hilo_b.start()
# hilo_a.join()
# hilo_b.join()

# Resultado esperado: 1, 4, 9, 16, 25 (en ese orden)


# ============================================================================
# EJERCICIO 10 — EXPERTO — Benchmark threading vs serie en CPU-bound
# ============================================================================
seccion("EJERCICIO 10 — EXPERTO — Benchmark threading vs serie en CPU-bound")

# Calcular la suma de cuadrados de 1 a 1.000.000 es CPU-bound (nada de
# I/O). Comprueba si dividirlo en varios hilos lo acelera o no, y por qué.


def suma_cuadrados(inicio: int, fin: int) -> int:
    return sum(n * n for n in range(inicio, fin))


def benchmark_gil(total: int, n_hilos: int) -> tuple[float, float]:
    # Devuelve (duracion_serie, duracion_hilos) calculando suma_cuadrados
    # de 0 a 'total':
    #   - en serie: una sola llamada a suma_cuadrados(0, total), medida con
    #     time.perf_counter()
    #   - con hilos: divide el rango en 'n_hilos' trozos iguales, lanza un
    #     Thread por trozo (guardando el resultado no hace falta, solo
    #     medir el tiempo), haz join a todos, mide con time.perf_counter()
    ...

# duracion_serie, duracion_hilos = benchmark_gil(1_000_000, 4)
# print(f"Serie:  {duracion_serie:.3f}s")
# print(f"Hilos:  {duracion_hilos:.3f}s")
# print("threading no acelera tareas CPU-bound por el GIL: para eso hace")
# print("falta multiprocessing o concurrent.futures.ProcessPoolExecutor")


seccion("FIN — completa los ejercicios y compáralos con ejercicios_resueltos.py")
