"""
Ejercicio 3 - Varias tareas a la vez con gather  (FÁCIL)
========================================================
CASO REAL: un comparador de vuelos consulta el precio en 3 aerolíneas
distintas. Cada consulta tarda ~1s. Si las haces una a una son 3s;
lanzándolas a la vez con gather, ~1s.

Crea `consultar_precio(aerolinea, precio)` que espere 1s y devuelva
una tupla (aerolinea, precio). Luego `comparar()` que consulte las
tres A LA VEZ con asyncio.gather y muestre la más barata.

Ejemplo de uso:
    asyncio.run(comparar())
"""
import asyncio


async def consultar_precio(aerolinea, precio):
    # Tu código aquí
    pass


async def comparar():
    # Tu código aquí (usa asyncio.gather con las 3 consultas)
    pass


# --- Prueba ---
if __name__ == "__main__":
    asyncio.run(comparar())
