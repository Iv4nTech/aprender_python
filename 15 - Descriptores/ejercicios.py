"""
================================================================================
 EJERCICIOS: DESCRIPTORES EN PYTHON
 Casos reales — de fácil a experto
================================================================================

Este fichero está pensado para ejecutarse de principio a fin:

    python3 ejercicios.py

Completa cada ejercicio donde encuentres "..." y descomenta los print()
para comprobar el resultado.
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

# Crea un descriptor `Constante` que solo defina __get__(self, obj, type=None)
# y devuelva siempre el valor que se le pasó al crearlo en __init__.
# Úsalo como atributo de clase en una clase `Sistema` (ej: version = Constante("2.0")).
...

# print(Sistema.version)
# print(Sistema().version)


# ============================================================================
# EJERCICIO 2 — FÁCIL — Non-data descriptor vs data descriptor
# ============================================================================
seccion("EJERCICIO 2 — Non-data descriptor vs data descriptor")

# Crea dos descriptores:
#   - `NonData`: solo __get__, devuelve un valor fijo guardado en __init__.
#   - `Data`: __get__ y __set__, devuelve/guarda un valor fijo guardado en __init__.
# Crea una clase `Demo` con un atributo de cada tipo. Crea una instancia,
# escribe directamente en su __dict__ una entrada con el MISMO nombre que
# cada atributo, y demuestra cuál gana en cada caso.
...

demo = ...
# demo.__dict__["non_data"] = "..."
# demo.__dict__["data"] = "..."
# print(demo.non_data)  # Esperado: gana el __dict__
# print(demo.data)      # Esperado: gana el descriptor


# ============================================================================
# EJERCICIO 3 — FÁCIL — Descriptor con validación de tipo
# ============================================================================
seccion("EJERCICIO 3 — Descriptor con validación de tipo")

# Crea un descriptor `TipoStr` con __get__ y __set__ que valide que el
# valor asignado sea un str, lanzando TypeError si no lo es.
# Úsalo en una clase `Persona` con el atributo `nombre`.
...

persona = ...
# persona.nombre = "Ana"
# print(persona.nombre)
try:
    ...  # persona.nombre = 123
except TypeError as e:
    ...
    # print(e)  # Esperado: TypeError


# ============================================================================
# EJERCICIO 4 — FÁCIL — Reutilizar el mismo descriptor en otra clase
# ============================================================================
seccion("EJERCICIO 4 — Reutilizar el mismo descriptor en otra clase")

# Usa el descriptor TipoStr del ejercicio 3 en una clase `Empresa` con el
# atributo `razon_social`. Demuestra que el mismo descriptor funciona en
# las dos clases (Persona y Empresa) sin duplicar código.
...

empresa = ...
# empresa.razon_social = "GAME S.L."
# print(empresa.razon_social)
try:
    ...  # empresa.razon_social = 123
except TypeError as e:
    ...
    # print(e)  # Esperado: TypeError


# ============================================================================
# EJERCICIO 5 — MEDIO — __set_name__ y validación de rango
# ============================================================================
seccion("EJERCICIO 5 — __set_name__ y validación de rango")

# Crea un descriptor `ValidarRango` que:
#  - En __init__ acepte min_val y max_val.
#  - Use __set_name__ para guardar el nombre del atributo.
#  - En __set__, lance ValueError si el valor está fuera de [min_val, max_val],
#    incluyendo el NOMBRE del atributo en el mensaje de error.
...


# ============================================================================
# EJERCICIO 6 — MEDIO — Aplicar ValidarRango a varios atributos
# ============================================================================
seccion("EJERCICIO 6 — Aplicar ValidarRango a varios atributos")

# Crea una clase `Temperatura` con dos atributos que usen ValidarRango:
#   - celsius: entre -273.15 y 1000
#   - humedad: entre 0 y 100
# Demuestra que el mismo descriptor valida ambos atributos correctamente.
...

t = ...
# t.celsius = 25
# t.humedad = 50
# print(t.celsius, t.humedad)
try:
    ...  # t.celsius = -300
except ValueError as e:
    ...
    # print(e)  # Esperado: ValueError mencionando "celsius"
try:
    ...  # t.humedad = 150
except ValueError as e:
    ...
    # print(e)  # Esperado: ValueError mencionando "humedad"


# ============================================================================
# EJERCICIO 7 — MEDIO — Descriptor de solo lectura (data descriptor)
# ============================================================================
seccion("EJERCICIO 7 — Descriptor de solo lectura")

# Crea un descriptor `SoloLectura` que defina __get__ (devuelve el valor
# guardado) y __set__ (SIEMPRE lanza AttributeError). Aunque no permita
# escribir, el hecho de definir __set__ lo convierte en DATA descriptor,
# así que gana siempre sobre el __dict__ de la instancia.
...

c = ...
# print(c.PI)
try:
    ...  # c.PI = 3.0
except AttributeError as e:
    ...
    # print(e)  # Esperado: AttributeError

# c.__dict__["PI"] = 99  # aunque lo colemos en el __dict__...
# print(c.PI)  # ...el descriptor sigue ganando: sigue devolviendo 3.14159


# ============================================================================
# EJERCICIO 8 — AVANZADO — Descriptor genérico de tipo con __set_name__
# ============================================================================
seccion("EJERCICIO 8 — Descriptor genérico de tipo")

# Crea un descriptor `ValidarTipo` que:
#  - Reciba el tipo esperado en __init__ (ej: ValidarTipo(float)).
#  - Use __set_name__ para guardar el nombre privado del atributo.
#  - Valide el tipo en __set__, lanzando TypeError si no coincide.
# Aplícalo a una clase `Coordenada` con atributos x: float e y: float.
...

coord = ...
# coord.x = 1.5
# coord.y = 2.5
# print(coord.x, coord.y)
try:
    ...  # coord.x = "no es un float"
except TypeError as e:
    ...
    # print(e)  # Esperado: TypeError


# ============================================================================
# EJERCICIO 9 — AVANZADO — Reimplementar @property como descriptor
# ============================================================================
seccion("EJERCICIO 9 — Reimplementar @property como descriptor")

# Crea un descriptor `MiProperty` que reciba fget, fset y fdel en __init__
# y reproduzca el comportamiento de @property mediante __get__, __set__
# y __delete__. Aplícalo a una clase `Circulo` con el atributo `radio`,
# validando en el setter que el radio sea positivo.
...

circulo = ...
# print(circulo.radio)
# circulo.radio = 10
# print(circulo.radio)
try:
    ...  # circulo.radio = -1
except ValueError as e:
    ...
    # print(e)  # Esperado: ValueError


# ============================================================================
# EJERCICIO 10 — EXPERTO — Descriptor de validación genérico y reutilizable
# ============================================================================
seccion("EJERCICIO 10 — Descriptor de validación genérico y reutilizable")

# Crea un descriptor `Validador` que:
#  - Reciba en __init__: tipo, min_val=None, max_val=None.
#  - Use __set_name__ para conocer el nombre del atributo.
#  - En __set__, lance TypeError si el tipo no coincide, o ValueError si
#    el valor está fuera de [min_val, max_val] (cuando se hayan indicado).
#  - Los mensajes de error deben incluir el nombre del atributo.
#
# Aplícalo a una clase `Empleado` con:
#   - nombre: str
#   - edad: int, entre 18 y 65
#   - salario: float, mayor que 0
#
# Demuestra que el mismo descriptor, sin duplicar código, valida
# correctamente los tres atributos.
...

empleado = ...
# print(empleado.nombre, empleado.edad, empleado.salario)
try:
    ...  # empleado.edad = 17
except ValueError as e:
    ...
    # print(e)  # Esperado: ValueError mencionando "edad"
try:
    ...  # empleado.salario = -100
except ValueError as e:
    ...
    # print(e)  # Esperado: ValueError mencionando "salario"
try:
    ...  # empleado.nombre = 123
except TypeError as e:
    ...
    # print(e)  # Esperado: TypeError mencionando "nombre"
