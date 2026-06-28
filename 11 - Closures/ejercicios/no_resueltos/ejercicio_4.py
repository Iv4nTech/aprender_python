"""
Ejercicio 4 - Contador de "me gusta"  (MEDIO)
=============================================
CASO REAL: en una red social, cada publicación tiene su propio
contador de "me gusta". Cada vez que alguien pulsa el botón, sube 1
y se muestra el total. Cada publicación debe llevar su cuenta
independiente.

Crea `crear_boton_like()` que devuelva una función. Cada llamada
suma un like y devuelve el total. (Pista: necesitas `nonlocal`).

Ejemplo de uso:
    like = crear_boton_like()
    print(like())  # 1
    print(like())  # 2
"""

def crear_boton_like():
    # Tu código aquí
    pass


# --- Prueba ---
if __name__ == "__main__":
    post_gatos = crear_boton_like()
    post_viaje = crear_boton_like()
    print(f"Post gatos: {post_gatos()} likes")
    print(f"Post gatos: {post_gatos()} likes")
    print(f"Post viaje: {post_viaje()} likes")   # cuenta aparte
    print(f"Post gatos: {post_gatos()} likes")
