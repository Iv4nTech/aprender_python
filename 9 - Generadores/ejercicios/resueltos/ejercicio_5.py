"""
Ejercicio 5 - Leer CSV en chunks
==================================
Crea un generador `leer_csv_chunks` que reciba una ruta CSV y un
tamaño `chunk_size` (int) y produzca listas de filas de ese tamaño.

La última lista puede tener menos filas si no completa el chunk.
No uses pandas, solo el módulo csv estándar.

Ejemplo de uso:
    for chunk in leer_csv_chunks("ventas.csv", chunk_size=3):
        print(f"Procesando {len(chunk)} filas...")

Caso real: importar millones de filas a una base de datos en lotes
           para no saturar la memoria ni el buffer de escritura.
"""

import csv

# Tu código aquí
def leer_csv_chunks(ruta, chunk_size):
    with open(ruta, "r", newline="") as f:
        reader = csv.reader(f)
        chunk = []
        for fila in reader:
            chunk.append(fila)
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
        if chunk:  # Si quedan filas sin procesar al final
            yield chunk

# --- Prueba ---
if __name__ == "__main__":
    import tempfile, os

    filas = "nombre,precio\n" + "\n".join(f"prod{i},{i*10}" for i in range(1, 11))
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(filas)
        ruta = f.name

    for chunk in leer_csv_chunks(ruta, chunk_size=3):
        print(f"Chunk de {len(chunk)} filas: {chunk}")

    os.unlink(ruta)
