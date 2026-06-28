"""
Ejercicio 2 - Conversor de divisas  (FÁCIL)
===========================================
CASO REAL: una app de viajes muestra precios en distintas monedas.
Cada moneda tiene su tasa de cambio respecto al euro. Quieres una
función "conversora" lista para cada moneda.

Crea `crear_conversor(tasa)` que devuelva una función que convierta
una cantidad en euros a esa moneda.

Ejemplo de uso:
    a_dolares = crear_conversor(1.08)
    print(a_dolares(100))   # 108.0
"""

def crear_conversor(tasa):
    def transformar(dinero):
        return dinero * tasa
    return transformar


# --- Prueba ---
if __name__ == "__main__":
    a_dolares = crear_conversor(1.08)
    a_libras = crear_conversor(0.85)
    print(f"50€ en dólares: {a_dolares(50)}$")
    print(f"50€ en libras:  {a_libras(50)}£")
