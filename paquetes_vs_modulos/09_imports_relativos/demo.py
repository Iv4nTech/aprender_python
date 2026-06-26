"""
Importamos el paquete y dejamos que sus imports relativos resuelvan solos.
(Ejecutar 'python proyecto/servicios/facturacion.py' fallaría con
 'attempted relative import with no known parent package'.
"""
from proyecto.servicios import facturacion

print(facturacion.factura(99.9))
