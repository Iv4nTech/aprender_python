"""
Leemos un fichero de datos que viaja DENTRO del paquete, sin rutas frágiles.
"""
from paquete_datos.cargar import capitales_con_file

for pais, capital in capitales_con_file().items():
    print(f"{pais} -> {capital}")
