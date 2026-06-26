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

class Producto():

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'{self.nombre} - {self.precio}€'

    def __repr__(self):
        return f'Producto({self.nombre !r}, {self.precio})'

    def __format__(self, format_spec):
        if format_spec == "iva":
            return f"{self.precio * 1.21:.2f}€"
        return self.__str__()

print(Producto("Raqueta Padel", 80))
print(repr(Producto("Raqueta Padel", 80)))
print(f"{Producto("Raqueta Padel", 80):iva}")
print(f"{Producto("Raqueta Padel", 80):hola}")