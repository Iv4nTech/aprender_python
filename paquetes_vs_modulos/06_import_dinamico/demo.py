"""
CONCEPTO 06 (AVANZADO) · Importar por NOMBRE en tiempo de ejecución
Con importlib.import_module puedes importar un módulo cuyo nombre solo
conoces como string (no escrito a mano con 'import').

CASO REAL: un sistema de PLUGINS. El usuario elige qué plugin cargar y tú
lo importas dinámicamente, sin tener un 'import' fijo por cada uno.
"""

import importlib

# Imagina que esta lista viene de una config, de la BBDD o de una carpeta:
plugins_a_cargar = ["despedida"]

for nombre in plugins_a_cargar:
    modulo = importlib.import_module(f"plugins.{nombre}")
    print(modulo.ejecutar())
