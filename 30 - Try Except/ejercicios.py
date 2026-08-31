"""
================================================================================
 EJERCICIOS: TRY EXCEPT EN PYTHON
 Ejecutar: python3 ejercicios.py

 Completa cada ejercicio donde encuentres '...' y descomenta los print()
 para comprobar el resultado.
================================================================================
"""


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ──────────────────────────────────────────────
# EJERCICIO 1 — FÁCIL
# Convertir precio de texto a número
# ──────────────────────────────────────────────
seccion("EJERCICIO 1 — FÁCIL — Convertir precio de texto a número")


# Implementa convertir_precio(texto) que convierte un string a float.
# Si no es convertible, devuelve 0.0 y avisa con un print.
def convertir_precio(texto: str) -> float:
    ...


# print(f"Precio: {convertir_precio('19.99')}")
# convertir_precio("gratis")
# convertir_precio("")

# Resultado esperado:
# Precio: 19.99
# [AVISO] 'gratis' no es un precio válido, usando 0.0
# [AVISO] '' no es un precio válido, usando 0.0


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Calcular descuento con varios tipos de error
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — Calcular descuento con varios tipos de error")


# Implementa calcular_descuento(precio, porcentaje) que:
# - lanza TypeError si precio o porcentaje no son numéricos (isinstance)
# - lanza ValueError si porcentaje no está entre 0 y 100
# - lanza ZeroDivisionError si precio es 0 (al calcular precio / precio * porcentaje)
# - devuelve el importe del descuento en caso correcto
def calcular_descuento(precio, porcentaje):
    ...


# try:
#     print(f"Descuento: {calcular_descuento(150.0, 10)}€")
# except (TypeError, ValueError, ZeroDivisionError) as e:
#     print(f"[{type(e).__name__}] {e}")
#
# try:
#     calcular_descuento("150", 10)
# except (TypeError, ValueError, ZeroDivisionError) as e:
#     print(f"[{type(e).__name__}] {e}")
#
# try:
#     calcular_descuento(150.0, 200)
# except (TypeError, ValueError, ZeroDivisionError) as e:
#     print(f"[{type(e).__name__}] {e}")

# Resultado esperado:
# Descuento: 15.0€
# [TypeError] Los valores deben ser numéricos
# [ValueError] El porcentaje debe estar entre 0 y 100


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Buscar producto en catálogo
# ──────────────────────────────────────────────
seccion("EJERCICIO 3 — FÁCIL — Buscar producto en catálogo")

catalogo = {
    "Teclado": {"precio": 79.99, "stock": 5},
    "Ratón": {"precio": 29.99, "stock": 0},
}


# Implementa buscar_producto(catalogo, nombre) con try/except/else:
# - lanza KeyError si nombre no está en catalogo
# - en el else, imprime el precio y el stock disponible
def buscar_producto(catalogo: dict, nombre: str) -> None:
    ...


# buscar_producto(catalogo, "Teclado")
# buscar_producto(catalogo, "Monitor")

# Resultado esperado:
# Teclado — 79.99€, stock: 5
# [ERROR] 'Monitor' no está en el catálogo


# ──────────────────────────────────────────────
# EJERCICIO 4 — FÁCIL
# Procesar fichero con cierre garantizado
# ──────────────────────────────────────────────
seccion("EJERCICIO 4 — FÁCIL — Procesar fichero con cierre garantizado")


# Implementa procesar_fichero(nombre) con try/except/finally:
# - imprime "Fichero abierto"
# - lanza RuntimeError("Formato incorrecto") si nombre termina en ".txt"
# - si no hay error, imprime "Procesando..."
# - en finally, imprime siempre "Fichero cerrado"
def procesar_fichero(nombre: str) -> None:
    ...


# procesar_fichero("datos.csv")
# procesar_fichero("datos.txt")

# Resultado esperado para "datos.txt":
# Fichero abierto
# [ERROR] Formato incorrecto
# Fichero cerrado


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Crear usuario con validación completa
# ──────────────────────────────────────────────
seccion("EJERCICIO 5 — MEDIO — Crear usuario con validación completa")


# Implementa crear_usuario(nombre, email, edad) que valida:
# - nombre: no puede ser string vacío -> ValueError
# - email: debe contener "@" -> ValueError
# - edad: debe ser int entre 18 y 99 -> TypeError si no es int,
#   ValueError si está fuera de rango
# Si todo es correcto, devuelve un diccionario con los datos.
def crear_usuario(nombre: str, email: str, edad) -> dict:
    ...


# casos = [
#     ("Ana", "ana@ejemplo.com", 28),
#     ("", "x@x.com", 30),
#     ("Luis", "no-es-un-email", 30),
#     ("Marta", "marta@x.com", "treinta"),
#     ("Pedro", "pedro@x.com", 150),
# ]
# for nombre, email, edad in casos:
#     try:
#         print(f"Usuario creado: {crear_usuario(nombre, email, edad)}")
#     except (TypeError, ValueError) as e:
#         print(f"[{type(e).__name__}] {e}")

# Resultado esperado:
# Usuario creado: {'nombre': 'Ana', 'email': 'ana@ejemplo.com', 'edad': 28}
# [ValueError] El nombre no puede estar vacío
# [ValueError] Email inválido: 'no-es-un-email'
# [TypeError] La edad debe ser un entero
# [ValueError] Edad fuera de rango: 150


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# Cargar configuración con re-raise
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — Cargar configuración con re-raise")


# Implementa cargar_configuracion(ruta):
# - lanza FileNotFoundError si ruta == "missing.cfg"
# - lanza PermissionError si ruta == "protegido.cfg"
# - devuelve {"ok": True} en cualquier otro caso
def cargar_configuracion(ruta: str) -> dict:
    ...


# Implementa arrancar_app(ruta) que llama a cargar_configuracion, captura
# cualquier excepción, la loguea con
# print(f"[LOG] {type(e).__name__}: {e}") y la relanza.
def arrancar_app(ruta: str) -> dict:
    ...


# for ruta in ("missing.cfg", "protegido.cfg", "app.cfg"):
#     try:
#         print(f"Config: {arrancar_app(ruta)}")
#     except FileNotFoundError:
#         print("[ACCION] El fichero de config no existe, usando valores por defecto")
#     except PermissionError:
#         print("[ACCION] Sin permisos para leer la config, abortando arranque")

# Resultado esperado para "missing.cfg":
# [LOG] FileNotFoundError: Fichero no encontrado: missing.cfg
# [ACCION] El fichero de config no existe, usando valores por defecto


# ──────────────────────────────────────────────
# EJERCICIO 7 — MEDIO
# Transferencia bancaria con try/except/else/finally
# ──────────────────────────────────────────────
seccion("EJERCICIO 7 — MEDIO — Transferencia bancaria con try/except/else/finally")


# Implementa realizar_transferencia(origen, destino, importe) con el flujo
# completo:
# - try: valida importe > 0 (si no, ValueError), valida origen != destino
#   (si no, ValueError), simula la transferencia con un print
# - except ValueError as e: imprime el motivo del error
# - else: imprime confirmación con los datos de la transferencia
# - finally: imprime "Auditoría registrada" siempre
def realizar_transferencia(origen: str, destino: str, importe: float) -> None:
    ...


# realizar_transferencia("ES01", "ES02", 150.0)
# realizar_transferencia("ES01", "ES02", -10.0)
# realizar_transferencia("ES01", "ES01", 50.0)

# Resultado esperado (transferencia correcta):
# Transferencia de 150.0€ de 'ES01' a 'ES02' realizada
# Auditoría registrada


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Importar CSV en capas, sin detenerse al primer error
# ──────────────────────────────────────────────
seccion("EJERCICIO 8 — AVANZADO — Importar CSV en capas, sin detenerse al primer error")


# Capa más baja: puede lanzar ValueError o IndexError.
# parsear_csv("Teclado,79.99,5") -> {"nombre": "Teclado", "precio": 79.99, "stock": 5}
# parsear_csv("Teclado,precio_malo,5") -> lanza ValueError
# parsear_csv("Teclado,79.99") -> lanza IndexError (falta columna)
def parsear_csv(linea: str) -> dict:
    ...


# Capa media: llama a parsear_csv, captura y relanza con contexto.
def extraer_producto(linea: str) -> dict:
    ...


# Capa alta: llama a extraer_producto por cada línea, acumula errores sin
# detenerse en la primera línea que falla.
def importar_lineas(lineas: list) -> None:
    ...


# lineas = ["Teclado,79.99,5", "Ratón,precio_malo,12", "Monitor,349"]
# importar_lineas(lineas)

# Resultado esperado:
# Importado: {'nombre': 'Teclado', 'precio': 79.99, 'stock': 5}
# [ERROR línea 2] ValueError al parsear: ...
# [ERROR línea 3] IndexError al parsear: ...


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# Corregir anti-patrones de manejo de errores
# ──────────────────────────────────────────────
seccion("EJERCICIO 9 — AVANZADO — Corregir anti-patrones de manejo de errores")

# VERSIÓN CON ANTI-PATRONES — no ejecutar, solo como referencia:
#
# def procesar_pedido(pedido):
#     try:
#         cantidad = int(pedido["cantidad"])
#         precio = float(pedido["precio"])
#         total = cantidad * precio
#         print(f"Total: {total}€")
#     except Exception:
#         pass
#
# def obtener_cliente(clientes, id):
#     try:
#         return clientes[id]
#     except Exception as e:
#         print(f"Error: {e}")
#
# def calcular_iva(precio):
#     try:
#         return precio * 0.21
#     except Exception as e:
#         print(f"Algo falló: {e}")


# Reescribe las tres funciones aplicando las buenas prácticas: capturar
# solo los tipos específicos que pueden ocurrir, no silenciar errores con
# pass sin justificación, relanzar cuando el llamador necesita saber que
# algo falló, y mensajes de error útiles.
def procesar_pedido(pedido: dict) -> float:
    ...


def obtener_cliente(clientes: dict, id_cliente) -> dict:
    ...


def calcular_iva(precio) -> float:
    ...


# print(f"Total: {procesar_pedido({'cantidad': '3', 'precio': '19.99'})}€")
# try:
#     procesar_pedido({"cantidad": "tres", "precio": "19.99"})
# except (TypeError, ValueError) as e:
#     print(f"[{type(e).__name__}] {e}")
#
# clientes = {1: {"nombre": "Ana"}}
# print(obtener_cliente(clientes, 1))
# try:
#     obtener_cliente(clientes, 99)
# except KeyError as e:
#     print(f"[KeyError] {e}")
#
# print(f"IVA: {calcular_iva(100)}")
# try:
#     calcular_iva("cien")
# except TypeError as e:
#     print(f"[TypeError] {e}")

# Resultado esperado: cada caso válido devuelve su resultado, cada caso
# inválido lanza la excepción específica que le corresponde (sin silenciarla)


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Sistema de reintentos
# ──────────────────────────────────────────────
seccion("EJERCICIO 10 — EXPERTO — Sistema de reintentos")


# Implementa con_reintento(func, intentos, *args) que:
# - llama a func(*args) hasta intentos veces
# - si la función lanza una excepción, imprime
#   f"[REINTENTO {n}/{intentos}] Reintentando..." y vuelve a intentarlo
# - si todos los intentos fallan, relanza la última excepción
# - si la función tiene éxito, devuelve el resultado
def con_reintento(func, intentos: int, *args):
    ...


# contador = [0]
#
# def llamar_api(url):
#     contador[0] += 1
#     if contador[0] < 3:
#         raise ConnectionError(f"No se pudo conectar tras {contador[0]} intentos")
#     return {"status": "ok"}
#
# resultado = con_reintento(llamar_api, 3, "https://api.ejemplo.com")
# print(f"Respuesta recibida: {resultado}")
#
# def siempre_falla(url):
#     raise ConnectionError(f"No se pudo conectar tras 3 intentos")
#
# try:
#     con_reintento(siempre_falla, 3, "https://api.ejemplo.com")
# except ConnectionError as e:
#     print(f"[ERROR FINAL] {type(e).__name__}: {e}")

# Resultado esperado (3 intentos, falla 2 veces):
# [REINTENTO 1/3] Reintentando...
# [REINTENTO 2/3] Reintentando...
# Respuesta recibida: {'status': 'ok'}
#
# Resultado esperado (siempre falla, 3 intentos):
# [REINTENTO 1/3] Reintentando...
# [REINTENTO 2/3] Reintentando...
# [REINTENTO 3/3] Reintentando...
# [ERROR FINAL] ConnectionError: No se pudo conectar tras 3 intentos
