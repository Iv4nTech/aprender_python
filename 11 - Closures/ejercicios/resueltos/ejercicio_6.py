"""
Ejercicio 6 - Generador de IDs únicos  (MEDIO)
==============================================
CASO REAL: cuando guardas registros en una base de datos (pedidos,
usuarios, facturas), cada uno necesita un ID único y correlativo:
PED-1, PED-2, PED-3... El sistema debe recordar por dónde iba.

Crea `crear_generador_id(prefijo)` que devuelva una función. Cada
llamada devuelve el siguiente ID con ese prefijo.

Ejemplo de uso:
    nuevo_pedido = crear_generador_id("PED")
    print(nuevo_pedido())  # PED-1
    print(nuevo_pedido())  # PED-2
"""

def crear_generador_id(prefijo):
    contador = 0
    def generar():
        nonlocal contador
        contador += 1
        return f"{prefijo}-{contador}"
    return generar

# --- Prueba ---
if __name__ == "__main__":
    nuevo_pedido = crear_generador_id("PED")
    nueva_factura = crear_generador_id("FAC")
    print(nuevo_pedido())   # PED-1
    print(nuevo_pedido())   # PED-2
    print(nueva_factura())  # FAC-1  (su propia secuencia)
    print(nuevo_pedido())   # PED-3
