"""
Ejercicio 2 - Encadenar esperas con await  (FÁCIL)
==================================================
CASO REAL: para publicar un post primero SUBES la imagen y, cuando
termina, PUBLICAS el texto. Son dos pasos que ocurren en orden, cada
uno con su espera.

Crea dos corrutinas:
  · subir_imagen()  → espera 1s y devuelve "imagen subida"
  · publicar_texto() → espera 1s y devuelve "post publicado"
Y una corrutina `publicar_post()` que haga await de las dos EN ORDEN
e imprima cada resultado.

Ejemplo de uso:
    asyncio.run(publicar_post())
"""
import asyncio


async def subir_imagen():
    # Tu código aquí
    pass


async def publicar_texto():
    # Tu código aquí
    pass


async def publicar_post():
    # Tu código aquí
    pass


# --- Prueba ---
if __name__ == "__main__":
    asyncio.run(publicar_post())
