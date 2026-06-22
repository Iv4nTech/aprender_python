"""
================================================================
 DUNDER METHODS · ITERACIÓN  (__iter__, __next__)
================================================================
Cuenta atrás de un lanzamiento. Quieres recorrer la cuenta con un
bucle for, desde el número inicial hasta 1.

1- Crea CuentaAtras(inicio). Define __iter__ y __next__ para que
   genere los números desde 'inicio' hasta 1 (incluido) y luego
   pare lanzando StopIteration.
   (Solución list(CuentaAtras(5)):       [5, 4, 3, 2, 1])
   (Solución for n in CuentaAtras(3):    3 2 1)
================================================================
"""

class CuentaAtras():
   def __init__(self, inicio):
      self.inicio = inicio

   def __iter__(self):
      self.actual = self.inicio
      return self
   
   def __next__(self):
      if self.actual < 1:
         raise StopIteration
      numero = self.actual
      self.actual -= 1
      return numero

print(list(CuentaAtras(20)))
for n in CuentaAtras(100):
   print(n)
