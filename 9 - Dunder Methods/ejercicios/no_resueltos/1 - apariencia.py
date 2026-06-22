"""
================================================================
 DUNDER METHODS · APARIENCIA  (__str__, __repr__, __format__)
================================================================
Tienda online. Necesitas controlar cómo se muestra un producto
en cada contexto: al cliente, en los logs y en una factura.

1- Crea la clase Producto(nombre, precio). Define __str__ para el
   cliente con el formato "nombre - precio€" y __repr__ para los
   logs con el formato "Producto('nombre', precio)".
   (Solución str(producto):   Camiseta - 19.99€)
   (Solución repr(producto):  Producto('Camiseta', 19.99))

2- Añade __format__ para que acepte el spec "iva": debe devolver
   el precio con el 21% de IVA, 2 decimales y "€". Sin spec, igual
   que __str__.
   (Solución f"{producto:iva}":  24.19€)
================================================================
"""

# Tu código aquí


# --- EJECUCIÓN (imprime aquí a mano) ---
