# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 8 — Difícil | Variables de entorno temporales
# Técnica: contextlib.contextmanager, os.environ, restaurar estado
# ─────────────────────────────────────────────────────────────────────────────
#
# CONTEXTO
#   En tests necesitas que tu código se ejecute creyendo que está en
#   producción, en staging o con una API key concreta, sin modificar el
#   entorno real del proceso. Cambiar os.environ directamente y no restaurarlo
#   contamina otros tests o el resto del programa.
#
# TAREA
#   Implementa con @contextmanager la función entorno_temporal(**variables).
#   - Al entrar: establece cada par clave=valor en os.environ, guardando
#                el valor anterior de cada clave (o None si no existía).
#   - Al salir:  restaura siempre los valores originales.
#                Las claves que no existían antes deben eliminarse de os.environ.
#
# USO ESPERADO
#   import os
#   os.environ["ENTORNO"] = "desarrollo"
#
#   with entorno_temporal(ENTORNO="produccion", API_KEY="abc123"):
#       print(os.environ["ENTORNO"])       # produccion
#       print(os.environ["API_KEY"])       # abc123
#
#   print(os.environ["ENTORNO"])           # desarrollo — restaurado
#   print("API_KEY" in os.environ)         # False — eliminada
# ─────────────────────────────────────────────────────────────────────────────

import os
from contextlib import contextmanager


@contextmanager
def entorno_temporal(**variables):
    pass


# --- Prueba (no modificar) ---
os.environ["ENTORNO"] = "desarrollo"

with entorno_temporal(ENTORNO="produccion", API_KEY="abc123"):
    assert os.environ["ENTORNO"] == "produccion"
    assert os.environ["API_KEY"] == "abc123"
    print(f"Dentro — ENTORNO: {os.environ['ENTORNO']}, API_KEY: {os.environ['API_KEY']}")

assert os.environ["ENTORNO"] == "desarrollo", "ERROR: ENTORNO no se restauró"
assert "API_KEY" not in os.environ, "ERROR: API_KEY debería haberse eliminado"
print(f"Después — ENTORNO: {os.environ['ENTORNO']}, API_KEY presente: {'API_KEY' in os.environ}")
print("OK")
