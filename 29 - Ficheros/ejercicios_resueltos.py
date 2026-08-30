"""
================================================================================
 EJERCICIOS RESUELTOS: FICHEROS EN PYTHON
 Ejecutar: python3 ejercicios_resueltos.py
================================================================================
"""

import csv
import json
import string
from datetime import datetime
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


# SOLUCIÓN
def registrar_visita(nombre: str, fichero: str) -> None:
    with open(fichero, "a", encoding="utf-8") as f:
        f.write(f"{nombre} - {datetime.now()}\n")


registrar_visita("Ana", "visitas.txt")
registrar_visita("Luis", "visitas.txt")
registrar_visita("Marta", "visitas.txt")
print(Path("visitas.txt").read_text(encoding="utf-8"))
Path("visitas.txt").unlink(missing_ok=True)


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Leer configuración
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — Leer configuración")


# SOLUCIÓN
def leer_config(ruta: str) -> dict:
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


Path("config.json").write_text(
    '{"host": "localhost", "puerto": 8080, "debug": true}', encoding="utf-8"
)
print(leer_config("config.json"))
print(leer_config("no_existe.json"))
Path("config.json").unlink(missing_ok=True)


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Contar líneas
# ──────────────────────────────────────────────
seccion("EJERCICIO 3 — FÁCIL — Contar líneas")


# SOLUCIÓN
def contar_lineas(ruta: str) -> int:
    contador = 0
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip():
                contador += 1
    return contador


Path("notas.txt").write_text("primera\nsegunda\n\ntercera\n\n", encoding="utf-8")
print(contar_lineas("notas.txt"))
Path("notas.txt").unlink(missing_ok=True)


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Filtrar logs de error
# ──────────────────────────────────────────────
seccion("EJERCICIO 4 — MEDIO — Filtrar logs de error")


# SOLUCIÓN
def extraer_errores(entrada: str, salida: str) -> None:
    with open(entrada, "r", encoding="utf-8") as f_in, open(
        salida, "w", encoding="utf-8"
    ) as f_out:
        for linea in f_in:
            if linea.startswith("[ERROR]"):
                f_out.write(linea)


Path("sistema.log").write_text(
    "[INFO] arranque completado\n"
    "[ERROR] fallo al conectar con la base de datos\n"
    "[WARNING] memoria por encima del 80%\n"
    "[ERROR] timeout en la pasarela de pago\n",
    encoding="utf-8",
)
extraer_errores("sistema.log", "errores.log")
print(Path("errores.log").read_text(encoding="utf-8"))
Path("sistema.log").unlink(missing_ok=True)
Path("errores.log").unlink(missing_ok=True)


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# CSV de ventas
# ──────────────────────────────────────────────
seccion("EJERCICIO 5 — MEDIO — CSV de ventas")


# SOLUCIÓN
def calcular_total(ruta_csv: str) -> float:
    total = 0.0
    with open(ruta_csv, "r", newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            total += float(fila["cantidad"]) * float(fila["precio"])
    return total


with open("ventas.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["producto", "cantidad", "precio"])
    escritor.writerow(["Teclado", 2, 45.99])
    escritor.writerow(["Ratón", 3, 19.99])
print(calcular_total("ventas.csv"))
Path("ventas.csv").unlink(missing_ok=True)


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# pathlib — inventario de ficheros
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — pathlib — inventario de ficheros")


# SOLUCIÓN
def crear_ficheros_prueba(carpeta: Path) -> None:
    carpeta.mkdir(exist_ok=True)
    for i in range(1, 6):
        (carpeta / f"fichero_{i}.txt").write_text(f"contenido {i}\n", encoding="utf-8")


def listar_txt(carpeta: Path) -> list[str]:
    return sorted(f.name for f in carpeta.glob("*.txt"))


carpeta_prueba = Path("inventario")
crear_ficheros_prueba(carpeta_prueba)
print(listar_txt(carpeta_prueba))
for f in carpeta_prueba.glob("*.txt"):
    f.unlink()
carpeta_prueba.rmdir()


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# Rotar logs
# ──────────────────────────────────────────────
seccion("EJERCICIO 7 — AVANZADO — Rotar logs")


# SOLUCIÓN
def rotar_log(ruta: str, max_lineas: int) -> None:
    camino = Path(ruta)
    lineas = camino.read_text(encoding="utf-8").splitlines()
    if len(lineas) > max_lineas:
        camino.write_text("\n".join(lineas[-max_lineas:]) + "\n", encoding="utf-8")


contenido = "\n".join(f"linea {i}" for i in range(1, 11)) + "\n"
Path("grande.log").write_text(contenido, encoding="utf-8")
rotar_log("grande.log", 3)
print(Path("grande.log").read_text(encoding="utf-8"))
Path("grande.log").unlink(missing_ok=True)


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Config con respaldo
# ──────────────────────────────────────────────
seccion("EJERCICIO 8 — AVANZADO — Config con respaldo")


# SOLUCIÓN
def guardar_config(config: dict, ruta: str) -> None:
    camino = Path(ruta)
    if camino.exists():
        camino.copy(Path(ruta + ".bak"))
    camino.write_text(json.dumps(config), encoding="utf-8")


guardar_config({"host": "localhost", "puerto": 8080}, "app_config.json")
print(Path("app_config.json.bak").exists())
guardar_config({"host": "localhost", "puerto": 9090}, "app_config.json")
print(Path("app_config.json.bak").exists())
print(Path("app_config.json.bak").read_text(encoding="utf-8"))
Path("app_config.json").unlink(missing_ok=True)
Path("app_config.json.bak").unlink(missing_ok=True)


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# CSV -> JSON
# ──────────────────────────────────────────────
seccion("EJERCICIO 9 — AVANZADO — CSV -> JSON")


# SOLUCIÓN
def _convertir(valor: str):
    try:
        return int(valor)
    except ValueError:
        pass
    try:
        return float(valor)
    except ValueError:
        return valor


def csv_a_json(ruta_csv: str, ruta_json: str) -> None:
    with open(ruta_csv, "r", newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        registros = [
            {clave: _convertir(valor) for clave, valor in fila.items()}
            for fila in lector
        ]
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(registros, f)


with open("clientes.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "edad", "saldo"])
    escritor.writerow(["Ana", "28", "150.5"])
    escritor.writerow(["Luis", "35", "0"])
csv_a_json("clientes.csv", "clientes.json")
print(Path("clientes.json").read_text(encoding="utf-8"))
Path("clientes.csv").unlink(missing_ok=True)
Path("clientes.json").unlink(missing_ok=True)


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Índice de palabras
# ──────────────────────────────────────────────
seccion("EJERCICIO 10 — EXPERTO — Índice de palabras")


# SOLUCIÓN
def construir_indice(ruta: str) -> dict[str, list[int]]:
    indice: dict[str, list[int]] = {}
    with open(ruta, "r", encoding="utf-8") as f:
        for numero, linea in enumerate(f, start=1):
            sin_puntuacion = linea.translate(str.maketrans("", "", string.punctuation))
            for palabra in sin_puntuacion.lower().split():
                lineas_palabra = indice.setdefault(palabra, [])
                if numero not in lineas_palabra:
                    lineas_palabra.append(numero)
    for lineas_palabra in indice.values():
        lineas_palabra.sort()
    with open(ruta + ".index.json", "w", encoding="utf-8") as f:
        json.dump(indice, f)
    return indice


texto = (
    "Python es un lenguaje.\n"
    "Python es fácil de leer.\n"
    "El lenguaje Python es muy usado.\n"
    "Es fácil empezar con Python.\n"
)
Path("articulo.txt").write_text(texto, encoding="utf-8")
indice = construir_indice("articulo.txt")
print(indice["python"])
print(indice["es"])
print(indice["fácil"])
Path("articulo.txt").unlink(missing_ok=True)
Path("articulo.txt.index.json").unlink(missing_ok=True)
