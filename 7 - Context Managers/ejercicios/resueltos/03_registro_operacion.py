# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 3 — Fácil | Registro automático de operaciones en fichero  [RESUELTO]
# Técnica: contextlib.contextmanager, escritura en fichero, datetime
# ─────────────────────────────────────────────────────────────────────────────
#
# CONCEPTO CLAVE
#   El bloque try/except/else alrededor del yield permite distinguir tres
#   caminos: entrada (antes del yield), salida limpia (else) y salida con
#   error (except). El finally garantiza que el fichero siempre se cierra.
# ─────────────────────────────────────────────────────────────────────────────

import time
from contextlib import contextmanager
from datetime import datetime


def _ahora():
    return datetime.now().strftime("%H:%M:%S")


@contextmanager
def registrar_operacion(nombre):
    with open("operaciones.log", "a") as log:
        log.write(f"[INICIO] {nombre} — {_ahora()}\n")
        try:
            yield
        except Exception as e:
            log.write(f"[ERROR]  {nombre} — {type(e).__name__}: {e}\n")
            raise                      # propaga la excepción
        else:
            log.write(f"[OK]     {nombre} — {_ahora()}\n")


# --- Prueba ---
with registrar_operacion("carga de datos"):
    time.sleep(0.05)

try:
    with registrar_operacion("exportar informe"):
        raise RuntimeError("disco lleno")
except RuntimeError:
    pass

with open("operaciones.log") as f:
    print(f.read())
