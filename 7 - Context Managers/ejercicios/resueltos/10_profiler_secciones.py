# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 10 — Experto | Profiler de secciones de código  [RESUELTO]
# Técnica: clase anidada como context manager, clase principal como context
#          manager, formateo de tabla en consola
# ─────────────────────────────────────────────────────────────────────────────
#
# CONCEPTO CLAVE
#   Un context manager puede devolver otro objeto que también sea context
#   manager. Aquí el Profiler devuelve self en __enter__, y cada llamada a
#   seccion() devuelve un objeto _Seccion con su propio __enter__/__exit__
#   que, al terminar, registra el resultado de vuelta en el Profiler padre.
#   Esto es composición de context managers: with anidados donde el interior
#   alimenta de datos al exterior.
# ─────────────────────────────────────────────────────────────────────────────

import time


class Profiler:

    class _Seccion:
        def __init__(self, profiler, nombre):
            self._profiler = profiler
            self._nombre = nombre

        def __enter__(self):
            self._inicio = time.perf_counter()
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            duracion = time.perf_counter() - self._inicio
            self._profiler._resultados.append((self._nombre, duracion))
            return False

    def __enter__(self):
        self._resultados = []
        return self

    def seccion(self, nombre):
        return self._Seccion(self, nombre)

    def __exit__(self, exc_type, exc_value, traceback):
        if not self._resultados:
            return False

        col_nombre = max(len(n) for n, _ in self._resultados)
        col_nombre = max(col_nombre, len("TOTAL"), 15)
        col_tiempo = 12
        ancho = col_nombre + col_tiempo + 5

        linea_h   = "─" * (col_nombre + 2)
        linea_t   = "─" * (col_tiempo + 2)
        sep_top   = f"┌{'─' * (ancho - 2)}┐"
        sep_title = f"│ {'Perfil de ejecución':<{ancho - 4}} │"
        sep_mid   = f"├{linea_h}┬{linea_t}┤"
        sep_bot_r = f"├{linea_h}┴{linea_t}┤"
        sep_bot   = f"└{'─' * (ancho - 2)}┘"

        print(sep_top)
        print(sep_title)
        print(sep_mid)

        total = 0.0
        for nombre, dur in self._resultados:
            total += dur
            print(f"│ {nombre:<{col_nombre}} │ {dur:>{col_tiempo - 2}.4f} s │")

        print(sep_bot_r)
        print(f"│ {'TOTAL':<{col_nombre}} │ {total:>{col_tiempo - 2}.4f} s │")
        print(sep_bot)
        return False


# --- Prueba ---
with Profiler() as p:
    with p.seccion("carga de datos"):
        time.sleep(0.05)
    with p.seccion("procesamiento"):
        time.sleep(0.12)
    with p.seccion("exportar"):
        time.sleep(0.03)
