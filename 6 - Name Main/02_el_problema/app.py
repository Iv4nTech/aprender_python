"""
PASO 2 (el problema): el archivo que importa al módulo sin protección.

Ejecuta:

    python app.py

Yo solo quiero usar la función saludar() de saludos.py.
Pero fíjate en la salida: aparecerán prints de saludos.py que yo NUNCA pedí,
ANTES incluso de mi primer print propio tras el import.
"""

print("[app.py] Soy app.py y me has ejecutado directamente.")
print(f"[app.py] Por eso MI __name__ vale: {__name__!r}")
print("[app.py] Ahora voy a hacer 'import saludos'. Mira lo que pasa:")
print("[app.py] ------------- empieza el import -------------")

import saludos  # <- En esta línea Python ejecuta saludos.py ENTERO.
                #    Todo lo que veas entre las rayas lo imprime saludos.py,
                #    no yo. Y yo no he llamado a nada todavía.

print("[app.py] ------------- termina el import -------------")
print("[app.py] ¿Has visto? Entre las rayas hay prints de saludos.py")
print("[app.py] que yo no pedí. Solo quería importar la función.")
print()
print("[app.py] Ahora sí, llamo YO a la función, a propósito:")
saludos.saludar("Iván")
print("[app.py] La solución a este lío está en la carpeta 03_la_solucion.")
