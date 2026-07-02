# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 1 — Fácil | Temporizador de bloques  [RESUELTO]
# Técnica: clase con __enter__ / __exit__
# ─────────────────────────────────────────────────────────────────────────────
#
# CONCEPTO CLAVE
#   __enter__ devuelve `self` para que el bloque pueda acceder al objeto
#   completo (y a su atributo `duracion`) después de que el with termine.
#   __exit__ devuelve False: no suprime excepciones, solo mide el tiempo.
# ─────────────────────────────────────────────────────────────────────────────

import time


class Temporizador:
    def __enter__(self):
        self.inicio = time.perf_counter()
        return self                                    # `t` en `with ... as t`

    def __exit__(self, exc_type, exc_value, traceback):
        self.duracion = time.perf_counter() - self.inicio
        print(f"Tiempo: {self.duracion:.4f} s")
        return False                                   # deja propagar excepciones


with Temporizador() as t:
    total = sum(x ** 2 for x in range(1_000_000))

print(f"Duración guardada: {t.duracion:.4f} s")
print(f"Resultado: {total}")
