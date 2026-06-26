# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 1 — Fácil | Temporizador de bloques
# Técnica: clase con __enter__ / __exit__
# ─────────────────────────────────────────────────────────────────────────────
#
# CONTEXTO
#   Cuando optimizas código necesitas medir cuánto tarda cada parte.
#   En lugar de llamar a time.perf_counter() antes y después de cada bloque
#   manualmente, un context manager lo hace de forma limpia y reutilizable.
#
# TAREA
#   Implementa la clase Temporizador:
#   - __enter__: guarda el instante de inicio y devuelve el propio objeto.
#   - __exit__: calcula el tiempo transcurrido, lo guarda en self.duracion
#               e imprime "Tiempo: X.XXXX s".
#
# USO ESPERADO
#   with Temporizador() as t:
#       total = sum(x ** 2 for x in range(1_000_000))
#
#   print(f"Tiempo: {total}")
#   print(f"Duración guardada: {t.duracion:.4f} s")
#
# SALIDA ESPERADA
#   Tiempo: 0.0521 s
#   Duración guardada: 0.0521 s
# ─────────────────────────────────────────────────────────────────────────────

import time


class Temporizador:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


# --- Prueba (no modificar) ---
with Temporizador() as t:
    total = sum(x ** 2 for x in range(1_000_000))
print(f"Duración guardada: {t.duracion:.4f} s")
print(f"Resultado: {total}")

