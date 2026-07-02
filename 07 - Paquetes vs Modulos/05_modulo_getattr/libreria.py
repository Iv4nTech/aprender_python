"""
CONCEPTO 05 (AVANZADO) · __getattr__ a nivel de MÓDULO (PEP 562, Python 3.7+)
Defines una función __getattr__(nombre) en el módulo y Python la llama cuando
alguien accede a un atributo que NO existe normalmente.

CASOS REALES:
  1) DEPRECAR un nombre antiguo: avisas con un warning pero sigues funcionando.
  2) CARGA PEREZOSA (lazy): no importas/creas algo costoso hasta que se usa.

"""
import warnings


def nueva_funcion():
    return "usa esta, es la buena"


def __getattr__(nombre):
    # Caso 1: nombre obsoleto -> avisamos pero redirigimos a la nueva.
    if nombre == "vieja_funcion":
        warnings.warn(
            "'vieja_funcion' está obsoleta; usa 'nueva_funcion'.",
            DeprecationWarning,
            stacklevel=2,
        )
        return nueva_funcion

    # Para cualquier otro nombre inexistente, el error normal de Python.
    raise AttributeError(f"el módulo 'libreria' no tiene el atributo {nombre!r}")
