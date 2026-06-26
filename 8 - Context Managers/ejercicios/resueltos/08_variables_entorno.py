# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 8 — Difícil | Variables de entorno temporales  [RESUELTO]
# Técnica: contextlib.contextmanager, os.environ, restaurar estado
# ─────────────────────────────────────────────────────────────────────────────
#
# CONCEPTO CLAVE
#   os.environ.get(clave) devuelve None si la clave no existe, lo que permite
#   distinguir "tenía valor anterior" de "no existía". En la restauración,
#   si el valor guardado es None significa que hay que eliminar la clave;
#   si tiene valor, hay que restaurarlo. Todo dentro de un finally para que
#   se ejecute aunque el bloque lanze una excepción.
# ─────────────────────────────────────────────────────────────────────────────

import os
from contextlib import contextmanager


@contextmanager
def entorno_temporal(**variables):
    anteriores = {k: os.environ.get(k) for k in variables}
    os.environ.update(variables)
    try:
        yield
    finally:
        for clave, valor_anterior in anteriores.items():
            if valor_anterior is None:
                os.environ.pop(clave, None)   # no existía → eliminar
            else:
                os.environ[clave] = valor_anterior


# --- Prueba ---
os.environ["ENTORNO"] = "desarrollo"

with entorno_temporal(ENTORNO="produccion", API_KEY="abc123"):
    assert os.environ["ENTORNO"] == "produccion"
    assert os.environ["API_KEY"] == "abc123"
    print(f"Dentro — ENTORNO: {os.environ['ENTORNO']}, API_KEY: {os.environ['API_KEY']}")

assert os.environ["ENTORNO"] == "desarrollo"
assert "API_KEY" not in os.environ
print(f"Después — ENTORNO: {os.environ['ENTORNO']}, API_KEY presente: {'API_KEY' in os.environ}")
print("OK")
