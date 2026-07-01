"""
Ejercicio 4 - El "efecto wow": secuencial vs concurrente  (MEDIO)
=================================================================
CASO REAL: tu script descarga 5 informes de un servidor. Cada
descarga tarda ~1s. Vas a MEDIR con un cronómetro la diferencia
entre hacerlas una a una y hacerlas todas a la vez.

Crea `descargar(n)` que espere 1s y devuelva f"informe_{n}".
Luego dos funciones que descarguen los informes 1..5:
  · secuencial() → con un bucle y await uno a uno
  · concurrente() → todas a la vez con gather
Mide e imprime cuánto tarda cada una con time.perf_counter().

Ejemplo de uso:
    asyncio.run(main())
"""
import asyncio
import time


async def descargar(n):
    # Tu código aquí
    pass


async def secuencial():
    # Tu código aquí (bucle con await uno a uno)
    pass


async def concurrente():
    # Tu código aquí (todas a la vez con gather)
    pass


async def main():
    t0 = time.perf_counter()
    await secuencial()
    print(f"  ✗ Secuencial:  {time.perf_counter() - t0:.2f}s")

    t0 = time.perf_counter()
    await concurrente()
    print(f"  ✓ Concurrente: {time.perf_counter() - t0:.2f}s")


# --- Prueba ---
if __name__ == "__main__":
    asyncio.run(main())
