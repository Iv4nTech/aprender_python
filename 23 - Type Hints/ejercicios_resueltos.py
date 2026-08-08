"""
================================================================================
 EJERCICIOS RESUELTOS: TYPE HINTS / ANOTACIONES DE TIPO EN PYTHON
 Ejecutar: python3 ejercicios_resueltos.py
================================================================================
"""

from typing import Callable, Literal, Protocol, TypedDict, TypeGuard, overload


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ──────────────────────────────────────────────
# EJERCICIO 1 — FÁCIL
# Tipar una función de saludo
# ──────────────────────────────────────────────
# El equipo de backend quiere que todas las funciones públicas tengan
# type hints antes de mergear a producción. Empieza por esta.
seccion("EJERCICIO 1 — FÁCIL — Tipar una función de saludo")

# SOLUCIÓN
def saludar(nombre: str, veces: int) -> str:
    return f"Hola, {nombre}! " * veces

# Resultado esperado: 'Hola, Ana! Hola, Ana! Hola, Ana! '
print(saludar("Ana", 3))


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Función con retorno None
# ──────────────────────────────────────────────
# Un sistema de logging registra eventos pero no devuelve nada.
# Tiparlo con -> None dice explícitamente que no hay valor de retorno útil.
seccion("EJERCICIO 2 — FÁCIL — Función con retorno None")

# SOLUCIÓN
def registrar_evento(evento: str, nivel: str) -> None:
    print(f"  [{nivel.upper()}] {evento}")

# Resultado esperado: [ERROR] fallo de conexión
registrar_evento("fallo de conexión", "error")


# ──────────────────────────────────────────────
# EJERCICIO 3 — MEDIO
# Lista de precios con descuento
# ──────────────────────────────────────────────
# La tienda online aplica un descuento global a una lista de precios
# antes de mostrar la campaña de Black Friday.
seccion("EJERCICIO 3 — MEDIO — Lista de precios con descuento")

# SOLUCIÓN
def aplicar_descuento(precios: list[float], descuento: float) -> list[float]:
    return [round(precio * (1 - descuento / 100), 2) for precio in precios]

# Resultado esperado: [80.0, 200.0, 60.0]
print(aplicar_descuento([100.0, 250.0, 75.0], 20))


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Búsqueda nullable
# ──────────────────────────────────────────────
# Una API de usuarios puede no encontrar el id solicitado. El tipo de
# retorno debe reflejar que puede devolver None, para que el checker
# obligue a comprobarlo antes de usar el resultado.
seccion("EJERCICIO 4 — MEDIO — Búsqueda nullable")

usuarios_bd = {
    1: {"nombre": "Ana", "rol": "admin"},
    2: {"nombre": "Luis", "rol": "editor"},
}

# SOLUCIÓN
def buscar_usuario(id_usuario: int) -> dict[str, str] | None:
    return usuarios_bd.get(id_usuario)

# Resultado esperado: {'nombre': 'Ana', 'rol': 'admin'}
print(buscar_usuario(1))
# Resultado esperado: None
print(buscar_usuario(999))


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Literal para estados
# ──────────────────────────────────────────────
# Un pedido solo puede pasar por estados concretos del flujo logístico.
# Cualquier otro string debería marcarse como error por el type checker.
seccion("EJERCICIO 5 — MEDIO — Literal para estados")

# SOLUCIÓN
def cambiar_estado(pedido_id: int, estado: Literal["pendiente", "enviado", "entregado"]) -> bool:
    print(f"  Pedido {pedido_id} -> {estado}")
    return True

# Resultado esperado: Pedido 42 -> enviado / True
print(cambiar_estado(42, "enviado"))


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# TypedDict para configuración
# ──────────────────────────────────────────────
# La conexión a base de datos se configura con un diccionario cuya forma
# debe estar garantizada: olvidar un campo debe fallar en el checker.
seccion("EJERCICIO 6 — MEDIO — TypedDict para configuración")

# SOLUCIÓN
class ConfigBD(TypedDict):
    host: str
    puerto: int
    nombre_db: str
    usuario: str

def conectar(config: ConfigBD) -> str:
    return f"Conectando a {config['host']}:{config['puerto']}/{config['nombre_db']}"

config: ConfigBD = {
    "host": "localhost",
    "puerto": 5432,
    "nombre_db": "produccion",
    "usuario": "admin",
}

# Resultado esperado: 'Conectando a localhost:5432/produccion'
print(conectar(config))


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# Callable como argumento
# ──────────────────────────────────────────────
# Un pipeline de datos aplica una lista de transformaciones a cada
# número, en orden. Cada transformación es una función int -> int.
seccion("EJERCICIO 7 — AVANZADO — Callable como argumento")

# SOLUCIÓN
def ejecutar_pipeline(datos: list[int], transformaciones: list[Callable[[int], int]]) -> list[int]:
    resultado = datos
    for transformacion in transformaciones:
        resultado = [transformacion(x) for x in resultado]
    return resultado

# Resultado esperado: [22, 42, 62]
print(ejecutar_pipeline([10, 20, 30], [lambda x: x + 1, lambda x: x * 2]))


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Protocol para exportadores
# ──────────────────────────────────────────────
# El sistema de reportes acepta cualquier exportador (CSV, Excel...) que
# implemente exportar(), sin obligarlos a heredar de una clase base.
seccion("EJERCICIO 8 — AVANZADO — Protocol para exportadores")

# SOLUCIÓN
class Exportable(Protocol):
    def exportar(self, ruta: str) -> bool: ...

class ExportadorCSV:
    def exportar(self, ruta: str) -> bool:
        print(f"  [CSV] escrito en {ruta}")
        return True

class ExportadorExcel:
    def exportar(self, ruta: str) -> bool:
        print(f"  [EXCEL] escrito en {ruta}")
        return True

def guardar(exportador: Exportable, ruta: str) -> bool:
    return exportador.exportar(ruta)

# Resultado esperado: True para ambas llamadas
print(guardar(ExportadorCSV(), "datos.csv"))
print(guardar(ExportadorExcel(), "datos.xlsx"))


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# Genérico con PEP 695
# ──────────────────────────────────────────────
# Necesitas un tipo Resultado que represente éxito o error sin usar
# excepciones, típico patrón "Result type" en APIs internas.
seccion("EJERCICIO 9 — AVANZADO — Genérico con PEP 695")

# SOLUCIÓN
class Resultado[T, E]:
    def __init__(self, valor: T | None = None, error: E | None = None) -> None:
        self.valor = valor
        self.error = error

    def es_exito(self) -> bool:
        return self.error is None

ok = Resultado(valor=10)
fallo = Resultado(error="no encontrado")

# Resultado esperado: primero éxito con valor 10, luego error con "no encontrado"
print(ok.es_exito(), ok.valor)
print(fallo.es_exito(), fallo.error)


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Overload + TypeGuard
# ──────────────────────────────────────────────
# Un parser recibe strings de un formulario y debe devolver int si el
# string son solo dígitos, float si tiene un punto decimal, o None si
# no es parseable. Añade además un TypeGuard para saber si el resultado
# es numérico antes de operar con él.
seccion("EJERCICIO 10 — EXPERTO — Overload + TypeGuard")

# SOLUCIÓN
@overload
def parsear_valor(dato: str) -> int | float | None: ...
def parsear_valor(dato):
    if dato.lstrip("-").isdigit():
        return int(dato)
    try:
        return float(dato)
    except ValueError:
        return None

def es_numerico(valor: int | float | None) -> TypeGuard[int | float]:
    return valor is not None

# Resultado esperado: 123 (int), 1.5 (float), None
print(parsear_valor("123"))
print(parsear_valor("1.5"))
print(parsear_valor("abc"))
print(f"es_numerico(parsear_valor('123')) -> {es_numerico(parsear_valor('123'))}")
print(f"es_numerico(parsear_valor('abc')) -> {es_numerico(parsear_valor('abc'))}")
