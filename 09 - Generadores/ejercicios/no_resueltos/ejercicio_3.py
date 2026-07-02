"""
Ejercicio 3 - Generador de IDs únicos
=======================================
Crea un generador infinito `generador_ids` que produzca IDs
con el formato "ID-0001", "ID-0002", "ID-0003"...

Usa itertools o un bucle while infinito con yield.

Ejemplo de uso:
    gen = generador_ids()
    print(next(gen))  # "ID-0001"
    print(next(gen))  # "ID-0002"

Caso real: asignar identificadores únicos a registros en un sistema
           de procesamiento de pedidos o eventos.
"""

# Tu código aquí


# --- Prueba ---
if __name__ == "__main__":
    gen = generador_ids()
    for _ in range(5):
        print(next(gen))
