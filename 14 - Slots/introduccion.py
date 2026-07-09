"""
================================================================================
 __slots__ EN PYTHON — GUÍA COMPLETA (de cero a experto)
================================================================================

Por defecto, cada instancia de una clase en Python guarda sus atributos en
un diccionario interno: __dict__. Eso da flexibilidad total (añadir
atributos en cualquier momento), pero cuesta memoria: cada instancia carga
con su propio diccionario, aunque todas las instancias tengan siempre los
mismos campos.

    __slots__ -> una lista/tupla de nombres de atributos que le dice a
                 Python: "estas instancias SOLO van a tener estos campos,
                 no reserves un __dict__ para cada una".

¿Por qué importa? Porque cuando creas miles o millones de objetos con la
misma forma (un Punto, un Pixel, un nodo de un árbol...), el __dict__ por
instancia es puro desperdicio. __slots__ cambia el almacenamiento interno
a algo mucho más compacto, a costa de perder la flexibilidad de añadir
atributos sobre la marcha.

Este fichero está pensado para ejecutarse de principio a fin:

    python3 introduccion.py

Cada sección imprime resultados para que veas el comportamiento real.
================================================================================
"""

import sys
import timeit


def seccion(titulo: str) -> None:
    """Pequeño helper para imprimir cabeceras y que la salida sea legible."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA: __dict__ POR INSTANCIA
# ============================================================================
seccion("1. El problema: __dict__ por instancia")

# Una clase normal guarda sus atributos en un diccionario propio de CADA
# instancia. Eso es lo que te permite añadir atributos nuevos en cualquier
# momento, aunque no estén en __init__.
class PuntoNormal:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

p_normal = PuntoNormal(1.0, 2.0)
print("¿Tiene __dict__?:", p_normal.__dict__)

# La flexibilidad tiene un precio: puedes colar cualquier atributo, incluso
# uno con una errata, y Python no se queja.
p_normal.z = 3.0            # atributo nuevo, no declarado en __init__
p_normal.zz = 99            # errata: nadie la va a detectar
print("Atributos colados:", p_normal.__dict__)

# Ese __dict__ ocupa memoria propia en CADA instancia, aunque todas tengan
# siempre los mismos campos (x, y). __slots__ existe para evitar ese coste.


# ============================================================================
# 2. DEFINIR UNA CLASE CON __slots__
# ============================================================================
seccion("2. Definir una clase con __slots__")

# __slots__ es un atributo de CLASE: una lista (o cualquier iterable de
# strings) con los nombres de los atributos permitidos.
class Punto:
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

pt = Punto(1.0, 2.0)
print("Punto creado:", pt.x, pt.y)

# __slots__ acepta cualquier iterable de strings: tupla, lista, incluso
# un solo string se interpreta como iterable de caracteres (evítalo).
class PuntoConLista:
    __slots__ = ["x", "y"]         # una lista funciona igual que una tupla

    def __init__(self, x, y):
        self.x = x
        self.y = y

pl = PuntoConLista(5, 6)
print("Con __slots__ como lista:", pl.x, pl.y)


# ============================================================================
# 3. ACCESO Y MODIFICACIÓN CON NOTACIÓN PUNTO
# ============================================================================
seccion("3. Acceso y modificación con notación punto")

# Los atributos declarados en __slots__ se leen y escriben exactamente
# igual que en una clase normal: con la notación punto de siempre.
pt = Punto(0.0, 0.0)
print("Valores iniciales:", pt.x, pt.y)

pt.x = 10.0
pt.y = 20.0
print("Tras modificar:", pt.x, pt.y)


# ============================================================================
# 4. AUSENCIA DE __dict__
# ============================================================================
seccion("4. Ausencia de __dict__")

# La contrapartida de __slots__: las instancias ya NO tienen __dict__.
# Python reserva espacio fijo para cada slot en vez de un diccionario.
print("¿pt tiene atributo __dict__?:", hasattr(pt, "__dict__"))
print("¿p_normal tiene atributo __dict__?:", hasattr(p_normal, "__dict__"))

# Acceder directamente a pt.__dict__ lanza AttributeError, no devuelve {}.
try:
    pt.__dict__
except AttributeError as e:
    print("pt.__dict__ ->", type(e).__name__, "->", e)


# ============================================================================
# 5. AÑADIR UN ATRIBUTO NO DECLARADO: AttributeError
# ============================================================================
seccion("5. Añadir un atributo no declarado")

# Sin __dict__, Python no tiene dónde guardar un atributo que no esté en
# __slots__. Intentarlo lanza AttributeError, justo lo contrario de lo
# que pasaba con PuntoNormal en la sección 1.
try:
    pt.z = 30.0
except AttributeError as e:
    print("pt.z = 30.0 ->", type(e).__name__, "->", e)

# Esto es una ventaja además de un ahorro de memoria: convierte los errores
# tipográficos ('slef.nombre = ...') en un fallo inmediato en vez de un
# atributo fantasma silencioso.


# ============================================================================
# 6. MEMORIA: CLASE NORMAL vs CLASE CON __slots__
# ============================================================================
seccion("6. Memoria: clase normal vs clase con __slots__")

normal = PuntoNormal(1.0, 2.0)
con_slots = Punto(1.0, 2.0)

# sys.getsizeof mide solo el objeto en sí, sin contar lo que cuelga de él.
# Para ver el ahorro real hay que sumar también el __dict__ de la instancia
# normal, que es donde vive el coste extra.
tam_normal = sys.getsizeof(normal) + sys.getsizeof(normal.__dict__)
tam_slots = sys.getsizeof(con_slots)
print(f"PuntoNormal (objeto + __dict__): {tam_normal} bytes")
print(f"Punto con __slots__:             {tam_slots} bytes")
print(f"Ahorro por instancia: {tam_normal - tam_slots} bytes")


# ============================================================================
# 7. HERENCIA CORRECTA: LA SUBCLASE TAMBIÉN DECLARA __slots__
# ============================================================================
seccion("7. Herencia correcta: la subclase también declara __slots__")

# Para que el ahorro de memoria se mantenga en la herencia, la subclase
# debe declarar su PROPIO __slots__, solo con los atributos NUEVOS que
# añade (los heredados ya están reservados por la clase base).
class Punto3D(Punto):
    __slots__ = ("z",)             # solo el atributo nuevo, x e y ya existen

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

p3 = Punto3D(1.0, 2.0, 3.0)
print("Punto3D:", p3.x, p3.y, p3.z)
print("¿Punto3D tiene __dict__?:", hasattr(p3, "__dict__"))

# Repetir un nombre de slot ya presente en la base es un error a evitar
# (desperdicia memoria y puede dar comportamientos confusos), aunque
# Python no siempre lo impide explícitamente: la regla es SOLO los nuevos.


# ============================================================================
# 8. HERENCIA INCORRECTA: LA SUBCLASE NO DECLARA __slots__
# ============================================================================
seccion("8. Herencia incorrecta: la subclase no declara __slots__")

# Si la subclase NO declara __slots__, Python le añade un __dict__ (y un
# __weakref__) automáticamente, como a cualquier clase normal. Se pierde
# TODO el ahorro de memoria, aunque la clase base sí tuviera __slots__.
class Punto3DSinSlots(Punto):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z              # esto NO iría a un slot, sino al __dict__

p3_sin = Punto3DSinSlots(1.0, 2.0, 3.0)
print("¿Punto3DSinSlots tiene __dict__?:", hasattr(p3_sin, "__dict__"))
print("Contenido de __dict__:", p3_sin.__dict__)

# Además, al recuperar __dict__, la subclase también puede recibir
# atributos completamente inventados, igual que una clase normal:
p3_sin.cualquier_cosa = "esto no debería existir"
print("Atributo colado en la subclase:", p3_sin.cualquier_cosa)


# ============================================================================
# 9. MODO HÍBRIDO: '__dict__' DENTRO DE __slots__
# ============================================================================
seccion("9. Modo híbrido: '__dict__' dentro de __slots__")

# Se puede incluir el string '__dict__' como un slot más. Esto reintroduce
# un __dict__ por instancia, recuperando la flexibilidad de añadir
# atributos arbitrarios, aunque los campos declarados en __slots__ siguen
# almacenándose en su hueco fijo y optimizado.
class PuntoHibrido:
    __slots__ = ("x", "y", "__dict__")

    def __init__(self, x, y):
        self.x = x
        self.y = y

ph = PuntoHibrido(1.0, 2.0)
print("¿PuntoHibrido tiene __dict__?:", hasattr(ph, "__dict__"))

# x e y siguen siendo slots optimizados...
ph.x = 99.0
print("x sigue siendo un slot:", ph.x)

# ...pero ahora también se pueden añadir atributos libres, que van al
# __dict__ recién recuperado.
ph.etiqueta = "punto libre"
print("Atributo libre añadido:", ph.etiqueta, "| __dict__:", ph.__dict__)

# Este modo híbrido es un término medio: pierdes parte del ahorro de
# memoria (vuelve a haber un __dict__), pero mantienes el ahorro en los
# campos que sí declaraste como slots.


# ============================================================================
# 10. BENCHMARK REAL: 100.000 INSTANCIAS
# ============================================================================
seccion("10. Benchmark real: 100.000 instancias")

N = 100_000

# --- Memoria: creamos N instancias de cada tipo y sumamos su tamaño real.
instancias_normales = [PuntoNormal(i, i) for i in range(N)]
instancias_slots = [Punto(i, i) for i in range(N)]

memoria_normal = sum(sys.getsizeof(o) + sys.getsizeof(o.__dict__) for o in instancias_normales)
memoria_slots = sum(sys.getsizeof(o) for o in instancias_slots)

print(f"Memoria {N:,} PuntoNormal: {memoria_normal:,} bytes")
print(f"Memoria {N:,} Punto (slots): {memoria_slots:,} bytes")
print(f"Ahorro total: {memoria_normal - memoria_slots:,} bytes "
      f"({(1 - memoria_slots / memoria_normal):.1%} menos)")

# --- Tiempo: cuánto se tarda en CREAR 100.000 instancias de cada clase.
tiempo_normal = timeit.timeit(lambda: [PuntoNormal(i, i) for i in range(N)], number=5)
tiempo_slots = timeit.timeit(lambda: [Punto(i, i) for i in range(N)], number=5)

print(f"\nTiempo creando {N:,} PuntoNormal (5 repeticiones): {tiempo_normal:.3f}s")
print(f"Tiempo creando {N:,} Punto (slots) (5 repeticiones): {tiempo_slots:.3f}s")


seccion("FIN — ya conoces __slots__ al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
