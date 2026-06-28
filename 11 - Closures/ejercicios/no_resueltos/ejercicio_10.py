"""
Ejercicio 10 - Cuenta bancaria sin clases  (EXPERTO)
====================================================
CASO REAL: quieres una cuenta bancaria con un saldo PRIVADO: nadie
debería poder cambiar el saldo "a mano", solo a través de operaciones
controladas (ingresar, retirar, consultar). Con clases usarías
atributos; aquí lo harás SOLO con closures: el saldo vive en la
mochila y es inaccesible desde fuera.

Idea: devuelve varias funciones que COMPARTEN la misma variable
`saldo` del ámbito exterior. Esto demuestra que un closure puede
encapsular estado igual que un objeto.
(Fuente del concepto de encapsulación con nonlocal: tutorial oficial
de ámbitos, https://docs.python.org/es/3/tutorial/classes.html)

Crea `crear_cuenta(saldo_inicial)` que devuelva un diccionario con
tres funciones: "ingresar", "retirar" y "saldo".

Ejemplo de uso:
    cuenta = crear_cuenta(100)
    cuenta["ingresar"](50)     # saldo 150
    cuenta["retirar"](30)      # saldo 120
    print(cuenta["saldo"]())   # 120
"""

def crear_cuenta(saldo_inicial):
    # Tu código aquí
    pass


# --- Prueba ---
if __name__ == "__main__":
    cuenta = crear_cuenta(100)
    print(cuenta["ingresar"](50))
    print(cuenta["retirar"](30))
    print(cuenta["retirar"](1000))      # fondos insuficientes
    print(f"Saldo final: {cuenta['saldo']()}€")
