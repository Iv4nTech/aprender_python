"""
Ejercicio 1 - Contador simple
==============================
Crea un generador llamado `contar_hasta` que reciba un número `n`
y genere los enteros del 1 hasta n (incluido).

Ejemplo de uso:
    for numero in contar_hasta(5):
        print(numero)
    # 1, 2, 3, 4, 5

Caso real: recorrer páginas de una API paginada (página 1, 2, 3...).
"""

# Tu código aquí
def contar_hasta(n):
    for i in range(1, n  + 1):
        yield i

# --- Prueba ---
if __name__ == "__main__":
    for numero in contar_hasta(5):
        print(numero)
