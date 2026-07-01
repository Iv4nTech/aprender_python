
# ════════════════════════════════════════════════════════════════
#   ASYNC / AWAIT EN PYTHON  ·  guía didáctica  (Python 3.11+)
# ════════════════════════════════════════════════════════════════
#
#   LA IDEA EN UNA FRASE
#   --------------------
#   async/await sirve para que, mientras una tarea ESPERA (una
#   descarga, una consulta a la base de datos...), el programa
#   aproveche ese hueco para avanzar OTRAS tareas, en vez de quedarse
#   parado mirando el reloj.
#
#   LA ANALOGÍA DEL CAMARERO 🧑‍🍳
#   -----------------------------
#   Un camarero NO se queda plantado en la cocina esperando a que se
#   fría un huevo. Toma nota de la mesa 1, la pasa a cocina y, MIENTRAS
#   se cocina, atiende la mesa 2 y la 3. Un solo camarero (un solo
#   hilo) atiende muchas mesas porque no se queda bloqueado esperando.
#   Eso es exactamente async: un solo hilo que no pierde el tiempo
#   esperando.
#
#   OJO: async NO es paralelismo. Sigue siendo UN solo hilo. Es útil
#   cuando el cuello de botella es ESPERAR (red, disco, I/O), no
#   cuando es CALCULAR (para eso están procesos/hilos).
#
#   FUENTES OFICIALES usadas en esta guía:
#     · asyncio:            https://docs.python.org/es/3/library/asyncio.html
#     · Corrutinas y Tasks: https://docs.python.org/es/3/library/asyncio-task.html
#     · Modelo de datos:    https://docs.python.org/es/3/reference/datamodel.html#coroutines
# ════════════════════════════════════════════════════════════════

import asyncio
import time

SEP = '─' * 60

print()
print('═' * 60)
print('       ASYNC / AWAIT EN PYTHON')
print('═' * 60)


# ── 1. Una función async NO se ejecuta al llamarla ───────────────
print('\n  1. async def crea una CORRUTINA, no la ejecuta\n')

# Al poner 'async' delante de def, llamar a la función ya NO ejecuta
# su código: devuelve un objeto "corrutina" (una tarea preparada
# pero pausada). Es como una receta escrita: tenerla no es cocinar.

async def saludar():
    return '¡Hola desde una corrutina!'

resultado = saludar()          # esto NO ejecuta nada todavía
print(f'  → al llamarla obtienes: {resultado!r}')
print('    (fíjate: es un objeto corrutina, aún no se ejecutó)')
resultado.close()              # cerramos la corrutina que no vamos a usar

print(f'\n{SEP}')


# ── 2. asyncio.run: la puerta de entrada ─────────────────────────
print('\n  2. asyncio.run() arranca el motor y ejecuta la corrutina\n')

# Para EJECUTAR una corrutina necesitas un "event loop" (el motor que
# reparte el tiempo entre tareas). asyncio.run() lo crea, ejecuta tu
# corrutina hasta el final y lo cierra. Es tu único punto de entrada.

async def main_saludo():
    return await saludar_a('Ivan')

async def saludar_a(nombre):
    return f'¡Hola, {nombre}!'

print(f'  → {asyncio.run(main_saludo())}')

print(f'\n{SEP}')


# ── 3. await: "espera esto y déjame el turno a otros" ────────────
print('\n  3. await: ceder el control mientras se espera\n')

# await hace dos cosas: (1) espera a que la otra corrutina termine y
# (2) MIENTRAS espera, devuelve el control al event loop para que
# haga otras cosas. asyncio.sleep(n) simula una espera de red/disco.

async def preparar_cafe():
    print('    → poniendo el café...')
    await asyncio.sleep(1)          # simula 1s de espera (la máquina)
    print('    → café listo ☕')
    return 'café'

async def main_cafe():
    bebida = await preparar_cafe()
    print(f'    → sirvo: {bebida}')

asyncio.run(main_cafe())

print(f'\n{SEP}')


# ── 4. EL TRUCO: concurrencia real con gather ────────────────────
print('\n  4. Secuencial vs concurrente (cronómetro en mano)\n')

# Cada tarea "tarda" 1 segundo. Si las hacemos una detrás de otra,
# son 3 segundos. Pero si las lanzamos A LA VEZ con gather, mientras
# una espera avanzan las otras → ~1 segundo total.

async def tarea(nombre, segundos):
    await asyncio.sleep(segundos)
    return f'{nombre} lista'

async def modo_secuencial():
    await tarea('A', 1)
    await tarea('B', 1)
    await tarea('C', 1)

async def modo_concurrente():
    # gather lanza las tres A LA VEZ y espera a que acaben todas
    await asyncio.gather(
        tarea('A', 1),
        tarea('B', 1),
        tarea('C', 1),
    )

t0 = time.perf_counter()
asyncio.run(modo_secuencial())
print(f'  ✗ Secuencial:  {time.perf_counter() - t0:.2f}s  (1+1+1)')

t0 = time.perf_counter()
asyncio.run(modo_concurrente())
print(f'  ✓ Concurrente: {time.perf_counter() - t0:.2f}s  (todas a la vez)')

print(f'\n{SEP}')


# ── 5. create_task: lanzar en segundo plano ──────────────────────
print('\n  5. create_task(): empezar una tarea y seguir a lo tuyo\n')

# gather te obliga a esperar ahí mismo. create_task() ARRANCA la
# tarea ya y te devuelve un objeto Task; puedes seguir haciendo cosas
# y hacer 'await' de la task más tarde para recoger su resultado.

async def descargar(archivo):
    await asyncio.sleep(1)
    return f'{archivo} descargado'

async def main_tasks():
    # arrancan YA, en este mismo instante, sin esperar
    t1 = asyncio.create_task(descargar('foto.jpg'))
    t2 = asyncio.create_task(descargar('video.mp4'))
    print('    → tareas lanzadas, sigo trabajando mientras descargan...')
    print(f'    → {await t1}')
    print(f'    → {await t2}')

asyncio.run(main_tasks())

print(f'\n{SEP}')


# ── 6. TaskGroup: la forma MODERNA recomendada (3.11+) ───────────
print('\n  6. asyncio.TaskGroup: agrupar tareas de forma segura\n')

# Desde Python 3.11, la forma recomendada de lanzar varias tareas es
# TaskGroup. Ventaja sobre gather: si UNA tarea falla, cancela
# automáticamente a las demás y no deja tareas "sueltas". Se usa con
# 'async with'.

async def main_taskgroup():
    async with asyncio.TaskGroup() as tg:
        # create_task devuelve un Task; lo guardamos para leer su resultado
        t1 = tg.create_task(descargar('a.zip'))
        t2 = tg.create_task(descargar('b.zip'))
        t3 = tg.create_task(descargar('c.zip'))
    # AL SALIR del 'async with' TODAS han terminado. Como ya acabaron, el
    # valor está listo: se lee con .result() (no hace falta await aquí).
    for t in (t1, t2, t3):
        print(f'    → {t.result()}')

asyncio.run(main_taskgroup())

print(f'\n{SEP}')


# ── 7. Cortar por tiempo: asyncio.timeout (3.11+) ────────────────
print('\n  7. timeout: no esperar eternamente\n')

# A veces una tarea se atasca. 'async with asyncio.timeout(s)' lanza
# un TimeoutError si el bloque no acaba a tiempo. Perfecto para APIs
# lentas.

async def api_lenta():
    await asyncio.sleep(5)          # tarda demasiado
    return 'datos'

async def main_timeout():
    try:
        async with asyncio.timeout(1):     # máximo 1 segundo
            await api_lenta()
    except TimeoutError:
        print('    → la API tardó demasiado, cancelada a tiempo ⏱️')

asyncio.run(main_timeout())

print(f'\n{SEP}')


# ── 8. Manejar errores sin caerse: return_exceptions ─────────────
print('\n  8. Recoger errores con gather(return_exceptions=True)\n')

# Por defecto, si UNA tarea de gather falla, gather aborta y propaga
# el error (tumba todo). Con return_exceptions=True, los errores NO
# se lanzan: llegan como un valor más en la lista, en su posición.
# Luego los distingues con isinstance(x, Exception).

async def comprobar_web(url, activa):
    await asyncio.sleep(0.2)
    if not activa:
        raise ConnectionError(f'{url} no responde')
    return f'{url} OK'

async def main_errores():
    resultados = await asyncio.gather(
        comprobar_web('google.com', True),
        comprobar_web('miweb.roto', False),   # esta está caída
        comprobar_web('github.com', True),
        return_exceptions=True,         # los errores vienen como valores
    )
    for r in resultados:
        if isinstance(r, Exception):    # ¿es un error? (todos heredan de Exception)
            print(f'    ✗ error: {r}')
        else:
            print(f'    ✓ {r}')

asyncio.run(main_errores())

print(f'\n{SEP}')


# ── 9. Limitar cuántas tareas van a la vez: Semaphore ────────────
print('\n  9. Semaphore: como mucho N tareas simultáneas\n')

# A veces no quieres lanzar 100 tareas a la vez (un servidor te banea,
# saturas la red...). Un Semaphore(N) reparte N "permisos": solo N
# tareas entran a la vez con 'async with sem:'; las demás esperan
# turno hasta que se libera un permiso.

async def geocodificar(direccion, sem):
    async with sem:                     # pide un permiso (espera si no hay)
        await asyncio.sleep(0.3)        # la API tarda en responder
        return f'{direccion} → (lat, lon)'

async def main_semaphore():
    direcciones = ['Calle A', 'Calle B', 'Calle C', 'Calle D']
    sem = asyncio.Semaphore(2)          # la API solo admite 2 peticiones a la vez
    resultados = await asyncio.gather(*(geocodificar(d, sem) for d in direcciones))
    for r in resultados:
        print(f'    → {r}')
    print('    (se resolvieron de 2 en 2, sin saturar la API)')

asyncio.run(main_semaphore())

print(f'\n{SEP}')


# ── 10. Cola de trabajo: asyncio.Queue ───────────────────────────
print('\n  10. Queue: repartir trabajo entre varios workers\n')

# Una Queue es una cola de tareas pendientes. Varios "workers"
# (tareas) van sacando trabajo de la MISMA cola y lo procesan a la
# vez. Piezas clave:
#   cola.put(x)     → mete trabajo         cola.get()      → saca trabajo
#   cola.task_done()→ "ya terminé este"    await cola.join()→ espera a que
#                                            todo esté hecho

async def moderador(nombre, cola):
    while True:                          # el moderador vive esperando trabajo
        comentario = await cola.get()    # espera hasta que haya algo
        await asyncio.sleep(0.1)         # revisarlo
        print(f'    [{nombre}] revisó "{comentario}"')
        cola.task_done()                 # avisa: este comentario está revisado

async def main_queue():
    cola = asyncio.Queue()
    for texto in ['spam', 'hola', 'insulto', 'buen post']:
        cola.put_nowait(texto)           # llenamos la cola de comentarios
    # 2 moderadores cogiendo de la misma cola
    moderadores = [asyncio.create_task(moderador(f'Mod{n}', cola)) for n in (1, 2)]
    await cola.join()                    # espera a revisar TODOS
    for m in moderadores:                # los moderadores están en bucle infinito:
        m.cancel()                       # los cancelamos al acabar

asyncio.run(main_queue())

print(f'\n{SEP}')


# ── 11. Producir datos poco a poco: async generator + async for ──
print('\n  11. Generador asíncrono y async for (streams)\n')

# Un generador asíncrono es una 'async def' con 'yield': va ENTREGANDO
# valores de uno en uno y puede hacer 'await' entre ellos (esperar que
# llegue cada dato). Se recorre con 'async for', que espera cada valor
# y cede el turno mientras tanto. Ideal para datos paginados/streams.

async def cotizaciones(veces):
    precio = 100
    for _ in range(veces):
        await asyncio.sleep(0.2)         # llega una nueva cotización de bolsa
        precio += 5
        yield precio                     # la entrega en cuanto está

async def main_stream():
    async for precio in cotizaciones(3): # reacciona a cada precio según llega
        print(f'    → nuevo precio: {precio}€')

asyncio.run(main_stream())

print(f'\n{SEP}')


# ── 12. Recursos que se abren y cierran: async with ──────────────
print('\n  12. Context manager asíncrono (__aenter__/__aexit__)\n')

# Es tu tema de Context Managers, pero para recursos async (hacer
# login tarda). Defines __aenter__ (al entrar) y __aexit__ (al salir,
# SIEMPRE, aunque haya error) y lo usas con 'async with'. Garantiza
# que la sesión se cierra (logout) pase lo que pase.

class Sesion:
    async def __aenter__(self):
        await asyncio.sleep(0.1)         # hacer login (tarda)
        print('    → sesión iniciada (login)')
        return self
    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(0.1)         # cerrar sesión (siempre)
        print('    → sesión cerrada (logout)')
        return False                     # no silencia errores

async def main_sesion():
    async with Sesion():                 # login al entrar, logout al salir
        print('    → consultando datos con la sesión...')

asyncio.run(main_sesion())

print(f'\n{SEP}')


# ── 13. Cuándo NO usar async ─────────────────────────────────────
print('\n  13. async NO acelera los CÁLCULOS\n')

# async brilla con ESPERA (red, disco, bases de datos). Pero si tu
# tarea es puro cálculo (procesar imágenes, sumar millones de
# números), async NO ayuda: sigue siendo un solo hilo. Para CPU se
# usan hilos o procesos (threading / multiprocessing), no asyncio.

print('  → I/O (esperar): red, disco, BD ........ ✓ usa async')
print('  → CPU (calcular): números, imágenes .... ✗ usa procesos')

print(f'\n{SEP}\n')
print('  RESUMEN')
print('  · async def crea una corrutina; asyncio.run() la ejecuta.')
print('  · await = espera algo Y cede el turno mientras tanto.')
print('  · gather / TaskGroup lanzan tareas a la vez (concurrencia).')
print('  · create_task() arranca una tarea en segundo plano.')
print('  · gather(return_exceptions=True) recoge errores sin abortar.')
print('  · Semaphore limita cuántas tareas van a la vez.')
print('  · Queue + workers reparten trabajo entre varias tareas.')
print('  · async generator + async for = producir/consumir streams.')
print('  · async with (__aenter__/__aexit__) para recursos async.')
print('  · async sirve para ESPERAR (I/O), no para CALCULAR (CPU).')
print('═' * 60)
print()
