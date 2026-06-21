# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 10 — Experto | Profiler de secciones de código
# Técnica: clase anidada como context manager, clase principal como context
#          manager, formateo de tabla en consola
# ─────────────────────────────────────────────────────────────────────────────
#
# CONTEXTO
#   En aplicaciones reales necesitas medir el tiempo de múltiples secciones
#   de código y ver un resumen al final. Este ejercicio combina varias técnicas:
#   un context manager principal que gestiona el ciclo de vida del profiler, y
#   un context manager interno para cada sección individual.
#   El resultado es una API fluida que se usa con with anidados.
#
# TAREA
#   Implementa la clase Profiler:
#   - __enter__: inicializa la lista de secciones y devuelve el propio objeto.
#   - __exit__:  imprime la tabla de resultados al salir del bloque principal.
#   - seccion(nombre): devuelve un objeto que funciona como context manager.
#                      Al entrar mide el inicio; al salir registra la duración
#                      en el Profiler padre.
#
#   La tabla de salida debe mostrar nombre y duración de cada sección,
#   más el tiempo total al final.
#
# USO ESPERADO
#   import time
#
#   with Profiler() as p:
#       with p.seccion("carga de datos"):
#           time.sleep(0.05)
#       with p.seccion("procesamiento"):
#           time.sleep(0.12)
#       with p.seccion("exportar"):
#           time.sleep(0.03)
#
# SALIDA ESPERADA
#   ┌──────────────────────────────────┐
#   │ Perfil de ejecución              │
#   ├─────────────────┬────────────────┤
#   │ carga de datos  │     0.0501 s   │
#   │ procesamiento   │     0.1203 s   │
#   │ exportar        │     0.0301 s   │
#   ├─────────────────┴────────────────┤
#   │ TOTAL           │     0.2005 s   │
#   └──────────────────────────────────┘
# ─────────────────────────────────────────────────────────────────────────────

import time


class Profiler:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def seccion(self, nombre):
        pass


# --- Prueba (no modificar) ---
with Profiler() as p:
    with p.seccion("carga de datos"):
        time.sleep(0.05)
    with p.seccion("procesamiento"):
        time.sleep(0.12)
    with p.seccion("exportar"):
        time.sleep(0.03)
