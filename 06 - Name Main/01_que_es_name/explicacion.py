"""
PASO 1: Descubrir que la variable __name__ EXISTE.

Ejecuta este archivo así:

    python explicacion.py

Punto clave: la variable __name__ NO la hemos creado nosotros en ningún
sitio de este archivo (búscala: no hay ningún "__name__ = ..." nuestro).
La crea Python AUTOMÁTICAMENTE en cada archivo .py que carga.
"""

# ---------------------------------------------------------------------------
# 1. Comprobamos que __name__ existe sin haberla definido nosotros.
# ---------------------------------------------------------------------------
print("[explicacion.py] Hola, soy el archivo explicacion.py")
print("[explicacion.py] Yo no he creado ninguna variable __name__...")
print("[explicacion.py] ...pero Python sí. Su valor ahora mismo es:", repr(__name__))

# Como has ejecutado este archivo DIRECTAMENTE (python explicacion.py),
# Python le ha dado a __name__ el valor especial "__main__".
# "__main__" significa: "este es el archivo principal, el que se lanzó".

# ---------------------------------------------------------------------------
# 2. Por tanto, esta comparación da True:
# ---------------------------------------------------------------------------
print("[explicacion.py] ¿__name__ == '__main__'?", __name__ == "__main__")

# ---------------------------------------------------------------------------
# 3. Y eso es TODO lo que hace el famoso if: una simple comparación de texto.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("[explicacion.py] Este print está DENTRO del if __name__ == '__main__'.")
    print("[explicacion.py] Se ve porque me has ejecutado directamente.")
    print("[explicacion.py] Si otro archivo me importara, esta parte NO se vería.")
    print("[explicacion.py] (Eso lo demostramos en las carpetas 02 y 03.)")
