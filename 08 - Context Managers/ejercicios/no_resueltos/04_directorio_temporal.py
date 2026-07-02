# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 4 — Medio | Directorio de trabajo temporal
# Técnica: contextlib.contextmanager, os.chdir, restaurar estado
# ─────────────────────────────────────────────────────────────────────────────
#
# CONTEXTO
#   Algunos scripts necesitan ejecutarse desde un directorio concreto para
#   que las rutas relativas funcionen. Cambiar de directorio con os.chdir()
#   sin restaurarlo puede romper el resto del programa porque el directorio
#   de trabajo es global al proceso.
#
# TAREA
#   Implementa con @contextmanager la función directorio_temporal(ruta).
#   - Al entrar: guarda el directorio actual y cambia a `ruta`.
#   - Al salir: restaura siempre el directorio original, aunque haya error.
#   - Devuelve la ruta absoluta del nuevo directorio (la que recibe el `as`).
#
# USO ESPERADO
#   original = os.getcwd()
#
#   with directorio_temporal("/tmp") as ruta:
#       print(os.getcwd())    # /tmp
#       print(ruta)           # /tmp
#       # aquí puedes crear archivos con rutas relativas a /tmp
#
#   print(os.getcwd())        # restaurado al directorio original
#   assert os.getcwd() == original
# ─────────────────────────────────────────────────────────────────────────────

import os
from contextlib import contextmanager


@contextmanager
def directorio_temporal(ruta):
    pass


# --- Prueba (no modificar) ---
original = os.getcwd()
print(f"Antes:   {os.getcwd()}")

with directorio_temporal("/tmp") as ruta:
    print(f"Dentro:  {os.getcwd()}")
    print(f"Ruta devuelta: {ruta}")

print(f"Después: {os.getcwd()}")
assert os.getcwd() == original, "ERROR: el directorio no se restauró"
print("OK — directorio restaurado correctamente")
