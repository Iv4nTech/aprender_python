"""
Ejercicio 9 - Ventana deslizante (sliding window)
===================================================
Crea un generador `ventana_deslizante` que reciba un iterable
y un tamaño `n`, y produzca tuplas de `n` elementos consecutivos.

Ejemplo de uso:
    datos = [1, 2, 3, 4, 5]
    print(list(ventana_deslizante(datos, 3)))
    # [(1,2,3), (2,3,4), (3,4,5)]

Restricción: no conviertas el iterable entero a lista.
Usa collections.deque para mantener solo `n` elementos en memoria.

Caso real: calcular medias móviles de precios de acciones, detectar
           anomalías en series temporales, análisis de logs por ventana
           de tiempo.
"""

from collections import deque

# Tu código aquí


# --- Prueba ---
if __name__ == "__main__":
    precios = [100, 102, 101, 105, 110, 108, 107]
    ventanas = list(ventana_deslizante(precios, 3))
    print(ventanas)

    # Media móvil de 3 días
    for ventana in ventana_deslizante(precios, 3):
        print(f"Ventana {ventana} → media: {sum(ventana)/len(ventana):.2f}")
