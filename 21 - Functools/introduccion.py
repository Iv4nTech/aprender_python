"""
================================================================================
 FUNCTOOLS EN PYTHON
 Ejecutar: python3 introduccion.py
================================================================================
"""

import time
from functools import partial, lru_cache, cache, reduce, wraps, cached_property, Placeholder


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA: FUNCIONES QUE REPITEN CONFIGURACIÓN
# ============================================================================
seccion("1. El problema: funciones que repiten configuración")


def llamar_api_pagos(endpoint: str, version: str, base_url: str, headers: dict, payload: dict) -> str:
    # Simula una llamada HTTP real sin depender de una librería externa.
    return f"POST {base_url}/{version}/{endpoint} headers={headers} payload={payload}"


# Sin partial: base_url y headers se repiten en cada llamada, con riesgo
# de que alguien copie mal un header y rompa un endpoint en producción.
headers_comunes = {"Authorization": "Bearer token123", "Content-Type": "application/json"}
r1 = llamar_api_pagos("cobros", "v1", "https://api.pagos.com", headers_comunes, {"importe": 50})
r2 = llamar_api_pagos("reembolsos", "v1", "https://api.pagos.com", headers_comunes, {"importe": 20})
r3 = llamar_api_pagos("cobros", "v2", "https://api.pagos.com", headers_comunes, {"importe": 99})
print("  Sin partial (repitiendo base_url y headers cada vez):")
print(f"    {r1}")
print(f"    {r2}")
print(f"    {r3}")

# Con partial: base_url y headers quedan "congelados" una sola vez.
api_pagos = partial(llamar_api_pagos, base_url="https://api.pagos.com", headers=headers_comunes)
print("\n  Con partial (base_url y headers fijados una sola vez):")
print(f"    {api_pagos('cobros', 'v1', payload={'importe': 50})}")
print(f"    {api_pagos('reembolsos', 'v1', payload={'importe': 20})}")
print(f"    {api_pagos('cobros', 'v2', payload={'importe': 99})}")

# partial es un objeto inspeccionable: guarda qué congeló, separando
# posicionales (.args) de nombrados (.keywords). Aquí .args sale vacío
# porque base_url y headers se fijaron como keyword, no por posición.
print(f"\n  api_pagos.func     = {api_pagos.func.__name__}")
print(f"  api_pagos.args     = {api_pagos.args}  (vacío: no fijamos nada por posición)")
print(f"  api_pagos.keywords = {api_pagos.keywords}")

# ¿Por qué no usar simplemente argumentos por defecto en la función en vez de
# partial? Porque un valor por defecto es UNO SOLO, fijado para siempre en la
# definición. Si la app tiene que hablar con producción Y con el sandbox de
# pruebas, un default no puede servir a los dos a la vez: solo partial permite
# crear, a partir de la MISMA función, dos configuraciones distintas sin
# tocar ni duplicar la definición original.
api_pagos_sandbox = partial(
    llamar_api_pagos,
    base_url="https://sandbox.pagos.com",
    headers={"Authorization": "Bearer sandbox-token", "Content-Type": "application/json"},
)
print("\n  Misma función, dos configuraciones (producción vs sandbox):")
print(f"    {api_pagos('cobros', 'v1', payload={'importe': 50})}")
print(f"    {api_pagos_sandbox('cobros', 'v1', payload={'importe': 50})}")


# ============================================================================
# 2. partial CON Placeholder (NOVEDAD 3.14)
# ============================================================================
seccion("2. partial con Placeholder (novedad 3.14)")


def enviar_mensaje(destinatario: str, canal: str, mensaje: str) -> str:
    return f"[{canal}] para {destinatario}: {mensaje}"


# partial clásico solo permite fijar los PRIMEROS argumentos posicionales.
# Si queremos fijar "canal" (el segundo) dejando "destinatario" libre,
# antes de 3.14 había dos salidas: kwarg (si el parámetro lo admite) o un
# lambda que reordena los argumentos a mano (funciona siempre, pero exige
# escribir un wrapper nuevo por cada combinación de argumentos fijos).
push_clasico = partial(enviar_mensaje, canal="push")  # esto sí, vía kwarg
print(f"  Con kwarg (ya funcionaba): {push_clasico('ana@empresa.com', mensaje='Tu pedido ha salido')}")

push_con_lambda = lambda destinatario, mensaje: enviar_mensaje(destinatario, "push", mensaje)
print(f"  Con lambda (sin depender de kwargs): "
      f"{push_con_lambda('ana@empresa.com', 'Tu pedido ha salido')}")

# Con Placeholder: se fija "canal" por posición, dejando un hueco explícito
# para "destinatario" (que ocupa el Placeholder) y el resto de posicionales
# que se pasen después ("mensaje") se añaden a continuación de "push". Mismo
# resultado que el lambda, pero sin escribir una función nueva a mano.
push_con_placeholder = partial(enviar_mensaje, Placeholder, "push")
print(f"  Con Placeholder (fija el 2º arg posicional): "
      f"{push_con_placeholder('ana@empresa.com', 'Tu pedido ha salido')}")

# Diferencia práctica: Placeholder permite fijar una posición que NO es
# la primera sin recurrir a un keyword. Antes de 3.14, si la función no
# aceptaba ese argumento como keyword, no había forma limpia de hacerlo.
sms_urgente = partial(enviar_mensaje, Placeholder, "sms")
print(f"  Otro canal reutilizando el mismo patrón: "
      f"{sms_urgente('600111222', 'Código de verificación: 4471')}")


# ============================================================================
# 3. @lru_cache: NO CALCULES LO MISMO DOS VECES
# ============================================================================
seccion("3. @lru_cache: no calcules lo mismo dos veces")


def consultar_impuestos_bd(pais: str) -> float:
    # Simula una consulta lenta a base de datos (I/O real tardaría similar).
    time.sleep(0.2)
    tasas = {"ES": 0.21, "FR": 0.20, "DE": 0.19, "IT": 0.22}
    return tasas.get(pais, 0.0)


# maxsize NO es una unidad de memoria (bytes, MB...): es un número de
# ENTRADAS. Cuenta combinaciones distintas de argumentos, no cuánto pesa
# cada una. maxsize=128 significa "recuerda hasta 128 llamadas distintas".
@lru_cache(maxsize=128)
def calcular_impuesto_cacheado(pais: str, importe: float) -> float:
    tasa = consultar_impuestos_bd(pais)
    return round(importe * tasa, 2)


inicio = time.perf_counter()
calcular_impuesto_cacheado("ES", 100.0)
duracion_primera = time.perf_counter() - inicio

inicio = time.perf_counter()
calcular_impuesto_cacheado("ES", 100.0)
duracion_segunda = time.perf_counter() - inicio

print(f"  1ª llamada (falla la cache, consulta BD): {duracion_primera:.3f}s")
print(f"  2ª llamada (acierta la cache):             {duracion_segunda:.3f}s")

calcular_impuesto_cacheado("FR", 200.0)
calcular_impuesto_cacheado("ES", 100.0)  # ya en cache, no cuenta como miss
info = calcular_impuesto_cacheado.cache_info()
print(f"  cache_info(): hits={info.hits} misses={info.misses} "
      f"maxsize={info.maxsize} currsize={info.currsize}")

calcular_impuesto_cacheado.cache_clear()
print(f"  Tras cache_clear(): {calcular_impuesto_cacheado.cache_info()}")
print("  Se invalida, por ejemplo, cuando las tasas de impuestos cambian "
      "y los valores cacheados ya no son válidos.")

# Restricción: los argumentos deben ser hashables. Una lista no lo es.
try:
    calcular_impuesto_cacheado("ES", [100.0])
except TypeError as e:
    print(f"  Pasar una lista rompe la cache: TypeError: {e}")

# Evicción real: con maxsize=2, la 3ª combinación distinta de argumentos
# desaloja a la MENOS USADA RECIENTEMENTE (LRU) para hacer sitio.
@lru_cache(maxsize=2)
def calcular_impuesto_pequeno(pais: str, importe: float) -> float:
    return round(importe * consultar_impuestos_bd(pais), 2)


calcular_impuesto_pequeno("ES", 100.0)   # currsize=1
calcular_impuesto_pequeno("FR", 200.0)   # currsize=2 (lleno)
calcular_impuesto_pequeno("DE", 80.0)    # entra DE, se desaloja ES (el menos usado)
print(f"\n  maxsize=2 tras 3 combinaciones distintas: {calcular_impuesto_pequeno.cache_info()}")
inicio = time.perf_counter()
calcular_impuesto_pequeno("ES", 100.0)   # ES ya no está: vuelve a consultar la BD
duracion_es_desalojado = time.perf_counter() - inicio
print(f"  Recalcular ES (fue desalojado): {duracion_es_desalojado:.3f}s (miss, no estaba)")


# ============================================================================
# 4. @cache: lru_cache SIN LÍMITE, MÁS LIGERO
# ============================================================================
seccion("4. @cache: lru_cache sin límite, más ligero")

grafo_rutas = {
    "Madrid": ["Barcelona", "Valencia"],
    "Barcelona": ["Madrid", "Zaragoza"],
    "Valencia": ["Madrid", "Alicante"],
    "Zaragoza": ["Barcelona"],
    "Alicante": ["Valencia"],
}


@cache
def vecinos_de(ciudad: str) -> tuple:
    # El grafo no cambia en runtime: no hace falta evicción LRU, solo memoria.
    time.sleep(0.05)
    return tuple(grafo_rutas.get(ciudad, []))


inicio = time.perf_counter()
vecinos_de("Madrid")
duracion_primera = time.perf_counter() - inicio

inicio = time.perf_counter()
vecinos_de("Madrid")
duracion_segunda = time.perf_counter() - inicio

print(f"  1ª consulta de vecinos (sin cache):  {duracion_primera:.3f}s")
print(f"  2ª consulta de vecinos (con cache):  {duracion_segunda:.3f}s")
print(f"  vecinos_de('Barcelona') = {vecinos_de('Barcelona')}")

# La prueba de que @cache ES @lru_cache(maxsize=None): cache_info() lo confirma.
print(f"\n  vecinos_de.cache_info() = {vecinos_de.cache_info()}  (maxsize=None: nunca evictúa)")

# En el código fuente de functools, lru_cache con maxsize=None usa una rama
# de implementación MÁS SIMPLE (un dict plano, sin lista enlazada de LRU),
# mientras que con maxsize acotado mantiene esa lista para saber a quién
# desalojar. Por eso @cache no es solo "más cómodo de escribir": literalmente
# se salta el trabajo de llevar la cuenta de qué entrada es la menos usada,
# porque nunca va a necesitar desalojar nada.
print("\n  @cache (maxsize=None) usa una rama de implementación más simple: sin")
print("  lista de seguimiento LRU, porque nunca va a desalojar nada. Un")
print("  lru_cache con maxsize acotado sí mantiene esa lista, para saber a")
print("  quién desalojar cuando se llena. Elige @cache cuando el número de")
print("  entradas distintas es acotado y conocido (un grafo fijo, un catálogo")
print("  cerrado); elige @lru_cache cuando el espacio de entradas es enorme o")
print("  desconocido y no quieres agotar memoria.")


# ============================================================================
# 5. reduce: PLEGAR UNA SECUENCIA EN UN VALOR
# ============================================================================
seccion("5. reduce: plegar una secuencia en un valor")


def aplicar_descuento(total: float, porcentaje: float) -> float:
    return round(total * (1 - porcentaje / 100), 2)


descuentos_encadenados = [10, 5, 15]  # tres descuentos aplicados en cadena
total_inicial = 200.0

print("  Descuentos encadenados paso a paso:")
acumulado = total_inicial
for porcentaje in descuentos_encadenados:
    anterior = acumulado
    acumulado = aplicar_descuento(acumulado, porcentaje)
    print(f"    {anterior:.2f} -{porcentaje}% -> {acumulado:.2f}")

# Lo mismo con reduce, usando initial como keyword (novedad 3.14).
total_reduce = reduce(aplicar_descuento, descuentos_encadenados, initial=total_inicial)
print(f"  reduce(..., initial={total_inicial}) = {total_reduce}")

# Honestidad: para una simple suma, sum() es más claro y más rápido.
importes_factura = [120.5, 89.99, 45.0]
print(f"\n  sum(importes_factura) = {sum(importes_factura)} "
      "(mejor que reduce(lambda a, b: a + b, importes_factura))")

# Caso real de reduce: fusionar capas de configuración en orden de
# prioridad creciente (defaults -> entorno -> archivo -> CLI).
capas_config = [
    {"host": "localhost", "puerto": 8000, "debug": True},
    {"puerto": 9000},
    {"debug": False, "workers": 4},
    {"puerto": 9100},
]
config_final = reduce(lambda base, capa: {**base, **capa}, capas_config, initial={})
print(f"  Config fusionada con reduce: {config_final}")


# ============================================================================
# 6. @wraps: DECORADORES QUE NO MIENTEN
# ============================================================================
seccion("6. @wraps: decoradores que no mienten")


def logging_sin_wraps(func):
    def envoltorio(*args, **kwargs):
        print(f"  [LOG] llamando a {func.__name__}")
        return func(*args, **kwargs)
    return envoltorio


def logging_con_wraps(func):
    @wraps(func)
    def envoltorio(*args, **kwargs):
        print(f"  [LOG] llamando a {func.__name__}")
        return func(*args, **kwargs)
    return envoltorio


@logging_sin_wraps
def calcular_total_pedido_sin_wraps(importe: float) -> float:
    """Calcula el total de un pedido con impuestos incluidos."""
    return round(importe * 1.21, 2)


@logging_con_wraps
def calcular_total_pedido_con_wraps(importe: float) -> float:
    """Calcula el total de un pedido con impuestos incluidos."""
    return round(importe * 1.21, 2)


calcular_total_pedido_sin_wraps(100.0)
print(f"  Sin @wraps -> __name__: {calcular_total_pedido_sin_wraps.__name__!r} "
      "(ya no es 'calcular_total_pedido_sin_wraps')")
print(f"  Sin @wraps -> __doc__:  {calcular_total_pedido_sin_wraps.__doc__!r}")

calcular_total_pedido_con_wraps(100.0)
print(f"  Con @wraps -> __name__: {calcular_total_pedido_con_wraps.__name__!r}")
print(f"  Con @wraps -> __doc__:  {calcular_total_pedido_con_wraps.__doc__!r}")

print("\n  Por qué importa en producción: sin @wraps, los logs muestran")
print("  'envoltorio' en vez del nombre real, Sphinx documenta la función")
print("  equivocada, y pytest/introspección pierden la referencia original.")


# ============================================================================
# 7. cached_property: CALCULA UNA VEZ, ACCEDE SIEMPRE
# ============================================================================
seccion("7. cached_property: calcula una vez, accede siempre")


class Informe:
    def __init__(self, datos: list):
        self.datos = datos
        self.veces_procesado = 0

    @cached_property
    def resumen(self) -> dict:
        # Simula un procesamiento pesado (agregaciones sobre datos grandes).
        self.veces_procesado += 1
        time.sleep(0.2)
        return {"total": sum(self.datos), "media": sum(self.datos) / len(self.datos)}


informe_ventas = Informe([100, 250, 75, 430, 89])

print(f"  1er acceso a .resumen:  {informe_ventas.resumen}")
print(f"  2º acceso a .resumen:   {informe_ventas.resumen}")
print(f"  3er acceso a .resumen:  {informe_ventas.resumen}")
print(f"  veces_procesado = {informe_ventas.veces_procesado} "
      "(solo 1, aunque se accedió 3 veces)")

# Invalidar la cache fuerza un recálculo en el siguiente acceso.
del informe_ventas.resumen
informe_ventas.datos.append(500)
print(f"  Tras 'del' y nuevo dato, recalcula: {informe_ventas.resumen}")
print(f"  veces_procesado = {informe_ventas.veces_procesado}")

print("\n  Aviso: cached_property necesita __dict__ por instancia para")
print("  guardar el valor calculado. Una clase con __slots__ (tema 14)")
print("  y sin '__dict__' en slots rompe con AttributeError al usarlo.")


# ============================================================================
# 8. TABLA COMPARATIVA: CUÁNDO USAR CADA HERRAMIENTA
# ============================================================================
seccion("8. Tabla comparativa: cuándo usar cada herramienta")

print("""
    Herramienta        Para qué sirve                          Cuándo NO usarla
    -----------------  ---------------------------------------  -----------------------------------------
    partial            Fijar args/kwargs de una función          Si solo se llama una vez, no aporta nada
    Placeholder (3.14) Fijar un arg posicional que no es el 1º   Si basta con pasar el argumento como kwarg
    lru_cache          Cachear resultados con límite de tamaño   Args no hashables, o función con efectos
                                                                  secundarios (I/O, mutación) que deben repetirse
    cache              Cachear resultados sin límite (3.9+)      Espacio de entradas enorme o no acotado
    reduce             Plegar una secuencia en un único valor    Cuando sum()/dict.update()/list ya lo resuelven
                                                                  de forma más legible
    wraps              Preservar metadatos al decorar             Nunca hay motivo real para omitirlo
    cached_property    Calcular una vez por instancia y reusar   Si el valor puede cambiar entre accesos sin
                                                                  invalidación explícita, o la clase usa __slots__
""")

seccion("FIN — ya conoces functools al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
