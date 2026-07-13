"""
================================================================================
 EJERCICIOS RESUELTOS: DESCRIPTORES EN PYTHON
 Casos reales — de fácil a experto
================================================================================

Este fichero está pensado para ejecutarse de principio a fin:

    python3 ejercicios_resueltos.py

Cada ejercicio imprime resultados reales para confirmar que funciona.
================================================================================
"""


def seccion(titulo: str) -> None:
    """Pequeño helper para imprimir cabeceras y que la salida sea legible."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# EJERCICIO 1 — FÁCIL — Descriptor básico de solo lectura
# ============================================================================
seccion("EJERCICIO 1 — Descriptor básico de solo lectura")

class Constante:
    def __init__(self, valor):
        self.valor = valor

    def __get__(self, obj, type=None):
        return self.valor


class Sistema:
    version = Constante("2.0")


print(Sistema.version)
print(Sistema().version)


# ============================================================================
# EJERCICIO 2 — FÁCIL — Non-data descriptor vs data descriptor
# ============================================================================
seccion("EJERCICIO 2 — Non-data descriptor vs data descriptor")

class NonData:
    def __init__(self, valor):
        self.valor = valor

    def __get__(self, obj, type=None):
        return self.valor


class Data:
    def __init__(self, valor):
        self.valor = valor

    def __get__(self, obj, type=None):
        return self.valor

    def __set__(self, obj, value):
        self.valor = value


class Demo:
    non_data = NonData("desde la clase (non-data)")
    data = Data("desde la clase (data)")


demo = Demo()
demo.__dict__["non_data"] = "desde el __dict__ de la instancia"
demo.__dict__["data"] = "desde el __dict__ de la instancia"

print(demo.non_data)  # gana el __dict__: el non-data descriptor pierde
print(demo.data)      # gana el descriptor: el data descriptor siempre gana


# ============================================================================
# EJERCICIO 3 — FÁCIL — Descriptor con validación de tipo
# ============================================================================
seccion("EJERCICIO 3 — Descriptor con validación de tipo")

class TipoStr:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.private_name[1:]} debe ser str")
        setattr(obj, self.private_name, value)


class Persona:
    nombre = TipoStr()


persona = Persona()
persona.nombre = "Ana"
print(persona.nombre)

try:
    persona.nombre = 123
except TypeError as e:
    print("persona.nombre = 123 ->", type(e).__name__, "->", e)


# ============================================================================
# EJERCICIO 4 — FÁCIL — Reutilizar el mismo descriptor en otra clase
# ============================================================================
seccion("EJERCICIO 4 — Reutilizar el mismo descriptor en otra clase")

class Empresa:
    razon_social = TipoStr()


empresa = Empresa()
empresa.razon_social = "Acme S.L."
print(empresa.razon_social)

try:
    empresa.razon_social = 123
except TypeError as e:
    print("empresa.razon_social = 123 ->", type(e).__name__, "->", e)


# ============================================================================
# EJERCICIO 5 — MEDIO — __set_name__ y validación de rango
# ============================================================================
seccion("EJERCICIO 5 — __set_name__ y validación de rango")

class ValidarRango:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(
                f"{self.public_name} debe estar entre {self.min_val} y {self.max_val}"
            )
        setattr(obj, self.private_name, value)


# ============================================================================
# EJERCICIO 6 — MEDIO — Aplicar ValidarRango a varios atributos
# ============================================================================
seccion("EJERCICIO 6 — Aplicar ValidarRango a varios atributos")

class Temperatura:
    celsius = ValidarRango(-273.15, 1000)
    humedad = ValidarRango(0, 100)


t = Temperatura()
t.celsius = 25
t.humedad = 50
print(t.celsius, t.humedad)

try:
    t.celsius = -300
except ValueError as e:
    print("t.celsius = -300 ->", type(e).__name__, "->", e)

try:
    t.humedad = 150
except ValueError as e:
    print("t.humedad = 150 ->", type(e).__name__, "->", e)


# ============================================================================
# EJERCICIO 7 — MEDIO — Descriptor de solo lectura (data descriptor)
# ============================================================================
seccion("EJERCICIO 7 — Descriptor de solo lectura")

class SoloLectura:
    def __init__(self, valor):
        self.valor = valor

    def __get__(self, obj, type=None):
        return self.valor

    def __set__(self, obj, value):
        raise AttributeError("no se puede modificar: atributo de solo lectura")


class Constantes:
    PI = SoloLectura(3.14159)


c = Constantes()
print(c.PI)

try:
    c.PI = 3.0
except AttributeError as e:
    print("c.PI = 3.0 ->", type(e).__name__, "->", e)

# Aunque colemos una entrada directamente en el __dict__ de la instancia,
# el descriptor sigue ganando por ser un DATA descriptor (define __set__).
c.__dict__["PI"] = 99
print("Tras colar 99 en __dict__, c.PI sigue siendo:", c.PI)


# ============================================================================
# EJERCICIO 8 — AVANZADO — Descriptor genérico de tipo con __set_name__
# ============================================================================
seccion("EJERCICIO 8 — Descriptor genérico de tipo")

class ValidarTipo:
    def __init__(self, tipo):
        self.tipo = tipo

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, self.tipo):
            raise TypeError(f"{self.public_name} debe ser {self.tipo.__name__}")
        setattr(obj, self.private_name, value)


class Coordenada:
    x = ValidarTipo(float)
    y = ValidarTipo(float)


coord = Coordenada()
coord.x = 1.5
coord.y = 2.5
print(coord.x, coord.y)

try:
    coord.x = "no es un float"
except TypeError as e:
    print("coord.x = 'no es un float' ->", type(e).__name__, "->", e)


# ============================================================================
# EJERCICIO 9 — AVANZADO — Reimplementar @property como descriptor
# ============================================================================
seccion("EJERCICIO 9 — Reimplementar @property como descriptor")

class MiProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("atributo no legible")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("no se puede asignar: atributo de solo lectura")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("no se puede borrar este atributo")
        self.fdel(obj)


class Circulo:
    def __init__(self, radio):
        self._radio = radio

    def _get_radio(self):
        return self._radio

    def _set_radio(self, value):
        if value <= 0:
            raise ValueError("el radio debe ser positivo")
        self._radio = value

    radio = MiProperty(_get_radio, _set_radio)


circulo = Circulo(5)
print(circulo.radio)
circulo.radio = 10
print(circulo.radio)

try:
    circulo.radio = -1
except ValueError as e:
    print("circulo.radio = -1 ->", type(e).__name__, "->", e)


# ============================================================================
# EJERCICIO 10 — EXPERTO — Descriptor de validación genérico y reutilizable
# ============================================================================
seccion("EJERCICIO 10 — Descriptor de validación genérico y reutilizable")

class Validador:
    def __init__(self, tipo, min_val=None, max_val=None):
        self.tipo = tipo
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, self.tipo):
            raise TypeError(f"{self.public_name} debe ser {self.tipo.__name__}")
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"{self.public_name} debe ser mayor o igual que {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"{self.public_name} debe ser menor o igual que {self.max_val}")
        setattr(obj, self.private_name, value)


class Empleado:
    nombre = Validador(str)
    edad = Validador(int, min_val=18, max_val=65)
    salario = Validador((int, float), min_val=0.01)

    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario


empleado = Empleado("Marta", 30, 32000.0)
print(empleado.nombre, empleado.edad, empleado.salario)

try:
    empleado.edad = 17
except ValueError as e:
    print("empleado.edad = 17 ->", type(e).__name__, "->", e)

try:
    empleado.salario = -100
except ValueError as e:
    print("empleado.salario = -100 ->", type(e).__name__, "->", e)

try:
    empleado.nombre = 123
except TypeError as e:
    print("empleado.nombre = 123 ->", type(e).__name__, "->", e)


seccion("FIN — todos los ejercicios resueltos")
