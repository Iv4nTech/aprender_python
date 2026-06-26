"""
DEMO DEL ZIP · La prueba de fuego de files() vs __file__
Metemos el paquete 'paquete_datos' DENTRO de un .zip y lo importamos desde ahí
(Python sabe importar desde zips). Entonces:
  - capitales_con_files()  -> FUNCIONA (lee el recurso aunque esté en el zip)
  - capitales_con_file()   -> FALLA  (open() no puede abrir algo dentro del zip)
"""
import os
import sys
import zipfile

base = os.path.dirname(__file__)
ruta_zip = os.path.join(base, "paquete_empaquetado.zip")

# 1) Creamos un .zip que contiene la carpeta del paquete -------------------
with zipfile.ZipFile(ruta_zip, "w") as z:
    for nombre in ("__init__.py", "cargar.py", "ciudades.json"):
        z.write(os.path.join(base, "paquete_datos", nombre),
                arcname=os.path.join("paquete_datos", nombre))

# 2) Hacemos que Python importe DESDE el zip (no desde la carpeta) ----------
sys.path.insert(0, ruta_zip)
for mod in list(sys.modules):
    if mod.startswith("paquete_datos"):
        del sys.modules[mod]   # limpiamos por si ya estaba importado

from paquete_datos.cargar import capitales_con_files, capitales_con_file

print(f"Paquete importado desde: {ruta_zip}\n")

# 3) Probamos las dos formas ----------------------------------------------
print("✅ Con files():")
print("  ", capitales_con_files())

print("\n❌ Con __file__ + open():")
try:
    print("  ", capitales_con_file())
except (FileNotFoundError, NotADirectoryError, OSError) as e:
    print("   ¡FALLA dentro del zip! ->", type(e).__name__, "-", e)

# 4) Limpieza --------------------------------------------------------------
os.remove(ruta_zip)
