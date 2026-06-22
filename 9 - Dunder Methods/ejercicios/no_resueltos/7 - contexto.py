"""
================================================================
 DUNDER METHODS · CONTEXTO  (__enter__, __exit__)
================================================================
Quieres medir cuánto tarda un bloque de código. Necesitas un
cronómetro que se use con 'with' y que al salir imprima solo el
tiempo transcurrido.

1- Crea Cronometro(). Define __enter__ (guarda el tiempo de inicio
   con time.perf_counter() y devuelve self) y __exit__ (calcula la
   duración e imprime "Tardó: X.XXXs"). Úsalo con un 'with' que
   haga un bucle grande, por ejemplo sumar de 0 a 1.000.000.
   (Solución: imprime algo parecido a  ->  Tardó: 0.012s)
================================================================
"""

# Tu código aquí


# --- EJECUCIÓN (imprime aquí a mano) ---
