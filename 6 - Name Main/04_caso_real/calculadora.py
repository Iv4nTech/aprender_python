"""
PASO 4 (caso real): así se usa en proyectos de verdad.

Este módulo tiene DOBLE VIDA, y esa es la gracia del if __name__ == "__main__":

  VIDA 1 - Como librería:   programa.py hace 'import calculadora' y usa
                            sus funciones. El bloque del if no se ejecuta.

  VIDA 2 - Como script:     'python calculadora.py' lanza una pequeña demo
                            de autocomprobación que vive dentro del if.

Pruébalo de las dos formas:

    python calculadora.py   -> corre la demo de autocomprobación
    python programa.py      -> usa las funciones, sin demo
"""


def sumar(a, b):
    return a + b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


# ---------------------------------------------------------------------------
# Zona de pruebas/demo: SOLO corre con 'python calculadora.py'.
# Es un truco habitual: cada módulo lleva su propia mini-demo para
# comprobarlo a mano, sin molestar a quien lo importa.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("[calculadora.py] Modo script: ejecutando mi demo de autocomprobación.")
    print(f"[calculadora.py] (mi __name__ vale {__name__!r}, por eso entré al if)")
    print("[calculadora.py] sumar(2, 3)    =", sumar(2, 3))
    print("[calculadora.py] dividir(10, 4) =", dividir(10, 4))
    print("[calculadora.py] Demo terminada. Nada de esto sale al importarme.")
