"""
================================================================================
 TYPE HINTS / ANOTACIONES DE TIPO EN PYTHON
 Ejecutar: python3 introduccion.py
================================================================================
"""

from typing import (
    Callable,
    Final,
    Literal,
    Protocol,
    Sequence,
    TypedDict,
    overload,
    runtime_checkable,
)
import annotationlib


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA SIN TIPOS — POR QUÉ IMPORTAN
# ============================================================================
seccion("1. El problema sin tipos: por qué importan")


def calcular_descuento_sin_tipos(precio, porcentaje):
    return precio - (precio * porcentaje / 100)


# Nada impide llamar a esto con basura: el error explota en PRODUCCIÓN,
# no al escribir el código.
try:
    calcular_descuento_sin_tipos("9.99", 10)
except TypeError as e:
    print(f"  Sin tipos, el bug aparece en tiempo de ejecución -> {e}")


def calcular_descuento(precio: float, porcentaje: float) -> float:
    return precio - (precio * porcentaje / 100)


# Con tipos, un type checker (mypy, pyright) marca esta llamada como error
# ANTES de ejecutar nada, aunque Python en sí no impida ejecutarla:
# calcular_descuento("9.99", 10)  # el checker dice: Argument 1 to
#                                 # "calcular_descuento" has incompatible type "str"
print(f"  calcular_descuento(9.99, 10) -> {calcular_descuento(9.99, 10)}")
print("  Los type hints son un CONTRATO que revisa una herramienta externa,")
print("  no decoración: Python los ignora en tiempo de ejecución.")


# ============================================================================
# 2. SINTAXIS BASE — VARIABLES, FUNCIONES Y RETORNOS
# ============================================================================
seccion("2. Sintaxis base: variables, funciones y retornos")

nombre: str = "Iván"
precio: float = 9.99
activo: bool = True

print(f"  Variable anotada: nombre: str = {nombre!r}")


def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"


def registrar_log(mensaje: str) -> None:
    # -> None dice explícitamente: esta función no devuelve nada útil.
    print(f"  [LOG] {mensaje}")


print(f"  {saludar('Marta')}")
registrar_log("evento registrado")


class Pedido:
    # Desde Python 3.14 (PEP 649), las anotaciones se evalúan de forma
    # diferida: ya no hace falta 'from __future__ import annotations'
    # para referenciar una clase que todavía no ha terminado de definirse.
    def clonar(self) -> "Pedido":
        return Pedido()

    def clonar_moderno(self) -> Pedido:  # funciona directo en 3.14, sin comillas
        return Pedido()


print("  En 3.14 ya no hace falta 'MiClase' entre comillas para forward refs.")


# ============================================================================
# 3. TIPOS COMPUESTOS — LISTAS, DICCIONARIOS, TUPLAS
# ============================================================================
seccion("3. Tipos compuestos: listas, diccionarios, tuplas")

nombres: list[str] = ["Ana", "Luis", "Marta"]
stock: dict[str, int] = {"teclado": 12, "raton": 30}
coordenada: tuple[int, str, float] = (1, "Madrid", 40.4)
etiquetas: set[str] = {"oferta", "nuevo"}
prohibidas: frozenset[int] = frozenset({403, 404, 500})

print(f"  list[str]:       {nombres}")
print(f"  dict[str, int]:  {stock}")
print(f"  tuple fija:      {coordenada}")
print(f"  set[str]:        {etiquetas}")
print(f"  frozenset[int]:  {prohibidas}")


def total_carrito(carrito: list[dict[str, float]]) -> float:
    return sum(item["precio"] * item["cantidad"] for item in carrito)


carrito: list[dict[str, float]] = [
    {"precio": 9.99, "cantidad": 2},
    {"precio": 19.50, "cantidad": 1},
]
# Si alguien pasa {"precio": "9.99", ...} el checker lo detecta antes de
# que el * falle o, peor, concatene strings en vez de sumar precios.
print(f"  Total carrito (list[dict[str, float]]): {total_carrito(carrito):.2f}")


# ============================================================================
# 4. UNION TYPES Y OPTIONAL — VALORES QUE PUEDEN SER None
# ============================================================================
seccion("4. Union types y Optional: valores que pueden ser None")


def normalizar_id(valor: int | str) -> str:
    return str(valor).strip()


print(f"  int | str: normalizar_id(42) -> {normalizar_id(42)!r}")
print(f"  int | str: normalizar_id(' 7 ') -> {normalizar_id(' 7 ')!r}")

usuarios_bd: dict[int, dict[str, str]] = {
    1: {"nombre": "Ana", "email": "ana@empresa.com"},
}


def buscar_usuario(id_usuario: int) -> dict[str, str] | None:
    # Si el checker no ve el "| None" aquí, el código que llama a esto
    # puede olvidarse de comprobar None y reventar con AttributeError
    # el día que un id no exista.
    return usuarios_bd.get(id_usuario)


usuario = buscar_usuario(1)
if usuario is not None:
    print(f"  buscar_usuario(1) -> {usuario}")

inexistente = buscar_usuario(999)
print(f"  buscar_usuario(999) -> {inexistente} (int | None, en vez de Optional[int])")


# ============================================================================
# 5. CALLABLE, SEQUENCE Y TIPOS DE COLECCIONES ABC
# ============================================================================
seccion("5. Callable, Sequence y tipos de colecciones ABC")


def con_autenticacion(peticion: dict[str, str]) -> bool:
    return "token" in peticion


def con_logging(peticion: dict[str, str]) -> bool:
    print(f"  [MIDDLEWARE] petición: {peticion.get('ruta', '?')}")
    return True


def ejecutar_middlewares(
    peticion: dict[str, str],
    middlewares: list[Callable[[dict[str, str]], bool]],
) -> bool:
    # Si un middleware no es Callable[[dict], bool] (p. ej. devuelve None),
    # el checker lo detecta antes de que "if not resultado" falle en runtime.
    return all(middleware(peticion) for middleware in middlewares)


peticion = {"ruta": "/checkout", "token": "abc123"}
resultado = ejecutar_middlewares(peticion, [con_logging, con_autenticacion])
print(f"  ejecutar_middlewares(...) -> {resultado}")


def mostrar_primeros(elementos: Sequence[str], n: int) -> list[str]:
    # Sequence acepta tanto list como tuple indistintamente, sin
    # comprometerse a un tipo concreto que el llamante no necesita.
    return list(elementos[:n])


print(f"  Sequence[str] con lista: {mostrar_primeros(['a', 'b', 'c'], 2)}")
print(f"  Sequence[str] con tupla: {mostrar_primeros(('x', 'y', 'z'), 2)}")


# ============================================================================
# 6. LITERAL Y FINAL — VALORES EXACTOS Y CONSTANTES
# ============================================================================
seccion("6. Literal y Final: valores exactos y constantes")

MetodoHTTP = Literal["GET", "POST", "PUT", "DELETE"]


def enviar_peticion(url: str, metodo: MetodoHTTP) -> str:
    # Si alguien pasa metodo="PATCH", el checker lo rechaza en el sitio
    # de la llamada; sin Literal, "PATCH" es un str válido como otro cualquiera.
    return f"{metodo} {url}"


print(f"  Literal restringido: {enviar_peticion('/api/pedidos', 'POST')}")

VERSION_API: Final[str] = "v2"
# VERSION_API = "v3"  # el checker marca esto como error: Final no se reasigna
print(f"  Final[str]: VERSION_API = {VERSION_API!r} (no reasignable según el checker)")


# ============================================================================
# 7. TYPEDDICT — DICCIONARIOS CON ESTRUCTURA GARANTIZADA
# ============================================================================
seccion("7. TypedDict: diccionarios con estructura garantizada")


class RespuestaAPI(TypedDict):
    status: int
    datos: list[str]


class ConfiguracionBD(TypedDict, total=False):
    # total=False: todos los campos son opcionales (ninguno obligatorio).
    timeout: int
    reintentos: int


def procesar_respuesta(respuesta: RespuestaAPI) -> str:
    # Si a esta función le llega un dict al que le falta "datos", el
    # checker lo marca en la llamada, no cuando accedas a respuesta["datos"].
    return f"status={respuesta['status']} datos={len(respuesta['datos'])}"


respuesta: RespuestaAPI = {"status": 200, "datos": ["a", "b", "c"]}
print(f"  TypedDict obligatorio: {procesar_respuesta(respuesta)}")

config: ConfiguracionBD = {"timeout": 30}
print(f"  TypedDict con total=False: {config}")


# ============================================================================
# 8. PROTOCOL — DUCK TYPING CON CONTRATO EXPLÍCITO
# ============================================================================
seccion("8. Protocol: duck typing con contrato explícito")


@runtime_checkable
class Exportador(Protocol):
    def exportar(self, ruta: str) -> bool: ...


class ExportadorCSV:
    # No hereda de Exportador. Cumple el Protocol solo por tener el método.
    def exportar(self, ruta: str) -> bool:
        print(f"  [CSV] escrito en {ruta}")
        return True


class ExportadorJSON:
    def exportar(self, ruta: str) -> bool:
        print(f"  [JSON] escrito en {ruta}")
        return True


def guardar_reporte(exportador: Exportador, ruta: str) -> bool:
    return exportador.exportar(ruta)


guardar_reporte(ExportadorCSV(), "reporte.csv")
guardar_reporte(ExportadorJSON(), "reporte.json")
# @runtime_checkable permite isinstance() sin que las clases hereden de nada.
print(f"  isinstance(ExportadorCSV(), Exportador) -> {isinstance(ExportadorCSV(), Exportador)}")


# ============================================================================
# 9. GENÉRICOS — PEP 695, SINTAXIS MODERNA (PYTHON 3.12+)
# ============================================================================
seccion("9. Genéricos: PEP 695, sintaxis moderna (Python 3.12+)")


def primero[T](lista: list[T]) -> T:
    # Ya no hace falta "from typing import TypeVar" ni declarar T aparte.
    return lista[0]


print(f"  primero([1, 2, 3]) -> {primero([1, 2, 3])}")
print(f"  primero(['a', 'b']) -> {primero(['a', 'b'])}")


class Pila[T]:
    def __init__(self) -> None:
        self._elementos: list[T] = []

    def push(self, valor: T) -> None:
        self._elementos.append(valor)

    def pop(self) -> T:
        return self._elementos.pop()


pila_enteros = Pila[int]()
pila_enteros.push(1)
pila_enteros.push(2)
print(f"  Pila[int]: pop() -> {pila_enteros.pop()}")

type FilaDeID = list[int]

ids_pedido: FilaDeID = [101, 102, 103]
print(f"  type FilaDeID = list[int]: {ids_pedido}")


class Cache[K, V]:
    def __init__(self) -> None:
        self._datos: dict[K, V] = {}

    def set(self, clave: K, valor: V) -> None:
        self._datos[clave] = valor

    def get(self, clave: K) -> V | None:
        return self._datos.get(clave)


cache_precios: Cache[str, float] = Cache()
cache_precios.set("teclado", 49.99)
print(f"  Cache[str, float].get('teclado') -> {cache_precios.get('teclado')}")


# ============================================================================
# 10. ANOTACIONES DIFERIDAS — PYTHON 3.14 (PEP 649)
# ============================================================================
seccion("10. Anotaciones diferidas: Python 3.14 (PEP 649)")


class Nodo:
    # Antes de 3.14, referenciar Nodo dentro de su propia definición exigía
    # "Nodo" entre comillas, porque la clase aún no existía cuando Python
    # evaluaba la anotación al definir el método.
    def siguiente(self) -> Nodo | None:
        return self._siguiente

    def __init__(self, valor: int) -> None:
        self.valor = valor
        self._siguiente: Nodo | None = None


n1 = Nodo(1)
print(f"  Forward reference directa (sin comillas) funciona: Nodo.siguiente -> {n1.siguiente()}")


def con_anotaciones(a: int, b: str) -> bool:
    return True


anotaciones_valor = annotationlib.get_annotations(con_anotaciones, format=annotationlib.Format.VALUE)
anotaciones_string = annotationlib.get_annotations(con_anotaciones, format=annotationlib.Format.STRING)
anotaciones_forwardref = annotationlib.get_annotations(con_anotaciones, format=annotationlib.Format.FORWARDREF)

print(f"  Format.VALUE:      {anotaciones_valor}")
print(f"  Format.STRING:     {anotaciones_string}")
print(f"  Format.FORWARDREF: {anotaciones_forwardref}")
print("  Las anotaciones ya no se ejecutan al importar el módulo: se evalúan")
print("  de forma diferida, solo cuando algo las pide (get_annotations, etc).")


# ============================================================================
# 11. OVERLOAD — MÚLTIPLES FIRMAS PARA UNA FUNCIÓN
# ============================================================================
seccion("11. Overload: múltiples firmas para una función")


@overload
def parsear(dato: Literal["entero"]) -> int: ...
@overload
def parsear(dato: Literal["decimal"]) -> float: ...
def parsear(dato: str) -> int | float:
    # Las firmas @overload solo existen para el checker; en runtime solo
    # se ejecuta esta última implementación, sin decorador.
    if dato == "entero":
        return 42
    return 4.20


print(f"  parsear('entero') -> {parsear('entero')} ({type(parsear('entero')).__name__})")
print(f"  parsear('decimal') -> {parsear('decimal')} ({type(parsear('decimal')).__name__})")
print("  El checker sabe que parsear('entero') siempre da int, sin necesitar")
print("  isinstance() después de la llamada.")


seccion("FIN — ya conoces type hints al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
