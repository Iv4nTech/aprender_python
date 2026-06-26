"""
CONCEPTO 10 (AVANZADO) · __main__.py hace EJECUTABLE un paquete
Si una carpeta-paquete tiene un __main__.py, puedes lanzarla con:
    python -m saludador  Mundo

CASO REAL: cualquier herramienta de línea de comandos seria (pip, http.server,
venv...) se ejecuta así: 'python -m pip', 'python -m http.server'. Tú puedes
hacer lo mismo con tu propio paquete.

"""
import sys


def main(argumentos):
    nombre = argumentos[0] if argumentos else "mundo"
    print(f"👋 ¡Hola, {nombre}! (ejecutado con: python -m saludador)")


if __name__ == "__main__":
    main(sys.argv[1:])
