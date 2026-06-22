"""
================================================================
 DUNDER METHODS · CREACIÓN  (__new__, __init__)
================================================================
Configuración global de una app. Por mucho que la instancies en
distintos sitios del código, debe existir UNA sola instancia
compartida (patrón Singleton).

1- Crea Configuracion(). Usa __new__ para que siempre se devuelva
   la misma instancia (guárdala en un atributo de clase _instancia).
   (Solución Configuracion() is Configuracion():  True)

2- Demuestra que ambas variables comparten estado: asigna un
   atributo en una y léelo desde la otra.
   (Solución a.modo = 'oscuro'; luego b.modo  ->  'oscuro')
================================================================
"""

# Tu código aquí


# --- EJECUCIÓN (imprime aquí a mano) ---
