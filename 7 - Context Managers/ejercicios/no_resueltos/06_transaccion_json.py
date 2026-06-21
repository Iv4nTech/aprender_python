# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 6 — Medio | Transacción sobre un fichero JSON
# Técnica: clase, json, rollback en __exit__
# ─────────────────────────────────────────────────────────────────────────────
#
# CONTEXTO
#   Modificar un fichero JSON directamente es arriesgado: si el programa
#   falla a mitad, el fichero queda con datos inconsistentes. El patrón
#   de transacción (leer → modificar en memoria → confirmar o deshacer)
#   resuelve este problema de forma elegante.
#
# TAREA
#   Implementa la clase TransaccionJSON:
#   - __init__: recibe la ruta del fichero JSON.
#   - __enter__: lee el JSON, guarda una copia del estado original y devuelve
#                el diccionario para que el bloque lo modifique directamente.
#   - __exit__ sin error: sobreescribe el fichero con los cambios.
#   - __exit__ con error: descarta los cambios (no toca el fichero) y suprime
#                         la excepción devolviendo True.
#
# USO ESPERADO
#   # config.json contiene: {"version": 1, "debug": false}
#
#   with TransaccionJSON("config.json") as cfg:
#       cfg["debug"] = True                # se confirma
#
#   with TransaccionJSON("config.json") as cfg:
#       cfg["version"] = 99
#       raise ValueError("algo salió mal") # rollback, version sigue siendo 1
#
#   print("El programa continúa")
# ─────────────────────────────────────────────────────────────────────────────

import json


class TransaccionJSON:
    def __init__(self, ruta):
        self.ruta = ruta

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


# --- Prueba (no modificar) ---
import os

# Crear fichero inicial
with open("config.json", "w") as f:
    json.dump({"version": 1, "debug": False}, f)

# Transacción exitosa
with TransaccionJSON("config.json") as cfg:
    cfg["debug"] = True

with open("config.json") as f:
    estado = json.load(f)
assert estado["debug"] is True, "ERROR: el cambio no se guardó"
print(f"Tras confirmación: {estado}")

# Transacción fallida
with TransaccionJSON("config.json") as cfg:
    cfg["version"] = 99
    raise ValueError("algo salió mal")

with open("config.json") as f:
    estado = json.load(f)
assert estado["version"] == 1, "ERROR: el rollback no funcionó"
print(f"Tras rollback:     {estado}")
print("OK")
