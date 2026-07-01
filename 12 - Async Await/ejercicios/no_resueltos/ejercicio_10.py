"""
Ejercicio 10 - Pool de workers con Queue y async context manager  (EXPERTO)
===========================================================================
CASO REAL: un sistema procesa una cola de pedidos. Tienes una COLA de
trabajo y varios TRABAJADORES (workers) que van cogiendo pedidos de la
cola a la vez. Además, cada worker abre una "conexión" a la base de
datos usando un CONTEXT MANAGER ASÍNCRONO (async with), que garantiza
que la conexión se cierra pase lo que pase.

Junta tres piezas que ya conoces:
  · asyncio.Queue        → la cola de pedidos
  · varios create_task   → los workers procesando a la vez
  · __aenter__/__aexit__ → un context manager async para la conexión
    (es tu tema de Context Managers, pero con 'async with')

Se pide:
  1. Clase `ConexionBD` con __aenter__ (espera 0.1s y "abre") y
     __aexit__ (espera 0.1s y "cierra"). Debe poder usarse con async with.
  2. `worker(nombre, cola)`: mientras haya trabajo, saca un pedido de
     la cola, lo procesa dentro de `async with ConexionBD()` (0.3s) y
     marca la tarea como hecha con cola.task_done().
  3. `main()`: mete 6 pedidos en la cola, lanza 3 workers con
     create_task, espera a que la cola se vacíe con `await cola.join()`
     y luego cancela los workers.

Ejemplo de uso:
    asyncio.run(main())
"""
import asyncio


class ConexionBD:
    """Context manager asíncrono: se usa con 'async with'."""
    async def __aenter__(self):
        # Tu código aquí (espera 0.1s y devuelve self)
        pass

    async def __aexit__(self, exc_type, exc, tb):
        # Tu código aquí (espera 0.1s; devuelve False)
        pass


async def worker(nombre, cola):
    # Tu código aquí (bucle: get de la cola, async with ConexionBD(), task_done)
    pass


async def main():
    # Tu código aquí (llena la cola, lanza 3 workers, cola.join(), cancela workers)
    pass


# --- Prueba ---
if __name__ == "__main__":
    asyncio.run(main())
