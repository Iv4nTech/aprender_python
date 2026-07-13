"""
================================================================================
 DESCRIPTORES EN PYTHON — GUÍA COMPLETA (de cero a experto)
================================================================================

Un descriptor es cualquier objeto que define uno o más de estos métodos:

    __get__(self, obj, type=None)   -> se ejecuta al LEER el atributo
    __set__(self, obj, value)       -> se ejecuta al ASIGNAR el atributo
    __delete__(self, obj)           -> se ejecuta al hacer `del` del atributo

Cuando un descriptor vive como atributo de CLASE, Python intercepta el acceso
normal a ese atributo (`instancia.atributo`) y lo redirige a estos métodos.
Es el mecanismo que hay POR DEBAJO de @property, de los atributos de las
dataclasses y de __slots__: todos son descriptores.

¿Por qué importa? Porque te permite escribir la lógica de validación,
cálculo o control de acceso UNA sola vez, en una clase descriptor, y
reutilizarla en cuantos atributos y clases haga falta, sin duplicar código.

Este fichero está pensado para ejecutarse de principio a fin:

    python3 introduccion.py

Cada sección imprime resultados para que veas el comportamiento real.
================================================================================
"""


def seccion(titulo: str) -> None:
    """Pequeño helper para imprimir cabeceras y que la salida sea legible."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROTOCOLO DESCRIPTOR
# ============================================================================
seccion("1. El protocolo descriptor")

# Un descriptor es CUALQUIER objeto que define __get__, __set__ o __delete__.
# Las firmas exactas, según la documentación oficial de Python 3.14, son:
#
#   __get__(self, obj, type=None)   obj: la instancia (o None si se accede
#                                    desde la clase). type: la clase dueña.
#   __set__(self, obj, value)       obj: la instancia. value: el valor nuevo.
#   __delete__(self, obj)           obj: la instancia sobre la que se borra.

# Ejemplo mínimo: un descriptor que solo define __get__ y siempre
# devuelve la misma constante, sin importar la instancia.
class Constante:
    def __init__(self, valor):
        self.valor = valor

    def __get__(self, obj, type=None):
        print(f"  __get__ llamado con obj={obj!r}, type={type.__name__}")
        return self.valor

class Config:
    version = Constante("1.0.0")

# Acceso desde la CLASE: obj es None.
print("Config.version ->", Config.version)

# Acceso desde una INSTANCIA: obj es la instancia concreta.
cfg = Config()
print("cfg.version ->", cfg.version)

# ¿Por qué no usar simplemente version = "1.0.0"? Porque un atributo de
# clase NORMAL no puede ejecutar código al leerlo: solo devuelve el valor
# guardado. Un descriptor SÍ puede, por ejemplo, contar cuántas veces se ha
# leído el atributo, algo imposible con un atributo plano.
class ContadorAcceso:
    def __init__(self, valor):
        self.valor = valor
        self.accesos = 0

    def __get__(self, obj, type=None):
        self.accesos += 1
        return self.valor

class ConfigConContador:
    version = ContadorAcceso("1.0.0")

cfg2 = ConfigConContador()
for _ in range(3):
    cfg2.version           # cada lectura pasa por __get__ y suma un acceso
print("Veces que se ha leído 'version':", ConfigConContador.__dict__["version"].accesos)


# ============================================================================
# 2. NON-DATA DESCRIPTOR vs DATA DESCRIPTOR
# ============================================================================
seccion("2. Non-data descriptor vs data descriptor")

# Non-data descriptor: solo define __get__. El __dict__ de la instancia
# tiene PRIORIDAD sobre él si existe una entrada con el mismo nombre.
class NonData:
    def __init__(self, valor):
        self.valor = valor

    def __get__(self, obj, type=None):
        return self.valor

# Data descriptor: define __set__ (o __delete__). GANA SIEMPRE sobre el
# __dict__ de la instancia, aunque haya una entrada con el mismo nombre.
class Data:
    def __init__(self, valor):
        self.valor = valor

    def __get__(self, obj, type=None):
        return self.valor

    def __set__(self, obj, value):
        self.valor = value

class Ejemplo:
    non_data = NonData("desde la CLASE (non-data)")
    data = Data("desde la CLASE (data)")

e = Ejemplo()
print("Antes de tocar __dict__:")
print("  e.non_data ->", e.non_data)
print("  e.data     ->", e.data)

# Colamos una entrada en el __dict__ de la INSTANCIA con el mismo nombre,
# sin pasar por __set__ (accedemos directamente al diccionario).
e.__dict__["non_data"] = "desde el __dict__ de la INSTANCIA"
e.__dict__["data"] = "desde el __dict__ de la INSTANCIA"

print("\nDespués de escribir directamente en e.__dict__:")
print("  e.non_data ->", e.non_data, "  (gana el __dict__: non-data pierde)")
print("  e.data     ->", e.data, "  (gana el descriptor: data siempre gana)")

# La entrada "data" SIGUE estando en el __dict__ de la instancia: no se
# pierde ni da error. Simplemente e.data nunca llega a consultarla, porque
# Python encuentra antes un data descriptor en la clase y corta ahí mismo.
print("  e.__dict__ (la entrada 'data' sigue ahí, pero nadie la lee):", e.__dict__)

# ¿POR QUÉ? Python busca el atributo primero en la clase. Si lo encuentra y
# es un DATA descriptor, lo usa YA, sin mirar el __dict__ de la instancia:
# así garantiza que nadie se salte __set__/__get__ escribiendo directamente
# en __dict__. Si es un NON-DATA descriptor (solo __get__), Python SÍ mira
# antes el __dict__ de la instancia, porque este tipo de descriptor (como
# los métodos normales) está pensado para poder sobrescribirse por instancia.

# Esto no es solo teoría: explica un comportamiento real de Python que ya
# conoces. Las funciones (los métodos de una clase) son NON-DATA
# descriptors, así que se pueden sobrescribir por instancia sin tocar la
# clase entera:
class ClaseConMetodo:
    def saludo(self):
        return "Hola desde el método de la clase"

obj = ClaseConMetodo()
print("Método normal:", obj.saludo())

obj.__dict__["saludo"] = lambda: "Hola desde la instancia (sobrescrito)"
print("Tras sobrescribir en la instancia:", obj.saludo())

# Si 'saludo' fuera un DATA descriptor (como @property, o Data de arriba),
# esto NO funcionaría: el descriptor seguiría ganando pase lo que pase.

# CUIDADO: el error más común al escribir un descriptor. La clase Data de
# arriba guarda el valor en SÍ MISMA (self.valor), no en la instancia. Pero
# el descriptor se crea UNA sola vez, en el cuerpo de la clase, y lo
# comparten TODAS las instancias de Ejemplo. Resultado: dos instancias
# distintas acaban compartiendo el mismo valor sin querer.
e1 = Ejemplo()
e2 = Ejemplo()
e1.data = "valor de e1"
print("e2.data cambia también, aunque nunca lo tocamos:", e2.data)

# El arreglo: el descriptor NUNCA debe guardar el estado en sí mismo si va
# a haber más de una instancia. Debe delegarlo a CADA instancia con
# setattr/getattr, tal y como hacen Validado, Validador y Positivo más
# abajo en este mismo fichero.
class DataCorregido:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)

class EjemploCorregido:
    data = DataCorregido()

ec1 = EjemploCorregido()
ec2 = EjemploCorregido()
ec1.data = "valor de ec1"
ec2.data = "valor de ec2"
print("Ahora cada instancia es independiente:", ec1.data, "|", ec2.data)


# ============================================================================
# 3. __set_name__
# ============================================================================
seccion("3. __set_name__")

# __set_name__(self, owner, name) permite que el descriptor sepa en qué
# nombre de atributo de clase fue asignado. Python lo llama AUTOMÁTICAMENTE
# al crear la clase (justo después de construirla), no en un momento
# posterior ni cuando se usa el descriptor por primera vez.
class Validado:
    def __set_name__(self, owner, name):
        print(f"  __set_name__ llamado para '{name}' en la clase {owner.__name__}")
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)

class Usuario:
    nombre = Validado()      # __set_name__ se dispara aquí, con name="nombre"
    email = Validado()       # y aquí, con name="email"

u = Usuario()
u.nombre = "Ana"
u.email = "ana@example.com"
print("u.nombre:", u.nombre, "| u.email:", u.email)
print("__dict__ real de la instancia:", u.__dict__)

# El mismo descriptor, reutilizado en dos atributos distintos de la misma
# clase, guarda su propio public_name/private_name gracias a __set_name__.
print("public_name de 'nombre':", Usuario.__dict__["nombre"].public_name)
print("public_name de 'email': ", Usuario.__dict__["email"].public_name)
print("private_name de 'nombre':", Usuario.__dict__["nombre"].private_name)
print("private_name de 'email': ", Usuario.__dict__["email"].private_name)

# ¿Por qué importa tanto __set_name__? Sin él, tendrías que pasarle el
# nombre A MANO a cada descriptor. Si por un copia-pega te equivocas y usas
# el MISMO nombre en dos atributos distintos, ambos comparten el mismo
# almacenamiento interno y se pisan en SILENCIO, sin ningún error visible.
class ValidadoManual:
    def __init__(self, nombre):
        self.private_name = "_" + nombre

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)

class UsuarioManual:
    nombre = ValidadoManual("nombre")
    email = ValidadoManual("nombre")   # copia-pega sin actualizar el string

um = UsuarioManual()
um.nombre = "Luis"
um.email = "luis@example.com"
print("um.nombre debería ser 'Luis', pero es:", um.nombre)   # bug silencioso

# Con __set_name__ (como en Validado, arriba) esto es IMPOSIBLE: el nombre
# privado siempre se deriva del atributo real de la clase, nunca de un
# string manual que se pueda copiar mal.


# ============================================================================
# 4. DESCRIPTOR REUTILIZABLE CON VALIDACIÓN
# ============================================================================
seccion("4. Descriptor reutilizable con validación")

# Un único descriptor puede validar tipo Y rango, configurándose distinto
# en cada atributo mediante los argumentos de su __init__.
class Validador:
    def __init__(self, tipo, minimo=None):
        self.tipo = tipo
        self.minimo = minimo

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        nombre_atributo = self.private_name[1:]
        if not isinstance(value, self.tipo):
            raise TypeError(f"{nombre_atributo} debe ser {self.tipo}")
        if self.minimo is not None and value <= self.minimo:
            raise ValueError(f"{nombre_atributo} debe ser mayor que {self.minimo}")
        setattr(obj, self.private_name, value)

    def __delete__(self, obj):
        delattr(obj, self.private_name)

# Aplicado a una clase real, SIN duplicar la lógica de validación.
class Producto:
    nombre = Validador(str)
    precio = Validador((int, float), minimo=0)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

p = Producto("Teclado mecánico", 45.99)
print("Producto válido:", p.nombre, "|", p.precio)

try:
    p.precio = -10
except ValueError as e:
    print("precio = -10 ->", type(e).__name__, "->", e)

try:
    p.nombre = 123
except TypeError as e:
    print("nombre = 123 ->", type(e).__name__, "->", e)

# __delete__(self, obj) se dispara con `del instancia.atributo`. Aquí borra
# el atributo privado; leerlo después falla, porque ya no existe.
del p.precio
try:
    p.precio
except AttributeError as e:
    print("p.precio tras 'del p.precio' ->", type(e).__name__, "->", e)


# ============================================================================
# 5. LA VENTAJA REAL: UN DESCRIPTOR SE REUTILIZA, UNA @property NO
# ============================================================================
seccion("5. La ventaja real: un descriptor se reutiliza, una @property no")

# @property también implementa el protocolo descriptor por dentro (tiene
# __get__, __set__ y __delete__), aunque se use con sintaxis de decorador.
print("property define __get__:   ", hasattr(property, "__get__"))
print("property define __set__:   ", hasattr(property, "__set__"))
print("property define __delete__:", hasattr(property, "__delete__"))

# El problema de @property: si necesitas la MISMA validación en varios
# atributos, tienes que copiar y pegar el getter y el setter en cada uno.
# Aquí un rectángulo donde ancho y alto deben ser positivos, con @property:
class RectanguloConProperty:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        if value <= 0:
            raise ValueError("ancho debe ser positivo")
        self._ancho = value

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, value):
        if value <= 0:
            raise ValueError("alto debe ser positivo")
        self._alto = value

# La comprobación "value <= 0 -> ValueError" está DUPLICADA dos veces.
# Con un descriptor, esa lógica se escribe UNA sola vez y se reutiliza
# instanciándolo tantas veces como atributos necesites validar igual.
class Positivo:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.private_name[1:]} debe ser positivo")
        setattr(obj, self.private_name, value)

class RectanguloConDescriptor:
    ancho = Positivo()
    alto = Positivo()

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

# Mismo comportamiento en los dos enfoques...
r1 = RectanguloConProperty(4, 5)
r2 = RectanguloConDescriptor(4, 5)
print("property:", r1.ancho, r1.alto, "| descriptor:", r2.ancho, r2.alto)

try:
    r1.ancho = -1
except ValueError as e:
    print("property  -> ancho = -1 ->", type(e).__name__, "->", e)

try:
    r2.ancho = -1
except ValueError as e:
    print("descriptor-> ancho = -1 ->", type(e).__name__, "->", e)

# ...pero fíjate en el coste de añadir un TERCER campo validado (ej: una
# Caja con profundidad). Con @property tocaría copiar OTRO bloque entero
# de getter+setter (7 líneas más). Con el descriptor, una línea y listo:
class Caja(RectanguloConDescriptor):
    profundidad = Positivo()          # <- toda la validación reutilizada aquí

    def __init__(self, ancho, alto, profundidad):
        super().__init__(ancho, alto)
        self.profundidad = profundidad

caja = Caja(2, 3, 4)
print("Caja:", caja.ancho, caja.alto, caja.profundidad)

try:
    caja.profundidad = -1
except ValueError as e:
    print("caja.profundidad = -1 ->", type(e).__name__, "->", e)

# ESA es la ventaja real de los descriptores frente a @property: no son
# "una property manual y ya está", son OBJETOS reutilizables. La misma
# clase Positivo() sirve para cualquier atributo de cualquier clase, sin
# escribir un getter/setter nuevo cada vez. @property no se puede
# reutilizar así entre atributos: cada uno exige su propio bloque de código.


seccion("FIN — ya conoces los descriptores al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
