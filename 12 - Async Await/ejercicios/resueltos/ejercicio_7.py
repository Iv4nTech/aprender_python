"""
Ejercicio 7 - Manejar errores sin que se caiga todo  (MEDIO)
============================================================
CASO REAL: procesas 4 pagos a la vez. Uno de ellos falla (tarjeta
rechazada), pero NO quieres que ese fallo tumbe los otros tres. Con
gather(..., return_exceptions=True) recoges tanto los éxitos como los
errores y decides qué hacer con cada uno.

Crea `cobrar(cliente, ok)` que espere 1s y:
  · si ok es True  → devuelva f"{cliente}: cobrado"
  · si ok es False → lance ValueError(f"{cliente}: tarjeta rechazada")
Luego `procesar_pagos()` que cobre a 4 clientes (uno falla) con
gather y return_exceptions=True, y separe éxitos de errores.

Ejemplo de uso:
    asyncio.run(procesar_pagos())
"""
import asyncio


async def cobrar(cliente, ok):
    await asyncio.sleep(1)
    if ok:
        return f"{cliente}: cobrado"
    else:
        raise ValueError(f"{cliente}: tarjeta rechazada")


async def procesar_pagos():
    clientes = [
        ("Cliente A", True),
        ("Cliente B", False),  # Este fallará
        ("Cliente C", True),
        ("Cliente D", True)
    ]

    resultados = await asyncio.gather(
        *(cobrar(cliente, ok) for cliente, ok in clientes),
        return_exceptions=True
    )

    exitos = [res for res in resultados if not isinstance(res, Exception)]
    errores = [res for res in resultados if isinstance(res, Exception)]

    print("Éxitos:")
    for exito in exitos:
        print(f"  {exito}")

    print("Errores:")
    for error in errores:
        print(f"  {error}")


# --- Prueba ---
if __name__ == "__main__":
    asyncio.run(procesar_pagos())
