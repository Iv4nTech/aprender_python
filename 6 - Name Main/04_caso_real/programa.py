"""
PASO 4 (caso real): el programa principal del proyecto.

Ejecuta:

    python programa.py

Aquí ves el patrón completo que usan los proyectos Python reales:

  1. El programa principal también protege su arranque con el if.
  2. Define una función main() con la lógica de arranque.
  3. La última parte del archivo es solo:  if __name__ == "__main__": main()

¿Por qué proteger TAMBIÉN el programa principal, si nadie lo importa?
Porque nunca se sabe: mañana otro archivo (o un test) podría querer
importar main() de aquí, y gracias al candado podrá hacerlo sin que
el programa se arranque solo.
"""

import calculadora  # Carga calculadora.py. Su demo NO corre porque allí
                    # __name__ vale 'calculadora', no '__main__'.


def main():
    """Punto de entrada del programa: aquí vive la lógica de arranque."""
    print("[programa.py -> main()] Programa principal en marcha.")
    print(f"[programa.py -> main()] Mi __name__ vale: {__name__!r}")
    print("[programa.py -> main()] Uso las funciones del módulo importado:")

    total = calculadora.sumar(15, 27)
    print(f"[programa.py -> main()] calculadora.sumar(15, 27) = {total}")

    mitad = calculadora.dividir(total, 2)
    print(f"[programa.py -> main()] calculadora.dividir({total}, 2) = {mitad}")

    print("[programa.py -> main()] Fíjate: la demo de calculadora.py no salió.")


# Punto de entrada estándar de casi cualquier programa Python:
if __name__ == "__main__":
    main()
