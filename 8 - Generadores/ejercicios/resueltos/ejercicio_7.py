"""
Ejercicio 7 - Generador con send(): control de flujo
======================================================
Crea un generador `acumulador` que:
- Reciba valores con send() y los vaya sumando.
- Produzca (yield) el total acumulado hasta ese momento.
- Cuando reciba None, reinicie el acumulador a 0.

Ejemplo de uso:
    gen = acumulador()
    next(gen)          # Arranca el generador (primer yield)
    print(gen.send(5))   # 5
    print(gen.send(3))   # 8
    print(gen.send(None))  # 0  (reset)
    print(gen.send(10))  # 10

Caso real: acumular métricas en streaming (bytes transferidos,
           eventos por ventana de tiempo) con posibilidad de reset.
"""

# Tu código aquí
def acumulador():
    total = 0
    while True:
        valor = yield total
        if valor is None:
            total = 0
        else:
            total += valor

# --- Prueba ---
if __name__ == "__main__":
    gen = acumulador()
    next(gen)
    print(gen.send(5))    # 5
    print(gen.send(3))    # 8
    print(gen.send(None)) # 0
    print(gen.send(10))   # 10
    print(gen.send(2))    # 12
