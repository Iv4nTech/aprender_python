"""
Ejercicio 3 - Validador de contraseñas configurable  (FÁCIL)
============================================================
CASO REAL: distintos formularios exigen contraseñas de distinta
longitud mínima (un foro pide 6, un banco pide 12). Fabrica un
validador reutilizable para cada caso.

Crea `crear_validador(min_longitud)` que devuelva una función que
reciba una contraseña y devuelva True/False según cumpla el mínimo.

Ejemplo de uso:
    validar_banco = crear_validador(12)
    print(validar_banco("1234"))             # False
    print(validar_banco("contraseña_larga")) # True
"""

def crear_validador(min_longitud):
    # Tu código aquí
    pass


# --- Prueba ---
if __name__ == "__main__":
    validar_foro = crear_validador(6)
    validar_banco = crear_validador(12)
    print(f"Foro  '12345':         {validar_foro('12345')}")
    print(f"Foro  'gatito':        {validar_foro('gatito')}")
    print(f"Banco 'gatito':        {validar_banco('gatito')}")
    print(f"Banco 'SuperClave123': {validar_banco('SuperClave123')}")
