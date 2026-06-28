"""
Ejercicio 1 - Descuentos de una tienda  (FÁCIL)
===============================================
CASO REAL: en una tienda online tienes varias campañas de descuento
(Black Friday -30%, Rebajas -50%, Empleados -10%). En vez de repetir
la fórmula del descuento por todas partes, fabrica una función por
cada campaña.

Crea `crear_descuento(porcentaje)` que devuelva una función capaz de
aplicar ese descuento a cualquier precio.

Ejemplo de uso:
    black_friday = crear_descuento(30)
    print(black_friday(100))   # 70.0
"""

def crear_descuento(porcentaje):
    def obtener_precio(precio):
        return precio - (precio * porcentaje/100)
    return obtener_precio


# --- Prueba ---
if __name__ == "__main__":
    black_friday = crear_descuento(30)
    rebajas = crear_descuento(50)
    print(f"Black Friday (camiseta 20€): {black_friday(20)}€")
    print(f"Rebajas (abrigo 100€):       {rebajas(100)}€")
