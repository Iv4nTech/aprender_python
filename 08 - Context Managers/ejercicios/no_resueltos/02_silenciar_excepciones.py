# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 2 — Fácil | Silenciar excepciones concretas
# Técnica: contextlib.contextmanager, suprimir excepción desde __exit__
# ─────────────────────────────────────────────────────────────────────────────
#
# CONTEXTO
#   A veces quieres ejecutar código que puede fallar sin detener el programa,
#   pero sin llenar el código de bloques try/except vacíos. Por ejemplo:
#   borrar un archivo que puede no existir, o leer una clave de un diccionario
#   que puede no estar.
#
# TAREA
#   Implementa con @contextmanager la función silenciar_errores(*tipos).
#   - Acepta uno o varios tipos de excepción.
#   - Si dentro del bloque ocurre una excepción de esos tipos, la suprime.
#   - Si la excepción es de un tipo distinto, se propaga con normalidad.
#
#   PISTA: en un @contextmanager, para suprimir una excepción captúrala en
#   el except del try/finally que rodea el yield. Si no la capturas, se propaga.
#
# USO ESPERADO
#   with silenciar_errores(KeyError, FileNotFoundError):
#       datos = {"nombre": "Ivan"}
#       print(datos["edad"])           # KeyError — silenciado
#
#   print("El programa continúa")
#
# SALIDA ESPERADA
#   El programa continúa
# ─────────────────────────────────────────────────────────────────────────────

from contextlib import contextmanager


@contextmanager
def silenciar_errores(*tipos_excepcion):
    pass


# --- Prueba (no modificar) ---
with silenciar_errores(KeyError, FileNotFoundError):
    datos = {"nombre": "Ivan"}
    print(datos["edad"])               # KeyError — debe silenciarse

print("El programa continúa")

# Un ValueError NO debe silenciarse
try:
    with silenciar_errores(KeyError):
        raise ValueError("este no se silencia")
except ValueError as e:
    print(f"Excepción propagada: {e}")
