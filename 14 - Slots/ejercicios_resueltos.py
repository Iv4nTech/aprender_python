# ============================================================
#   EJERCICIOS PRÁCTICOS: __slots__ (RESUELTOS)
#   Casos reales, de fácil a experto.
# ============================================================
# python3 ejercicios_resueltos.py

import sys
import timeit


def seccion(titulo: str) -> None:
    """Pequeño helper para imprimir cabeceras y que la salida sea legible."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ──────────────────────────────────────────────
# EJERCICIO 1 — FÁCIL
# Clase básica con __slots__
# ──────────────────────────────────────────────
# Modelas un producto de un almacén y quieres evitar el coste de un
# __dict__ por instancia, ya que todos los productos tienen siempre
# los mismos campos: nombre y precio.
seccion("EJERCICIO 1 — Clase básica con __slots__")

class Producto:
    __slots__ = ("nombre", "precio")

    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio

producto = Producto("Laptop", 999.99)
print(producto.nombre, producto.precio)


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Comprobar ausencia de __dict__
# ──────────────────────────────────────────────
# Quieres demostrar, para una charla interna sobre optimización, que las
# instancias de Producto ya no tienen __dict__.
seccion("EJERCICIO 2 — Comprobar ausencia de __dict__")

tiene_dict = hasattr(producto, "__dict__")
print(tiene_dict)  # Esperado: False

try:
    dict_producto = producto.__dict__
except AttributeError as e:
    print("Error:", e)


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Acceso y modificación con notación punto
# ──────────────────────────────────────────────
# El precio de "producto" ha cambiado tras una revisión de tarifas.
seccion("EJERCICIO 3 — Acceso y modificación con notación punto")

print(producto.precio)
producto.precio = 39.99
print(producto.precio)


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Añadir un atributo no declarado
# ──────────────────────────────────────────────
# Un compañero intenta añadir un campo "stock" a `producto` que nunca se
# declaró en __slots__. Debes capturar el error correctamente en vez de
# dejar que rompa el programa.
seccion("EJERCICIO 4 — Añadir un atributo no declarado")

try:
    producto.stock = 10
except AttributeError as e:
    print("Error:", e)


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Memoria: clase normal vs clase con __slots__
# ──────────────────────────────────────────────
# El equipo de infraestructura quiere datos concretos del ahorro de
# memoria antes de migrar un modelo de datos a __slots__.
seccion("EJERCICIO 5 — Memoria: clase normal vs clase con __slots__")

class ProductoNormal:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio

normal = ProductoNormal("Laptop", 999.99)
con_slots = Producto("Laptop", 999.99)

tam_normal = sys.getsizeof(normal) + sys.getsizeof(normal.__dict__)
tam_slots = sys.getsizeof(con_slots)

print(f"Normal: {tam_normal} bytes | Slots: {tam_slots} bytes")


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# Herencia correcta: la subclase también declara __slots__
# ──────────────────────────────────────────────
# Necesitas un ProductoConStock que añada un campo `stock` a Producto,
# manteniendo el ahorro de memoria de __slots__.
seccion("EJERCICIO 6 — Herencia correcta")

class ProductoConStock(Producto):
    __slots__ = ("stock",)

    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        super().__init__(nombre, precio)
        self.stock = stock

con_stock = ProductoConStock("Laptop", 999.99, 10)
print(con_stock.nombre, con_stock.precio, con_stock.stock)
print(hasattr(con_stock, "__dict__"))  # Esperado: False


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# Herencia incorrecta: la subclase no declara __slots__
# ──────────────────────────────────────────────
# Un compañero crea ProductoConDescuento heredando de Producto pero
# se olvida de declarar __slots__. Debes demostrar qué ocurre.
seccion("EJERCICIO 7 — Herencia incorrecta")

class ProductoConDescuento(Producto):
    def __init__(self, nombre: str, precio: float, descuento: float) -> None:
        super().__init__(nombre, precio)
        self.descuento = descuento

con_descuento = ProductoConDescuento("Laptop", 999.99, 0.1)
print(hasattr(con_descuento, "__dict__"))  # Esperado: True
print(con_descuento.__dict__)              # Esperado: {'descuento': ...}

# Al recuperar __dict__, también se pueden colar atributos no declarados
# en ningún sitio.
con_descuento.campo_inventado = "¡Hola!"
print(con_descuento.campo_inventado)


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Modo híbrido: '__dict__' dentro de __slots__
# ──────────────────────────────────────────────
# Necesitas un ProductoFlexible que mantenga nombre y precio como slots
# optimizados, pero permita añadir metadatos arbitrarios sobre la marcha.
seccion("EJERCICIO 8 — Modo híbrido")

class ProductoFlexible:
    __slots__ = ("nombre", "precio", "__dict__")

    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio

flexible = ProductoFlexible("Laptop", 999.99)

print(hasattr(flexible, "__dict__"))  # Esperado: True

flexible.proveedor = "TechCorp"
print(flexible.proveedor, flexible.__dict__)


# ──────────────────────────────────────────────
# EJERCICIO 9 — EXPERTO
# Benchmark real: 100.000 instancias
# ──────────────────────────────────────────────
# Antes de aprobar la migración a __slots__ en producción, necesitas
# cuantificar el ahorro de memoria y la diferencia de tiempo de
# creación con un caso a gran escala.
seccion("EJERCICIO 9 — Benchmark real: 100.000 instancias")

N = 100_000

instancias_normales = [ProductoNormal(f"Producto {i}", i * 1.0) for i in range(N)]
instancias_slots = [Producto(f"Producto {i}", i * 1.0) for i in range(N)]

memoria_normal = sum(sys.getsizeof(instancia) + sys.getsizeof(instancia.__dict__) for instancia in instancias_normales)
memoria_slots = sum(sys.getsizeof(instancia) for instancia in instancias_slots)

print(f"Memoria normal: {memoria_normal:,} bytes")
print(f"Memoria slots:  {memoria_slots:,} bytes")

tiempo_normal = timeit.timeit(lambda: [ProductoNormal(f"Producto {i}", i * 1.0) for i in range(N)], number=5)
tiempo_slots = timeit.timeit(lambda: [Producto(f"Producto {i}", i * 1.0) for i in range(N)], number=5)

print(f"Tiempo normal: {tiempo_normal:.3f}s")
print(f"Tiempo slots:  {tiempo_slots:.3f}s")
