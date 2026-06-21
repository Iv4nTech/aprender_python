# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 5 — Medio | Capturar la salida estándar  [RESUELTO]
# Técnica: clase, sys.stdout, io.StringIO
# ─────────────────────────────────────────────────────────────────────────────
#
# CONCEPTO CLAVE
#   sys.stdout es simplemente un objeto con un método write(). Reemplazarlo
#   por un io.StringIO (buffer en memoria) hace que todos los print() del
#   bloque escriban ahí en lugar de en la terminal. Al salir se restaura
#   el stdout original guardado previamente.
#   Este patrón lo usa el módulo unittest.mock internamente.
# ─────────────────────────────────────────────────────────────────────────────

import sys
import io


class CapturarSalida:
    def __enter__(self):
        self._buffer = io.StringIO()
        self._stdout_original = sys.stdout
        sys.stdout = self._buffer          # redirige print() al buffer
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self._stdout_original # restaura siempre
        return False

    def leer(self):
        return self._buffer.getvalue()


# --- Prueba ---
with CapturarSalida() as salida:
    print("hola")
    print("mundo")

texto = salida.leer()
print(f"Capturado: {repr(texto)}")
assert texto == "hola\nmundo\n", f"Inesperado: {repr(texto)}"
print("OK")
