"""
CONCEPTO 08 · API pública limpia con el __init__.py
Truco de librería profesional: re-exportar en el __init__.py lo importante,
para que el usuario escriba  'from miapp import Usuario'  en vez de tener que
conocer la estructura interna ('from miapp.modelos import Usuario').

__all__ aquí marca la API pública oficial del paquete.
"""
from .modelos import Usuario
from .servicios import crear_usuario

__all__ = ["Usuario", "crear_usuario"]
