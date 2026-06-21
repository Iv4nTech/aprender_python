"""
================================================================================
 TUPLAS EN PYTHON — GUÍA COMPLETA (de cero a experto)
================================================================================

Una tupla es una secuencia ORDENADA e INMUTABLE de elementos.

    "Ordenada"  -> mantiene el orden de inserción y permite acceso por índice.
    "Inmutable" -> una vez creada NO puedes añadir, quitar ni reasignar
                   sus elementos. Esta es la diferencia clave frente a la lista.

¿Por qué importa la inmutabilidad? Porque comunica intención y da garantías:
si algo es una tupla, el lector del código sabe que NO va a cambiar. Eso permite
usarla como clave de diccionario, como elemento de un set, cachear funciones,
y razonar sobre el código con más seguridad.

Este fichero está pensado para ejecutarse de principio a fin:

    python3 introduccion.py

Cada sección imprime resultados para que veas el comportamiento real.
================================================================================
"""

from collections import namedtuple
from typing import NamedTuple


def seccion(titulo: str) -> None:
    """Pequeño helper para imprimir cabeceras y que la salida sea legible."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. CREACIÓN DE TUPLAS
# ============================================================================
seccion("1. Creación de tuplas")

# La forma más habitual: paréntesis y comas.
coordenada = (40.4168, -3.7038)            # Latitud/longitud de Madrid
print("Con paréntesis:", coordenada)

# Los paréntesis son OPCIONALES. Lo que crea la tupla es la COMA, no el ().
coordenada_sin_parentesis = 40.4168, -3.7038
print("Sin paréntesis:", coordenada_sin_parentesis)

# TRAMPA CLÁSICA: una tupla de un solo elemento necesita coma final.
no_es_tupla = (5)        # esto es simplemente el entero 5
si_es_tupla = (5,)       # esto SÍ es una tupla de un elemento
print("(5)  ->", type(no_es_tupla).__name__, no_es_tupla)
print("(5,) ->", type(si_es_tupla).__name__, si_es_tupla)

# Tupla vacía.
vacia = ()
print("Tupla vacía:", vacia, "| len:", len(vacia))

# Con el constructor tuple() a partir de cualquier iterable.
desde_string = tuple("Python")           # cada carácter es un elemento
desde_rango = tuple(range(5))
print("tuple('Python'):", desde_string)
print("tuple(range(5)):", desde_rango)


# ============================================================================
# 2. TUPLA vs LISTA: la comparación clave
# ============================================================================
seccion("2. Tupla vs Lista")

lista = [1, 2, 3]
tupla = (1, 2, 3)

# Ambas se indexan y recorren igual.
print("lista[0]:", lista[0], "| tupla[0]:", tupla[0])

# Pero la lista se puede MUTAR...
lista[0] = 99
print("Lista tras mutar:", lista)

# ...y la tupla NO. Intentarlo lanza TypeError.
try:
    tupla[0] = 99
except TypeError as e:
    print("Mutar tupla ->", type(e).__name__, "->", e)

# Diferencia de memoria: la tupla ocupa menos y es más rápida de crear.
import sys
print("Bytes lista [1,2,3]:", sys.getsizeof([1, 2, 3]))
print("Bytes tupla (1,2,3):", sys.getsizeof((1, 2, 3)))

# CUÁNDO USAR CADA UNA (regla práctica):
#   - Lista: colección que va a crecer/cambiar (carrito, resultados, buffer).
#   - Tupla: registro de campos fijos (un punto x/y, una fila de BD, RGB),
#            o cualquier dato que NO debe cambiar.


# ============================================================================
# 3. INMUTABILIDAD CON MATICES (el malentendido más común)
# ============================================================================
seccion("3. Inmutabilidad: superficial, no profunda")

# La tupla es inmutable en sus REFERENCIAS, no en los objetos que contiene.
# Si guardas una lista dentro de una tupla, la lista sigue siendo mutable.
config = ("servidor", ["log", "cache"])
config[1].append("metrics")              # mutamos la lista interna: PERMITIDO
print("Tupla con lista mutada dentro:", config)

# Lo que NO puedes es reasignar la posición:
try:
    config[1] = ["otra"]
except TypeError as e:
    print("Reasignar posición ->", type(e).__name__)

# Consecuencia práctica: una tupla solo es "hashable" si TODOS sus elementos
# lo son. Una tupla con lista dentro NO puede ser clave de diccionario.
print("hash((1, 2, 3)):", hash((1, 2, 3)))
try:
    hash((1, [2, 3]))
except TypeError as e:
    print("hash((1, [2,3])) ->", type(e).__name__, "->", e)


# ============================================================================
# 4. EMPAQUETADO Y DESEMPAQUETADO (packing / unpacking)
# ============================================================================
seccion("4. Empaquetado y desempaquetado")

# Empaquetar: varios valores en una tupla.
punto = 3, 4
# Desempaquetar: repartir la tupla en variables. Nº de variables = nº elementos.
x, y = punto
print(f"x={x}, y={y}")

# El intercambio idiomático de Python usa tuplas por debajo:
a, b = 10, 20
a, b = b, a
print("Swap sin variable temporal:", a, b)

# Desempaquetado con * (star) para capturar "el resto" en una lista.
primero, *medio, ultimo = (1, 2, 3, 4, 5)
print("primero:", primero, "| medio:", medio, "| ultimo:", ultimo)

# Caso real: separar cabecera y filas de un CSV ya parseado.
filas = [("nombre", "edad"), ("Ana", "30"), ("Luis", "25")]
cabecera, *datos = filas
print("Cabecera:", cabecera)
print("Datos:", datos)

# Ignorar valores con _ (convención para "no me interesa").
_, lat, lon = ("ES", 40.41, -3.70)
print("Lat/Lon ignorando país:", lat, lon)


# ============================================================================
# 5. TUPLAS COMO VALOR DE RETORNO MÚLTIPLE
# ============================================================================
seccion("5. Retornar varios valores con tuplas")

def estadisticas(numeros: tuple) -> tuple:
    """Devuelve (mínimo, máximo, media). En Python esto ES una tupla."""
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

ventas = (120, 340, 90, 500, 210)
minimo, maximo, media = estadisticas(ventas)   # desempaquetado directo
print(f"min={minimo}, max={maximo}, media={media:.1f}")

# divmod, una función estándar, devuelve una tupla (cociente, resto).
cociente, resto = divmod(17, 5)
print(f"17 = 5*{cociente} + {resto}")


# ============================================================================
# 6. MÉTODOS Y OPERACIONES DISPONIBLES
# ============================================================================
seccion("6. Métodos y operaciones")

# Las tuplas SOLO tienen DOS métodos (por ser inmutables): count() e index().
notas = (7, 8, 7, 9, 7, 10)
print("count(7):", notas.count(7))           # cuántas veces aparece
print("index(9):", notas.index(9))           # primera posición del valor

# Operaciones de secuencia que SÍ funcionan (crean tuplas NUEVAS):
print("Concatenación (+):", (1, 2) + (3, 4))
print("Repetición   (*):", (0,) * 5)
print("Pertenencia (in):", 9 in notas)
print("Longitud  (len):", len(notas))
print("Slicing [1:4]:", notas[1:4])
print("Reverso [::-1]:", notas[::-1])

# Funciones built-in que aceptan tuplas:
print("min/max/sum:", min(notas), max(notas), sum(notas))
print("sorted (devuelve lista):", sorted(notas))


# ============================================================================
# 7. TUPLAS COMO CLAVES DE DICCIONARIO (caso real potente)
# ============================================================================
seccion("7. Tuplas como claves de diccionario")

# Como son hashables, sirven para indexar por una combinación de campos.
# Ejemplo: precio según (origen, destino) de un vuelo.
precios = {
    ("MAD", "BCN"): 49.99,
    ("MAD", "LON"): 120.50,
    ("BCN", "PAR"): 89.00,
}
ruta = ("MAD", "BCN")
print(f"Precio {ruta}:", precios[ruta])

# Otro patrón: matriz dispersa / tablero, indexado por (fila, columna).
tablero = {}
tablero[(0, 0)] = "torre"
tablero[(0, 4)] = "rey"
print("Pieza en (0,0):", tablero[(0, 0)])


# ============================================================================
# 8. NAMEDTUPLE: tuplas con campos con nombre
# ============================================================================
seccion("8. namedtuple (collections)")

# Problema: en una tupla normal accedes por índice (punto[0]) y es ilegible.
# namedtuple te da nombres SIN perder la inmutabilidad ni el rendimiento.
Punto = namedtuple("Punto", ["x", "y"])
p = Punto(3, 4)
print("p:", p, "| p.x:", p.x, "| p.y:", p.y)

# Sigue siendo una tupla: se desempaqueta e indexa igual.
px, py = p
print("Desempaquetado:", px, py, "| p[0]:", p[0])

# _replace crea una COPIA con un campo cambiado (no muta el original).
p2 = p._replace(y=99)
print("Original:", p, "| Copia con _replace:", p2)

# Versión moderna y con tipos usando typing.NamedTuple (clase):
class Empleado(NamedTuple):
    nombre: str
    salario: float
    activo: bool = True              # admite valores por defecto

e = Empleado("Ana", 45000)
print("Empleado:", e, "| .nombre:", e.nombre, "| .activo:", e.activo)


# ============================================================================
# 9. RENDIMIENTO E INMUTABILIDAD EN LA PRÁCTICA
# ============================================================================
seccion("9. Rendimiento y constantes")

import timeit
t_tupla = timeit.timeit(stmt="(1,2,3,4,5)", number=1_000_000)
t_lista = timeit.timeit(stmt="[1,2,3,4,5]", number=1_000_000)
print(f"Crear 1M tuplas: {t_tupla:.3f}s")
print(f"Crear 1M listas: {t_lista:.3f}s  (la tupla suele ser más rápida)")

# Como no cambian, son ideales para CONSTANTES de configuración.
DIAS_SEMANA = ("Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom")
COLORES_RGB = {
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
}
print("Días:", DIAS_SEMANA)
print("RGB rojo:", COLORES_RGB["rojo"])


# ============================================================================
# 10. PATRONES REALES DE USO
# ============================================================================
seccion("10. Patrones reales")

# (a) Iterar índice + valor: enumerate() produce tuplas (i, valor).
for i, dia in enumerate(DIAS_SEMANA[:3], start=1):
    print(f"  Día {i}: {dia}")

# (b) Recorrer dos secuencias a la vez: zip() produce tuplas.
nombres = ("Ana", "Luis", "Eva")
edades = (30, 25, 41)
for nombre, edad in zip(nombres, edades):
    print(f"  {nombre} tiene {edad} años")

# (c) Ordenar por varias claves usando tuplas (orden lexicográfico).
personas = [("Ana", 30), ("Luis", 25), ("Ana", 22)]
# Ordena por nombre y, a igualdad, por edad:
print("Ordenado por (nombre, edad):", sorted(personas, key=lambda p: (p[0], p[1])))

# (d) Devolver coordenadas inmutables que nadie debe modificar por accidente.
def centro_pantalla(ancho: int, alto: int) -> tuple:
    return (ancho // 2, alto // 2)
print("Centro de 1920x1080:", centro_pantalla(1920, 1080))


seccion("FIN — ya conoces las tuplas al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
