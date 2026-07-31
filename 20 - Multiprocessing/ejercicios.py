"""
================================================================================
 EJERCICIOS: MULTIPROCESSING EN PYTHON
 Casos reales — de fácil a experto
 Ejecutar: python3 ejercicios.py

Completa cada ejercicio donde encuentres "..." dentro de su bloque del
if __name__ == "__main__" final.
================================================================================
"""

import itertools
import math
import multiprocessing
import os
import queue
import time
import zlib
from concurrent.futures import ProcessPoolExecutor


def seccion(titulo: str) -> None:
    """Pequeño helper para imprimir cabeceras y que la salida sea legible."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# Con forkserver/spawn (defecto en 3.14 en Linux) los procesos hijo
# reimportan este fichero para localizar la función objetivo. Si seccion()
# u otro código con efectos (print, creación de procesos...) estuviera a
# nivel de módulo, esa reimportación lo volvería a ejecutar y duplicaría la
# salida. Por eso, igual que en introduccion.py, TODO el código con efectos
# vive dentro de un único "if __name__ == '__main__':" al final; a nivel de
# módulo solo hay definiciones (funciones, clases, datos), que reimportar
# no tiene ningún efecto visible.


# ============================================================================
# EJERCICIO 1 — FÁCIL — Renderizado de frames de un vídeo
# ============================================================================
# Un estudio de animación tiene que renderizar 8 frames de un vídeo. Cada
# frame es CPU-bound: aplica una transformación matemática a cada píxel.


def renderizar_frame(pixeles: list[int]) -> list[int]:
    return [((p * 37 + 11) % 256) for p in pixeles]


frames = [[(i * 3 + j) % 256 for j in range(500)] for i in range(8)]

# Procesa los 8 frames en paralelo con ProcessPoolExecutor.map(), y compara
# el resultado con la versión secuencial (list comprehension normal) para
# verificar que ambas dan exactamente el mismo resultado.
# Resultado esperado: los 8 frames en paralelo coinciden con los de la versión secuencial
# (produce 'resultados_secuenciales' y 'resultados_paralelos' con los 8 frames renderizados)


# ============================================================================
# EJERCICIO 2 — FÁCIL — Proceso hijo que reporta su PID
# ============================================================================
# Un sistema de diagnóstico necesita comprobar que efectivamente se están
# lanzando procesos del sistema operativo independientes, no hilos.


def reportar_pid_hijo(cola: multiprocessing.Queue) -> None:
    cola.put((os.getpid(), os.getppid()))


# Lanza 4 procesos con multiprocessing.Process (target=reportar_pid_hijo),
# recoge los 4 pares (pid, ppid) desde una multiprocessing.Queue en el
# proceso padre, y comprueba que los 4 PIDs de hijo son distintos entre sí
# y que ninguno coincide con os.getpid() del padre.
# Resultado esperado: 4 PIDs de hijo, todos distintos entre sí y del padre
# (produce la lista 'pids_hijos' con los 4 PIDs recogidos de la Queue)


# ============================================================================
# EJERCICIO 3 — MEDIO — Compresión paralela de ficheros de log
# ============================================================================
# Un sistema de rotación de logs tiene que comprimir 6 ficheros antes de
# archivarlos. Comprimir es CPU-bound: hacerlo en serie retrasa la rotación.


def comprimir_log(texto: str) -> tuple[bytes, int, int]:
    comprimido = zlib.compress(texto.encode())
    return comprimido, len(texto.encode()), len(comprimido)


logs_simulados = [f"{i:04d} INFO petición procesada correctamente\n" * 300 for i in range(6)]

# Comprime los 6 logs en paralelo con multiprocessing.Pool.map(), calcula el
# ratio de compresión total (tamaño comprimido / tamaño original) y verifica
# con zlib.decompress() que cada log comprimido se recupera igual al original.
# Resultado esperado: un ratio de compresión bajo (los logs se repiten mucho)
# y todos los logs se descomprimen igual al original
# (produce 'resultados_compresion': una lista de (comprimido, len_original, len_comprimido))


# ============================================================================
# EJERCICIO 4 — MEDIO — Pipeline de análisis de texto con Pipe
# ============================================================================
# Un agregador de noticias genera titulares y necesita, para cada uno, un
# recuento de palabras calculado en OTRO proceso, sin pasar por disco ni red.


def contador_de_palabras(conexion) -> None:
    while True:
        titular = conexion.recv()
        if titular is None:
            break
        conexion.send((titular, len(titular.split())))
    conexion.close()


titulares = [
    "Bolsa sube tras el dato de empleo",
    "Nueva ley fiscal entra en vigor la próxima semana",
    "El banco central mantiene los tipos de interés",
]

# Crea un Pipe(), lanza un proceso con target=contador_de_palabras conectado
# a un extremo, envía cada titular por el otro extremo con .send(), recibe
# la tupla (titular, num_palabras) de vuelta con .recv() y muéstrala. Al
# terminar, envía None como señal de que no hay más titulares.
# Resultado esperado: el recuento de palabras de cada uno de los 3 titulares
# (produce 'resultados': una lista de tuplas (titular, num_palabras))


# ============================================================================
# EJERCICIO 5 — MEDIO — Búsqueda paralela en ficheros de configuración
# ============================================================================
# Antes de un despliegue hay que auditar 8 ficheros de configuración y
# encontrar cuáles tienen un modo concreto activado.


def contiene_clave_valor(fichero: dict, clave: str, valor) -> bool:
    return fichero.get(clave) == valor


configs = [
    {"nombre": f"config-{i}.json", "host": f"10.0.0.{i}", "puerto": 8080, "modo": modo}
    for i, modo in enumerate(
        ["produccion", "desarrollo", "produccion", "test", "produccion", "desarrollo", "test", "produccion"],
        start=1,
    )
]

# Busca en paralelo, con ProcessPoolExecutor.map(), qué ficheros tienen
# modo == "produccion" y devuelve la lista de sus nombres.
# Resultado esperado: ['config-1.json', 'config-3.json', 'config-5.json', 'config-8.json']
# (produce 'ficheros_en_produccion' con la lista de nombres coincidentes)


# ============================================================================
# EJERCICIO 6 — MEDIO — Contador de visitas compartido entre workers
# ============================================================================
# Un servidor web simulado reparte peticiones entre 4 workers, y todos
# incrementan el mismo contador global de visitas. Sin protección, el
# resultado final no sería fiable (la misma race condition que con hilos,
# pero entre procesos).


# Crea ContadorVisitas con self._valor = multiprocessing.Value('i', 0) y
# self._lock = multiprocessing.Lock() en __init__, y un método
# registrar_visita(self) que incremente self._valor.value en 1 protegido
# por el lock. Añade también una property valor que devuelva self._valor.value
class ContadorVisitas:
    ...


def trabajo_worker(contador: "ContadorVisitas") -> None:
    for _ in range(500):
        contador.registrar_visita()


# Lanza 4 procesos con target=trabajo_worker sobre un mismo ContadorVisitas,
# espera a que terminen y comprueba que el valor final es exacto.
# Resultado esperado: Visitas totales: 2000 (4 workers x 500 visitas)
# (produce 'contador_visitas': el ContadorVisitas ya actualizado por los 4 workers)


# ============================================================================
# EJERCICIO 7 — AVANZADO — Acumulador de métricas con Manager dict
# ============================================================================
# Un sistema de métricas tiene 5 workers, cada uno midiendo la latencia de
# sus propias peticiones. Hace falta acumular todas las mediciones de todos
# los workers en un único sitio para calcular estadísticas globales.


def generar_metricas(worker_id: int, resultados: dict) -> None:
    resultados[worker_id] = [50 + worker_id * 10 + i for i in range(6)]


# Usa multiprocessing.Manager().dict() para que 5 procesos (worker_id 1..5)
# acumulen sus mediciones con generar_metricas. Después calcula la latencia
# media global (de TODAS las mediciones juntas) y cuál worker tiene la
# media más alta.
# Resultado esperado: latencia media global ~82.50ms, worker más lento: 5
# (produce 'latencia_media_global', 'worker_mas_lento' y 'medias_por_worker')


# ============================================================================
# EJERCICIO 8 — AVANZADO — Pool de transcodificación con límite de recursos
# ============================================================================
# Una plataforma de vídeo transcodifica 10 vídeos en paralelo, pero solo
# tiene una GPU compartida que aguanta 3 transcodificaciones simultáneas.
# Si se lanzan más de 3 a la vez, la GPU se satura.

videos = [(f"video-{i}.mp4", resolucion, duracion) for i, (resolucion, duracion) in enumerate(
    [
        ("1080p", 30), ("720p", 45), ("4K", 20), ("1080p", 60), ("720p", 15),
        ("4K", 25), ("1080p", 40), ("720p", 50), ("4K", 35), ("1080p", 10),
    ],
    start=1,
)]

# Un Semaphore/Value NO se puede pasar como argumento normal de
# pool.starmap(): las tareas de un Pool viajan a los workers ya arrancados
# por una cola con pickling estándar, y los objetos de sincronización de
# multiprocessing solo se comparten "por herencia", en el momento de crear
# el proceso. La forma correcta es un initializer de Pool (se ejecuta una
# vez por worker AL CREAR el pool) que guarda los objetos compartidos en
# variables globales del proceso worker.
_semaforo_gpu = None
_contador_activos = None
_maximo_observado = None
_lock_contador = None


# Completa _inicializar_worker_gpu(semaforo, contador_activos,
# maximo_observado, lock_contador): guarda los 4 argumentos en las 4
# variables globales de arriba (con 'global').
def _inicializar_worker_gpu(semaforo, contador_activos, maximo_observado, lock_contador) -> None:
    ...


# Completa transcodificar_video(nombre, resolucion, duracion): dentro de
# _semaforo_gpu, incrementa _contador_activos.value (protegido por
# _lock_contador), actualiza _maximo_observado.value si _contador_activos.value
# lo supera, duerme 0.05s (simula el trabajo de la GPU) y decrementa
# _contador_activos.value. Devuelve "{nombre} transcodificado a {resolucion}".
def transcodificar_video(nombre: str, resolucion: str, duracion: int) -> str:
    ...


# Crea un Pool(processes=6, initializer=_inicializar_worker_gpu,
# initargs=(...)) con un Semaphore(3), un Value contador y un Value máximo,
# y procesa 'videos' con pool.starmap(transcodificar_video, videos).
# Resultado esperado: máximo de transcodificaciones simultáneas observado <= 3
# (produce 'maximo_observado' y 'resultados_transcodificacion')


# ============================================================================
# EJERCICIO 9 — AVANZADO — Proceso centinela con Event
# ============================================================================
# Un pipeline de ingesta de datos tiene un productor y un consumidor. Si el
# consumidor deja de procesar datos (el productor ha terminado y la cola se
# vació), un proceso "watchdog" debe detectar la inactividad y parar el
# sistema de forma ordenada, sin perder ningún dato producido.


def productor_datos(cola: multiprocessing.Queue, cantidad: int) -> None:
    for i in range(1, cantidad + 1):
        time.sleep(0.2)
        cola.put(i)


def consumidor_datos(cola, resultados, ultimo_procesado, evento_parada) -> None:
    while not evento_parada.is_set():
        try:
            dato = cola.get(timeout=0.1)
        except queue.Empty:
            continue
        resultados.append(dato)
        with ultimo_procesado.get_lock():
            ultimo_procesado.value = time.time()


# Completa watchdog(ultimo_procesado, evento_parada, umbral_inactividad):
# en bucle, mientras evento_parada no esté activo, duerme 0.1s y comprueba
# cuánto tiempo ha pasado desde ultimo_procesado.value; si supera
# umbral_inactividad, llama a evento_parada.set() y termina el bucle.
def watchdog(ultimo_procesado, evento_parada, umbral_inactividad: float) -> None:
    ...


# Crea (con Manager) una lista compartida de resultados, una Queue, un Value
# 'd' con time.time() inicial y un Event, lanza productor/consumidor/watchdog
# como 3 Process, espera a que terminen y comprueba que no se ha perdido
# ningún dato.
# Resultado esperado: Datos procesados sin pérdidas: [1, 2, 3, 4, 5]
# (produce 'resultados_ingesta' con los datos recogidos por el consumidor)


# ============================================================================
# EJERCICIO 10 — EXPERTO — Pipeline ETL multiproceso de dos etapas
# ============================================================================
# Un informe financiero diario necesita procesar 20 ventas en dos etapas:
# normalizarlas (convertir moneda, calcular impuestos) y luego agregarlas
# en totales por categoría. Ambas etapas son CPU-bound y se paralelizan.

TIPO_CAMBIO_USD_EUR = 0.92

ventas = [
    {"id": i, "categoria": categoria, "importe": importe}
    for i, (categoria, importe) in enumerate(
        [
            ("Electronica", 120.0), ("Ropa", 45.5), ("Hogar", 89.99), ("Alimentacion", 32.2),
            ("Electronica", 300.0), ("Ropa", 60.0), ("Hogar", 150.75), ("Alimentacion", 18.4),
            ("Electronica", 75.25), ("Ropa", 22.0), ("Hogar", 99.0), ("Alimentacion", 45.6),
            ("Electronica", 200.0), ("Ropa", 33.3), ("Hogar", 60.0), ("Alimentacion", 27.8),
            ("Electronica", 180.0), ("Ropa", 55.0), ("Hogar", 120.0), ("Alimentacion", 40.0),
        ],
        start=1,
    )
]


# Completa normalizar_lote(lote, tipo_cambio): para cada registro del lote,
# calcula importe_eur = importe * tipo_cambio (valida que sea >= 0) y
# impuesto = importe_eur * 0.21. Devuelve una lista de dicts
# {"categoria":, "importe_eur":, "impuesto":} por cada registro del lote.
def normalizar_lote(lote: list[dict], tipo_cambio: float) -> list[dict]:
    ...


def totales_por_categoria(lote_normalizado: list[dict]) -> dict[str, float]:
    totales: dict[str, float] = {}
    for registro in lote_normalizado:
        totales[registro["categoria"]] = totales.get(registro["categoria"], 0.0) + registro["importe_eur"]
    return totales


# Etapa 1: divide 'ventas' en 4 lotes de 5 y normaliza cada uno en paralelo
# con ProcessPoolExecutor. Etapa 2: calcula los totales por categoría de
# cada lote normalizado, también en paralelo, y combínalos en un único
# informe final. Verifica (con math.isclose) que el total del informe
# coincide con la suma de todos los importes originales aplicando
# TIPO_CAMBIO_USD_EUR.
# Resultado esperado: el total del informe coincide con el total esperado
# (produce 'informe_final', 'total_informe' y 'total_esperado')


if __name__ == "__main__":
    seccion("EJERCICIO 1 — FÁCIL — Renderizado de frames de un vídeo")
    try:
        ...
        assert resultados_secuenciales == resultados_paralelos
        print("Los 8 frames renderizados en paralelo coinciden con la versión secuencial")
    except (NameError, AssertionError):
        print("  (ejercicio sin resolver o solución incorrecta)")

    seccion("EJERCICIO 2 — FÁCIL — Proceso hijo que reporta su PID")
    try:
        ...
        assert len(set(pids_hijos)) == 4
        assert os.getpid() not in pids_hijos
        print(f"PIDs de los 4 hijos, todos distintos entre sí y del padre: {pids_hijos}")
    except (NameError, AssertionError):
        print("  (ejercicio sin resolver o solución incorrecta)")

    seccion("EJERCICIO 3 — MEDIO — Compresión paralela de ficheros de log")
    try:
        ...
        for (comprimido, _, _), original in zip(resultados_compresion, logs_simulados):
            assert zlib.decompress(comprimido).decode() == original
        tamano_original_total = sum(r[1] for r in resultados_compresion)
        tamano_comprimido_total = sum(r[2] for r in resultados_compresion)
        ratio = tamano_comprimido_total / tamano_original_total
        print(f"Ratio de compresión total: {ratio:.2%} (todos los logs se descomprimen igual al original)")
    except (NameError, AssertionError):
        print("  (ejercicio sin resolver o solución incorrecta)")

    seccion("EJERCICIO 4 — MEDIO — Pipeline de análisis de texto con Pipe")
    try:
        ...
        for titular_recibido, num_palabras in resultados:
            print(f"  '{titular_recibido}' -> {num_palabras} palabras")
    except NameError:
        print("  (ejercicio sin resolver)")

    seccion("EJERCICIO 5 — MEDIO — Búsqueda paralela en ficheros de configuración")
    try:
        ...
        print(f"Ficheros en modo producción: {ficheros_en_produccion}")
    except NameError:
        print("  (ejercicio sin resolver)")

    seccion("EJERCICIO 6 — MEDIO — Contador de visitas compartido entre workers")
    try:
        ...
        assert contador_visitas.valor == 4 * 500
        print(f"Visitas totales: {contador_visitas.valor} (4 workers x 500 visitas)")
    except (NameError, AssertionError):
        print("  (ejercicio sin resolver o solución incorrecta)")

    seccion("EJERCICIO 7 — AVANZADO — Acumulador de métricas con Manager dict")
    try:
        ...
        print(f"Latencia media global: {latencia_media_global:.2f}ms")
        print(f"Worker más lento: {worker_mas_lento} ({medias_por_worker[worker_mas_lento]:.2f}ms)")
    except NameError:
        print("  (ejercicio sin resolver)")

    seccion("EJERCICIO 8 — AVANZADO — Pool de transcodificación con límite de recursos")
    try:
        ...
        assert maximo_observado.value <= 3
        print(f"Máximo de transcodificaciones simultáneas observado: {maximo_observado.value} (límite: 3)")
        print(f"Vídeos procesados: {len(resultados_transcodificacion)}")
    except (NameError, AssertionError):
        print("  (ejercicio sin resolver o solución incorrecta)")

    seccion("EJERCICIO 9 — AVANZADO — Proceso centinela con Event")
    try:
        ...
        assert sorted(resultados_ingesta) == [1, 2, 3, 4, 5]
        print(f"Datos procesados sin pérdidas: {sorted(resultados_ingesta)}")
    except (NameError, AssertionError):
        print("  (ejercicio sin resolver o solución incorrecta)")

    seccion("EJERCICIO 10 — EXPERTO — Pipeline ETL multiproceso de dos etapas")
    try:
        ...
        assert math.isclose(total_informe, total_esperado, rel_tol=1e-9)
        informe_redondeado = {k: round(v, 2) for k, v in informe_final.items()}
        print(f"Informe final por categoría: {informe_redondeado}")
        print(f"Total informe: {total_informe:.2f}€ (coincide con el total esperado)")
    except (NameError, AssertionError):
        print("  (ejercicio sin resolver o solución incorrecta)")

    seccion("FIN — completa los ejercicios y compáralos con ejercicios_resueltos.py")
