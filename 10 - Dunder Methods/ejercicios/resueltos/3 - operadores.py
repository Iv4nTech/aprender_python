"""
================================================================
 DUNDER METHODS · OPERADORES  (__add__, __mul__)
================================================================
Editor de gráficos 2D. Representas posiciones y desplazamientos
como vectores y quieres combinarlos con + y escalarlos con *.

1- Crea Vector2D(x, y) y define __add__ para sumar dos vectores
   componente a componente. Añade __repr__ para poder verlo.
   (Solución Vector2D(1,2) + Vector2D(3,4):  Vector2D(4, 6))

2- Define __mul__ para multiplicar el vector por un número (escalar)
   y escalar ambas componentes.
   (Solución Vector2D(2,3) * 3:  Vector2D(6, 9))
================================================================
"""

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
      
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __mul__(self, other):
        return Vector2D(self.x * other, self.y * other)
    




    
print(Vector2D(4, 5) + Vector2D(4,3))
print(Vector2D(4, 5) * 10)


