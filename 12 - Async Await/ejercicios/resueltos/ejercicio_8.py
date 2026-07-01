"""
Ejercicio 8 - Limitar la concurrencia con Semaphore  (AVANZADO)
===============================================================
CASO REAL: tienes que descargar 10 archivos, pero el servidor te
banea si haces más de 3 peticiones a la vez. Un asyncio.Semaphore(3)
actúa como 3 "permisos": solo 3 tareas entran al mismo tiempo, las
demás esperan su turno.

Crea `descargar(n, sem)` que:
  · pida el permiso con `async with sem:`
  · espere 1s (la descarga) y devuelva f"archivo_{n}"
Luego `main()` que descargue los archivos 1..10 compartiendo un
Semaphore(3) y los recoja con gather. Deberían tardar ~4s (10/3
tandas), no ~1s.

Ejemplo de uso:
    asyncio.run(main())
"""
import asyncio
import time


async def descargar(n, sem):
    async with sem:
        await asyncio.sleep(1)
        return f"archivo_{n}"


async def main():
    sem = asyncio.Semaphore(3)         # máximo 3 simultáneas
    t0 = time.perf_counter()
    resultados = await asyncio.gather(
        *(descargar(n, sem) for n in range(1, 11))
    )
    print(f"  → {len(resultados)} archivos en {time.perf_counter() - t0:.2f}s")
    print(f"  → {resultados}")


# --- Prueba ---
if __name__ == "__main__":
    asyncio.run(main())
