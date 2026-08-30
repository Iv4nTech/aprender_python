"""
================================================================================
 EJERCICIOS: FICHEROS EN PYTHON
 Ejecutar: python3 ejercicios.py

 Completa cada ejercicio donde encuentres '...' y descomenta los print()
 para comprobar el resultado.
================================================================================
"""

from pathlib import Path


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ──────────────────────────────────────────────
# EJERCICIO 1 — FÁCIL
# Registro de visitas
# ──────────────────────────────────────────────
seccion("EJERCICIO 1 — FÁCIL — Registro de visitas")


# Escribe registrar_visita(nombre, fichero) que añada una línea al fichero
# con el nombre y el timestamp actual (usa datetime.now()). Si el fichero
# no existe, se crea automáticamente (modo append).
def registrar_visita(nombre: str, fichero: str) -> None:
    ...


# registrar_visita("Ana", "visitas.txt")
# registrar_visita("Luis", "visitas.txt")
# registrar_visita("Marta", "visitas.txt")
# print(Path("visitas.txt").read_text(encoding="utf-8"))
# Path("visitas.txt").unlink(missing_ok=True)

# Resultado esperado: tres líneas, cada una con un nombre y una fecha/hora


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Leer configuración
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — Leer configuración")


# Dado un fichero config.json con claves "host", "puerto" y "debug",
# escribe leer_config(ruta) -> dict que lo lea y devuelva el diccionario.
# Incluye manejo de FileNotFoundError (si no existe, devuelve {}).
def leer_config(ruta: str) -> dict:
    ...


# Path("config.json").write_text(
#     '{"host": "localhost", "puerto": 8080, "debug": true}', encoding="utf-8"
# )
# print(leer_config("config.json"))
# print(leer_config("no_existe.json"))
# Path("config.json").unlink(missing_ok=True)

# Resultado esperado:
# {'host': 'localhost', 'puerto': 8080, 'debug': True}
# {}


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Contar líneas
# ──────────────────────────────────────────────
seccion("EJERCICIO 3 — FÁCIL — Contar líneas")


# Escribe contar_lineas(ruta) -> int que devuelva el número de líneas no
# vacías de un fichero de texto. Usa un bucle sobre el objeto fichero (no
# readlines()).
def contar_lineas(ruta: str) -> int:
    ...


# Path("notas.txt").write_text("primera\nsegunda\n\ntercera\n\n", encoding="utf-8")
# print(contar_lineas("notas.txt"))
# Path("notas.txt").unlink(missing_ok=True)

# Resultado esperado: 3


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Filtrar logs de error
# ──────────────────────────────────────────────
seccion("EJERCICIO 4 — MEDIO — Filtrar logs de error")


# Dado un fichero de log donde cada línea empieza por "[INFO]", "[WARNING]"
# o "[ERROR]", escribe extraer_errores(entrada, salida) que lea el fichero
# de entrada y escriba en el de salida solo las líneas de error.
def extraer_errores(entrada: str, salida: str) -> None:
    ...


# Path("sistema.log").write_text(
#     "[INFO] arranque completado\n"
#     "[ERROR] fallo al conectar con la base de datos\n"
#     "[WARNING] memoria por encima del 80%\n"
#     "[ERROR] timeout en la pasarela de pago\n",
#     encoding="utf-8",
# )
# extraer_errores("sistema.log", "errores.log")
# print(Path("errores.log").read_text(encoding="utf-8"))
# Path("sistema.log").unlink(missing_ok=True)
# Path("errores.log").unlink(missing_ok=True)

# Resultado esperado:
# [ERROR] fallo al conectar con la base de datos
# [ERROR] timeout en la pasarela de pago


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# CSV de ventas
# ──────────────────────────────────────────────
seccion("EJERCICIO 5 — MEDIO — CSV de ventas")


# Escribe calcular_total(ruta_csv) -> float que lea un CSV con columnas
# producto,cantidad,precio y devuelva el total (suma de cantidad * precio
# por fila).
def calcular_total(ruta_csv: str) -> float:
    ...


# import csv
# with open("ventas.csv", "w", newline="", encoding="utf-8") as f:
#     escritor = csv.writer(f)
#     escritor.writerow(["producto", "cantidad", "precio"])
#     escritor.writerow(["Teclado", 2, 45.99])
#     escritor.writerow(["Ratón", 3, 19.99])
# print(calcular_total("ventas.csv"))
# Path("ventas.csv").unlink(missing_ok=True)

# Resultado esperado: 151.95


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# pathlib — inventario de ficheros
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — pathlib — inventario de ficheros")


# Escribe crear_ficheros_prueba(carpeta) que cree la carpeta (mkdir con
# exist_ok=True) y genere 5 ficheros .txt con contenido cualquiera.
# Escribe listar_txt(carpeta) -> list[str] que devuelva los nombres de
# todos los .txt ordenados alfabéticamente.
def crear_ficheros_prueba(carpeta: Path) -> None:
    ...


def listar_txt(carpeta: Path) -> list[str]:
    ...


# carpeta_prueba = Path("inventario")
# crear_ficheros_prueba(carpeta_prueba)
# print(listar_txt(carpeta_prueba))
# for f in carpeta_prueba.glob("*.txt"):
#     f.unlink()
# carpeta_prueba.rmdir()

# Resultado esperado: lista con 5 nombres de fichero .txt, ordenados


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# Rotar logs
# ──────────────────────────────────────────────
seccion("EJERCICIO 7 — AVANZADO — Rotar logs")


# Escribe rotar_log(ruta, max_lineas) que lea el fichero de log, y si tiene
# más de max_lineas líneas, guarde solo las últimas max_lineas (descartando
# las más antiguas) y sobrescriba el fichero. Usa pathlib.
def rotar_log(ruta: str, max_lineas: int) -> None:
    ...


# contenido = "\n".join(f"linea {i}" for i in range(1, 11)) + "\n"
# Path("grande.log").write_text(contenido, encoding="utf-8")
# rotar_log("grande.log", 3)
# print(Path("grande.log").read_text(encoding="utf-8"))
# Path("grande.log").unlink(missing_ok=True)

# Resultado esperado:
# linea 8
# linea 9
# linea 10


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Config con respaldo
# ──────────────────────────────────────────────
seccion("EJERCICIO 8 — AVANZADO — Config con respaldo")


# Escribe guardar_config(config, ruta) que, antes de sobreescribir el JSON
# existente, cree una copia de respaldo en ruta + ".bak" (usa Path.copy(),
# Python 3.14). Si el fichero no existía todavía, no intenta copiarlo.
def guardar_config(config: dict, ruta: str) -> None:
    ...


# guardar_config({"host": "localhost", "puerto": 8080}, "app_config.json")
# print(Path("app_config.json.bak").exists())  # False: no había nada que respaldar
# guardar_config({"host": "localhost", "puerto": 9090}, "app_config.json")
# print(Path("app_config.json.bak").exists())  # True: ya existía y se respaldó
# print(Path("app_config.json.bak").read_text(encoding="utf-8"))
# Path("app_config.json").unlink(missing_ok=True)
# Path("app_config.json.bak").unlink(missing_ok=True)

# Resultado esperado:
# False
# True
# {"host": "localhost", "puerto": 8080}


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# CSV -> JSON
# ──────────────────────────────────────────────
seccion("EJERCICIO 9 — AVANZADO — CSV -> JSON")


# Escribe csv_a_json(ruta_csv, ruta_json) que convierta un CSV (con
# cabecera) en un JSON con la estructura [{"col1": val, ...}, ...]. Usa
# csv.DictReader. Intenta convertir cada valor a int o float si es
# posible; si no, déjalo como string.
def csv_a_json(ruta_csv: str, ruta_json: str) -> None:
    ...


# import csv
# with open("clientes.csv", "w", newline="", encoding="utf-8") as f:
#     escritor = csv.writer(f)
#     escritor.writerow(["nombre", "edad", "saldo"])
#     escritor.writerow(["Ana", "28", "150.5"])
#     escritor.writerow(["Luis", "35", "0"])
# csv_a_json("clientes.csv", "clientes.json")
# print(Path("clientes.json").read_text(encoding="utf-8"))
# Path("clientes.csv").unlink(missing_ok=True)
# Path("clientes.json").unlink(missing_ok=True)

# Resultado esperado (formato JSON, tipos numéricos sin comillas):
# [{"nombre": "Ana", "edad": 28, "saldo": 150.5}, {"nombre": "Luis", "edad": 35, "saldo": 0}]


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Índice de palabras
# ──────────────────────────────────────────────
seccion("EJERCICIO 10 — EXPERTO — Índice de palabras")


# Escribe construir_indice(ruta) -> dict[str, list[int]] que lea un
# fichero de texto y devuelva un diccionario donde cada clave es una
# palabra (en minúsculas, sin puntuación) y el valor es la lista de
# números de línea donde aparece (sin duplicados, ordenada). Escribe el
# índice resultante también en un JSON (ruta + ".index.json").
def construir_indice(ruta: str) -> dict[str, list[int]]:
    ...


# texto = (
#     "Python es un lenguaje.\n"
#     "Python es fácil de leer.\n"
#     "El lenguaje Python es muy usado.\n"
#     "Es fácil empezar con Python.\n"
# )
# Path("articulo.txt").write_text(texto, encoding="utf-8")
# indice = construir_indice("articulo.txt")
# print(indice["python"])
# print(indice["es"])
# print(indice["fácil"])
# Path("articulo.txt").unlink(missing_ok=True)
# Path("articulo.txt.index.json").unlink(missing_ok=True)

# Resultado esperado:
# [1, 2, 3, 4]
# [1, 2, 3, 4]
# [2, 4]
