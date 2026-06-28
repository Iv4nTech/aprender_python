"""
Ejercicio 8 - Botones de una interfaz (el bug del late binding)  (AVANZADO)
==========================================================================
CASO REAL: estás montando un menú con 3 botones. En un bucle creas
para cada botón una función "callback" que debería avisar de QUÉ
botón se pulsó. Pero te llevas una sorpresa: ¡todos dicen lo mismo!

Esto pasa porque todos los closures comparten la misma variable del
bucle y acaban viendo su ÚLTIMO valor.
(Fuente: FAQ oficial de Python, "Why do lambdas defined in a loop
with different values all return the same result?",
https://docs.python.org/3/faq/programming.html)

Tu tarea:
    1. Reproduce el comportamiento incorrecto (callbacks_mal).
    2. Arréglalo capturando el valor con un argumento por defecto
       (callbacks_bien), de forma que diga Inicio, Perfil, Ajustes.
"""

botones = ["Inicio", "Perfil", "Ajustes"]

# Tu código aquí
# 1) VERSIÓN CON BUG:
callbacks_mal = []

# 2) VERSIÓN CORRECTA:
callbacks_bien = []


# --- Prueba ---
if __name__ == "__main__":
    print("Con bug:")
    for cb in callbacks_mal:
        print(f"  {cb()}")

    print("Corregido:")
    for cb in callbacks_bien:
        print(f"  {cb()}")
