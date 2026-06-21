# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 9 — Difícil | Escritura atómica de ficheros  [RESUELTO]
# Técnica: clase, tempfile, os.replace, proteger ficheros en producción
# ─────────────────────────────────────────────────────────────────────────────
#
# CONCEPTO CLAVE
#   os.replace() es una operación atómica en la mayoría de sistemas de
#   ficheros: o el fichero destino se reemplaza completamente o no se toca.
#   No hay estado intermedio visible para otros procesos.
#   El temporal debe estar en el mismo sistema de ficheros que el destino
#   para que os.replace sea realmente atómico (no una copia entre discos).
#   Por eso se pasa dir=os.path.dirname(destino) al crear el temporal.
# ─────────────────────────────────────────────────────────────────────────────

import os
import tempfile


class FicheroAtomico:
    def __init__(self, ruta_destino):
        self.ruta_destino = ruta_destino

    def __enter__(self):
        directorio = os.path.dirname(os.path.abspath(self.ruta_destino))
        tmp = tempfile.NamedTemporaryFile(
            mode="w", delete=False, dir=directorio, suffix=".tmp"
        )
        self._ruta_tmp = tmp.name
        self._fichero_tmp = tmp
        return self._fichero_tmp

    def __exit__(self, exc_type, exc_value, traceback):
        self._fichero_tmp.close()
        if exc_type is None:
            os.replace(self._ruta_tmp, self.ruta_destino)  # reemplaza atómicamente
        else:
            os.remove(self._ruta_tmp)                       # descarta el temporal
        return False                                        # propaga la excepción


# --- Prueba ---
with FicheroAtomico("config.cfg") as f:
    f.write("[base]\nhost=localhost\n")

with open("config.cfg") as f:
    contenido = f.read()
assert "localhost" in contenido
print(f"Tras escritura exitosa:\n{contenido}")

try:
    with FicheroAtomico("config.cfg") as f:
        f.write("contenido corrupto...")
        raise IOError("disco lleno")
except IOError:
    pass

with open("config.cfg") as f:
    contenido_tras_error = f.read()
assert contenido_tras_error == contenido
print(f"Tras error (sin cambios):\n{contenido_tras_error}")
print("OK")
