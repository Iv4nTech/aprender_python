import time
import tracemalloc
from itertools import islice

SEP  = '─' * 58
SEP2 = '═' * 58
REGISTROS = 8_000_000


def decorador_tiempo_memoria(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        _, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f'  ⏱  Tiempo  : {fin - inicio:.3f} s')
        print(f'  💾 Memoria : {pico / 1024 / 1024:.1f} MB (pico)')
        return resultado
    return wrapper


# ══════════════════════════════════════════════════════════
#  BENCHMARK 1 — MEMORIA
#  Procesar 8 millones de transacciones de principio a fin
# ══════════════════════════════════════════════════════════

@decorador_tiempo_memoria
def procesar_listas(n):
    # 3 listas completas cargadas en RAM al mismo tiempo
    registros  = [f'TX-{i}|{"ERR" if i % 7 == 0 else "OK"}|{i * 1.5:.2f}'
                  for i in range(n)]
    errores    = [r for r in registros   if '|ERR|' in r]
    importes   = [float(r.split('|')[2]) for r in errores]
    return sum(importes)


def _gen_registros(n):
    for i in range(n):
        yield f'TX-{i}|{"ERR" if i % 7 == 0 else "OK"}|{i * 1.5:.2f}'

def _gen_errores(registros):
    for r in registros:
        if '|ERR|' in r:
            yield r

def _gen_importes(registros):
    for r in registros:
        yield float(r.split('|')[2])

@decorador_tiempo_memoria
def procesar_generadores(n):
    # Pipeline perezoso — nunca hay más de 1 registro en memoria
    pipeline = _gen_importes(_gen_errores(_gen_registros(n)))
    return sum(pipeline)


# ══════════════════════════════════════════════════════════
#  BENCHMARK 2 — TIEMPO (terminación temprana)
#  Solo necesitamos las primeras 5 transacciones > 1.000.000€
#  Listas: procesa los 8M igualmente. Generadores: para al 5º.
# ══════════════════════════════════════════════════════════

BUSCAR = 5  # solo queremos los primeros 5 resultados

@decorador_tiempo_memoria
def buscar_con_listas(n):
    registros = [f'TX-{i}|{"ERR" if i % 7 == 0 else "OK"}|{i * 1.5:.2f}'
                 for i in range(n)]
    errores   = [r for r in registros   if '|ERR|' in r]
    importes  = [float(r.split('|')[2]) for r in errores if float(r.split('|')[2]) > 1_000_000]
    return importes[:BUSCAR]  # ya procesó todo, ahora descarta


@decorador_tiempo_memoria
def buscar_con_generadores(n):
    grandes = (
        float(r.split('|')[2])
        for r in _gen_errores(_gen_registros(n))
        if float(r.split('|')[2]) > 1_000_000
    )
    return list(islice(grandes, BUSCAR))  # para en cuanto tiene 5


# ══════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════

print()
print(SEP2)
print('    GENERADORES vs LISTAS — BENCHMARK EXTREMO')
print(f'    {REGISTROS:,} registros de transacciones')
print(SEP2)

# ── Benchmark 1 ──────────────────────────────────────────
print('\n  [ BENCHMARK 1 — MEMORIA ]')
print(f'  Sumar todos los importes con error\n')

print(f'  ❌  CON LISTAS  (3 listas completas en RAM)\n')
r1 = procesar_listas(REGISTROS)
print(f'  → Resultado: {r1:,.2f}€')

print(f'\n{SEP}\n')

print(f'  ✅  CON GENERADORES  (pipeline perezoso, sin listas)\n')
r2 = procesar_generadores(REGISTROS)
print(f'  → Resultado: {r2:,.2f}€')

print(f'\n{SEP}')
print(f'  Resultados idénticos : {r1 == r2}')

# ── Benchmark 2 ──────────────────────────────────────────
print(f'\n{SEP2}')
print('\n  [ BENCHMARK 2 — TIEMPO ]')
print(f'  Encontrar las primeras {BUSCAR} transacciones > 1.000.000€\n')

print(f'  ❌  CON LISTAS  (procesa los {REGISTROS:,} aunque solo necesita {BUSCAR})\n')
r3 = buscar_con_listas(REGISTROS)
print(f'  → Encontradas: {r3[:2]}...')

print(f'\n{SEP}\n')

print(f'  ✅  CON GENERADORES  (para en cuanto encuentra {BUSCAR})\n')
r4 = buscar_con_generadores(REGISTROS)
print(f'  → Encontradas: {r4[:2]}...')

print(f'\n{SEP2}\n')
