"""
================================================================
 DUNDER METHODS · INVOCABLES Y VERDAD  (__call__, __bool__)
================================================================
Sistema de precios de una tienda. Quieres "calculadoras"
reutilizables que se usen como funciones y un carrito que sepa
por sí mismo si está vacío.

1- Crea Impuesto(tasa). Define __call__ para que al llamar al
   objeto con un precio le aplique la tasa.  Ej: iva = Impuesto(0.21)
   (Solución iva(100):  121.0)

2- Crea Carrito() con una lista interna 'productos'. Define __bool__
   para que el carrito sea True solo si contiene productos.
   (Solución bool(carrito vacío):           False)
   (Solución bool(carrito con 1 producto):  True)
================================================================
"""

class CrearImpuesto():
    def __init__(self, tasa):
        self.tasa = tasa

    def __call__(self, precio ,*args, **kwds):
        return precio * (1 + self.tasa)

class Carrito():
    def __init__(self):
        self.lista = []
     
    def __bool__(self):
      if self.lista:
          return True
      return False

iva = CrearImpuesto(0.21)
print(iva(200))

c1 = Carrito()
c1.lista.extend(['Macarrones', 'Pizza', 'Hamburguesa', 'Pan'])
print(c1.lista)
if c1:
   print(True)
else:
    print(False)

c2 = Carrito()
if c2:
   print(True)
else:
    print(False)