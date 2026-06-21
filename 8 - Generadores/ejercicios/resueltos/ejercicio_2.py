"""
Ejercicio 2 - Leer un fichero línea a línea
=============================================
Crea un generador `leer_lineas` que reciba una ruta de fichero
y vaya produciendo cada línea sin el salto de línea final (\n).

NO cargues todo el fichero en memoria (nada de readlines()).

Ejemplo de uso:
    for linea in leer_lineas("datos.txt"):
        print(linea)

Caso real: procesar logs de servidor o CSVs enormes sin agotar la RAM.
"""

# Tu código aquí
def leer_lineas(ruta):
    with open(ruta, "r") as f:
        for linea in f:
            yield linea.rstrip("\n") # Eliminamos el salto de línea final

# --- Prueba ---
if __name__ == "__main__":
    import tempfile, os

    contenido = "línea 1\nlínea 2\nlínea 3\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write(contenido)
        ruta = f.name

    for linea in leer_lineas(ruta):
        print(linea)

    os.unlink(ruta)
