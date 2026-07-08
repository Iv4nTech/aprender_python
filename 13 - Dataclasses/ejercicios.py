# ============================================================
# EJERCICIOS: DATACLASSES EN PYTHON
# Casos reales — de fácil a experto
# ============================================================

from dataclasses import dataclass, field, replace, asdict
from typing import ClassVar


def separador(titulo: str) -> None:
    """Imprime una cabecera para separar la salida de cada ejercicio."""
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


# ──────────────────────────────────────────────
# EJERCICIO 1 — FÁCIL
# Dataclass básica
# ──────────────────────────────────────────────
# Necesitas modelar un libro para una librería.
separador("EJERCICIO 1 — Dataclass básica")

# Define la dataclass Libro con campos: titulo: str, autor: str, paginas: int
...

# Crea dos instancias con los MISMOS datos y comprueba que == funciona
# sin haber escrito __eq__ a mano.
libro1 = ...
libro2 = ...

# Imprime una instancia y comprueba que el __repr__ es legible.
# print(libro1)                # Esperado: Libro(titulo=..., autor=..., paginas=...)
# print(libro1 == libro2)      # Esperado: True


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Valor por defecto
# ──────────────────────────────────────────────
# Sistema de tareas donde algunas empiezan completadas y otras no.
separador("EJERCICIO 2 — Valor por defecto")

# Define la dataclass Tarea con: descripcion: str, completada: bool = False
...

# Crea una tarea SIN pasar completada, y otra pasándola como True
tarea1 = ...
tarea2 = ...

# print(tarea1)  # Esperado: Tarea(descripcion=..., completada=False)
# print(tarea2)  # Esperado: Tarea(descripcion=..., completada=True)


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# __post_init__ para validar
# ──────────────────────────────────────────────
# Pasarela de pagos donde los importes negativos deben rechazarse.
separador("EJERCICIO 3 — __post_init__ para validar")

# Define la dataclass Pago con: concepto: str, importe: float
# En __post_init__ lanza ValueError si importe <= 0
...

# Prueba con un importe válido
pago_ok = ...
# print(pago_ok)  # Esperado: Pago(concepto=..., importe=...)

# Prueba con un importe negativo dentro de un try/except
try:
    pago_malo = ...
except ValueError as e:
    ...
    # print("Error:", e)  # Esperado: Error: <tu mensaje de validación>


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Campo calculado con field(init=False)
# ──────────────────────────────────────────────
# Carrito de compra donde el total se calcula automáticamente.
separador("EJERCICIO 4 — Campo calculado con field(init=False)")

# Define la dataclass LineaCarrito con:
#   producto: str
#   precio: float
#   cantidad: int
#   total: float = field(init=False)
# Calcula total en __post_init__ (precio * cantidad)
...

# Crea una línea SIN pasar total y comprueba que se rellena solo
linea = ...
# print(linea)  # Esperado: LineaCarrito(producto=..., precio=..., cantidad=..., total=precio*cantidad)


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# ClassVar y la trampa del atributo de clase
# ──────────────────────────────────────────────
# Todos los artículos de una tienda comparten el mismo IVA.
separador("EJERCICIO 5 — ClassVar y la trampa del atributo de clase")

# Define la dataclass ArticuloTienda con:
#   nombre: str
#   precio_base: float
#   IVA: ClassVar[float] = 0.21
# Añade un método precio_final(self) que devuelva precio_base * (1 + IVA)
...

articulo = ...
# print(articulo.precio_final())  # Esperado: precio_base * 1.21

# Comprueba que IVA NO aparece en el __init__ intentando pasarlo
# como argumento (debe lanzar TypeError)
try:
    otro = ...  # ArticuloTienda("X", 10.0, IVA=0.10)
except TypeError as e:
    ...
    # print("Error:", e)  # Esperado: TypeError, IVA no es un parámetro del __init__


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# frozen=True y hashabilidad
# ──────────────────────────────────────────────
# Sistema de coordenadas GPS donde las posiciones no deben modificarse.
separador("EJERCICIO 6 — frozen=True y hashabilidad")

# Define la dataclass Coordenada con frozen=True y campos: lat: float, lon: float
...

coord = ...

# Intenta modificar lat dentro de un try/except y muestra el error
try:
    ...  # coord.lat = 0.0
except Exception as e:
    ...
    # print("Error:", e)  # Esperado: cannot assign to field 'lat' (FrozenInstanceError)

# Mete dos coordenadas distintas en un set para demostrar que son hashables
coordenadas_unicas = ...
# print(coordenadas_unicas)  # Esperado: set con las dos coordenadas


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# order=True: ordenar objetos
# ──────────────────────────────────────────────
# Clasificación de atletas en una competición.
separador("EJERCICIO 7 — order=True: ordenar objetos")

# Define la dataclass Atleta con order=True y campos: nombre: str, tiempo: float
...

atletas = [
    # crea varios Atleta con distintos tiempos
]

# CUIDADO: con nombre declarado antes que tiempo, sorted(atletas) sin
# key ordenaría por nombre (orden tipo tupla), no por tiempo.
# Ordénalos por tiempo usando key=lambda a: a.tiempo
atletas_ordenados = ...
# print(atletas_ordenados)  # Esperado: lista ordenada de menor a mayor tiempo


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# replace(): copias con campos modificados
# ──────────────────────────────────────────────
# Sistema de precios donde los productos se actualizan sin mutar el original.
separador("EJERCICIO 8 — replace(): copias con campos modificados")

# Define la dataclass Articulo con:
#   nombre: str
#   precio: float
#   precio_con_iva: float = field(init=False)
# Calcula precio_con_iva en __post_init__ (precio * 1.21)
...

original = ...

# Usa replace() para crear una copia con precio rebajado
rebajado = ...

# Imprime original y copia: comprueba que precio_con_iva se RECALCULA
# en la copia, no se copia el valor antiguo
# print(original)   # Esperado: Articulo(nombre=..., precio=..., precio_con_iva=precio*1.21)
# print(rebajado)   # Esperado: mismo nombre, precio nuevo, precio_con_iva RECALCULADO


# ──────────────────────────────────────────────
# EJERCICIO 9 — EXPERTO
# Herencia de dataclasses
# ──────────────────────────────────────────────
# Jerarquía de vehículos en un concesionario.
separador("EJERCICIO 9 — Herencia de dataclasses")

# Define la dataclass base Vehiculo con: marca: str, año: int
...

# Define Coche(Vehiculo) que añade: num_puertas: int = 4
...

# Crea un Coche pasando solo marca y año
coche1 = ...

# Crea otro Coche pasando también num_puertas
coche2 = ...

# Imprime ambos para ver el __repr__ con todos los campos heredados
# print(coche1)  # Esperado: Coche(marca=..., año=..., num_puertas=4)
# print(coche2)  # Esperado: Coche(marca=..., año=..., num_puertas=<el que pases>)


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# asdict() + dataclasses anidadas
# ──────────────────────────────────────────────
# API REST que serializa pedidos a JSON.
separador("EJERCICIO 10 — asdict() + dataclasses anidadas")

# Define la dataclass Direccion con: calle: str, ciudad: str
...

# Define la dataclass Pedido con: id: int, cliente: str, direccion: Direccion
...

pedido = ...

# Conviértelo con asdict() e imprime el resultado
pedido_dict = ...
# print(pedido_dict)  # Esperado: {'id': ..., 'cliente': ..., 'direccion': {'calle': ..., 'ciudad': ...}}

# Comprueba que direccion también se ha convertido a dict
# (no sigue siendo una instancia de Direccion)
# print(type(pedido_dict["direccion"]))  # Esperado: <class 'dict'>
