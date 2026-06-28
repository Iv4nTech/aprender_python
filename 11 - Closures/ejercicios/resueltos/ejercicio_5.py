"""
Ejercicio 5 - Carrito de la compra  (MEDIO)
===========================================
CASO REAL: en una tienda online, según el usuario va añadiendo
productos al carrito, el total se va actualizando. Quieres una
función "carrito" que recuerde el total acumulado.

Crea `crear_carrito()` que devuelva una función. Esa función recibe
el precio de un producto, lo añade al total y devuelve el total
actualizado.

Ejemplo de uso:
    anadir = crear_carrito()
    print(anadir(19.99))  # 19.99
    print(anadir(5.50))   # 25.49
"""

def crear_carrito():
    total = 0
    def anadir(precio):
        nonlocal total
        total += precio
        return total
    return anadir

# --- Prueba ---
if __name__ == "__main__":
    anadir = crear_carrito()
    print(f"Camiseta:   total {anadir(19.99)}€")
    print(f"Calcetines: total {anadir(5.50)}€")
    print(f"Gorra:      total {anadir(12.00)}€")
