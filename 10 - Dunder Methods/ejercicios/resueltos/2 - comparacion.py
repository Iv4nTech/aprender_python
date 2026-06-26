"""
================================================================
 DUNDER METHODS · COMPARACIÓN  (__eq__, __lt__, __hash__)
================================================================
Gestor de versiones de software. Necesitas comparar versiones
para saber cuál es más reciente y poder ordenarlas.

1- Crea la clase Version(mayor, menor). Define __eq__ y __lt__
   comparando primero 'mayor' y, si empata, 'menor'.
   (Solución Version(1,2) < Version(1,5):  True)
   (Solución Version(2,0) < Version(1,9):  False)

2- Ordena de menor a mayor [Version(1,5), Version(1,2), Version(2,0)]
   e imprime cada una como (v.mayor, v.menor).
   (Solución:  [(1, 2), (1, 5), (2, 0)])

3- Define __hash__ basado en la tupla (mayor, menor) y mete en un
   set dos versiones iguales para comprobar que se elimina el duplicado.
   (Solución len del set con dos iguales:  1)
================================================================
"""

class Version():
    
   def __init__(self, mayor, menor):
      self.mayor = mayor
      self.menor = menor

   def __eq__(self, other):
      return self.mayor == other.mayor and self.menor == other.menor
   
   def __lt__(self, other):
      if self.mayor < other.mayor:
         return True
      if self.mayor == other.mayor:
         if self.menor < other.menor:
            return True
      return False
   
   def __repr__(self):
      return f"({self.mayor}, {self.menor})"
   
   def __hash__(self):
      return hash((self.mayor, self.menor))

print(Version(1,2) < Version(1,5))
print(Version(2,0) < Version(1,9))
versiones_ordenadas = sorted([Version(1,5), Version(1,2), Version(2,0)])
print(versiones_ordenadas)
lista_versiones = [Version(3,5), Version(3,5)]
print(set(lista_versiones))