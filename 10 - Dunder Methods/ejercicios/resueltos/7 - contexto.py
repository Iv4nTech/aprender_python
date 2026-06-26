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

from time import perf_counter

class Cronometro():
    
    def __enter__(self):
        self.inicio = perf_counter()
        return self
    
    def __exit__(self, exc_type, exc, tb):
        tiempo = perf_counter() - self.inicio
        print(f'Tardó: {tiempo:.3f}s')


c1 = Cronometro()

with Cronometro() as t:
    sum(range(1, 100_000_000))
