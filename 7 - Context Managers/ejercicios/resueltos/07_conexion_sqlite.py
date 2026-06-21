# ─────────────────────────────────────────────────────────────────────────────
# Ejercicio 7 — Difícil | Gestión de conexión SQLite con transacciones  [RESUELTO]
# Técnica: clase, sqlite3, commit / rollback, cierre garantizado
# ─────────────────────────────────────────────────────────────────────────────
#
# CONCEPTO CLAVE
#   isolation_level=None abre SQLite en modo "autocommit desactivado", lo
#   que nos da control manual sobre las transacciones.
#   El bloque try/except/finally en __exit__ cubre los tres casos:
#     - sin error  → commit + cierre
#     - con error  → rollback + cierre + propagar
#   El finally garantiza que la conexión SIEMPRE se cierra.
# ─────────────────────────────────────────────────────────────────────────────

import sqlite3


class ConexionSQLite:
    def __init__(self, ruta_db):
        self.ruta_db = ruta_db

    def __enter__(self):
        self._conn = sqlite3.connect(self.ruta_db)
        self._conn.execute("BEGIN")
        return self._conn.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if exc_type is None:
                self._conn.commit()
            else:
                self._conn.rollback()
        finally:
            self._conn.close()
        return False                   # deja propagar la excepción si la hay


# --- Prueba ---
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
assert len(filas) == 2
assert filas[0][0] == "manzana"
print("OK — commit y rollback funcionan correctamente")
