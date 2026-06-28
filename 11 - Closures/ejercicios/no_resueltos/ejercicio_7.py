"""
Ejercicio 7 - Logger con prefijo por módulo  (MEDIO-AVANZADO)
============================================================
CASO REAL: en una aplicación grande quieres que cada parte (PAGOS,
ENVÍOS, LOGIN) escriba sus mensajes con su propia etiqueta y la hora,
sin repetir esa lógica. Fabricas un "logger" configurado por módulo.

Crea `crear_logger(modulo)` que devuelva una función `log(mensaje)`
que imprima:  [HH:MM:SS] [MODULO] mensaje

Pista para la hora (fuente: doc oficial de `datetime`,
https://docs.python.org/es/3/library/datetime.html):
    from datetime import datetime
    datetime.now().strftime("%H:%M:%S")

Ejemplo de salida:
    [12:30:01] [PAGOS] Cobro realizado
"""

def crear_logger(modulo):
    # Tu código aquí
    pass


# --- Prueba ---
if __name__ == "__main__":
    log_pagos = crear_logger("PAGOS")
    log_envios = crear_logger("ENVÍOS")
    log_pagos("Cobro de 49.99€ realizado")
    log_envios("Paquete entregado en Madrid")
