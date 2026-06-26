"""
CONCEPTO 01 · ¿Qué es un MÓDULO?
Un módulo es, simplemente, UN FICHERO .py con código reutilizable
(funciones, clases, variables).

CASO REAL: tienes lógica de precios que usas en varias partes de la app.
La pones en un módulo y la importas donde haga falta, sin copiar y pegar.

"""

def sumar(a, b):
    return a + b


def aplicar_iva(precio, tasa=0.21):
    return round(precio * (1 + tasa), 2)
