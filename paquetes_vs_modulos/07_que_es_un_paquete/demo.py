"""
CASO REAL: una tienda organizada en paquete + subpaquete.
Estructura:
    tienda/                 (paquete)
        __init__.py
        productos.py        (módulo)
        carrito.py          (módulo)
        pagos/              (SUBpaquete)
            __init__.py
            tarjeta.py      (módulo)

Se importa con notación de puntos:  tienda.pagos.tarjeta
"""
from tienda import carrito
from tienda.pagos import tarjeta

compra = ["camiseta", "taza", "camiseta"]
importe = carrito.total(compra)

print("Total del carrito:", importe, "€")
print(tarjeta.cobrar(importe))
