"""
Ejercicio 5 - Tareas en segundo plano con create_task  (MEDIO)
==============================================================
CASO REAL: al confirmar un pedido quieres, EN SEGUNDO PLANO, enviar
el email de confirmación y actualizar el stock, sin bloquear la
respuesta al cliente. Arrancas las dos tareas ya y sigues.

Crea:
  · enviar_email(pedido)     → espera 1s, devuelve "email de <pedido>"
  · actualizar_stock(pedido) → espera 2s, devuelve "stock de <pedido>"
Y `confirmar(pedido)` que lance las dos con asyncio.create_task,
imprima "pedido confirmado" INMEDIATAMENTE y, al final, recoja los
resultados de ambas tasks con await.

Ejemplo de uso:
    asyncio.run(confirmar("#A123"))
"""
import asyncio


async def enviar_email(pedido):
    await asyncio.sleep(1)
    return f"email de {pedido}"


async def actualizar_stock(pedido):
    await asyncio.sleep(2)
    return f"stock de {pedido}"


async def confirmar(pedido):
    task_email = asyncio.create_task(enviar_email(pedido))
    task_stock = asyncio.create_task(actualizar_stock(pedido))

    print("pedido confirmado")

    resultado_email = await task_email
    resultado_stock = await task_stock

    print(resultado_email)
    print(resultado_stock)


# --- Prueba ---
if __name__ == "__main__":
    asyncio.run(confirmar("#A123"))
