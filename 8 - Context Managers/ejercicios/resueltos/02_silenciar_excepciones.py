# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 2 — Fácil | Silenciar excepciones concretas  [RESUELTO]
# Técnica: contextlib.contextmanager, suprimir excepción desde __exit__
# ─────────────────────────────────────────────────────────────────────────────
#
# CONCEPTO CLAVE
#   En un @contextmanager, si capturas la excepción en el except que rodea
#   el yield y no la relanzas, queda suprimida (equivale a que __exit__
#   devuelva True). Si no la capturas, se propaga.
#
#   Python ya incluye contextlib.suppress que hace exactamente esto.
#   Este ejercicio muestra cómo está implementado por dentro.
# ─────────────────────────────────────────────────────────────────────────────

from contextlib import contextmanager


@contextmanager
def silenciar_errores(*tipos_excepcion):
    try:
        yield
    except tipos_excepcion:
        pass                           # capturada → suprimida


# --- Prueba ---
with silenciar_errores(KeyError, FileNotFoundError):
    datos = {"nombre": "Ivan"}
    print(datos["edad"])               # KeyError — silenciado

print("El programa continúa")

with silenciar_errores(KeyError):
        raise ValueError("este no se silencia")

