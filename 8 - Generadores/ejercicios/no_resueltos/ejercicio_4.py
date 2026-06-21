"""
Ejercicio 4 - Pipeline de transformación
==========================================
Crea tres generadores que formen un pipeline:

1. `leer_numeros(lista)`  → produce cada número de la lista
2. `solo_pares(gen)`      → filtra y pasa solo los pares
3. `al_cuadrado(gen)`     → eleva al cuadrado cada valor recibido

Encadénalos para procesar la lista sin crear listas intermedias.

Ejemplo de uso:
    datos = [1, 2, 3, 4, 5, 6, 7, 8]
    resultado = al_cuadrado(solo_pares(leer_numeros(datos)))
    print(list(resultado))  # [4, 16, 36, 64]

Caso real: pipelines ETL donde cada etapa transforma el flujo de datos
           (leer CSV → filtrar filas → transformar columnas).
"""

# Tu código aquí


# --- Prueba ---
if __name__ == "__main__":
    datos = [1, 2, 3, 4, 5, 6, 7, 8]
    resultado = al_cuadrado(solo_pares(leer_numeros(datos)))
    print(list(resultado))  # [4, 16, 36, 64]
