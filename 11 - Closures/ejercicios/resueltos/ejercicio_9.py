"""
Ejercicio 9 - Caché para una consulta cara  (AVANZADO)
======================================================
CASO REAL: consultar el precio de un producto a un proveedor externo
es LENTO (tarda en responder por la red). Si te piden el mismo
producto dos veces, no quieres volver a preguntar: lo guardas en una
caché. El diccionario de caché vive en la "mochila" del closure, así
que es privado y persiste entre llamadas.

Crea `crear_consultor_precios()` que devuelva una función
`consultar(producto)`. La primera vez "consulta" (simúlalo con un
print y time.sleep) y guarda el resultado; las siguientes lo devuelve
al instante desde la caché.

Pista (fuente: doc oficial de `time`,
https://docs.python.org/es/3/library/time.html): time.sleep(1)

Nota PRO: la librería estándar trae esto hecho con el decorador
@functools.lru_cache (https://docs.python.org/es/3/library/functools.html),
que por dentro es justamente un closure como este.
"""

import time

def crear_consultor_precios():
    cache = {}
    def consultar(producto):
        if producto not in cache:
            time.sleep(5)
            cache[producto] = 20
            return cache[producto]
        else:
            return cache[producto]
    return consultar



# --- Prueba ---
if __name__ == "__main__":
    consultar = crear_consultor_precios()
    print("teclado:", consultar("teclado"))   # lento
    print("teclado:", consultar("teclado"))   # instantáneo (caché)
    print("ratón:  ", consultar("ratón"))     # lento (nuevo)
