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
    await asyncio.sleep(1)
    return (aerolinea, precio)


async def comparar():
    resultados = await asyncio.gather(
        consultar_precio("Aerolínea A", 200),
        consultar_precio("Aerolínea B", 150),
        consultar_precio("Aerolínea C", 180)
    )
    mas_barata = min(resultados, key=lambda x: x[1])
    print(f"La aerolínea más barata es: {mas_barata[0]} con un precio de {mas_barata[1]}")


# --- Prueba ---
if __name__ == "__main__":
    asyncio.run(comparar())
