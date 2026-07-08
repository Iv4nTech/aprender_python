# ============================================================
#   EJERCICIOS PRÁCTICOS: DATACLASSES (RESUELTOS)
#   Casos reales, de fácil a experto.
# ============================================================

from dataclasses import dataclass, field, replace, asdict
from typing import ClassVar


def separador(titulo: str) -> None:
    """Imprime una cabecera para separar la salida de cada ejercicio."""
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


# ------------------------------------------------------------
# EJERCICIO 1 (FÁCIL) — Dataclass básica
# Define Libro con titulo, autor y paginas. Comprueba que == y
# __repr__ funcionan sin escribirlos a mano.
# ------------------------------------------------------------
separador("EJERCICIO 1 (FÁCIL) — Dataclass básica")

@dataclass
class Libro:
    titulo: str
    autor: str
    paginas: int

libro1 = Libro("El Quijote", "Miguel de Cervantes", 1000)
libro2 = Libro("El Quijote", "Miguel de Cervantes", 1000)

print(libro1)            # Esperado: Libro(titulo='El Quijote', autor='Miguel de Cervantes', paginas=1000)
print(libro1 == libro2)  # Esperado: True


# ------------------------------------------------------------
# EJERCICIO 2 (FÁCIL) — Valor por defecto
# Tarea con descripcion y completada (por defecto False).
# ------------------------------------------------------------
separador("EJERCICIO 2 (FÁCIL) — Valor por defecto")

@dataclass
class Tarea:
    descripcion: str
    completada: bool = False

tarea1 = Tarea("Hacer la compra")
tarea2 = Tarea("Limpiar la casa", completada=True)

print(tarea1)  # Esperado: Tarea(descripcion='Hacer la compra', completada=False)
print(tarea2)  # Esperado: Tarea(descripcion='Limpiar la casa', completada=True)


# ------------------------------------------------------------
# EJERCICIO 3 (FÁCIL) — __post_init__ para validar
# Pago con concepto e importe. Rechaza importes <= 0.
# ------------------------------------------------------------
separador("EJERCICIO 3 (FÁCIL) — __post_init__ para validar")

@dataclass
class Pago:
    concepto: str
    importe: float

    def __post_init__(self):
        if self.importe <= 0:
            raise ValueError("El importe debe ser un valor positivo")

pago_ok = Pago("Compra de libros", 50.0)
print(pago_ok)  # Esperado: Pago(concepto='Compra de libros', importe=50.0)

try:
    pago_malo = Pago("Compra de libros", -50.0)
except ValueError as e:
    print("Error:", e)  # Esperado: Error: El importe debe ser un valor positivo


# ------------------------------------------------------------
# EJERCICIO 4 (MEDIO) — Campo calculado con field(init=False)
# LineaCarrito calcula total = precio * cantidad en __post_init__.
# ------------------------------------------------------------
separador("EJERCICIO 4 (MEDIO) — Campo calculado con field(init=False)")

@dataclass
class LineaCarrito:
    producto: str
    precio: float
    cantidad: int
    total: float = field(init=False)

    def __post_init__(self):
        self.total = self.precio * self.cantidad

linea = LineaCarrito("Libro", 10.0, 5)
print(linea)  # Esperado: LineaCarrito(producto='Libro', precio=10.0, cantidad=5, total=50.0)


# ------------------------------------------------------------
# EJERCICIO 5 (MEDIO) — ClassVar y la trampa del atributo de clase
# ArticuloTienda comparte IVA como ClassVar, no como campo.
# ------------------------------------------------------------
separador("EJERCICIO 5 (MEDIO) — ClassVar y la trampa del atributo de clase")

@dataclass
class ArticuloTienda:
    nombre: str
    precio_base: float
    IVA: ClassVar[float] = 0.21

    def precio_final(self):
        return self.precio_base * (1 + self.IVA)

articulo = ArticuloTienda("Libro", 10.0)
print(articulo.precio_final())  # Esperado: 12.1

try:
    otro = ArticuloTienda("X", 10.0, IVA=0.10)
except TypeError as e:
    print("Error:", e)  # Esperado: TypeError, IVA no es un parámetro del __init__


# ------------------------------------------------------------
# EJERCICIO 6 (MEDIO) — frozen=True y hashabilidad
# Coordenada GPS inmutable y usable en un set.
# ------------------------------------------------------------
separador("EJERCICIO 6 (MEDIO) — frozen=True y hashabilidad")

@dataclass(frozen=True)
class Coordenada:
    lat: float
    lon: float

coord = Coordenada(40.4168, -3.7038)

try:
    coord.lat = 0.0
except Exception as e:
    print("Error:", e)  # Esperado: cannot assign to field 'lat' (FrozenInstanceError)

coordenadas_unicas = {Coordenada(40.4168, -3.7038), Coordenada(37.9838, -122.5005)}
print(coordenadas_unicas)  # Esperado: set con las dos coordenadas (son hashables)


# ------------------------------------------------------------
# EJERCICIO 7 (AVANZADO) — order=True: ordenar objetos
# Atleta declara nombre antes que tiempo. Con order=True, sorted()
# SIN key compararía primero por nombre (orden tipo tupla), no por
# tiempo. Para ordenar realmente por tiempo hay que pasar key=
# lambda a: a.tiempo, ignorando el orden natural de los campos.
# ------------------------------------------------------------
separador("EJERCICIO 7 (AVANZADO) — order=True: ordenar objetos")

@dataclass(order=True)
class Atleta:
    nombre: str
    tiempo: float

atletas = [
    Atleta("Usain Bolt", 9.58),
    Atleta("Tyson", 9.69),
    Atleta("Yohan Blake", 9.69),
    Atleta("Justin Gatlin", 9.74),
]

atletas_ordenados = sorted(atletas, key=lambda a: a.tiempo)
print(atletas_ordenados)
# Esperado: [Atleta(nombre='Usain Bolt', tiempo=9.58), Atleta(nombre='Tyson', tiempo=9.69),
#            Atleta(nombre='Yohan Blake', tiempo=9.69), Atleta(nombre='Justin Gatlin', tiempo=9.74)]


# ------------------------------------------------------------
# EJERCICIO 8 (AVANZADO) — replace(): copias con campos modificados
# precio_con_iva se recalcula en la copia, no se copia del original.
# ------------------------------------------------------------
separador("EJERCICIO 8 (AVANZADO) — replace(): copias con campos modificados")

@dataclass
class Articulo:
    nombre: str
    precio: float
    precio_con_iva: float = field(init=False)

    def __post_init__(self):
        self.precio_con_iva = self.precio * 1.21

original = Articulo("X", 10.0)
rebajado = replace(original, precio=8.0)

print(original)   # Esperado: Articulo(nombre='X', precio=10.0, precio_con_iva=12.1)
print(rebajado)    # Esperado: Articulo(nombre='X', precio=8.0, precio_con_iva=9.68) -> recalculado, no copiado


# ------------------------------------------------------------
# EJERCICIO 9 (EXPERTO) — Herencia de dataclasses
# Coche hereda marca y año de Vehiculo, y añade num_puertas.
# ------------------------------------------------------------
separador("EJERCICIO 9 (EXPERTO) — Herencia de dataclasses")

@dataclass
class Vehiculo:
    marca: str
    año: int

@dataclass
class Coche(Vehiculo):
    num_puertas: int = 4

coche1 = Coche("Toyota", 2020)
coche2 = Coche("Ford", 2018, num_puertas=2)

print(coche1)  # Esperado: Coche(marca='Toyota', año=2020, num_puertas=4)
print(coche2)  # Esperado: Coche(marca='Ford', año=2018, num_puertas=2)


# ------------------------------------------------------------
# EJERCICIO 10 (EXPERTO) — asdict() + dataclasses anidadas
# Pedido con una Direccion anidada, convertido a dict recursivo.
# ------------------------------------------------------------
separador("EJERCICIO 10 (EXPERTO) — asdict() + dataclasses anidadas")

@dataclass
class Direccion:
    calle: str
    ciudad: str

@dataclass
class Pedido:
    id: int
    cliente: str
    direccion: Direccion

pedido = Pedido(1, "John Doe", Direccion("123 Main St", "Anytown"))
pedido_dict = asdict(pedido)

print(pedido_dict)
# Esperado: {'id': 1, 'cliente': 'John Doe', 'direccion': {'calle': '123 Main St', 'ciudad': 'Anytown'}}
print(type(pedido_dict["direccion"]))  # Esperado: <class 'dict'>
