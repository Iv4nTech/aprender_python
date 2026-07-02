"""
Ejercicio 8 - Generador recursivo con yield from
==================================================
Crea un generador `recorrer_arbol` que reciba un diccionario
anidado (árbol) y produzca todas las hojas (valores no-dict)
en orden de profundidad primero (DFS).

Usa `yield from` para delegar en la recursión.

Ejemplo de uso:
    arbol = {
        "a": 1,
        "b": {"c": 2, "d": {"e": 3}},
        "f": 4,
    }
    print(list(recorrer_arbol(arbol)))  # [1, 2, 3, 4]

Caso real: aplanar respuestas JSON anidadas de APIs (configuraciones,
           estructuras organizativas, árboles de categorías).
"""

# Tu código aquí


# --- Prueba ---
if __name__ == "__main__":
    arbol = {
        "usuarios": {
            "admin": {"nivel": 1, "activo": True},
            "editor": {"nivel": 2, "activo": False},
        },
        "version": "1.0",
        "max_conexiones": 100,
    }
    print(list(recorrer_arbol(arbol)))
    # [1, True, 2, False, '1.0', 100]  (orden según dict)
