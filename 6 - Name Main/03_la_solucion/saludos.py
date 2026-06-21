"""
PASO 3 (la solución): el MISMO módulo, pero CON el candado.

Es idéntico al saludos.py de la carpeta 02, con un único cambio:
el código suelto del final ahora está dentro de if __name__ == "__main__".

Pruébalo de las dos formas y compara:

    python saludos.py   -> el bloque del if SÍ se ejecuta (eres tú quien lo lanza)
    python app.py       -> el bloque del if NO se ejecuta (solo te importan)
"""

# Este print sigue suelto A PROPÓSITO, para que veas que el archivo
# se carga igualmente y qué valor recibe __name__ en cada caso:
#   - python saludos.py  -> __name__ = '__main__'
#   - python app.py      -> __name__ = 'saludos'   (su propio nombre)
print(f"[saludos.py] Me están cargando. Mi __name__ vale: {__name__!r}")


def saludar(nombre):
    """Función reutilizable: disponible siempre, se importe o se ejecute."""
    print(f"[saludos.py -> saludar()] ¡Hola, {nombre}!")


# ---------------------------------------------------------------------------
# EL CANDADO. Léelo como: "si este archivo es el que se lanzó directamente".
#
#   python saludos.py -> __name__ == "__main__" -> True  -> el bloque corre
#   import saludos    -> __name__ == "saludos"  -> False -> el bloque NO corre
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("[saludos.py] Estoy DENTRO del if __name__ == '__main__'.")
    print("[saludos.py] Si lees esto es porque hiciste 'python saludos.py'.")
    saludar("prueba interna de saludos.py")
    print("[saludos.py] Cuando app.py me importa, nada de esto aparece.")
