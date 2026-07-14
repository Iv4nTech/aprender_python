"""
================================================================================
 EJERCICIOS RESUELTOS: ABC (ABSTRACT BASE CLASSES) EN PYTHON
 Casos reales — de fácil a experto
================================================================================

Este fichero está pensado para ejecutarse de principio a fin:

    python3 ejercicios_resueltos.py

Cada ejercicio imprime resultados reales para confirmar que funciona.
================================================================================
"""

from abc import ABC, abstractmethod
from collections.abc import MutableSequence
import json


def seccion(titulo: str) -> None:
    """Pequeño helper para imprimir cabeceras y que la salida sea legible."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# EJERCICIO 1 — FÁCIL — ABC básica de forma geométrica
# ============================================================================
seccion("EJERCICIO 1 — ABC básica de forma geométrica")

# SOLUCIÓN
class Forma(ABC):
    @abstractmethod
    def area(self):
        ...

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

try:
    Forma()
except TypeError as e:
    print("Forma() ->", type(e).__name__, "->", e)

print("Cuadrado(4).area():", Cuadrado(4).area())


# ============================================================================
# EJERCICIO 2 — FÁCIL — Verificar contrato con isinstance
# ============================================================================
seccion("EJERCICIO 2 — Verificar contrato con isinstance")

# SOLUCIÓN
class Serializable(ABC):
    @abstractmethod
    def serializar(self):
        ...

class JSONSerializer(Serializable):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def serializar(self):
        return json.dumps(self.__dict__)

obj = JSONSerializer(nombre="Ana", edad=30)
print("isinstance(obj, Serializable):", isinstance(obj, Serializable))
print("obj.serializar():", obj.serializar())


# ============================================================================
# EJERCICIO 3 — FÁCIL — Propiedad abstracta
# ============================================================================
seccion("EJERCICIO 3 — Propiedad abstracta")

# SOLUCIÓN
class Descuento(ABC):
    @property
    @abstractmethod
    def porcentaje(self):
        ...

class DescuentoVIP(Descuento):
    @property
    def porcentaje(self):
        return 20

class DescuentoEstandar(Descuento):
    @property
    def porcentaje(self):
        return 5

print("DescuentoVIP().porcentaje:", DescuentoVIP().porcentaje)
print("DescuentoEstandar().porcentaje:", DescuentoEstandar().porcentaje)


# ============================================================================
# EJERCICIO 4 — MEDIO — Patrón Template Method
# ============================================================================
seccion("EJERCICIO 4 — Patrón Template Method")

# SOLUCIÓN
class Reporte(ABC):
    def generar(self):
        return f"{self.cabecera()}\n{self.cuerpo()}\n{self.pie()}"

    @abstractmethod
    def cabecera(self):
        ...

    @abstractmethod
    def cuerpo(self):
        ...

    @abstractmethod
    def pie(self):
        ...

class ReporteVentas(Reporte):
    def cabecera(self):
        return "=== REPORTE DE VENTAS ==="

    def cuerpo(self):
        return "Ventas del mes: $10,000"

    def pie(self):
        return "Fin del reporte de ventas."

class ReporteInventario(Reporte):
    def cabecera(self):
        return "=== REPORTE DE INVENTARIO ==="

    def cuerpo(self):
        return "Productos en stock: 150"

    def pie(self):
        return "Fin del reporte de inventario."

print(ReporteVentas().generar())
print()
print(ReporteInventario().generar())


# ============================================================================
# EJERCICIO 5 — MEDIO — ABC con múltiples métodos abstractos
# ============================================================================
seccion("EJERCICIO 5 — ABC con múltiples métodos abstractos")

# SOLUCIÓN
class BaseDeDatos(ABC):
    @abstractmethod
    def conectar(self):
        ...

    @abstractmethod
    def desconectar(self):
        ...

    @abstractmethod
    def ejecutar_query(self, query):
        ...

class PostgreSQLDB(BaseDeDatos):
    def conectar(self):
        print("Conectando a PostgreSQL...")

    def desconectar(self):
        print("Desconectando de PostgreSQL...")

    def ejecutar_query(self, query):
        print(f"Ejecutando query en PostgreSQL: {query}")

class SQLiteDB(BaseDeDatos):
    def conectar(self):
        print("Conectando a SQLite...")

    def desconectar(self):
        print("Desconectando de SQLite...")

    def ejecutar_query(self, query):
        print(f"Ejecutando query en SQLite: {query}")

class OracleDB(BaseDeDatos):
    def conectar(self):
        print("Conectando a Oracle...")

    def desconectar(self):
        print("Desconectando de Oracle...")
    # falta ejecutar_query a propósito

pg = PostgreSQLDB()
pg.conectar()
pg.ejecutar_query("SELECT * FROM usuarios")
pg.desconectar()

lite = SQLiteDB()
lite.conectar()
lite.ejecutar_query("SELECT * FROM productos")
lite.desconectar()

try:
    OracleDB()
except TypeError as e:
    print("OracleDB() ->", type(e).__name__, "->", e)


# ============================================================================
# EJERCICIO 6 — MEDIO — register() para clases externas
# ============================================================================
seccion("EJERCICIO 6 — register() para clases externas")

class Exportable(ABC):
    @abstractmethod
    def exportar(self):
        ...

# Clase externa: no la puedes modificar, imagina que viene de una librería.
class PDFExporter:
    def exportar(self):
        return "documento.pdf generado"

# SOLUCIÓN
Exportable.register(PDFExporter)

print("isinstance(PDFExporter(), Exportable):", isinstance(PDFExporter(), Exportable))
print("issubclass(PDFExporter, Exportable):", issubclass(PDFExporter, Exportable))


# ============================================================================
# EJERCICIO 7 — AVANZADO — ABCs de collections.abc
# ============================================================================
seccion("EJERCICIO 7 — ABCs de collections.abc")

# SOLUCIÓN
class Pila(MutableSequence):
    def __init__(self):
        self._items = []

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]

    def __len__(self):
        return len(self._items)

    def insert(self, index, value):
        self._items.insert(index, value)

pila = Pila()
pila.append(1)
pila.append(2)
pila.insert(0, 0)
print("list(pila):", list(pila))
print("isinstance(pila, MutableSequence):", isinstance(pila, MutableSequence))


# ============================================================================
# EJERCICIO 8 — AVANZADO — Herencia múltiple de ABCs
# ============================================================================
seccion("EJERCICIO 8 — Herencia múltiple de ABCs")

# SOLUCIÓN
class Imprimible(ABC):
    @abstractmethod
    def imprimir(self):
        ...

class Exportable2(ABC):
    @abstractmethod
    def exportar(self):
        ...

class Documento(Imprimible, Exportable2):
    def __init__(self, contenido):
        self._contenido = contenido

    def imprimir(self):
        print(f"Imprimiendo: {self._contenido}")

    def exportar(self):
        return f"Exportando: {self._contenido}"

doc = Documento("Contenido del documento")
doc.imprimir()
print("exportar():", doc.exportar())
print("isinstance(doc, Imprimible):", isinstance(doc, Imprimible), "| isinstance(doc, Exportable2):", isinstance(doc, Exportable2))


# ============================================================================
# EJERCICIO 9 — AVANZADO — ABC como validador de contratos en runtime
# ============================================================================
seccion("EJERCICIO 9 — ABC como validador de contratos en runtime")

# SOLUCIÓN
class ProcesadorPago(ABC):
    @abstractmethod
    def autorizar(self, importe):
        ...

    @abstractmethod
    def reembolsar(self, importe):
        ...

class TarjetaCredito(ProcesadorPago):
    def __init__(self):
        self._limite = 1000

    def autorizar(self, importe):
        if importe <= self._limite:
            self._limite -= importe
            return True
        return False

    def reembolsar(self, importe):
        self._limite += importe

def procesar_pago(procesador, importe):
    if not isinstance(procesador, ProcesadorPago):
        raise TypeError("El procesador no implementa el contrato de ProcesadorPago")
    return procesador.autorizar(importe)

print("procesar_pago(TarjetaCredito(), 100):", procesar_pago(TarjetaCredito(), 100))

try:
    procesar_pago({"tipo": "falso"}, 100)
except TypeError as e:
    print("procesar_pago(dict, 100) ->", type(e).__name__, "->", e)


# ============================================================================
# EJERCICIO 10 — EXPERTO — Sistema de plugins con ABCs
# ============================================================================
seccion("EJERCICIO 10 — Sistema de plugins con ABCs")

# SOLUCIÓN
class Plugin(ABC):
    @property
    @abstractmethod
    def nombre(self):
        ...

    @property
    @abstractmethod
    def version(self):
        ...

    @abstractmethod
    def ejecutar(self, datos):
        ...

    def info(self):
        print(f"{self.nombre} v{self.version}")

class PluginCSV(Plugin):
    def __init__(self):
        self._nombre = "PluginCSV"
        self._version = "1.0"

    @property
    def nombre(self):
        return self._nombre

    @property
    def version(self):
        return self._version

    def ejecutar(self, datos):
        print(f"Ejecutando PluginCSV con datos: {datos}")

class PluginJSON(Plugin):
    def __init__(self):
        self._nombre = "PluginJSON"
        self._version = "1.0"

    @property
    def nombre(self):
        return self._nombre

    @property
    def version(self):
        return self._version

    def ejecutar(self, datos):
        print(f"Ejecutando PluginJSON con datos: {datos}")

class PluginManager:
    def __init__(self):
        self._plugins = []

    def registrar(self, plugin):
        if not isinstance(plugin, Plugin):
            raise TypeError("El plugin no implementa el contrato de Plugin")
        self._plugins.append(plugin)

    def ejecutar_todos(self, datos):
        for plugin in self._plugins:
            plugin.info()
            plugin.ejecutar(datos)

manager = PluginManager()
manager.registrar(PluginCSV())
manager.registrar(PluginJSON())
manager.ejecutar_todos({"valor": 42})

try:
    manager.registrar(object())
except TypeError as e:
    print("manager.registrar(object()) ->", type(e).__name__, "->", e)


seccion("FIN — todos los ejercicios resueltos")
