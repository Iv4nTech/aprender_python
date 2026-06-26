"""
Gracias al re-export en miapp/__init__.py, el usuario importa desde el
paquete directamente, sin saber en qué fichero interno vive cada cosa.
"""
from miapp import *  # API limpia: NO necesitamos 'from miapp.modelos import Usuario'

usuario = crear_usuario("Ivan")
print("Creado:", usuario)
print("¿es Usuario?:", isinstance(usuario, Usuario))
