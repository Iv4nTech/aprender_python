"""
================================================================================
 EJERCICIOS RESUELTOS: MULTIPROCESSING EN PYTHON
 Casos reales — de fácil a experto
 Ejecutar: python3 ejercicios_resueltos.py
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


# Con forkserver/spawn (defecto en 3.14 en Linux) el target de un
# Process/Pool tiene que ser localizable como atributo del módulo, así que
# TODAS las funciones y clases objetivo de este fichero están a nivel de
# módulo. El bloque "if __name__ == '__main__':" del final solo orquesta:
# crea Process/Pool/Manager y llama a start/join/map.


# ============================================================================
# EJERCICIO 1 — FÁCIL — Renderizado de frames de un vídeo
# ============================================================================
def renderizar_frame(pixeles: list[int]) -> list[int]:
    return [((p * 37 + 11) % 256) for p in pixeles]


frames = [[(i * 3 + j) % 256 for j in range(500)] for i in range(8)]


# ============================================================================
# EJERCICIO 2 — FÁCIL — Proceso hijo que reporta su PID
# ============================================================================
def reportar_pid_hijo(cola: multiprocessing.Queue) -> None:
    cola.put((os.getpid(), os.getppid()))


# ============================================================================
# EJERCICIO 3 — MEDIO — Compresión paralela de ficheros de log
# ============================================================================
def comprimir_log(texto: str) -> tuple[bytes, int, int]:
    comprimido = zlib.compress(texto.encode())
    return comprimido, len(texto.encode()), len(comprimido)


logs_simulados = [f"{i:04d} INFO petición procesada correctamente\n" * 300 for i in range(6)]


# ============================================================================
# EJERCICIO 4 — MEDIO — Pipeline de análisis de texto con Pipe
# ============================================================================
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


# ============================================================================
# EJERCICIO 5 — MEDIO — Búsqueda paralela en ficheros de configuración
# ============================================================================
def contiene_clave_valor(fichero: dict, clave: str, valor) -> bool:
    return fichero.get(clave) == valor


configs = [
    {"nombre": f"config-{i}.json", "host": f"10.0.0.{i}", "puerto": 8080, "modo": modo}
    for i, modo in enumerate(
        ["produccion", "desarrollo", "produccion", "test", "produccion", "desarrollo", "test", "produccion"],
        start=1,
    )
]


# ============================================================================
# EJERCICIO 6 — MEDIO — Contador de visitas compartido entre workers
# ============================================================================
# SOLUCIÓN
class ContadorVisitas:
    def __init__(self) -> None:
        self._valor = multiprocessing.Value("i", 0)
        self._lock = multiprocessing.Lock()

    def registrar_visita(self) -> None:
        with self._lock:
            self._valor.value += 1

    @property
    def valor(self) -> int:
        return self._valor.value


def trabajo_worker(contador: ContadorVisitas) -> None:
    for _ in range(500):
        contador.registrar_visita()


# ============================================================================
# EJERCICIO 7 — AVANZADO — Acumulador de métricas con Manager dict
# ============================================================================
def generar_metricas(worker_id: int, resultados: dict) -> None:
    resultados[worker_id] = [50 + worker_id * 10 + i for i in range(6)]


# ============================================================================
# EJERCICIO 8 — AVANZADO — Pool de transcodificación con límite de recursos
# ============================================================================
videos = [(f"video-{i}.mp4", resolucion, duracion) for i, (resolucion, duracion) in enumerate(
    [
        ("1080p", 30), ("720p", 45), ("4K", 20), ("1080p", 60), ("720p", 15),
        ("4K", 25), ("1080p", 40), ("720p", 50), ("4K", 35), ("1080p", 10),
    ],
    start=1,
)]


# Un Semaphore/Value pasado como argumento normal de pool.starmap() no
# funciona: las tareas de un Pool viajan a los workers ya arrancados por una
# cola normal, con pickling estándar, y los objetos de sincronización de
# multiprocessing solo se pueden compartir "por herencia" (en el momento en
# que se crea el proceso, como en Process(args=...)), no metidos después en
# una cola. La solución estándar es un initializer de Pool: se ejecuta una
# vez por worker, AL CREAR el pool (ahí sí hay herencia), y guarda los
# objetos compartidos en variables globales del proceso worker.
_semaforo_gpu = None
_contador_activos = None
_maximo_observado = None
_lock_contador = None


def _inicializar_worker_gpu(semaforo, contador_activos, maximo_observado, lock_contador) -> None:
    global _semaforo_gpu, _contador_activos, _maximo_observado, _lock_contador
    _semaforo_gpu = semaforo
    _contador_activos = contador_activos
    _maximo_observado = maximo_observado
    _lock_contador = lock_contador


# SOLUCIÓN
def transcodificar_video(nombre: str, resolucion: str, duracion: int) -> str:
    with _semaforo_gpu:
        with _lock_contador:
            _contador_activos.value += 1
            if _contador_activos.value > _maximo_observado.value:
                _maximo_observado.value = _contador_activos.value
        time.sleep(0.05)
        with _lock_contador:
            _contador_activos.value -= 1
    return f"{nombre} transcodificado a {resolucion}"


# ============================================================================
# EJERCICIO 9 — AVANZADO — Proceso centinela con Event
# ============================================================================
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


# SOLUCIÓN
def watchdog(ultimo_procesado, evento_parada, umbral_inactividad: float) -> None:
    while not evento_parada.is_set():
        time.sleep(0.1)
        inactivo = time.time() - ultimo_procesado.value
        if inactivo > umbral_inactividad:
            evento_parada.set()


# ============================================================================
# EJERCICIO 10 — EXPERTO — Pipeline ETL multiproceso de dos etapas
# ============================================================================
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


# SOLUCIÓN
def normalizar_lote(lote: list[dict], tipo_cambio: float) -> list[dict]:
    normalizado = []
    for registro in lote:
        importe_eur = registro["importe"] * tipo_cambio
        assert importe_eur >= 0
        impuesto = importe_eur * 0.21
        normalizado.append({"categoria": registro["categoria"], "importe_eur": importe_eur, "impuesto": impuesto})
    return normalizado


def totales_por_categoria(lote_normalizado: list[dict]) -> dict[str, float]:
    totales: dict[str, float] = {}
    for registro in lote_normalizado:
        totales[registro["categoria"]] = totales.get(registro["categoria"], 0.0) + registro["importe_eur"]
    return totales


if __name__ == "__main__":
    # ========================================================================
    # EJERCICIO 1 — FÁCIL — Renderizado de frames de un vídeo
    # ========================================================================
    seccion("EJERCICIO 1 — FÁCIL — Renderizado de frames de un vídeo")

    # SOLUCIÓN
    resultados_secuenciales = [renderizar_frame(f) for f in frames]
    with ProcessPoolExecutor() as executor:
        resultados_paralelos = list(executor.map(renderizar_frame, frames))
    assert resultados_secuenciales == resultados_paralelos
    print("Los 8 frames renderizados en paralelo coinciden con la versión secuencial")

    # ========================================================================
    # EJERCICIO 2 — FÁCIL — Proceso hijo que reporta su PID
    # ========================================================================
    seccion("EJERCICIO 2 — FÁCIL — Proceso hijo que reporta su PID")

    # SOLUCIÓN
    cola_pids = multiprocessing.Queue()
    procesos_pid = [multiprocessing.Process(target=reportar_pid_hijo, args=(cola_pids,)) for _ in range(4)]
    for p in procesos_pid:
        p.start()
    for p in procesos_pid:
        p.join()
    pids_hijos = [cola_pids.get()[0] for _ in range(4)]
    assert len(set(pids_hijos)) == 4
    assert os.getpid() not in pids_hijos
    print(f"PIDs de los 4 hijos, todos distintos entre sí y del padre: {pids_hijos}")

    # ========================================================================
    # EJERCICIO 3 — MEDIO — Compresión paralela de ficheros de log
    # ========================================================================
    seccion("EJERCICIO 3 — MEDIO — Compresión paralela de ficheros de log")

    # SOLUCIÓN
    with multiprocessing.Pool(processes=4) as pool:
        resultados_compresion = pool.map(comprimir_log, logs_simulados)
    tamano_original_total = sum(r[1] for r in resultados_compresion)
    tamano_comprimido_total = sum(r[2] for r in resultados_compresion)
    for (comprimido, _, _), original in zip(resultados_compresion, logs_simulados):
        assert zlib.decompress(comprimido).decode() == original
    ratio = tamano_comprimido_total / tamano_original_total
    print(f"Ratio de compresión total: {ratio:.2%} (todos los logs se descomprimen igual al original)")

    # ========================================================================
    # EJERCICIO 4 — MEDIO — Pipeline de análisis de texto con Pipe
    # ========================================================================
    seccion("EJERCICIO 4 — MEDIO — Pipeline de análisis de texto con Pipe")

    # SOLUCIÓN
    extremo_main, extremo_worker = multiprocessing.Pipe()
    proceso_contador = multiprocessing.Process(target=contador_de_palabras, args=(extremo_worker,))
    proceso_contador.start()
    for titular in titulares:
        extremo_main.send(titular)
        titular_recibido, num_palabras = extremo_main.recv()
        print(f"  '{titular_recibido}' -> {num_palabras} palabras")
    extremo_main.send(None)
    proceso_contador.join()

    # ========================================================================
    # EJERCICIO 5 — MEDIO — Búsqueda paralela en ficheros de configuración
    # ========================================================================
    seccion("EJERCICIO 5 — MEDIO — Búsqueda paralela en ficheros de configuración")

    # SOLUCIÓN
    with ProcessPoolExecutor() as executor:
        coincidencias = list(
            executor.map(contiene_clave_valor, configs, itertools.repeat("modo"), itertools.repeat("produccion"))
        )
    ficheros_en_produccion = [c["nombre"] for c, coincide in zip(configs, coincidencias) if coincide]
    print(f"Ficheros en modo producción: {ficheros_en_produccion}")

    # ========================================================================
    # EJERCICIO 6 — MEDIO — Contador de visitas compartido entre workers
    # ========================================================================
    seccion("EJERCICIO 6 — MEDIO — Contador de visitas compartido entre workers")

    # SOLUCIÓN
    contador_visitas = ContadorVisitas()
    workers_visitas = [multiprocessing.Process(target=trabajo_worker, args=(contador_visitas,)) for _ in range(4)]
    for w in workers_visitas:
        w.start()
    for w in workers_visitas:
        w.join()
    assert contador_visitas.valor == 4 * 500
    print(f"Visitas totales: {contador_visitas.valor} (4 workers x 500 visitas)")

    # ========================================================================
    # EJERCICIO 7 — AVANZADO — Acumulador de métricas con Manager dict
    # ========================================================================
    seccion("EJERCICIO 7 — AVANZADO — Acumulador de métricas con Manager dict")

    # SOLUCIÓN
    with multiprocessing.Manager() as manager:
        resultados_metricas = manager.dict()
        workers_metricas = [
            multiprocessing.Process(target=generar_metricas, args=(i, resultados_metricas)) for i in range(1, 6)
        ]
        for w in workers_metricas:
            w.start()
        for w in workers_metricas:
            w.join()
        todas_las_mediciones = [m for mediciones in resultados_metricas.values() for m in mediciones]
        latencia_media_global = sum(todas_las_mediciones) / len(todas_las_mediciones)
        medias_por_worker = {w: sum(m) / len(m) for w, m in resultados_metricas.items()}
        worker_mas_lento = max(medias_por_worker, key=medias_por_worker.get)
    print(f"Latencia media global: {latencia_media_global:.2f}ms")
    print(f"Worker más lento: {worker_mas_lento} ({medias_por_worker[worker_mas_lento]:.2f}ms)")

    # ========================================================================
    # EJERCICIO 8 — AVANZADO — Pool de transcodificación con límite de recursos
    # ========================================================================
    seccion("EJERCICIO 8 — AVANZADO — Pool de transcodificación con límite de recursos")

    # SOLUCIÓN
    semaforo_gpu = multiprocessing.Semaphore(3)
    contador_activos = multiprocessing.Value("i", 0)
    maximo_observado = multiprocessing.Value("i", 0)
    lock_contador = multiprocessing.Lock()
    with multiprocessing.Pool(
        processes=6,
        initializer=_inicializar_worker_gpu,
        initargs=(semaforo_gpu, contador_activos, maximo_observado, lock_contador),
    ) as pool:
        resultados_transcodificacion = pool.starmap(transcodificar_video, videos)
    assert maximo_observado.value <= 3
    print(f"Máximo de transcodificaciones simultáneas observado: {maximo_observado.value} (límite: 3)")
    print(f"Vídeos procesados: {len(resultados_transcodificacion)}")

    # ========================================================================
    # EJERCICIO 9 — AVANZADO — Proceso centinela con Event
    # ========================================================================
    seccion("EJERCICIO 9 — AVANZADO — Proceso centinela con Event")

    # SOLUCIÓN
    with multiprocessing.Manager() as manager:
        resultados_ingesta = manager.list()
        cola_datos = multiprocessing.Queue()
        ultimo_procesado = multiprocessing.Value("d", time.time())
        evento_parada = multiprocessing.Event()
        p_productor = multiprocessing.Process(target=productor_datos, args=(cola_datos, 5))
        p_consumidor = multiprocessing.Process(
            target=consumidor_datos, args=(cola_datos, resultados_ingesta, ultimo_procesado, evento_parada)
        )
        p_watchdog = multiprocessing.Process(target=watchdog, args=(ultimo_procesado, evento_parada, 1.0))
        p_productor.start()
        p_consumidor.start()
        p_watchdog.start()
        p_productor.join()
        p_consumidor.join()
        p_watchdog.join()
        assert sorted(resultados_ingesta) == [1, 2, 3, 4, 5]
        print(f"Datos procesados sin pérdidas: {sorted(resultados_ingesta)}")

    # ========================================================================
    # EJERCICIO 10 — EXPERTO — Pipeline ETL multiproceso de dos etapas
    # ========================================================================
    seccion("EJERCICIO 10 — EXPERTO — Pipeline ETL multiproceso de dos etapas")

    # SOLUCIÓN
    lotes = [ventas[0:5], ventas[5:10], ventas[10:15], ventas[15:20]]
    with ProcessPoolExecutor() as executor:
        lotes_normalizados = list(executor.map(normalizar_lote, lotes, itertools.repeat(TIPO_CAMBIO_USD_EUR)))
    with ProcessPoolExecutor() as executor:
        totales_parciales = list(executor.map(totales_por_categoria, lotes_normalizados))
    informe_final: dict[str, float] = {}
    for parcial in totales_parciales:
        for categoria, total in parcial.items():
            informe_final[categoria] = informe_final.get(categoria, 0.0) + total
    total_informe = sum(informe_final.values())
    total_esperado = sum(v["importe"] for v in ventas) * TIPO_CAMBIO_USD_EUR
    assert math.isclose(total_informe, total_esperado, rel_tol=1e-9)
    informe_redondeado = {k: round(v, 2) for k, v in informe_final.items()}
    print(f"Informe final por categoría: {informe_redondeado}")
    print(f"Total informe: {total_informe:.2f}€ (coincide con el total esperado)")

    seccion("FIN — 10/10 ejercicios resueltos")
