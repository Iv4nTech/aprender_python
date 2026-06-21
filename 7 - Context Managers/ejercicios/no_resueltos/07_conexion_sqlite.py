# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 7 — Difícil | Gestión de conexión SQLite con transacciones
# Técnica: clase, sqlite3, commit / rollback, cierre garantizado
# ─────────────────────────────────────────────────────────────────────────────
#
# CONTEXTO
#   Trabajar con bases de datos requiere siempre el mismo patrón: abrir
#   conexión → ejecutar operaciones en una transacción → hacer commit si
#   todo fue bien o rollback si algo falló → cerrar la conexión.
#   Sin un context manager hay que repetir ese patrón en cada función que
#   toque la base de datos.
#
# TAREA
#   Implementa la clase ConexionSQLite:
#   - __init__:  recibe la ruta del fichero .db.
#   - __enter__: abre la conexión, inicia la transacción y devuelve el cursor.
#   - __exit__ sin error: hace commit y cierra la conexión.
#   - __exit__ con error: hace rollback, cierra la conexión y deja propagar
#                         la excepción.
#
# USO ESPERADO
#   with ConexionSQLite("tienda.db") as cur:
#       cur.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT, precio REAL)")
#       cur.execute("INSERT INTO productos VALUES (?, ?)", ("manzana", 0.50))
#       cur.execute("INSERT INTO productos VALUES (?, ?)", ("naranja", 0.80))
#   # commit automático
#
#   try:
#       with ConexionSQLite("tienda.db") as cur:
#           cur.execute("INSERT INTO productos VALUES (?, ?)", ("kiwi", 1.20))
#           raise RuntimeError("error de stock")
#   except RuntimeError:
#       pass
#   # rollback automático — kiwi no se guardó
#
#   with ConexionSQLite("tienda.db") as cur:
#       cur.execute("SELECT * FROM productos")
#       print(cur.fetchall())
#   # [('manzana', 0.5), ('naranja', 0.8)]
# ─────────────────────────────────────────────────────────────────────────────

import sqlite3


class ConexionSQLite:
    def __init__(self, ruta_db):
        self.ruta_db = ruta_db

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


# --- Prueba (no modificar) ---
import os
if os.path.exists("tienda.db"):
    os.remove("tienda.db")

with ConexionSQLite("tienda.db") as cur:
    cur.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT, precio REAL)")
    cur.execute("INSERT INTO productos VALUES (?, ?)", ("manzana", 0.50))
    cur.execute("INSERT INTO productos VALUES (?, ?)", ("naranja", 0.80))

try:
    with ConexionSQLite("tienda.db") as cur:
        cur.execute("INSERT INTO productos VALUES (?, ?)", ("kiwi", 1.20))
        raise RuntimeError("error de stock")
except RuntimeError:
    pass

with ConexionSQLite("tienda.db") as cur:
    cur.execute("SELECT * FROM productos")
    filas = cur.fetchall()

print(filas)
assert len(filas) == 2, f"ERROR: se esperaban 2 filas, hay {len(filas)}"
assert filas[0][0] == "manzana"
print("OK — commit y rollback funcionan correctamente")
