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
    for i in range(total):
        await asyncio.sleep(0.3)
        yield f"dato_{i}"


async def main():
    async for dato in leer_paginas(10):
        print(dato)


# --- Prueba ---
if __name__ == "__main__":
    asyncio.run(main())
