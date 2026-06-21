"""
PASO 3 (la solución): el mismo app.py de antes, importando al módulo protegido.

Ejecuta:

    python app.py

Compara la salida con la de 02_el_problema/app.py:
ahora entre las rayas del import solo aparece UN print de saludos.py
(el que dejamos suelto a propósito para enseñar su __name__).
Las pruebas internas de saludos.py ya NO se cuelan, porque están
dentro de su if __name__ == "__main__" y al importarlo da False.
"""

print("[app.py] Soy app.py y me has ejecutado directamente.")
print(f"[app.py] Por eso MI __name__ vale: {__name__!r}")
print("[app.py] Hago 'import saludos' (versión CON candado):")
print("[app.py] ------------- empieza el import -------------")

import saludos  # Python sigue ejecutando saludos.py entero, PERO el bloque
                # del if __name__ == "__main__" da False y se lo salta.

print("[app.py] ------------- termina el import -------------")
print("[app.py] Limpio: solo se cargó la función, sin ejecutar las pruebas.")
print()
print("[app.py] Ahora llamo YO a la función, cuando yo quiero:")
saludos.saludar("Iván")
