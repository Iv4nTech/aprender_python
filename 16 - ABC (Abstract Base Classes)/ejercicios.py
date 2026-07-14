"""
================================================================================
 EJERCICIOS: ABC (ABSTRACT BASE CLASSES) EN PYTHON
 Casos reales — de fácil a experto
================================================================================

Este fichero está pensado para ejecutarse de principio a fin:

    python3 ejercicios.py

Completa cada ejercicio donde encuentres "..." y descomenta los print()
para comprobar el resultado.
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

# Estás modelando figuras geométricas para una app de dibujo. Necesitas
# que TODAS las figuras garanticen tener un método area(), sin excepción.

# Crea la ABC Forma con un método abstracto area().
class Forma(ABC):
    ...

# Implementa Cuadrado(lado) que calcule area() = lado ** 2
class Cuadrado(Forma):
    ...

# Verifica que Forma no se puede instanciar directamente
# try:
#     Forma()
# except TypeError as e:
#     print(e)

# Verifica que Cuadrado(4) sí se puede instanciar y area() devuelve 16
# print(Cuadrado(4).area())


# ============================================================================
# EJERCICIO 2 — FÁCIL — Verificar contrato con isinstance
# ============================================================================
seccion("EJERCICIO 2 — Verificar contrato con isinstance")

# Tu aplicación necesita garantizar que cualquier objeto "serializable"
# tenga un método serializar() antes de guardarlo en disco.

# Crea la ABC Serializable con el método abstracto serializar().
class Serializable(ABC):
    ...

# Implementa JSONSerializer que herede de Serializable, guarde datos en
# self.__dict__ mediante __init__(**kwargs) y serialice con json.dumps
class JSONSerializer(Serializable):
    ...

# Verifica con isinstance que una instancia es Serializable
# obj = JSONSerializer(nombre="Ana", edad=30)
# print(isinstance(obj, Serializable))
# print(obj.serializar())

# Resultado esperado: True y '{"nombre": "Ana", "edad": 30}'


# ============================================================================
# EJERCICIO 3 — FÁCIL — Propiedad abstracta
# ============================================================================
seccion("EJERCICIO 3 — Propiedad abstracta")

# El sistema de precios de una tienda aplica distintos descuentos según
# el tipo de cliente. El porcentaje debe leerse como una PROPIEDAD.

# Crea la ABC Descuento con la propiedad abstracta porcentaje.
class Descuento(ABC):
    ...

# Implementa DescuentoVIP (20%) y DescuentoEstandar (5%)
class DescuentoVIP(Descuento):
    ...

class DescuentoEstandar(Descuento):
    ...

# El acceso debe ser SIN paréntesis: obj.porcentaje (no obj.porcentaje())
# print(DescuentoVIP().porcentaje)
# print(DescuentoEstandar().porcentaje)

# Resultado esperado: 20 y 5


# ============================================================================
# EJERCICIO 4 — MEDIO — Patrón Template Method
# ============================================================================
seccion("EJERCICIO 4 — Patrón Template Method")

# El departamento de informes necesita que TODOS los reportes se generen
# siguiendo el mismo esqueleto: cabecera, cuerpo y pie, en ese orden.

# Crea la ABC Reporte con:
#  - un método CONCRETO generar() que llama en orden a cabecera(), cuerpo() y pie()
#    y devuelve la concatenación de las tres partes con saltos de línea
#  - tres métodos ABSTRACTOS: cabecera(), cuerpo(), pie()
class Reporte(ABC):
    ...

# Implementa ReporteVentas y ReporteInventario con su propio contenido
class ReporteVentas(Reporte):
    ...

class ReporteInventario(Reporte):
    ...

# print(ReporteVentas().generar())
# print(ReporteInventario().generar())


# ============================================================================
# EJERCICIO 5 — MEDIO — ABC con múltiples métodos abstractos
# ============================================================================
seccion("EJERCICIO 5 — ABC con múltiples métodos abstractos")

# Tu backend soporta varios motores de base de datos. Todos deben exponer
# la misma interfaz: conectar, desconectar y ejecutar consultas.

# Crea la ABC BaseDeDatos con: conectar(), desconectar(), ejecutar_query(query)
class BaseDeDatos(ABC):
    ...

# Implementa PostgreSQLDB y SQLiteDB (simula cada acción con un print)
class PostgreSQLDB(BaseDeDatos):
    ...

class SQLiteDB(BaseDeDatos):
    ...

# Crea OracleDB SIN implementar ejecutar_query y comprueba que falla
class OracleDB(BaseDeDatos):
    ...

# try:
#     OracleDB()
# except TypeError as e:
#     print(e)


# ============================================================================
# EJERCICIO 6 — MEDIO — register() para clases externas
# ============================================================================
seccion("EJERCICIO 6 — register() para clases externas")

# Usas una librería de terceros con la clase PDFExporter. No puedes tocar
# su código (no hereda de nada), pero ya implementa un método exportar().
# Necesitas que tu sistema la reconozca como Exportable.

class Exportable(ABC):
    @abstractmethod
    def exportar(self):
        ...

# Clase externa: no la puedes modificar, imagina que viene de una librería.
class PDFExporter:
    def exportar(self):
        return "documento.pdf generado"

# Usa Exportable.register(...) para reconocer PDFExporter como Exportable
...

# print(isinstance(PDFExporter(), Exportable))
# print(issubclass(PDFExporter, Exportable))

# Resultado esperado: True y True


# ============================================================================
# EJERCICIO 7 — AVANZADO — ABCs de collections.abc
# ============================================================================
seccion("EJERCICIO 7 — ABCs de collections.abc")

# Necesitas una pila (stack) que se comporte como una secuencia mutable
# completa de Python: indexable, iterable, con append, insert, etc.

# Crea Pila(MutableSequence) implementando los métodos abstractos que
# exige MutableSequence: __getitem__, __setitem__, __delitem__, __len__, insert
class Pila(MutableSequence):
    ...

# pila = Pila()
# pila.append(1)
# pila.append(2)
# pila.insert(0, 0)
# print(list(pila))
# print(isinstance(pila, MutableSequence))

# Resultado esperado: [0, 1, 2] y True


# ============================================================================
# EJERCICIO 8 — AVANZADO — Herencia múltiple de ABCs
# ============================================================================
seccion("EJERCICIO 8 — Herencia múltiple de ABCs")

# Un documento de tu aplicación debe poder imprimirse Y exportarse.
# Cada capacidad es un contrato independiente.

# Crea Imprimible(ABC) con el método abstracto imprimir()
class Imprimible(ABC):
    ...

# Crea Exportable2(ABC) con el método abstracto exportar()
class Exportable2(ABC):
    ...

# Crea Documento que herede de AMBAS e implemente los dos métodos
class Documento(Imprimible, Exportable2):
    ...

# doc = Documento()
# print(isinstance(doc, Imprimible), isinstance(doc, Exportable2))

# Resultado esperado: True True


# ============================================================================
# EJERCICIO 9 — AVANZADO — ABC como validador de contratos en runtime
# ============================================================================
seccion("EJERCICIO 9 — ABC como validador de contratos en runtime")

# La pasarela de pagos debe rechazar en el acto cualquier objeto que no
# implemente correctamente el contrato de procesador de pago.

# Crea la ABC ProcesadorPago con: autorizar(importe) y reembolsar(importe)
class ProcesadorPago(ABC):
    ...

# Implementa TarjetaCredito que cumpla el contrato
class TarjetaCredito(ProcesadorPago):
    ...

# Implementa procesar_pago(procesador) que verifique con isinstance que
# procesador es un ProcesadorPago; si no lo es, lanza TypeError con mensaje claro
def procesar_pago(procesador, importe):
    ...

# procesar_pago(TarjetaCredito(), 100)      # debe funcionar
# procesar_pago({"tipo": "falso"}, 100)     # debe lanzar TypeError


# ============================================================================
# EJERCICIO 10 — EXPERTO — Sistema de plugins con ABCs
# ============================================================================
seccion("EJERCICIO 10 — Sistema de plugins con ABCs")

# Estás construyendo un motor de plugins. Cada plugin debe declarar su
# nombre, versión y saber ejecutarse sobre unos datos. El manager debe
# rechazar cualquier objeto que no cumpla el contrato Plugin.

# Crea la ABC Plugin con:
#  - propiedad abstracta nombre
#  - propiedad abstracta version
#  - método abstracto ejecutar(datos)
#  - método CONCRETO info() que imprime "nombre vversion"
class Plugin(ABC):
    ...

# Implementa PluginCSV y PluginJSON
class PluginCSV(Plugin):
    ...

class PluginJSON(Plugin):
    ...

# Crea PluginManager con: registrar(plugin) que valide con isinstance y
# lance TypeError si no es un Plugin válido, y ejecutar_todos(datos) que
# ejecute ejecutar(datos) en todos los plugins registrados
class PluginManager:
    def __init__(self):
        ...

    def registrar(self, plugin):
        ...

    def ejecutar_todos(self, datos):
        ...

# manager = PluginManager()
# manager.registrar(PluginCSV())
# manager.registrar(PluginJSON())
# manager.ejecutar_todos({"valor": 42})
# try:
#     manager.registrar(object())
# except TypeError as e:
#     print(e)
