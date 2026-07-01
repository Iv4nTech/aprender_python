"""
Ejercicio 6 - Cortar por tiempo con timeout  (MEDIO)
====================================================
CASO REAL: consultas una API del tiempo, pero no quieres que tu app
se quede colgada si el servidor va lento. Le das un máximo de 2
segundos; si no responde, usas un valor por defecto.

Crea `consultar_tiempo(ciudad, tarda)` que espere `tarda` segundos y
devuelva f"{ciudad}: soleado". Luego `tiempo_con_limite(ciudad, tarda)`
que la llame dentro de `async with asyncio.timeout(2)` y, si salta
TimeoutError, devuelva f"{ciudad}: sin datos (timeout)".

Ejemplo de uso:
    print(asyncio.run(tiempo_con_limite("Madrid", 1)))   # responde
    print(asyncio.run(tiempo_con_limite("Oslo", 5)))     # timeout
"""
import asyncio


async def consultar_tiempo(ciudad, tarda):
    # Tu código aquí
    pass


async def tiempo_con_limite(ciudad, tarda):
    # Tu código aquí (usa async with asyncio.timeout(2) y captura TimeoutError)
    pass


# --- Prueba ---
if __name__ == "__main__":
    print(asyncio.run(tiempo_con_limite("Madrid", 1)))
    print(asyncio.run(tiempo_con_limite("Oslo", 5)))
