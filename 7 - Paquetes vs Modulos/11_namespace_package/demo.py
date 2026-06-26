"""
Unimos dos carpetas distintas bajo el MISMO paquete 'extensiones',
sin que ninguna tenga __init__.py. Eso es un namespace package (PEP 420).
"""
import sys
import os

base = os.path.dirname(__file__)
# Añadimos las DOS raíces al path de búsqueda de Python:
sys.path.insert(0, os.path.join(base, "ruta_a"))
sys.path.insert(0, os.path.join(base, "ruta_b"))

# Aunque viven en carpetas separadas, son el mismo paquete 'extensiones':
from extensiones import audio, video

print(audio.reproducir())
print(video.reproducir())

import extensiones
print("Rutas que componen el paquete:", list(extensiones.__path__))
