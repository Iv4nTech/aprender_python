# ============================================================
# EJERCICIOS: __slots__ EN PYTHON
# Casos reales — de fácil a experto
# ============================================================
# python3 ejercicios.py

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

# Define la clase Producto con __slots__ = ("nombre", "precio")
# y un __init__ que reciba ambos valores.
...

# Crea una instancia y muestra sus valores
producto = ...
# print(producto.nombre, producto.precio)


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Comprobar ausencia de __dict__
# ──────────────────────────────────────────────
# Quieres demostrar, para una charla interna sobre optimización, que las
# instancias de Producto ya no tienen __dict__.
seccion("EJERCICIO 2 — Comprobar ausencia de __dict__")

# Usa hasattr() para comprobar si `producto` tiene atributo __dict__
tiene_dict = ...
# print(tiene_dict)  # Esperado: False

# Intenta acceder a producto.__dict__ dentro de un try/except
# capturando AttributeError y mostrando el mensaje del error
try:
    ...
except AttributeError as e:
    ...
    # print("Error:", e)


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Acceso y modificación con notación punto
# ──────────────────────────────────────────────
# El precio de "producto" ha cambiado tras una revisión de tarifas.
seccion("EJERCICIO 3 — Acceso y modificación con notación punto")

# Muestra el precio actual de producto
# print(producto.precio)

# Modifica producto.precio a 39.99 usando notación punto
...

# Muestra el precio ya actualizado
# print(producto.precio)


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Añadir un atributo no declarado
# ──────────────────────────────────────────────
# Un compañero intenta añadir un campo "stock" a `producto` que nunca se
# declaró en __slots__. Debes capturar el error correctamente en vez de
# dejar que rompa el programa.
seccion("EJERCICIO 4 — Añadir un atributo no declarado")

# Dentro de un try/except, intenta hacer producto.stock = 10
# Captura AttributeError e imprime el mensaje del error
try:
    ...
except AttributeError as e:
    ...
    # print("Error:", e)


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Memoria: clase normal vs clase con __slots__
# ──────────────────────────────────────────────
# El equipo de infraestructura quiere datos concretos del ahorro de
# memoria antes de migrar un modelo de datos a __slots__.
seccion("EJERCICIO 5 — Memoria: clase normal vs clase con __slots__")

# Define ProductoNormal, una clase SIN __slots__, con el mismo
# __init__ que Producto (nombre, precio)
...

# Crea una instancia de cada clase con los mismos valores
normal = ...
con_slots = ...

# Calcula el tamaño de `normal` sumando sys.getsizeof(normal) y
# sys.getsizeof(normal.__dict__), y el tamaño de `con_slots` con
# sys.getsizeof(con_slots)
tam_normal = ...
tam_slots = ...

# print(f"Normal: {tam_normal} bytes | Slots: {tam_slots} bytes")


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# Herencia correcta: la subclase también declara __slots__
# ──────────────────────────────────────────────
# Necesitas un ProductoConStock que añada un campo `stock` a Producto,
# manteniendo el ahorro de memoria de __slots__.
seccion("EJERCICIO 6 — Herencia correcta")

# Define ProductoConStock(Producto) con __slots__ = ("stock",)
# (solo el atributo NUEVO, nombre y precio ya están en la clase base)
# Su __init__ debe llamar a super().__init__(nombre, precio) y
# asignar self.stock
...

# Crea una instancia y comprueba que sigue sin tener __dict__
con_stock = ...
# print(con_stock.nombre, con_stock.precio, con_stock.stock)
# print(hasattr(con_stock, "__dict__"))  # Esperado: False


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# Herencia incorrecta: la subclase no declara __slots__
# ──────────────────────────────────────────────
# Un compañero crea ProductoConDescuento heredando de Producto pero
# se olvida de declarar __slots__. Debes demostrar qué ocurre.
seccion("EJERCICIO 7 — Herencia incorrecta")

# Define ProductoConDescuento(Producto) SIN __slots__, con un __init__
# que llame a super().__init__(nombre, precio) y guarde self.descuento
...

# Crea una instancia y comprueba que SÍ tiene __dict__
con_descuento = ...
# print(hasattr(con_descuento, "__dict__"))  # Esperado: True
# print(con_descuento.__dict__)              # Esperado: {'descuento': ...}

# Demuestra que, al recuperar __dict__, también se pueden colar
# atributos no declarados en ningún sitio
...
# print(con_descuento.campo_inventado)


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Modo híbrido: '__dict__' dentro de __slots__
# ──────────────────────────────────────────────
# Necesitas un ProductoFlexible que mantenga nombre y precio como slots
# optimizados, pero permita añadir metadatos arbitrarios sobre la marcha.
seccion("EJERCICIO 8 — Modo híbrido")

# Define ProductoFlexible con __slots__ = ("nombre", "precio", "__dict__")
# y el mismo __init__ que Producto
...

flexible = ...

# Comprueba que tiene __dict__
# print(hasattr(flexible, "__dict__"))  # Esperado: True

# Añade un atributo libre no declarado, por ejemplo "proveedor"
...
# print(flexible.proveedor, flexible.__dict__)


# ──────────────────────────────────────────────
# EJERCICIO 9 — EXPERTO
# Benchmark real: 100.000 instancias
# ──────────────────────────────────────────────
# Antes de aprobar la migración a __slots__ en producción, necesitas
# cuantificar el ahorro de memoria y la diferencia de tiempo de
# creación con un caso a gran escala.
seccion("EJERCICIO 9 — Benchmark real: 100.000 instancias")

N = 100_000

# Crea una lista de N instancias de ProductoNormal y otra de N
# instancias de Producto (con slots), con valores cualesquiera
instancias_normales = ...
instancias_slots = ...

# Calcula la memoria total de cada lista (suma de tamaños de cada
# instancia; para ProductoNormal recuerda sumar también su __dict__)
memoria_normal = ...
memoria_slots = ...

# print(f"Memoria normal: {memoria_normal:,} bytes")
# print(f"Memoria slots:  {memoria_slots:,} bytes")

# Usa timeit.timeit() para medir el tiempo de crear N instancias de
# cada clase (usa una lambda con list comprehension y number=5)
tiempo_normal = ...
tiempo_slots = ...

# print(f"Tiempo normal: {tiempo_normal:.3f}s")
# print(f"Tiempo slots:  {tiempo_slots:.3f}s")
