"""
================================================================================
 DATACLASSES EN PYTHON — GUÍA COMPLETA (de cero a experto)
================================================================================

Una dataclass es una clase normal a la que el decorador @dataclass le genera
automáticamente el "código de fontanería" (boilerplate) que casi toda clase
que solo almacena datos necesita: __init__, __repr__ y __eq__.

    "Boilerplate" -> código repetitivo que escribirías igual en cada clase
                      de este tipo: asignar self.campo = campo, construir un
                      repr legible, comparar campo a campo...

¿Por qué importa? Porque ese código es mecánico y propenso a errores (olvidar
un campo en el __eq__, un repr desactualizado tras añadir un atributo...).
@dataclass lo genera a partir de las anotaciones de tipo de la clase, así que
declaras los campos una sola vez y el resto se deriva automáticamente.

Este fichero está pensado para ejecutarse de principio a fin:

    python3 introduccion.py

Cada sección imprime resultados para que veas el comportamiento real.
================================================================================
"""

from dataclasses import dataclass, field, replace, asdict, FrozenInstanceError
from typing import ClassVar


def seccion(titulo: str) -> None:
    """Pequeño helper para imprimir cabeceras y que la salida sea legible."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA QUE RESUELVE @dataclass
# ============================================================================
seccion("1. El problema: boilerplate escrito a mano")

# Una clase "normal" para modelar un producto necesita escribir a mano
# __init__, __repr__ y __eq__ si quieres que se comporte de forma razonable.
class ProductoNormal:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"ProductoNormal(nombre={self.nombre!r}, precio={self.precio!r}, stock={self.stock!r})"

    def __eq__(self, other):
        if not isinstance(other, ProductoNormal):
            return NotImplemented
        return (self.nombre, self.precio, self.stock) == (other.nombre, other.precio, other.stock)

p1 = ProductoNormal("Teclado", 45.99, 10)
p2 = ProductoNormal("Teclado", 45.99, 10)
print("Objeto:", p1)
print("¿p1 == p2?:", p1 == p2)

# Todo ese __init__/__repr__/__eq__ es boilerplate mecánico: se deduce
# completamente de los campos (nombre, precio, stock). @dataclass lo genera
# por ti a partir de las anotaciones de tipo.


# ============================================================================
# 2. LA MISMA CLASE CON @dataclass
# ============================================================================
seccion("2. La misma clase con @dataclass")

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int

q1 = Producto("Teclado", 45.99, 10)
q2 = Producto("Teclado", 45.99, 10)
print("Objeto:", q1)                    # __repr__ generado automáticamente
print("¿q1 == q2?:", q1 == q2)          # __eq__ generado automáticamente

# La firma completa del decorador, con TODOS sus parámetros por defecto, es:
#
# @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False,
#            frozen=False, match_args=True, kw_only=False, slots=False,
#            weakref_slot=False)
#
# Tres formas EQUIVALENTES de usarlo cuando quieres los valores por defecto:

@dataclass
class A:
    x: int

@dataclass()
class B:
    x: int

@dataclass(init=True, repr=True, eq=True)
class C:
    x: int

print("A(1):", A(1), "| B(1):", B(1), "| C(1):", C(1))


# ============================================================================
# 3. VALORES POR DEFECTO Y field()
# ============================================================================
seccion("3. Valores por defecto y field()")

# Un valor por defecto simple funciona igual que en cualquier función.
@dataclass
class ProductoConStock:
    nombre: str
    precio: float
    stock: int = 0

print("Sin indicar stock:", ProductoConStock("Ratón", 19.99))

# TRAMPA: los objetos MUTABLES no están permitidos como valor por defecto
# directo. Python los compartiría entre TODAS las instancias (el mismo bug
# clásico de "def f(lista=[])").
try:
    @dataclass
    class ProductoConEtiquetas:
        nombre: str
        etiquetas: list = []          # ValueError al definir la clase
except ValueError as e:
    print("etiquetas: list = [] ->", type(e).__name__, "->", e)

# La solución correcta: field(default_factory=list). La factory se llama
# UNA VEZ POR INSTANCIA, así que cada objeto recibe su propia lista.
@dataclass
class ProductoConEtiquetasOK:
    nombre: str
    etiquetas: list = field(default_factory=list)

e1 = ProductoConEtiquetasOK("Monitor")
e2 = ProductoConEtiquetasOK("Monitor")
e1.etiquetas.append("oferta")
print("e1.etiquetas:", e1.etiquetas, "| e2.etiquetas:", e2.etiquetas)  # no se comparten

# field(repr=False) excluye el campo del __repr__.
# field(init=False) excluye el campo del __init__ (no se puede pasar como argumento).
@dataclass
class ProductoConCampoOculto:
    nombre: str
    precio: float
    codigo_interno: str = field(default="SIN-ASIGNAR", repr=False)
    veces_vendido: int = field(default=0, init=False)

f1 = ProductoConCampoOculto("Webcam", 59.99)
print("repr (sin codigo_interno):", f1)
print("codigo_interno sigue existiendo:", f1.codigo_interno)


# ============================================================================
# 4. ClassVar: ATRIBUTOS DE CLASE, NO DE INSTANCIA
# ============================================================================
seccion("4. ClassVar: el error más común al empezar")

# Un campo anotado con ClassVar es IGNORADO por completo por @dataclass:
# no entra en __init__, no aparece en __repr__, no participa en __eq__.
# Es un atributo de la CLASE, compartido por todas las instancias.
@dataclass
class ProductoConIVA:
    nombre: str
    precio: float
    IVA: ClassVar[float] = 0.21     # compartido, no es un campo de instancia

g1 = ProductoConIVA("Silla", 120.0)
print("g1:", g1)                              # IVA NO aparece en el repr
print("ProductoConIVA.IVA:", ProductoConIVA.IVA, "| g1.IVA:", g1.IVA)

# El error clásico: olvidar ClassVar y poner el atributo "a pelo".
# Entonces SÍ se convierte en un campo normal y aparece en __init__:
@dataclass
class ProductoSinClassVar:
    nombre: str
    IVA: float = 0.21               # esto SÍ es un campo de instancia

print("Sin ClassVar, IVA es un parámetro más:", ProductoSinClassVar("Mesa", 0.10))


# ============================================================================
# 5. __post_init__: VALIDACIONES Y CAMPOS CALCULADOS
# ============================================================================
seccion("5. __post_init__: validar y calcular")

# El __init__ generado llama automáticamente a __post_init__ (si existe)
# justo después de asignar todos los campos. Es el sitio para validar
# datos o calcular campos derivados.
@dataclass
class Articulo:
    nombre: str
    precio: float
    precio_con_iva: float = field(init=False)   # se calcula, no se pasa

    IVA: ClassVar[float] = 0.21

    def __post_init__(self):
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio_con_iva = round(self.precio * (1 + Articulo.IVA), 2)

art = Articulo("Lámpara", 40.0)
print("Artículo con precio_con_iva calculado:", art)

try:
    Articulo("Roto", -5.0)
except ValueError as e:
    print("precio negativo ->", type(e).__name__, "->", e)


# ============================================================================
# 6. frozen=True: INSTANCIAS INMUTABLES
# ============================================================================
seccion("6. frozen=True: inmutabilidad y hash")

# Con frozen=True, @dataclass genera __setattr__ y __delattr__ que lanzan
# FrozenInstanceError (subclase de AttributeError) al intentar modificar
# o borrar un campo tras la creación.
@dataclass(frozen=True)
class Punto:
    x: float
    y: float

pt = Punto(1.0, 2.0)
try:
    pt.x = 99.0
except FrozenInstanceError as e:
    print("Modificar campo frozen ->", type(e).__name__, "->", e)

# Además, cuando frozen=True y eq=True (el default), @dataclass genera
# automáticamente __hash__. Eso hace la instancia hashable: usable como
# clave de dict o elemento de un set.
puntos_vistos = {Punto(0, 0), Punto(1, 1), Punto(0, 0)}   # el duplicado se descarta
print("Set de puntos (hashable):", puntos_vistos)
cache = {Punto(1.0, 2.0): "esquina"}
print("Como clave de dict:", cache[Punto(1.0, 2.0)])


# ============================================================================
# 7. order=True: COMPARACIÓN Y ORDENACIÓN
# ============================================================================
seccion("7. order=True: comparar y ordenar")

# Con order=True se generan __lt__, __le__, __gt__, __ge__ que comparan
# la clase como si fuera una tupla de sus campos en el orden declarado.
#
# Reglas importantes documentadas:
#   - Si order=True y eq=False -> ValueError al definir la clase.
#   - Si la clase ya define alguno de esos métodos -> TypeError.
@dataclass(order=True)
class Jugador:
    puntos: int
    nombre: str

jugadores = [Jugador(50, "Ana"), Jugador(90, "Luis"), Jugador(70, "Eva")]
print("Ordenado por puntos (campo declarado primero):", sorted(jugadores))
print("¿Jugador(50,'Ana') < Jugador(90,'Luis')?:", jugadores[0] < jugadores[1])

try:
    @dataclass(order=True, eq=False)
    class Invalido:
        x: int
except ValueError as e:
    print("order=True, eq=False ->", type(e).__name__, "->", e)


# ============================================================================
# 8. replace(): CREAR COPIAS MODIFICADAS
# ============================================================================
seccion("8. replace(): copias con campos modificados")

# dataclasses.replace(obj, **cambios) crea un objeto NUEVO del mismo tipo,
# reemplazando los campos indicados. Llama a __init__ y, por tanto,
# también a __post_init__. Es el equivalente a _replace() de namedtuple.
articulo_original = Articulo("Silla", 100.0)
articulo_rebajado = replace(articulo_original, precio=80.0)
print("Original:       ", articulo_original)
print("Copia (replace):", articulo_rebajado)

# TRAMPA documentada oficialmente: los campos con init=False NO se copian
# del objeto original, se RECALCULAN en __post_init__. Aquí se ve con
# precio_con_iva: no es el valor antiguo ajustado, es el nuevo calculado
# desde cero a partir del precio actualizado.
print("precio_con_iva original:", articulo_original.precio_con_iva)
print("precio_con_iva copia (recalculado, no copiado):", articulo_rebajado.precio_con_iva)


# ============================================================================
# 9. asdict(): CONVERSIÓN A DICT
# ============================================================================
seccion("9. asdict(): conversión recursiva a dict")

# dataclasses.asdict() convierte la dataclass (y las dataclasses anidadas
# dentro de ella) a un dict de forma recursiva. Muy útil para serializar
# a JSON o pasar datos a funciones que esperan dicts planos.
@dataclass
class Direccion:
    calle: str
    ciudad: str

@dataclass
class Cliente:
    nombre: str
    direccion: Direccion

cliente = Cliente("Marta", Direccion("Gran Vía 1", "Madrid"))
cliente_dict = asdict(cliente)
print("Cliente como dict:", cliente_dict)
print("¿direccion es dict?:", type(cliente_dict["direccion"]) is dict)


# ============================================================================
# 10. HERENCIA ENTRE DATACLASSES
# ============================================================================
seccion("10. Herencia entre dataclasses")

# @dataclass recorre las clases base en MRO inverso y combina los campos
# en ese orden: los campos del padre van ANTES que los del hijo.
#
# Regla importante: si el padre tiene campos con valor por defecto, los
# campos del hijo SIN valor por defecto deben declararse antes de cualquier
# campo con default en el conjunto combinado, o se lanza TypeError.
@dataclass
class Vehiculo:
    marca: str
    año: int

@dataclass
class Coche(Vehiculo):
    num_puertas: int = 4

coche = Coche("Toyota", 2022)
print("Coche (hereda marca y año):", coche)
print("Con num_puertas explícito:", Coche("Seat", 2020, 3))
# __init__ generado equivalente a:
#   def __init__(self, marca: str, año: int, num_puertas: int = 4): ...


# ============================================================================
# 11. @dataclass vs CLASE NORMAL vs namedtuple
# ============================================================================
seccion("11. Cuándo usar cada una")

# +-------------------+------------------+------------------+------------------+
# |                   | clase normal     | @dataclass       | namedtuple       |
# +-------------------+------------------+------------------+------------------+
# | Mutable            | sí (por defecto) | sí (o frozen)     | no (inmutable)   |
# | Boilerplate        | lo escribes tú   | generado          | generado         |
# | Métodos propios    | sí               | sí                | limitado         |
# | Comportamiento rico | ideal            | ideal             | pobre            |
# +-------------------+------------------+------------------+------------------+
#
# Regla práctica:
#   - namedtuple / NamedTuple: registro de datos fijo e inmutable, ligero.
#   - @dataclass: la opción por defecto para clases que sobre todo guardan
#     datos, con validaciones, campos calculados o mutabilidad opcional.
#   - clase normal: cuando el comportamiento pesa más que los datos, o
#     necesitas control total sobre __init__/__eq__/etc.

seccion("FIN — ya conoces las dataclasses al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
