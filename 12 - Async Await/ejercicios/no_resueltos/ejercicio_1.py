"""
Ejercicio 1 - Tu primera corrutina  (FÁCIL)
===========================================
CASO REAL: una app de mensajería envía una notificación de bienvenida
cuando alguien se registra. El envío "tarda" un poco (simula la red).

Crea una corrutina `enviar_bienvenida(nombre)` que espere 1 segundo
(simulando la red con asyncio.sleep) y luego devuelva el texto
"Bienvenido/a, <nombre>". Ejecútala con asyncio.run.

Ejemplo de uso:
    print(asyncio.run(enviar_bienvenida("Ivan")))   # Bienvenido/a, Ivan
"""
import asyncio


async def enviar_bienvenida(nombre):
    # Tu código aquí
    pass


# --- Prueba ---
if __name__ == "__main__":
    mensaje = asyncio.run(enviar_bienvenida("Ivan"))
    print(mensaje)
