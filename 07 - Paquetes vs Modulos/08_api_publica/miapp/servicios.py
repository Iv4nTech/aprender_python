from .modelos import Usuario


def crear_usuario(nombre):
    # Aquí iría validación, guardar en BBDD, etc. (detalle interno oculto)
    return Usuario(nombre)
