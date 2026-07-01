"""
Ejercicio 9 - Streams de datos con async generators  (AVANZADO)
===============================================================
CASO REAL: una API devuelve resultados PAGINADOS (de 3 en 3). En vez
de esperar a tenerlos todos, quieres ir procesándolos según llegan.
Un GENERADOR ASÍNCRONO (async def + yield) produce valores poco a
poco, y se consume con `async for`.

Crea `leer_paginas(total)` como async generator que, por cada
elemento de 0..total-1, espere 0.3s (llegada del dato) y haga yield
de f"dato_{i}". Luego `main()` que lo recorra con `async for` e
imprima cada dato en cuanto llega.

Ejemplo de uso:
    asyncio.run(main())
"""
import asyncio


async def leer_paginas(total):
    # Tu código aquí (bucle con await asyncio.sleep(0.3) y yield)
    pass


async def main():
    # Tu código aquí (recorre leer_paginas(5) con async for)
    pass


# --- Prueba ---
if __name__ == "__main__":
    asyncio.run(main())
