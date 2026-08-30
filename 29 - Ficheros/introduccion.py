"""
================================================================================
 FICHEROS EN PYTHON
 Ejecutar: python3 introduccion.py
================================================================================
"""

import csv
import json
from pathlib import Path

# Todos los ficheros de ejemplo se generan en esta misma carpeta, sin
# importar desde qué directorio se ejecute el script.
BASE_DIR = Path(__file__).resolve().parent

# Si es True (por defecto), los ficheros de ejemplo se borran al terminar
# para no dejar basura en el repo. Ponlo a False para dejarlos en disco,
# en esta misma carpeta, y poder abrirlos tú mismo tras ejecutar el script.
LIMPIAR_AL_FINALIZAR = True


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA SIN FICHEROS
# ============================================================================
seccion("1. El problema sin ficheros")

# Tu programa genera logs valiosos mientras corre: cada error, cada
# operación importante queda registrada... en una lista de Python.
logs_en_memoria = []
logs_en_memoria.append("Usuario Ana ha iniciado sesión")
logs_en_memoria.append("Pedido #4521 procesado correctamente")
logs_en_memoria.append("ERROR: fallo al conectar con la pasarela de pago")

for entrada in logs_en_memoria:
    print(entrada)

# El programa termina aquí. En este punto 'logs_en_memoria' desaparece de
# la RAM. Si mañana hay que investigar por qué falló la pasarela de pago,
# no hay nada que consultar: la evidencia se perdió al cerrar el proceso.
# Para que un dato sobreviva más allá de la ejecución del programa, tiene
# que escribirse en un fichero (o una base de datos, pero eso empieza por
# lo mismo: persistencia en disco).


# ============================================================================
# 2. open() Y MODOS — LA FORMA CLÁSICA
# ============================================================================
seccion("2. open() y modos — la forma clásica")

RUTA_LOG = BASE_DIR / "app.log"

# 'w' (write): crea el fichero si no existe, y lo SOBREESCRIBE si existe.
fichero = open(RUTA_LOG, "w", encoding="utf-8")
fichero.write("Usuario Ana ha iniciado sesión\n")
fichero.write("Pedido #4521 procesado correctamente\n")
fichero.close()  # si te olvidas de esto, no hay garantía de que se escriba

# 'a' (append): añade al final sin borrar lo que ya había.
fichero = open(RUTA_LOG, "a", encoding="utf-8")
fichero.write("ERROR: fallo al conectar con la pasarela de pago\n")
fichero.close()

# 'r' (read): lee el contenido existente.
fichero = open(RUTA_LOG, "r", encoding="utf-8")
contenido = fichero.read()
fichero.close()
print(contenido)

# El riesgo real de open()/close() manual: si algo lanza una excepción
# entre el open() y el close(), el close() nunca se ejecuta. El fichero
# puede quedar con el buffer sin volcar a disco, o bloqueado para otros
# procesos. La documentación oficial de Python avisa explícitamente de
# esto y recomienda no depender de close() manual.


# ============================================================================
# 3. with open() — LA FORMA CORRECTA
# ============================================================================
seccion("3. with open() — la forma correcta")

# Mismo ejemplo que antes, pero con un context manager: 'with' garantiza
# que fichero.close() se llama siempre, incluso si algo falla dentro del
# bloque. (El mecanismo de 'with' — __enter__/__exit__ — ya se explicó a
# fondo en el vídeo de Context Managers del canal; aquí solo se aplica.)
with open(RUTA_LOG, "w", encoding="utf-8") as fichero:
    fichero.write("Usuario Ana ha iniciado sesión\n")
    fichero.write("Pedido #4521 procesado correctamente\n")
    fichero.write("ERROR: fallo al conectar con la pasarela de pago\n")

print("¿Fichero cerrado tras el with?", fichero.closed)

# Demostración de que se cierra incluso con una excepción de por medio.
try:
    with open(RUTA_LOG, "a", encoding="utf-8") as fichero:
        fichero.write("Línea antes del fallo\n")
        raise ValueError("algo ha explotado dentro del bloque with")
except ValueError as error:
    print(f"Excepción capturada: {error}")

print("¿Sigue cerrado pese a la excepción?", fichero.closed)


# ============================================================================
# 4. LEER FICHEROS — read(), readline(), readlines() Y BUCLE
# ============================================================================
seccion("4. Leer ficheros — read(), readline(), readlines() y bucle")

with open(RUTA_LOG, "r", encoding="utf-8") as fichero:
    todo = fichero.read()
print("read() -> todo el contenido de una vez:")
print(repr(todo))

with open(RUTA_LOG, "r", encoding="utf-8") as fichero:
    primera_linea = fichero.readline()
    segunda_linea = fichero.readline()
print("readline() -> una línea cada vez que se llama:")
print(repr(primera_linea), repr(segunda_linea))

with open(RUTA_LOG, "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
print("readlines() -> lista con todas las líneas:")
print(lineas)

# La forma eficiente para ficheros grandes: iterar línea a línea sin
# cargar el fichero entero en memoria. Un log de 10 GB no cabe en RAM con
# read(), pero sí se puede recorrer línea a línea con este bucle.
print("for line in fichero -> línea a línea, sin cargar todo en memoria:")
with open(RUTA_LOG, "r", encoding="utf-8") as fichero:
    for linea in fichero:
        print(f"  > {linea.strip()}")


# ============================================================================
# 5. pathlib — LA FORMA MODERNA
# ============================================================================
seccion("5. pathlib — la forma moderna")

# Construcción de rutas con '/': funciona igual en Windows, Linux o macOS,
# sin que tengas que preocuparte de si el separador es '\' o '/'.
ruta_log = BASE_DIR / "app.log"

# Leer y escribir de una sola línea, sin abrir/cerrar manualmente.
ruta_log.write_text("Reinicio del sistema completado\n", encoding="utf-8")
print("Contenido escrito con write_text() y releído con read_text():")
print(repr(ruta_log.read_text(encoding="utf-8")))

print("¿Existe?", ruta_log.exists())
print("¿Es un fichero?", ruta_log.is_file())

# Novedad de Python 3.14: Path.copy() y Path.move() para copiar y mover
# ficheros sin importar el módulo 'shutil' aparte.
copia_log = BASE_DIR / "app_backup.log"
ruta_log.copy(copia_log)
print("¿Existe la copia?", copia_log.exists())
# copy() no solo crea el fichero destino: el CONTENIDO viaja con él.
print("Contenido de la copia (idéntico al original):")
print(repr(copia_log.read_text(encoding="utf-8")))

# Limpieza: unlink(missing_ok=True) no lanza error si el fichero ya no está.
copia_log.unlink(missing_ok=True)
ruta_log.unlink(missing_ok=True)
print("¿Existe la copia tras borrarla?", copia_log.exists())
print("¿Existe la original tras borrarla?", ruta_log.exists())

# Por qué pathlib es mejor que concatenar strings para rutas: "carpeta" +
# "/" + "fichero" se rompe en Windows (usa "\"), y no distingue una ruta
# de un simple texto. Un objeto Path sabe cómo unirse, normalizarse y
# consultar el sistema de ficheros según el sistema operativo real.


# ============================================================================
# 6. FICHEROS CSV — SIN LIBRERÍAS EXTERNAS
# ============================================================================
seccion("6. Ficheros CSV — sin librerías externas")

RUTA_VENTAS = BASE_DIR / "ventas.csv"

# Un fichero de ventas real: producto, cantidad, precio unitario.
with open(RUTA_VENTAS, "w", newline="", encoding="utf-8") as fichero:
    escritor = csv.writer(fichero)
    escritor.writerow(["producto", "cantidad", "precio"])
    escritor.writerow(["Teclado", 3, 45.99])
    escritor.writerow(["Monitor", 1, 299.99])
    escritor.writerow(["Ratón", 5, 19.99])

# csv.reader: cada fila llega como una lista de strings.
with open(RUTA_VENTAS, "r", newline="", encoding="utf-8") as fichero:
    lector = csv.reader(fichero)
    cabecera = next(lector)
    print("Cabecera:", cabecera)
    for fila in lector:
        print("Fila:", fila)

# csv.DictReader: cada fila llega como un diccionario, usando la cabecera
# como claves. Caso real: filtrar las ventas por encima de un umbral.
umbral = 50.0
with open(RUTA_VENTAS, "r", newline="", encoding="utf-8") as fichero:
    lector_dict = csv.DictReader(fichero)
    ventas_grandes = [
        fila for fila in lector_dict if float(fila["precio"]) > umbral
    ]
print(f"Ventas con precio > {umbral}€:", ventas_grandes)


# ============================================================================
# 7. FICHEROS JSON — CONFIGURACIÓN DE LA APLICACIÓN
# ============================================================================
seccion("7. Ficheros JSON — configuración de la aplicación")

RUTA_CONFIG = BASE_DIR / "config.json"

configuracion = {
    "host": "localhost",
    "puerto": 8080,
    "debug": True,
    "modulos_activos": ["auth", "pagos", "notificaciones"],
}

# json.dump() escribe un objeto Python directamente en un fichero abierto.
with open(RUTA_CONFIG, "w", encoding="utf-8") as fichero:
    json.dump(configuracion, fichero, indent=2)

# json.load() hace el camino inverso: fichero -> diccionario de Python.
with open(RUTA_CONFIG, "r", encoding="utf-8") as fichero:
    config_leida = json.load(fichero)
print("Configuración leída:", config_leida)
print("¿Debug activo?", config_leida["debug"])

# json.dumps() (con 's' de string) sirve para obtener el JSON como texto,
# por ejemplo para mostrarlo formateado sin tocar ningún fichero.
print(json.dumps(configuracion, indent=2))

# El error más común: abrir un JSON sin encoding="utf-8". Si el fichero
# contiene tildes o eñes ("depuración", "notificación") y Python decide
# abrirlo con un encoding distinto según el sistema operativo, json.load()
# puede lanzar UnicodeDecodeError o, peor, leer caracteres corruptos sin
# avisar. Especificar encoding="utf-8" siempre elimina esa dependencia del
# sistema operativo de quien ejecuta el programa.


# ============================================================================
# 8. MANEJO DE ERRORES AL TRABAJAR CON FICHEROS
# ============================================================================
seccion("8. Manejo de errores al trabajar con ficheros")

# FileNotFoundError: leer algo que no existe.
try:
    with open(BASE_DIR / "no_existe.txt", "r", encoding="utf-8") as fichero:
        fichero.read()
except FileNotFoundError as error:
    print(f"FileNotFoundError: {error}")

# PermissionError: escribir en un fichero sin permisos de escritura.
ruta_solo_lectura = BASE_DIR / "solo_lectura.txt"
ruta_solo_lectura.write_text("contenido inicial\n", encoding="utf-8")
ruta_solo_lectura.chmod(0o444)
try:
    with open(ruta_solo_lectura, "w", encoding="utf-8") as fichero:
        fichero.write("esto no debería poder escribirse")
except PermissionError as error:
    print(f"PermissionError: {error}")
finally:
    ruta_solo_lectura.chmod(0o644)
    ruta_solo_lectura.unlink(missing_ok=True)

# IsADirectoryError: confundir una carpeta con un fichero.
try:
    with open(BASE_DIR, "r", encoding="utf-8") as fichero:
        fichero.read()
except IsADirectoryError as error:
    print(f"IsADirectoryError: {error}")

# Patrón correcto: el try/except envuelve TODA la operación de I/O (open
# incluido), no solo una línea suelta. El error puede saltar al abrir, al
# leer o al escribir, y cualquiera de los tres puntos necesita quedar
# cubierto por el mismo bloque.


# ============================================================================
# 9. TABLA COMPARATIVA — open() vs pathlib vs CASO DE USO
# ============================================================================
seccion("9. Tabla comparativa — open() vs pathlib vs caso de uso")

tabla = [
    ("Leer/escribir fichero de texto simple", "pathlib (read_text / write_text)"),
    ("Append, seek, control fino del cursor", "open() con with"),
    ("Datos estructurados (filas/columnas)", "csv"),
    ("Configuración o datos anidados", "json"),
    ("Rutas del sistema de ficheros", "pathlib.Path siempre"),
]
for situacion, recomendacion in tabla:
    print(f"  {situacion:45} -> {recomendacion}")


# Limpieza final: controlada por LIMPIAR_AL_FINALIZAR (ver cabecera del
# fichero). Con True no deja ficheros de ejemplo sueltos en el repo; con
# False los deja en esta carpeta para que los abras tú mismo.
ficheros_de_ejemplo = (RUTA_LOG, RUTA_VENTAS, RUTA_CONFIG)
if LIMPIAR_AL_FINALIZAR:
    for ruta in ficheros_de_ejemplo:
        ruta.unlink(missing_ok=True)
else:
    print("LIMPIAR_AL_FINALIZAR = False -> ficheros dejados en disco:")
    for ruta in ficheros_de_ejemplo:
        print(f"  {ruta}")


seccion("FIN — ya conoces los ficheros en Python al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
