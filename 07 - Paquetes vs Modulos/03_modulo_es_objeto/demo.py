"""
CONCEPTO 03 · Un módulo es un OBJETO y se importa UNA sola vez (singleton)
Cuando importas un módulo, Python crea un objeto y lo guarda en sys.modules.
Si lo vuelves a importar, NO se re-ejecuta: te da el MISMO objeto.

CASO REAL: aunque importes 'config' en 10 ficheros distintos, es el mismo
objeto en memoria. Esa es la base para compartir estado (concepto 04 lo usa).
"""

import sys
import herramienta

# El módulo trae atributos especiales "de fábrica":
print("__name__ :", herramienta.__name__)
print("__doc__  :", herramienta.__doc__)
print("__file__ :", herramienta.__file__)

# Tras importarlo, queda cacheado en sys.modules:
print("¿cacheado en sys.modules?:", "herramienta" in sys.modules)

# ── PRUEBA VISUAL DEL SINGLETON ──────────────────────────────────────────
# Importamos el módulo OTRA VEZ con un nombre distinto. Parecen dos, pero
# por debajo Python entrega el MISMO objeto cacheado.
import herramienta as otra_referencia

print("\n-- Antes del cambio --")
print("herramienta.config     :", herramienta.config)
print("otra_referencia.config :", otra_referencia.config)

# Cambiamos el estado SOLO a través de 'herramienta'...
herramienta.config["tema"] = "oscuro"

print("\n-- Después de cambiarlo solo en 'herramienta' --")
print("herramienta.config     :", herramienta.config)
print("otra_referencia.config :", otra_referencia.config)  # ¡también cambió!

# Y la prueba definitiva: son literalmente el mismo objeto en memoria.
print("\n¿es el mismo objeto? :", herramienta is otra_referencia)   # True
print("mismo id en memoria  :", id(herramienta) == id(otra_referencia))
