# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 4 — Medio | Directorio de trabajo temporal  [RESUELTO]
# Técnica: contextlib.contextmanager, os.chdir, restaurar estado
# ─────────────────────────────────────────────────────────────────────────────
#
# CONCEPTO CLAVE
#   El patrón guardar → modificar → restaurar en finally es el núcleo de
#   muchos context managers: garantiza que el estado global del proceso
#   vuelve a su valor original sin importar lo que ocurra dentro del bloque.
#   os.path.abspath convierte rutas relativas en absolutas antes de cambiar,
#   para que el yield devuelva siempre una ruta completa.
# ─────────────────────────────────────────────────────────────────────────────

import os
from contextlib import contextmanager


@contextmanager
def directorio_temporal(ruta):
    anterior = os.getcwd()
    os.chdir(ruta)
    try:
        yield os.path.abspath(ruta)    # el bloque recibe la ruta absoluta
    finally:
        os.chdir(anterior)             # siempre se restaura


# --- Prueba ---
original = os.getcwd()
print(f"Antes:   {os.getcwd()}")

with directorio_temporal("/tmp") as ruta:
    print(f"Dentro:  {os.getcwd()}")
    print(f"Ruta devuelta: {ruta}")

print(f"Después: {os.getcwd()}")
assert os.getcwd() == original, "ERROR: el directorio no se restauró"
print("OK — directorio restaurado correctamente")
