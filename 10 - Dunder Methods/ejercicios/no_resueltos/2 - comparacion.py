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

# Tu código aquí


# --- EJECUCIÓN (imprime aquí a mano) ---
