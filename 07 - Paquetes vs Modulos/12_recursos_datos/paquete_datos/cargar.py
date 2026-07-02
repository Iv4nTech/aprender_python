"""
CONCEPTO 12 (AVANZADO) · Leer DATOS empaquetados con importlib.resources
Un paquete no solo tiene código: puede llevar ficheros de datos (json, csv,
plantillas...). Para leerlos de forma CORRECTA no se usa una ruta a mano
(open("ciudades.json") se rompe según desde dónde ejecutes), sino
importlib.resources, que los localiza dentro del paquete pase lo que pase.

CASO REAL: una librería que trae datos de configuración, plantillas o
diccionarios y debe encontrarlos aunque se instale en otra máquina... o
aunque viaje DENTRO de un .zip (ver demo_zip.py).
"""
import os
import json
from importlib.resources import files


def capitales_con_files():
    """Forma MODERNA y robusta. Funciona en carpeta Y dentro de un .zip."""
    recurso = files("paquete_datos").joinpath("ciudades.json")
    return json.loads(recurso.read_text(encoding="utf-8"))


def capitales_con_file():
    """Forma ANTIGUA con __file__. Se ROMPE si el paquete está en un .zip,
    porque open() no sabe abrir algo que no es un fichero real del disco."""
    carpeta = os.path.dirname(__file__)
    ruta = os.path.join(carpeta, "ciudades.json")
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)
