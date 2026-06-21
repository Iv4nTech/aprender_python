# Introducción a los context managers en Python
#
# Un context manager garantiza que ciertos recursos se adquieren antes de un bloque
# de código y se liberan al salir, sin importar si ocurrió una excepción.
# Se usa con la sentencia `with`.

# ─────────────────────────────────────────────────────────────────────────────
# Ejemplo 1 — El problema que resuelven: apertura de archivos
#
# Sin context manager, si `file.read()` lanza una excepción, `file.close()`
# nunca se ejecuta y el archivo queda abierto.
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 50)
print("Ejemplo 1: Archivos — sin vs con context manager")
print("=" * 50)

# Sin context manager: hay que cerrar manualmente en el bloque finally
file = open('archivo.txt', 'r')
try:
    palabras = file.read().split()
    print(f"[sin CM] Total de palabras: {len(palabras)}")
finally:
    file.close()

# Con context manager: el cierre es automático al salir del bloque with
with open('archivo.txt', 'r') as file:
    palabras = file.read().split()
    print(f"[con CM] Total de palabras: {len(palabras)}")


# ─────────────────────────────────────────────────────────────────────────────
# Ejemplo 2 — Context manager propio con __enter__ / __exit__: temporizador
#
# Mide cuánto tarda en ejecutarse el bloque de código.
# __enter__ guarda el instante de inicio y lo devuelve al bloque `with`.
# __exit__ calcula el tiempo transcurrido al salir.
# ─────────────────────────────────────────────────────────────────────────────

import time

print("\n" + "=" * 50)
print("Ejemplo 2: Temporizador con __enter__ / __exit__")
print("=" * 50)


class Temporizador:
    def __enter__(self):
        self.inicio = time.perf_counter()
        return self                       # disponible como `t` en `with ... as t`

    def __exit__(self, exc_type, exc_value, traceback):
        self.duracion = time.perf_counter() - self.inicio
        print(f"Tiempo transcurrido: {self.duracion:.4f} s")
        return False                      # no suprime posibles excepciones


with Temporizador() as t:
    total = sum(x ** 2 for x in range(500_000))

print(f"Suma de cuadrados: {total}")


# ─────────────────────────────────────────────────────────────────────────────
# Ejemplo 3 — __exit__ con manejo de excepciones: transacción en memoria
#
# Simula una "transacción": si el bloque termina sin errores, los cambios
# se confirman; si lanza una excepción, se deshacen automáticamente (rollback).
# __exit__ recibe exc_type, exc_value y traceback cuando ocurre una excepción.
# Devolver True suprime la excepción; False la deja propagarse.
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Ejemplo 3: Transacción en memoria — rollback automático")
print("=" * 50)


class Transaccion:
    def __init__(self, datos: list):
        self.datos = datos

    def __enter__(self):
        self._copia = self.datos.copy()   # guarda el estado original
        return self.datos                 # el bloque trabaja directamente con la lista

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.datos.clear()
            self.datos.extend(self._copia)  # restaura el estado original
            print(f"Rollback aplicado — error: {exc_value}")
            return True                     # suprime la excepción
        print("Transacción confirmada")
        return False


inventario = ["manzana", "naranja", "platano"]
print(f"Inventario inicial: {inventario}")

# Transacción que falla a mitad: los cambios se deshacen
with Transaccion(inventario) as datos:
    datos.append("kiwi")
    datos.remove("naranja")
    raise ValueError("Stock insuficiente para completar el pedido")

print(f"Inventario tras rollback: {inventario}")

# Transacción exitosa: los cambios se mantienen
with Transaccion(inventario) as datos:
    datos.append("mango")
    datos.remove("platano")

print(f"Inventario tras confirmación: {inventario}")


# ─────────────────────────────────────────────────────────────────────────────
# Ejemplo 4 — contextlib.contextmanager: configuración temporal
#
# El decorador @contextmanager convierte un generador en context manager.
# El código antes del `yield` equivale a __enter__; después, a __exit__.
# Aquí se usa para cambiar temporalmente la precisión de los float al imprimir
# y restaurarla al salir del bloque, sin tocar el estado global de forma permanente.
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Ejemplo 4: contextlib — precisión decimal temporal")
print("=" * 50)

from contextlib import contextmanager

_precision_actual = {"decimales": 2}


def formatear(valor: float) -> str:
    return f"{valor:.{_precision_actual['decimales']}f}"


@contextmanager
def precision_temporal(decimales: int):
    anterior = _precision_actual["decimales"]
    _precision_actual["decimales"] = decimales
    try:
        yield                             # el bloque with se ejecuta aquí
    finally:
        _precision_actual["decimales"] = anterior   # siempre se restaura


pi = 3.141592653589793

print(f"Precisión normal:  {formatear(pi)}")

with precision_temporal(6):
    print(f"Dentro del bloque: {formatear(pi)}")

print(f"Tras salir:        {formatear(pi)}")


# ─────────────────────────────────────────────────────────────────────────────
# Ejemplo 5 — with anidados: transformar un archivo
#
# Abrir dos archivos al mismo tiempo es el caso de uso más natural para
# los with anidados. Python permite combinarlos en una sola línea con coma.
# Aquí se lee un archivo de frutas y se escribe uno nuevo con las palabras
# en mayúsculas y ordenadas alfabéticamente.
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("Ejemplo 5: with anidados — transformar archivo")
print("=" * 50)

with open('archivo.txt', 'r') as entrada:
    palabras = sorted(entrada.read().split())
    with open('resultado.txt', 'w') as salida:
        salida.write('\n'.join(p.upper() for p in palabras) + '\n')

with open('resultado.txt', 'r') as f:
    print("Contenido de resultado.txt:")
    print(f.read())
