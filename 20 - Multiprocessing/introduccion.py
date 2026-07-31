"""
================================================================================
 MULTIPROCESSING EN PYTHON
 Ejecutar: python3 introduccion.py
================================================================================
"""

import multiprocessing
import os
import time
import zlib
from concurrent.futures import ProcessPoolExecutor


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. POR QUÉ THREADING NO ES SUFICIENTE: EL GIL
# ============================================================================
def contar_primos(inicio: int, fin: int) -> int:
    def es_primo(n: int) -> bool:
        if n < 2:
            return False
        for d in range(2, int(n**0.5) + 1):
            if n % d == 0:
                return False
        return True

    return sum(1 for n in range(inicio, fin) if es_primo(n))


# ============================================================================
# 2. multiprocessing.Process: EL BLOQUE BÁSICO
# ============================================================================
def reportar_pid_hijo() -> None:
    print(f"  [hijo]  os.getpid()={os.getpid()}  os.getppid()={os.getppid()}")


contador_padre = {"valor": 0}


def modificar_contador_en_hijo() -> None:
    contador_padre["valor"] += 100
    print(f"  [hijo]  contador_padre['valor'] = {contador_padre['valor']}")


# ============================================================================
# 4. Pool: EL EXECUTOR CLÁSICO
# ============================================================================
def procesar_pedido(id_pedido: int) -> int:
    # Caso real: recalcular impuestos y totales de un pedido es CPU-bound.
    total = sum(n * n for n in range(id_pedido * 20_000, id_pedido * 20_000 + 200_000))
    return total


# ============================================================================
# 5. ProcessPoolExecutor: LA FORMA MODERNA
# ============================================================================
def renderizar_miniatura(id_imagen: int) -> int:
    return sum(n * n for n in range(200_000))


# ============================================================================
# 6. COMUNICACIÓN ENTRE PROCESOS: Queue Y Pipe
# ============================================================================
def productor_ordenes(cola: multiprocessing.Queue) -> None:
    for orden in ["compra-BTC", "venta-ETH", "compra-SOL"]:
        cola.put(orden)
    cola.put(None)  # centinela: avisa al consumidor de que no hay más


def consumidor_ordenes(cola: multiprocessing.Queue) -> None:
    while True:
        orden = cola.get()
        if orden is None:
            break
        print(f"  [consumidor] procesando orden: {orden}")


def generador_titulares(conexion) -> None:
    titulares = ["Bolsa sube tras el dato de empleo", "Nueva ley fiscal entra en vigor"]
    for titular in titulares:
        conexion.send(titular)
    conexion.send(None)
    conexion.close()


# ============================================================================
# 7. MEMORIA COMPARTIDA: Value Y Array
# ============================================================================
def incrementar_sin_lock(contador, veces: int) -> None:
    for _ in range(veces):
        temporal = contador.value
        time.sleep(0.0001)  # simula un cálculo que tarda un poco
        contador.value = temporal + 1


def incrementar_con_lock(contador, veces: int) -> None:
    for _ in range(veces):
        with contador.get_lock():
            contador.value += 1


# ============================================================================
# 8. Manager: OBJETOS COMPARTIDOS DE ALTO NIVEL
# ============================================================================
def registrar_metricas(worker_id: int, resultados: dict) -> None:
    resultados[worker_id] = sum(range(worker_id * 1000, worker_id * 1000 + 1000))


# ============================================================================
# 9. SINCRONIZACIÓN: Lock, Event, Semaphore
# ============================================================================
def usar_recurso_limitado(semaforo, id_proceso: int) -> None:
    with semaforo:
        print(f"  proceso-{id_proceso} accede al recurso")
        time.sleep(0.2)
        print(f"  proceso-{id_proceso} libera el recurso")


def esperar_senal(evento) -> None:
    print("  [proceso] esperando señal...")
    evento.wait()
    print("  [proceso] señal recibida, continúo")


# Con forkserver/spawn (defecto en 3.14 en Linux, ver sección 3) el target de
# un Process/Pool tiene que ser localizable como atributo del módulo para
# poder "picklearse" y enviarse al proceso hijo. Una función definida DENTRO
# de "if __name__ == '__main__':" no cumple eso: existe solo como variable
# local de ese bloque, no como algo importable desde __mp_main__. Por eso
# TODAS las funciones objetivo de este fichero están a nivel de módulo, y
# dentro del bloque principal solo se orquesta (se crean Process/Pool y se
# llama a start/join/map).
def calcular_descuento(precio: float, porcentaje: float) -> float:
    return round(precio * (1 - porcentaje / 100), 2)


if __name__ == "__main__":
    # ========================================================================
    # 1. POR QUÉ THREADING NO ES SUFICIENTE: EL GIL
    # ========================================================================
    seccion("1. Por qué threading no es suficiente: el GIL")

    # Recordatorio: el GIL permite que solo un hilo ejecute bytecode Python a
    # la vez dentro de un proceso. Durante I/O (red, disco) el hilo libera el
    # GIL y otros avanzan; por eso threading brilla en I/O-bound (ver tema
    # anterior). Pero contar primos es puro cálculo: no hay ninguna espera
    # que libere el GIL, así que repartirlo en hilos no acelera nada.
    import threading

    RANGO_TOTAL = 1_000_000

    inicio = time.perf_counter()
    contar_primos(0, RANGO_TOTAL)
    duracion_serie = time.perf_counter() - inicio
    print(f"  Serie (1 sola llamada):        {duracion_serie:.3f}s")

    cuarto = RANGO_TOTAL // 4
    hilos_gil = [
        threading.Thread(target=contar_primos, args=(0, cuarto)),
        threading.Thread(target=contar_primos, args=(cuarto, cuarto * 2)),
        threading.Thread(target=contar_primos, args=(cuarto * 2, cuarto * 3)),
        threading.Thread(target=contar_primos, args=(cuarto * 3, RANGO_TOTAL)),
    ]
    inicio = time.perf_counter()
    for h in hilos_gil:
        h.start()
    for h in hilos_gil:
        h.join()
    duracion_threading = time.perf_counter() - inicio
    print(f"  threading (4 hilos):           {duracion_threading:.3f}s (no mejora, incluso puede empeorar)")

    with ProcessPoolExecutor(max_workers=4) as executor:
        inicio = time.perf_counter()
        list(executor.map(contar_primos, [0, cuarto, cuarto * 2, cuarto * 3],  [cuarto,  cuarto*2, cuarto*3,  RANGO_TOTAL]))
        duracion_multiproceso = time.perf_counter() - inicio
    print(f"  multiprocessing (4 procesos):  {duracion_multiproceso:.3f}s (paralelismo real en CPU)")

    # Regla que justifica todo lo que viene: si la tarea CALCULA (CPU-bound),
    # usa multiprocessing. Si la tarea ESPERA (I/O-bound), usa threading.

    # ========================================================================
    # 2. multiprocessing.Process: EL BLOQUE BÁSICO
    # ========================================================================
    seccion("2. multiprocessing.Process: el bloque básico")

    print(f"  [padre] os.getpid()={os.getpid()}")
    proceso = multiprocessing.Process(target=reportar_pid_hijo)
    proceso.start()
    proceso.join()

    # Cada proceso tiene su propia memoria: modificar una variable en el hijo
    # NO cambia lo que ve el padre, al contrario que con threading.
    print(f"  [padre] contador_padre['valor'] antes  = {contador_padre['valor']}")
    proceso_modificador = multiprocessing.Process(target=modificar_contador_en_hijo)
    proceso_modificador.start()
    proceso_modificador.join()
    print(f"  [padre] contador_padre['valor'] después = {contador_padre['valor']} (el hijo no pudo tocarlo)")

    # ========================================================================
    # 3. MÉTODO DE INICIO: fork, spawn, forkserver (Python 3.14)
    # ========================================================================
    seccion("3. Método de inicio: fork, spawn, forkserver (Python 3.14)")

    print(f"""
  fork:        (Unix) clona el proceso actual entero, memoria incluida.
               Rápido, pero si hay hilos activos en el padre puede heredar
               locks a medio adquirir y quedarse en deadlock en el hijo.
  spawn:       arranca un intérprete Python nuevo y limpio, sin heredar
               memoria. Más lento y necesita re-importar el módulo, pero
               es el más seguro y el único disponible en Windows/macOS.
  forkserver:  arranca un proceso servidor auxiliar (limpio, sin hilos) al
               principio, y cada nuevo proceso se crea haciendo fork de ESE
               servidor, no del proceso principal. Evita el deadlock de fork
               sin pagar el coste completo de spawn.
""")

    print(f"  Método de inicio activo en este sistema: {multiprocessing.get_start_method()}")

    # Novedad Python 3.14: en Unix (excepto macOS), el método por defecto
    # cambia de 'fork' a 'forkserver'. Motivo: si el proceso padre tiene
    # hilos vivos (algo común en apps reales: logging, pools, frameworks
    # web), fork() solo copia el hilo que llama a fork, y si otro hilo tenía
    # un lock interno de Python adquirido en ese instante, el hijo hereda el
    # lock ya bloqueado para siempre: deadlock silencioso e intermitente.
    # forkserver evita esto porque el servidor auxiliar no tiene esos hilos.
    print(f"  ¿Es forkserver el nuevo defecto en 3.14 (Unix, no macOS)?: {multiprocessing.get_start_method() == 'forkserver'}")

    # Si un caso concreto necesita explícitamente el comportamiento de fork
    # (más rápido, sin hilos peligrosos), se pide un contexto propio:
    contexto_fork = multiprocessing.get_context("fork")
    proceso_fork = contexto_fork.Process(target=reportar_pid_hijo)
    proceso_fork.start()
    proceso_fork.join()

    # El bloque "if __name__ == '__main__':" es obligatorio con spawn y
    # forkserver porque, al no heredar memoria, el proceso hijo RE-IMPORTA
    # el módulo desde cero para encontrar la función objetivo. Sin ese
    # guard, importar el módulo volvería a ejecutar todo el script y
    # lanzaría procesos hijos de forma infinita (fork bomb accidental).

    # ========================================================================
    # 4. Pool: EL EXECUTOR CLÁSICO
    # ========================================================================
    seccion("4. Pool: el executor clásico")

    ids_pedidos = list(range(1, 9))

    inicio = time.perf_counter()
    totales_serie = [procesar_pedido(i) for i in ids_pedidos]
    duracion_pool_serie = time.perf_counter() - inicio

    with multiprocessing.Pool(processes=4) as pool:
        inicio = time.perf_counter()
        totales_pool = pool.map(procesar_pedido, ids_pedidos)
        duracion_pool_paralelo = time.perf_counter() - inicio

    print(f"  Secuencial: {duracion_pool_serie:.3f}s  —  Pool (4 procesos): {duracion_pool_paralelo:.3f}s")
    print(f"  Resultados iguales: {totales_serie == totales_pool}")

    # starmap desempaqueta tuplas de argumentos, útil cuando la función
    # recibe varios parámetros por elemento.
    with multiprocessing.Pool(processes=2) as pool:
        pares_precio_descuento = [(100, 10), (250, 20), (80, 5)]
        descuentos = pool.starmap(calcular_descuento, pares_precio_descuento)
    print(f"  pool.starmap descuentos: {descuentos}")

    # apply_async: lanza una tarea suelta sin bloquear, y se recoge el
    # resultado más tarde con .get(). Útil para tareas asíncronas sueltas
    # que no encajan en un map() sobre una lista.
    with multiprocessing.Pool(processes=1) as pool:
        tarea_async = pool.apply_async(procesar_pedido, (1,))
        print(f"  apply_async().get() = {tarea_async.get()}")

    # ========================================================================
    # 5. ProcessPoolExecutor: LA FORMA MODERNA
    # ========================================================================
    seccion("5. ProcessPoolExecutor: la forma moderna")

    # Preferible a Pool en código moderno: misma interfaz que
    # ThreadPoolExecutor (basta cambiar la clase para pasar de hilos a
    # procesos), usa Future con .result() y propaga excepciones del proceso
    # hijo de forma limpia (Pool las serializa peor y silencia más fácil).
    with ProcessPoolExecutor(max_workers=4) as executor:
        futuros = [executor.submit(renderizar_miniatura, i) for i in range(4)]
        resultados_submit = [f.result() for f in futuros]
    print(f"  executor.submit + .result(): {len(resultados_submit)} miniaturas renderizadas")

    with ProcessPoolExecutor(max_workers=4) as executor:
        resultados_map = list(executor.map(renderizar_miniatura, range(4)))
    print(f"  executor.map: {len(resultados_map)} miniaturas renderizadas")

    print(f"  ProcessPoolExecutor.terminate_workers existe (3.14): {hasattr(ProcessPoolExecutor, 'terminate_workers')}")
    print(f"  ProcessPoolExecutor.kill_workers existe (3.14):      {hasattr(ProcessPoolExecutor, 'kill_workers')}")
    # terminate_workers() pide a los procesos que acaben con SIGTERM (dan
    # tiempo a limpiar); kill_workers() los mata en seco con SIGKILL. Útiles
    # para cancelar un pool colgado sin esperar a que el 'with' lo cierre.

    # Novedad 3.14: executor.map(..., buffersize=N) limita cuántos
    # resultados se mantienen en memoria a la espera de ser consumidos,
    # útil con iterables muy grandes para no acumularlos todos de golpe.
    with ProcessPoolExecutor(max_workers=2) as executor:
        resultados_buffer = []
        for result, i in enumerate(executor.map(renderizar_miniatura, range(100), buffersize=2)):
            print(i,result)
            resultados_buffer.append(result)
    print(f"  executor.map(buffersize=2): {len(resultados_buffer)} resultados (sin acumular todo en memoria)")

    # ========================================================================
    # 6. COMUNICACIÓN ENTRE PROCESOS: Queue Y Pipe
    # ========================================================================
    seccion("6. Comunicación entre procesos: Queue y Pipe")

    # Los procesos no comparten memoria (sección 2): para comunicarse
    # necesitan canales explícitos. Queue: varios productores/consumidores.
    cola_ordenes = multiprocessing.Queue()
    p_productor = multiprocessing.Process(target=productor_ordenes, args=(cola_ordenes,))
    p_consumidor = multiprocessing.Process(target=consumidor_ordenes, args=(cola_ordenes,))
    p_productor.start()
    p_consumidor.start()
    p_productor.join()
    p_consumidor.join()

    # Pipe: comunicación bidireccional punto a punto entre exactamente dos
    # procesos, más ligero que una Queue cuando solo hay un emisor y un
    # receptor.
    extremo_a, extremo_b = multiprocessing.Pipe()
    p_generador = multiprocessing.Process(target=generador_titulares, args=(extremo_a,))
    p_generador.start()
    while True:
        titular = extremo_b.recv()
        if titular is None:
            break
        print(f"  [main] titular recibido por Pipe: {titular}")
    p_generador.join()

    # Bidireccional y unidireccional: Pipe puede ser de ambos tipos. Por defecto es bidireccional

    # duplex=True (por defecto) → los DOS extremos pueden enviar y recibir
    conn_padre, conn_hijo = multiprocessing.Pipe(duplex=True)

    conn_padre.send("hola")      # padre envía
    print(f"  [hijo] mensaje recibido por Pipe: {conn_hijo.recv()}")             # hijo recibe

    conn_hijo.send("ok")         # hijo envía
    print(f"  [padre] mensaje recibido por Pipe: {conn_padre.recv()}")            # padre recibe

    # duplex=False → unidireccional, como una tubería Unix
    conn_recv, conn_send = multiprocessing.Pipe(duplex=False)
    conn_send.send("hola")       # solo puede enviar
    print(f"  [conn_recv] mensaje recibido por Pipe: {conn_recv.recv()}")             # solo puede recibir
    # conn_recv.send() → ERROR

    # ========================================================================
    # 7. MEMORIA COMPARTIDA: Value Y Array
    # ========================================================================
    seccion("7. Memoria compartida: Value y Array")

    contador_sin_lock = multiprocessing.Value("i", 0)
    procesos_sin_lock = [
        multiprocessing.Process(target=incrementar_sin_lock, args=(contador_sin_lock, 2000)) for _ in range(4)
    ]
    for p in procesos_sin_lock:
        p.start()
    for p in procesos_sin_lock:
        p.join()
    print(f"  Sin lock  — esperado: 8000 — obtenido: {contador_sin_lock.value} (race condition entre procesos)")

    contador_con_lock = multiprocessing.Value("i", 0)
    procesos_con_lock = [
        multiprocessing.Process(target=incrementar_con_lock, args=(contador_con_lock, 2000)) for _ in range(4)
    ]
    for p in procesos_con_lock:
        p.start()
    for p in procesos_con_lock:
        p.join()
    print(f"  Con lock  — esperado: 8000 — obtenido: {contador_con_lock.value}")

    # Array comparte un bloque de memoria de tipo fijo entre procesos, igual
    # que Value pero para varios elementos.
    precios_compartidos = multiprocessing.Array("d", [10.0, 20.0, 30.0])
    with precios_compartidos.get_lock():
        for i in range(len(precios_compartidos)):
            precios_compartidos[i] *= 1.21  # aplica IVA
    print(f"  Array compartido con IVA aplicado: {list(precios_compartidos)}")

    # Sin .get_lock(), leer-modificar-escribir sobre Value/Array tiene la
    # misma race condition de tres pasos que un contador de threading: entre
    # procesos, no solo entre hilos.

    # ========================================================================
    # 8. Manager: OBJETOS COMPARTIDOS DE ALTO NIVEL
    # ========================================================================
    seccion("8. Manager: objetos compartidos de alto nivel")

    with multiprocessing.Manager() as manager:
        resultados_metricas = manager.dict()
        procesos_metricas = [
            multiprocessing.Process(target=registrar_metricas, args=(i, resultados_metricas)) for i in range(1, 4)
        ]
        for p in procesos_metricas:
            p.start()
        for p in procesos_metricas:
            p.join()
        print(f"  dict compartido tras 3 workers: {dict(resultados_metricas)}")

        # Novedad 3.14: SyncManager.set() crea un set compartido entre
        # procesos, igual que ya existían dict() y list().
        etiquetas_compartidas = manager.set()
        etiquetas_compartidas.update({"urgente", "revisar", "urgente"})
        print(f"  set compartido (3.14): {etiquetas_compartidas}")

    # Aviso: Manager levanta un proceso servidor interno que intermedia cada
    # acceso (más overhead que Value/Array, que son memoria compartida
    # directa). Usarlo cuando hace falta la flexibilidad de dict/list/set,
    # no como opción por defecto para un simple contador.

    # ========================================================================
    # 9. SINCRONIZACIÓN: Lock, Event, Semaphore
    # ========================================================================
    seccion("9. Sincronización: Lock, Event, Semaphore")

    # Lock: igual que threading.Lock pero entre procesos (ya usado dentro de
    # Value.get_lock() en la sección 7).
    lock_procesos = multiprocessing.Lock()
    with lock_procesos:
        print("  Lock adquirido y liberado entre procesos sin problema")

    # Event: un proceso espera a que otro lo active, sin sondear en bucle.
    evento_listo = multiprocessing.Event()
    p_espera = multiprocessing.Process(target=esperar_senal, args=(evento_listo,))
    p_espera.start()
    time.sleep(0.3)
    print("  [main] doy la señal")
    evento_listo.set()
    p_espera.join()

    # Semaphore: limita cuántos procesos acceden a un recurso a la vez.
    # Caso real: como máximo 2 procesos pueden usar una "GPU" compartida.
    semaforo_recurso = multiprocessing.Semaphore(2)
    procesos_recurso = [
        multiprocessing.Process(target=usar_recurso_limitado, args=(semaforo_recurso, i)) for i in range(5)
    ]
    for p in procesos_recurso:
        p.start()
    for p in procesos_recurso:
        p.join()

    # ========================================================================
    # 10. CUÁNDO USAR QUÉ: TABLA DE DECISIÓN
    # ========================================================================
    seccion("10. Cuándo usar qué: tabla de decisión")

    print("""
    Herramienta                     Tarea ideal      Memoria compartida   Overhead arranque   Facilidad
    -------------------------------  ---------------  --------------------  ------------------  -----------
    threading                        I/O-bound        Directa (mismo proc)  Bajo                Media
    multiprocessing.Process directo  CPU-bound a medida  No (por defecto)   Medio-alto           Baja (control total, más código)
    multiprocessing.Pool             CPU-bound en lote   No (por defecto)   Medio-alto           Alta (map/starmap)
    ProcessPoolExecutor              CPU-bound en lote   No (por defecto)   Medio-alto           Alta (Futures, errores limpios)

    Regla práctica final:
      - El código pasa tiempo CALCULANDO (CPU)   -> multiprocessing
      - El código pasa tiempo ESPERANDO (I/O)    -> threading o asyncio
      - Necesitas lo más simple posible en CPU   -> ProcessPoolExecutor
""")

    seccion("FIN — ya conoces multiprocessing al 100%")
    print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
