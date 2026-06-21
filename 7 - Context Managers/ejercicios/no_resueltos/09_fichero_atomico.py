# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 9 — Difícil | Escritura atómica de ficheros
# Técnica: clase, tempfile, os.replace, proteger ficheros en producción
# ─────────────────────────────────────────────────────────────────────────────
#
# CONTEXTO
#   Cuando un script sobreescribe un fichero de configuración o datos, si el
#   proceso se interrumpe a mitad el fichero queda corrupto. La solución es
#   escribir primero en un fichero temporal y, solo si todo fue bien, reemplazar
#   el original con el temporal. Esto se llama "escritura atómica" y es el
#   patrón que usa Python internamente al escribir .pyc y otros ficheros críticos.
#
# TAREA
#   Implementa la clase FicheroAtomico:
#   - __init__:  recibe la ruta del fichero destino.
#   - __enter__: crea un fichero temporal en el mismo directorio que el destino,
#                lo abre en modo escritura y devuelve el objeto fichero.
#   - __exit__ sin error: cierra el temporal y lo mueve sobre el destino
#                         (reemplazándolo) con os.replace().
#   - __exit__ con error: cierra y elimina el temporal. El fichero original
#                         queda intacto. Deja propagar la excepción.
#
#   PISTA: usa tempfile.NamedTemporaryFile(delete=False, dir=...) para crear
#   el temporal en el mismo directorio que el destino (necesario para os.replace).
#
# USO ESPERADO
#   with FicheroAtomico("config.cfg") as f:
#       f.write("[base]\nhost=localhost\n")
#   # config.cfg contiene el nuevo contenido
#
#   with FicheroAtomico("config.cfg") as f:
#       f.write("contenido a medias...")
#       raise IOError("disco lleno")
#   # config.cfg NO se modificó — sigue con el contenido anterior
# ─────────────────────────────────────────────────────────────────────────────

import os
import tempfile


class FicheroAtomico:
    def __init__(self, ruta_destino):
        self.ruta_destino = ruta_destino

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

# --- Prueba (no modificar) ---
# Escritura exitosa
with FicheroAtomico("config.cfg") as f:
    f.write("[base]\nhost=localhost\n")

with open("config.cfg") as f:
    contenido = f.read()
assert "localhost" in contenido, "ERROR: el fichero no se escribió"
print(f"Tras escritura exitosa:\n{contenido}")

# Escritura fallida — el fichero original debe quedar intacto
try:
    with FicheroAtomico("config.cfg") as f:
        f.write("contenido corrupto...")
        raise IOError("disco lleno")
except IOError:
    pass

with open("config.cfg") as f:
    contenido_tras_error = f.read()
assert contenido_tras_error == contenido, "ERROR: el fichero se corrompió"
print(f"Tras error (sin cambios):\n{contenido_tras_error}")
print("OK")
