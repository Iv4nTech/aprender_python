# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 5 — Medio | Capturar la salida estándar
# Técnica: clase, sys.stdout, io.StringIO
# ─────────────────────────────────────────────────────────────────────────────
#
# CONTEXTO
#   En tests automatizados a veces necesitas comprobar qué imprime una función
#   sin modificarla. La solución es redirigir sys.stdout a un buffer en memoria
#   para capturar todo lo que se imprime dentro del bloque y luego inspeccionarlo.
#
# TAREA
#   Implementa la clase CapturarSalida:
#   - __enter__: redirige sys.stdout a un buffer en memoria (io.StringIO)
#                y devuelve el propio objeto.
#   - __exit__:  restaura sys.stdout original, aunque haya excepción.
#   - leer():    devuelve como string todo lo que se imprimió dentro del bloque.
#
# USO ESPERADO
#   with CapturarSalida() as salida:
#       print("hola")
#       print("mundo")
#
#   texto = salida.leer()
#   print(repr(texto))          # 'hola\nmundo\n'
#   assert "hola" in texto
#   assert texto.count("\n") == 2
# ─────────────────────────────────────────────────────────────────────────────

import sys
import io


class CapturarSalida:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def leer(self):
        pass


# --- Prueba (no modificar) ---
with CapturarSalida() as salida:
    print("hola")
    print("mundo")

texto = salida.leer()
print(f"Capturado: {repr(texto)}")
assert texto == "hola\nmundo\n", f"Inesperado: {repr(texto)}"
print("OK")
