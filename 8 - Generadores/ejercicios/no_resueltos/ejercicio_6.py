"""
Ejercicio 6 - Paginación de API simulada
==========================================
Simula una API REST paginada con la función `api_simulada(pagina)`
que ya está implementada abajo.

Crea un generador `paginar_api` que llame a la API página a página
y produzca cada ITEM individual (no cada página completa).
Para cuando la respuesta venga vacía.

Ejemplo de uso:
    for item in paginar_api():
        print(item)

Caso real: consumir endpoints paginados de GitHub, Twitter/X, Shopify,
           etc., de forma eficiente sin cargar todas las páginas a la vez.
"""

def api_simulada(pagina: int) -> list[dict]:
    """Simula un endpoint que devuelve 3 items por página (5 páginas en total)."""
    datos = [{"id": i, "valor": i * 2} for i in range(1, 16)]
    inicio = (pagina - 1) * 3
    return datos[inicio:inicio + 3]


# Tu código aquí: generador `paginar_api`


# --- Prueba ---
if __name__ == "__main__":
    for item in paginar_api():
        print(item)
