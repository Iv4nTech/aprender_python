"""
================================================================================
 EJERCICIOS: FUNCTOOLS EN PYTHON
 Ejecutar: python3 ejercicios.py

 Completa cada ejercicio donde encuentres '...' y descomenta los print()
 para comprobar el resultado.
================================================================================
"""

import time
from functools import partial, lru_cache, reduce, wraps, cached_property, Placeholder


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ──────────────────────────────────────────────
# EJERCICIO 1 — FÁCIL
# Remitente fijo para el sistema de emails
# ──────────────────────────────────────────────
# Tu aplicación envía emails desde muchos puntos del código, pero siempre
# desde el mismo remitente corporativo. Repetirlo en cada llamada es un
# error esperando a pasar (un typo en el remitente y el email rebota).
seccion("EJERCICIO 1 — FÁCIL — Remitente fijo para emails")


def enviar_email(destinatario: str, asunto: str, cuerpo: str, remitente: str) -> str:
    return f"De: {remitente} | Para: {destinatario} | Asunto: {asunto} | Cuerpo: {cuerpo}"


# Usa partial para fijar remitente="notificaciones@miapp.com"
enviar_email_app = ...

# Resultado esperado:
# De: notificaciones@miapp.com | Para: ana@gmail.com | Asunto: Bienvenida | Cuerpo: Gracias por unirte
# print(enviar_email_app("ana@gmail.com", "Bienvenida", "Gracias por unirte"))


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Funciones de redondeo reutilizables
# ──────────────────────────────────────────────
# Tu app financiera necesita redondear precios a 2 decimales para mostrar
# al usuario, y a 4 decimales para cálculos internos de tipos de cambio.
seccion("EJERCICIO 2 — FÁCIL — Funciones de redondeo reutilizables")

# Usa partial(round, ndigits=N) para crear redondear_2 y redondear_4
redondear_2 = ...
redondear_4 = ...

# Resultado esperado: 3.14 y 3.1416
# print(redondear_2(3.14159265))
# print(redondear_4(3.14159265))


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Fibonacci con y sin cache
# ──────────────────────────────────────────────
# Un endpoint calcula el n-ésimo número de Fibonacci de forma recursiva.
# Sin cache, cada llamada recalcula los mismos subproblemas una y otra vez,
# y el tiempo crece exponencialmente.
seccion("EJERCICIO 3 — FÁCIL — Fibonacci con y sin cache")


def fibonacci_sin_cache(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_sin_cache(n - 1) + fibonacci_sin_cache(n - 2)


# Aplica @lru_cache a esta versión para comparar el tiempo
def fibonacci_con_cache(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_con_cache(n - 1) + fibonacci_con_cache(n - 2)


# Resultado esperado: mismo valor (fib(28) = 317811), pero fibonacci_con_cache
# mucho más rápido en la segunda llamada
# inicio = time.perf_counter()
# resultado_sin_cache = fibonacci_sin_cache(28)
# duracion_sin_cache = time.perf_counter() - inicio
#
# inicio = time.perf_counter()
# resultado_con_cache = fibonacci_con_cache(28)
# duracion_con_cache = time.perf_counter() - inicio
#
# print(f"Sin cache: {resultado_sin_cache} en {duracion_sin_cache:.4f}s")
# print(f"Con cache: {resultado_con_cache} en {duracion_con_cache:.4f}s")


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Catálogo de productos con cache_info()
# ──────────────────────────────────────────────
# Un catálogo de e-commerce consulta el "precio de producto" en una función
# que simula una base de datos lenta. Quieres verificar cuántas consultas
# realmente golpean la BD y cuántas se resuelven desde cache.
seccion("EJERCICIO 4 — MEDIO — Catálogo de productos con cache_info()")

precios_bd = {"teclado": 45.99, "monitor": 299.99, "raton": 19.99}


# Decora esta función con @lru_cache para evitar consultas repetidas
def consultar_precio(producto: str) -> float:
    time.sleep(0.1)  # simula latencia de BD
    return precios_bd.get(producto, 0.0)


# Consulta "teclado" dos veces, "monitor" una vez y revisa cache_info()
# Resultado esperado: hits=1, misses=2, currsize=2
# consultar_precio("teclado")
# consultar_precio("monitor")
# consultar_precio("teclado")
# print(consultar_precio.cache_info())


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Logger con origen fijo usando Placeholder (3.14)
# ──────────────────────────────────────────────
# Tu módulo de pagos genera logs con formato (nivel, origen, mensaje). Quieres
# una versión especializada que siempre registre origen="pagos", pero
# "nivel" va antes y "mensaje" va después en la firma de la función.
seccion("EJERCICIO 5 — MEDIO — Logger con origen fijo usando Placeholder")


def formatear_log(nivel: str, origen: str, mensaje: str) -> str:
    return f"[{nivel}] ({origen}) {mensaje}"


# Usa partial + Placeholder para fijar origen="pagos" sin tocar nivel/mensaje
log_pagos = ...

# Resultado esperado: [ERROR] (pagos) Tarjeta rechazada
# print(log_pagos("ERROR", "Tarjeta rechazada"))


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# Descuento total acumulado con reduce
# ──────────────────────────────────────────────
# Una tienda aplica varios descuentos en cadena sobre un pedido: descuento
# de socio, descuento de campaña y descuento de cupón. Cada uno se aplica
# sobre el resultado del anterior, no sobre el precio original.
seccion("EJERCICIO 6 — MEDIO — Descuento total acumulado con reduce")

precio_original = 300.0
descuentos = [10, 15, 5]  # porcentajes aplicados en cadena


def aplicar_descuento(total: float, porcentaje: float) -> float:
    return round(total * (1 - porcentaje / 100), 2)


# Usa reduce con initial=precio_original (keyword, novedad 3.14)
precio_final = ...

# Resultado esperado: 218.02
# print(precio_final)


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# Fusionar capas de configuración con reduce
# ──────────────────────────────────────────────
# Tu aplicación carga configuración en capas de prioridad creciente:
# valores por defecto, luego variables de entorno, luego archivo de config,
# luego argumentos de línea de comandos. Cada capa sobrescribe a la anterior.
seccion("EJERCICIO 7 — AVANZADO — Fusionar capas de configuración con reduce")

capas = [
    {"host": "localhost", "puerto": 8000, "debug": True, "workers": 1},
    {"puerto": 8080},
    {"debug": False},
    {"puerto": 9000, "workers": 4},
]

# Usa reduce para fusionar todas las capas en un único dict, empezando
# desde initial={}
config_final = ...

# Resultado esperado:
# {'host': 'localhost', 'puerto': 9000, 'debug': False, 'workers': 4}
# print(config_final)


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Decorador cronometrar: antes y después de @wraps
# ──────────────────────────────────────────────
# Añades un decorador de cronometraje a funciones de tu API. Quieres ver
# en carne propia cómo, sin @wraps, la introspección de la función se rompe.
seccion("EJERCICIO 8 — AVANZADO — Decorador cronometrar: antes y después de @wraps")


# Versión SIN @wraps
def cronometrar_sin_wraps(func):
    def envoltorio(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        duracion = time.perf_counter() - inicio
        print(f"  {func.__name__} tardó {duracion:.4f}s")
        return resultado
    return envoltorio


# Reescribe esta versión añadiendo @wraps(func) al envoltorio
def cronometrar_con_wraps(func):
    def envoltorio(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        duracion = time.perf_counter() - inicio
        print(f"  {func.__name__} tardó {duracion:.4f}s")
        return resultado
    return envoltorio


@cronometrar_sin_wraps
def procesar_pedido_sin_wraps(id_pedido: int) -> int:
    """Procesa un pedido y devuelve su total."""
    return id_pedido * 10


@cronometrar_con_wraps
def procesar_pedido_con_wraps(id_pedido: int) -> int:
    """Procesa un pedido y devuelve su total."""
    return id_pedido * 10


# Resultado esperado: el primero pierde __name__/__doc__, el segundo los conserva
# procesar_pedido_sin_wraps(1)
# procesar_pedido_con_wraps(1)
# print(f"Sin wraps -> __name__: {procesar_pedido_sin_wraps.__name__!r}")
# print(f"Con wraps -> __name__: {procesar_pedido_con_wraps.__name__!r}")


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# Dataset con estadísticas costosas cacheadas
# ──────────────────────────────────────────────
# Una clase Dataset carga una lista de valores y calcula estadísticas
# (media, máximo, mínimo) que son costosas de calcular. Acceder varias
# veces a .estadisticas no debe recalcularlas cada vez.
seccion("EJERCICIO 9 — AVANZADO — Dataset con estadísticas costosas cacheadas")


class Dataset:
    def __init__(self, valores: list):
        self.valores = valores
        self.veces_calculado = 0

    # Convierte esta property en cached_property
    @property
    def estadisticas(self) -> dict:
        self.veces_calculado += 1
        time.sleep(0.1)  # simula cálculo costoso
        return {
            "media": sum(self.valores) / len(self.valores),
            "maximo": max(self.valores),
            "minimo": min(self.valores),
        }


# Resultado esperado: veces_calculado == 1 tras acceder 3 veces
# dataset = Dataset([10, 20, 30, 40, 50])
# print(dataset.estadisticas)
# print(dataset.estadisticas)
# print(dataset.estadisticas)
# print(f"veces_calculado: {dataset.veces_calculado}")


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Pipeline de procesamiento de ventas
# ──────────────────────────────────────────────
# El equipo de finanzas necesita procesar una lista de ventas: aplicar el
# impuesto correspondiente a cada país (cacheado, porque se repiten países)
# y luego sumar el total general con reduce. La configuración de impuestos
# por país se fija de antemano con partial.
seccion("EJERCICIO 10 — EXPERTO — Pipeline de procesamiento de ventas")

tasas_impuestos = {"ES": 0.21, "FR": 0.20, "DE": 0.19}

ventas = [
    {"pais": "ES", "importe": 100.0},
    {"pais": "FR", "importe": 200.0},
    {"pais": "ES", "importe": 150.0},
    {"pais": "DE", "importe": 80.0},
    {"pais": "FR", "importe": 120.0},
]


def _consultar_tasa_base(pais: str, tasas: dict) -> float:
    time.sleep(0.1)  # simula ir a buscar la tasa a un servicio externo
    return tasas.get(pais, 0.0)


# Paso 1: usa partial para fijar tasas=tasas_impuestos (pais libre), y envuelve
# el resultado con lru_cache para no recalcular la tasa de países repetidos
consultar_tasa = ...


# Paso 2: calcula el impuesto de una venta multiplicando importe * tasa
def calcular_impuesto(pais: str, importe: float) -> float:
    ...


# Paso 3: usa reduce para sumar importe + impuesto de cada venta, con initial=0.0
total_recaudado = ...

# Resultado esperado: 781.70
# print(f"Total recaudado (con impuestos): {total_recaudado:.2f}")
