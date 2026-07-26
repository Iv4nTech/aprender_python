"""
================================================================================
 EJERCICIOS RESUELTOS: THREADING EN PYTHON
 Casos reales — de fácil a experto
 Ejecutar: python3 ejercicios_resueltos.py
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


def descargar_archivo(url: str, delay: float) -> None:
    time.sleep(delay)
    print(f"  descargado: {url}")


urls = [("informe.pdf", 0.3), ("foto.png", 0.2), ("backup.zip", 0.4)]

# SOLUCIÓN
inicio = time.perf_counter()
hilos_descarga = [threading.Thread(target=descargar_archivo, args=(url, delay)) for url, delay in urls]
for h in hilos_descarga:
    h.start()
for h in hilos_descarga:
    h.join()
duracion = time.perf_counter() - inicio

print(f"Duración: {duracion:.2f}s (suma en serie sería 0.90s)")


# ============================================================================
# EJERCICIO 2 — FÁCIL — MonitorEstado como subclase de Thread
# ============================================================================
seccion("EJERCICIO 2 — FÁCIL — MonitorEstado como subclase de Thread")


# SOLUCIÓN
class MonitorEstado(threading.Thread):
    def __init__(self, iteraciones: int) -> None:
        super().__init__()
        self.iteraciones = iteraciones
        self.intentos = 0

    def run(self) -> None:
        for _ in range(self.iteraciones):
            time.sleep(0.05)
            self.intentos += 1


monitor = MonitorEstado(3)
monitor.start()
monitor.join()
print(f"Intentos realizados: {monitor.intentos}")


# ============================================================================
# EJERCICIO 3 — FÁCIL — Heartbeat con daemon thread
# ============================================================================
seccion("EJERCICIO 3 — FÁCIL — Heartbeat con daemon thread")


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


# SOLUCIÓN
hilo_heartbeat = threading.Thread(target=hilo_daemon_heartbeat, daemon=True)
hilo_heartbeat.start()
time.sleep(1.5)

print("Programa principal termina sin esperar al heartbeat")


# ============================================================================
# EJERCICIO 4 — MEDIO — ContadorSeguro con Lock
# ============================================================================
seccion("EJERCICIO 4 — MEDIO — ContadorSeguro con Lock")


# SOLUCIÓN
class ContadorSeguro:
    def __init__(self) -> None:
        self.valor = 0
        self._lock = threading.Lock()

    def incrementar(self) -> None:
        with self._lock:
            self.valor += 1


contador = ContadorSeguro()


def trabajo_contador() -> None:
    for _ in range(500):
        contador.incrementar()


hilos_contador = [threading.Thread(target=trabajo_contador) for _ in range(5)]
for h in hilos_contador:
    h.start()
for h in hilos_contador:
    h.join()

print(f"Valor final: {contador.valor}")


# ============================================================================
# EJERCICIO 5 — MEDIO — Cola de tareas con Event
# ============================================================================
seccion("EJERCICIO 5 — MEDIO — Cola de tareas con Event")

tareas = []
tareas_listas = threading.Event()


# SOLUCIÓN
def cola_tareas_con_event() -> None:
    for i in range(1, 4):
        time.sleep(0.05)
        tareas.append(f"tarea-{i}")
    tareas_listas.set()


def consumidor_tareas() -> None:
    tareas_listas.wait()
    print(f"Tareas recibidas: {tareas}")


hilo_productor = threading.Thread(target=cola_tareas_con_event)
hilo_consumidor = threading.Thread(target=consumidor_tareas)
hilo_consumidor.start()
hilo_productor.start()
hilo_productor.join()
hilo_consumidor.join()


# ============================================================================
# EJERCICIO 6 — MEDIO — PoolConexiones con BoundedSemaphore
# ============================================================================
seccion("EJERCICIO 6 — MEDIO — PoolConexiones con BoundedSemaphore")


# SOLUCIÓN
class PoolConexiones:
    def __init__(self) -> None:
        self._semaforo = threading.BoundedSemaphore(2)

    def conectar(self, id_hilo: int) -> None:
        with self._semaforo:
            print(f"  hilo-{id_hilo} entra")
            time.sleep(0.1)
            print(f"  hilo-{id_hilo} sale")


pool = PoolConexiones()
hilos_pool = [threading.Thread(target=pool.conectar, args=(i,)) for i in range(6)]
for h in hilos_pool:
    h.start()
for h in hilos_pool:
    h.join()


# ============================================================================
# EJERCICIO 7 — AVANZADO — GestorCache con RLock
# ============================================================================
seccion("EJERCICIO 7 — AVANZADO — GestorCache con RLock")


# SOLUCIÓN
class GestorCache:
    def __init__(self) -> None:
        self._cache = {}
        self._lock = threading.RLock()

    def obtener(self, clave: str) -> str:
        with self._lock:
            if clave not in self._cache:
                self._cargar(clave)
            return self._cache[clave]

    def _cargar(self, clave: str) -> None:
        with self._lock:  # mismo hilo, mismo lock: con Lock normal sería deadlock
            time.sleep(0.05)
            self._cache[clave] = f"valor-de-{clave}"


cache = GestorCache()
print(cache.obtener("usuario:42"))
print(cache.obtener("usuario:42"))  # segunda vez: ya está en caché, no recarga


# ============================================================================
# EJERCICIO 8 — AVANZADO — ContextoPeticion con threading.local
# ============================================================================
seccion("EJERCICIO 8 — AVANZADO — ContextoPeticion con threading.local")

contexto = threading.local()


# SOLUCIÓN
def atender(usuario_id: str, idioma: str) -> None:
    contexto.usuario_id = usuario_id
    contexto.idioma = idioma
    time.sleep(0.05)
    print(f"  hilo atendiendo usuario_id={contexto.usuario_id} idioma={contexto.idioma}")


peticiones = [("u1", "es"), ("u2", "en"), ("u3", "fr"), ("u4", "de")]
hilos_peticiones = [threading.Thread(target=atender, args=p) for p in peticiones]
for h in hilos_peticiones:
    h.start()
for h in hilos_peticiones:
    h.join()


# ============================================================================
# EJERCICIO 9 — AVANZADO — Pipeline de dos etapas con Event
# ============================================================================
seccion("EJERCICIO 9 — AVANZADO — Pipeline de dos etapas con Event")

dato_listo = threading.Event()
dato_procesado = threading.Event()
dato_procesado.set()  # al principio, A puede generar el primer dato
dato_compartido = {"valor": None, "fin": False}
lock_dato = threading.Lock()


# SOLUCIÓN
def pipeline_generador() -> None:
    for numero in range(1, 6):
        dato_procesado.wait()
        dato_procesado.clear()
        with lock_dato:
            dato_compartido["valor"] = numero
        dato_listo.set()
    dato_procesado.wait()
    dato_compartido["fin"] = True
    dato_listo.set()


def pipeline_consumidor() -> None:
    while True:
        dato_listo.wait()
        dato_listo.clear()
        if dato_compartido["fin"]:
            break
        with lock_dato:
            valor = dato_compartido["valor"]
        print(f"  {valor} al cuadrado es {valor * valor}")
        dato_procesado.set()


hilo_a = threading.Thread(target=pipeline_generador)
hilo_b = threading.Thread(target=pipeline_consumidor)
hilo_a.start()
hilo_b.start()
hilo_a.join()
hilo_b.join()


# ============================================================================
# EJERCICIO 10 — EXPERTO — Benchmark threading vs serie en CPU-bound
# ============================================================================
seccion("EJERCICIO 10 — EXPERTO — Benchmark threading vs serie en CPU-bound")


def suma_cuadrados(inicio: int, fin: int) -> int:
    return sum(n * n for n in range(inicio, fin))


# SOLUCIÓN
def benchmark_gil(total: int, n_hilos: int, repeticiones: int = 3) -> tuple[float, float]:
    # Con cargas pequeñas el ruido de medición puede hacer que "hilos" salga
    # más rápido por casualidad, así que se repite varias veces y se toma
    # el mínimo de cada modo (la técnica estándar de timeit para benchmarks).
    tiempos_serie = []
    tiempos_hilos = []

    trozo = total // n_hilos
    rangos = [(i * trozo, (i + 1) * trozo if i < n_hilos - 1 else total) for i in range(n_hilos)]

    for _ in range(repeticiones):
        inicio_serie = time.perf_counter()
        suma_cuadrados(0, total)
        tiempos_serie.append(time.perf_counter() - inicio_serie)

        hilos_cpu = [threading.Thread(target=suma_cuadrados, args=rango) for rango in rangos]
        inicio_hilos = time.perf_counter()
        for h in hilos_cpu:
            h.start()
        for h in hilos_cpu:
            h.join()
        tiempos_hilos.append(time.perf_counter() - inicio_hilos)

    return min(tiempos_serie), min(tiempos_hilos)


duracion_serie, duracion_hilos = benchmark_gil(10_000_000, 4)
print(f"Serie:  {duracion_serie:.3f}s")
print(f"Hilos:  {duracion_hilos:.3f}s")
print("threading no acelera tareas CPU-bound por el GIL: solo un hilo ejecuta")
print("bytecode Python a la vez, así que repartir el cálculo en hilos no")
print("añade paralelismo real y solo suma overhead de creación/cambio de")
print("contexto. Para acelerar CPU-bound de verdad hace falta multiprocessing")
print("o concurrent.futures.ProcessPoolExecutor, que usan procesos separados")
print("con su propio intérprete y su propio GIL cada uno.")


seccion("FIN — 10/10 ejercicios resueltos")
