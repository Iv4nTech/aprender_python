# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 3 — Fácil | Registro automático de operaciones en fichero
# Técnica: contextlib.contextmanager, escritura en fichero, datetime
# ─────────────────────────────────────────────────────────────────────────────
#
# CONTEXTO
#   En aplicaciones reales se registra cuándo empieza y termina cada
#   operación importante, y si tuvo éxito o falló. Sin un context manager
#   hay que poner ese código de log antes y después de cada bloque a mano.
#
# TAREA
#   Implementa con @contextmanager la función registrar_operacion(nombre).
#   Debe escribir en "operaciones.log" (modo append):
#   - Al entrar:          "[INICIO] nombre — HH:MM:SS"
#   - Al salir sin error: "[OK]     nombre — HH:MM:SS"
#   - Al salir con error: "[ERROR]  nombre — TipoExcepcion: mensaje"
#     y dejar propagar la excepción (no suprimirla).
#
# USO ESPERADO
#   with registrar_operacion("carga de datos"):
#       time.sleep(0.05)
#
#   try:
#       with registrar_operacion("exportar informe"):
#           raise RuntimeError("disco lleno")
#   except RuntimeError:
#       pass
#
# CONTENIDO ESPERADO EN operaciones.log
#   [INICIO] carga de datos — 14:23:01
#   [OK]     carga de datos — 14:23:01
#   [INICIO] exportar informe — 14:23:01
#   [ERROR]  exportar informe — RuntimeError: disco lleno
# ─────────────────────────────────────────────────────────────────────────────

import time
from contextlib import contextmanager
from datetime import datetime


@contextmanager
def registrar_operacion(nombre):
    pass


# --- Prueba (no modificar) ---
with registrar_operacion("carga de datos"):
    time.sleep(1)

try:
    with registrar_operacion("exportar informe"):
        raise RuntimeError("disco lleno")
except RuntimeError:
    pass

with open("operaciones.log") as f:
    print(f.read())
