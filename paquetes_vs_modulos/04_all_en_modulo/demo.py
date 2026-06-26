"""
Con  __all__ = ["funcion_publica"]  el  import *  trae SOLO esa.
Las demás NO salen con *, pero OJO: siguen existiendo en el módulo.
__all__ no borra nada, solo decide qué entra con el comodín '*'.
"""

# ── 1) Lo que el comodín '*' SÍ trae ─────────────────────────────────────
from api import *

print("1) Con import *  -> ", funcion_publica())

# ── 2) Comprobamos que las ocultas NO entraron con '*' ───────────────────
print("\n2) ¿Qué trajo el '*'?")
print("   funcion_no_listada en dir()? ->", "funcion_no_listada" in dir())  # False
print("   _ayudante_interno  en dir()? ->", "_ayudante_interno" in dir())   # False

# ── 3) Pero SIGUEN EXISTIENDO: accedemos a ellas a través del módulo ──────
# Importamos el módulo entero para alcanzar lo que '*' no expuso.
import api

print("\n3) Las ocultas existen, solo hay que pedirlas a mano:")
print("   api.funcion_no_listada() ->", api.funcion_no_listada())
print("   api._ayudante_interno()  ->", api._ayudante_interno())
