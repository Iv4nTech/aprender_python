"""
CONCEPTO 04 · __all__ en un MÓDULO controla 'from api import *'
- SIN __all__: 'import *' trae todos los nombres públicos (los que no
  empiezan por guion bajo).
- CON __all__: trae SOLO los nombres que listes. Así defines tu API pública
  y proteges lo interno aunque sea público técnicamente.

CASO REAL: una librería que quiere exponer 2 funciones y ocultar el resto
de helpers al hacer 'from libreria import *'.
"""

__all__ = ["funcion_publica"]


def funcion_publica():
    return "soy parte de la API pública"


def funcion_no_listada():
    return "soy pública, pero NO salgo en import * por culpa de __all__"


def _ayudante_interno():
    return "empiezo por _, nunca salgo en import *"
