# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 6 — Medio | Transacción sobre un fichero JSON  [RESUELTO]
# Técnica: clase, json, rollback en __exit__
# ─────────────────────────────────────────────────────────────────────────────
#
# CONCEPTO CLAVE
#   __exit__ recibe exc_type=None cuando no hubo error. En ese caso confirma.
#   Cuando exc_type no es None hubo un error: descarta los cambios (la copia
#   original sigue intacta en self._original) y devuelve True para suprimir
#   la excepción y dejar que el programa continúe.
# ─────────────────────────────────────────────────────────────────────────────

import json
import copy


class TransaccionJSON:
    def __init__(self, ruta):
        self.ruta = ruta

    def __enter__(self):
        with open(self.ruta) as f:
            self._datos = json.load(f)
        self._original = copy.deepcopy(self._datos)  # copia de seguridad
        return self._datos                            # el bloque modifica esto

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            with open(self.ruta, "w") as f:          # confirma cambios
                json.dump(self._datos, f, indent=2)
        return exc_type is not None                  # True suprime la excepción


# --- Prueba ---
import os

with open("config.json", "w") as f:
    json.dump({"version": 1, "debug": False}, f)

with TransaccionJSON("config.json") as cfg:
    cfg["debug"] = True

with open("config.json") as f:
    estado = json.load(f)
assert estado["debug"] is True
print(f"Tras confirmación: {estado}")

with TransaccionJSON("config.json") as cfg:
    cfg["version"] = 99
    raise ValueError("algo salió mal")

with open("config.json") as f:
    estado = json.load(f)
assert estado["version"] == 1
print(f"Tras rollback:     {estado}")
print("OK")
