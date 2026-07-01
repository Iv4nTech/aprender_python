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
    await asyncio.sleep(1)
    return "imagen subida"


async def publicar_texto():
    await asyncio.sleep(1)
    return "post publicado"


async def publicar_post():
    resultado_imagen = await subir_imagen()
    print(resultado_imagen)
    resultado_texto = await publicar_texto()
    print(resultado_texto)


# --- Prueba ---
if __name__ == "__main__":
    asyncio.run(publicar_post())
