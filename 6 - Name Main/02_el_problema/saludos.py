"""
PASO 2 (el problema): un módulo SIN protección.

Este archivo NO usa if __name__ == "__main__". Tiene código "suelto"
al final, fuera de toda función. Eso va a darnos un problema.

Pruébalo de las dos formas:

    python saludos.py   -> todo bien, es lo que esperas
    python app.py       -> ¡sorpresa! este archivo se ejecuta solo
"""

# Cuando Python carga este archivo (sea ejecutándolo o importándolo),
# lo lee y EJECUTA de arriba a abajo. Este print es la prueba:
print(f"[saludos.py] Me están cargando. Mi __name__ vale: {__name__!r}")


def saludar(nombre):
    """Función reutilizable: esto es lo que app.py quiere usar."""
    print(f"[saludos.py -> saludar()] ¡Hola, {nombre}!")


# ---------------------------------------------------------------------------
# AQUÍ ESTÁ EL PROBLEMA: código suelto, sin candado.
# Estas líneas se ejecutan SIEMPRE que se cargue el archivo,
# da igual si lo ejecutaste tú o si alguien solo quería importarlo.
# ---------------------------------------------------------------------------
print("[saludos.py] ATENCIÓN: este print está SUELTO (sin if __name__...).")
saludar("prueba interna de saludos.py")
print("[saludos.py] Estas 3 líneas se colarán cuando app.py me importe. MAL.")
