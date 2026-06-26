"""Una herramienta de ejemplo con un atributo de ESTADO para ver el singleton."""

# Este atributo es un dato MUTABLE del módulo. Como el módulo es único en
# memoria, si lo cambias por una referencia, cambia para todas.
config = {"tema": "claro"}


def saludar(nombre):
    return f"Hola, {nombre}"
