"""
================================================================================
 EJERCICIOS: EXCEPCIONES PERSONALIZADAS EN PYTHON
 Casos reales — de fácil a experto
================================================================================

Este fichero está pensado para ejecutarse de principio a fin:

    python3 ejercicios.py

Completa cada ejercicio donde encuentres "..." y descomenta los print()
para comprobar el resultado.
================================================================================
"""

import json


def seccion(titulo: str) -> None:
    """Pequeño helper para imprimir cabeceras y que la salida sea legible."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# EJERCICIO 1 — FÁCIL — Excepción personalizada básica
# ============================================================================
seccion("EJERCICIO 1 — FÁCIL — Excepción personalizada básica")

# API de usuarios. Cuando se busca un usuario que no existe, el error debe
# decir claramente qué usuario se buscó, no un "Exception" genérico.

# Crea UsuarioNoEncontradoError(Exception) con __init__(self, usuario_id: str)
# que construya el mensaje "Usuario '{usuario_id}' no encontrado"
class UsuarioNoEncontradoError(Exception):
    ...

# Lánzala y captúrala mostrando el mensaje
# try:
#     raise UsuarioNoEncontradoError("u-4821")
# except UsuarioNoEncontradoError as e:
#     print(e)

# Resultado esperado: Usuario 'u-4821' no encontrado


# ============================================================================
# EJERCICIO 2 — FÁCIL — Jerarquía de dos niveles
# ============================================================================
seccion("EJERCICIO 2 — FÁCIL — Jerarquía de dos niveles")

# App de inventario. Necesitas distinguir un producto agotado de un
# producto que directamente no existe, pero también poder capturar
# "cualquier error de inventario" de una sola vez.

# Crea InventarioError(Exception) como raíz
class InventarioError(Exception):
    ...

# Crea ProductoAgotadoError(InventarioError) y ProductoNoExisteError(InventarioError)
# con __init__ que reciba el nombre del producto / sku y construya un mensaje
class ProductoAgotadoError(InventarioError):
    ...

class ProductoNoExisteError(InventarioError):
    ...

# Lanza cada una en un try/except: primero captura el tipo específico,
# luego captura InventarioError para demostrar la jerarquía
# for excepcion in (ProductoAgotadoError("Teclado"), ProductoNoExisteError("SKU-999")):
#     try:
#         raise excepcion
#     except ProductoAgotadoError as e:
#         print("Específico (agotado):", e)
#     except InventarioError as e:
#         print(f"Genérico ({type(e).__name__}):", e)


# ============================================================================
# EJERCICIO 3 — FÁCIL — Excepción con atributos propios
# ============================================================================
seccion("EJERCICIO 3 — FÁCIL — Excepción con atributos propios")

# Sistema de archivos. Al subir un fichero demasiado grande, el error debe
# llevar el nombre, el tamaño real y el límite permitido como datos, no
# solo como texto.

# Crea ArchivoDemasiadoGrandeError(Exception) con __init__(self, nombre_archivo: str,
# tamaño_mb: float, limite_mb: float) y mensaje:
# "El archivo '{nombre}' pesa {tamaño}MB, límite es {limite}MB"
class ArchivoDemasiadoGrandeError(Exception):
    ...

# Lánzala con datos reales y accede a sus atributos desde el except
# try:
#     raise ArchivoDemasiadoGrandeError("informe.zip", 512.3, 200.0)
# except ArchivoDemasiadoGrandeError as e:
#     print(e)
#     print(e.nombre_archivo, e.tamaño_mb, e.limite_mb)


# ============================================================================
# EJERCICIO 4 — MEDIO — try / except / else / finally
# ============================================================================
seccion("EJERCICIO 4 — MEDIO — try / except / else / finally")

# Lectura de un fichero de configuración en formato JSON.

def leer_configuracion(contenido_json):
    # try: parsea contenido_json con json.loads()
    # except json.JSONDecodeError: imprime "JSON inválido: {e}"
    # else: imprime "Configuración cargada: {config}"
    # finally: imprime siempre "Operación de lectura finalizada"
    ...

# Pruébalo con un JSON válido y con uno inválido
# leer_configuracion('{"debug": true, "puerto": 8080}')
# leer_configuracion('esto no es json')

# Resultado esperado (2ª llamada): "JSON inválido: ..." y luego
# "Operación de lectura finalizada" en ambos casos


# ============================================================================
# EJERCICIO 5 — MEDIO — Encadenamiento con raise ... from ...
# ============================================================================
seccion("EJERCICIO 5 — MEDIO — Encadenamiento con raise ... from ...")

# Cliente de base de datos. conectar_db() falla a bajo nivel; obtener_usuario()
# no debe dejar que ese detalle se filtre tal cual hacia el llamador.

class DatabaseError(Exception):
    ...

def conectar_db(host):
    raise ConnectionRefusedError("Puerto cerrado")

def obtener_usuario(usuario_id):
    # Llama a conectar_db("localhost"); si falla, envuelve el error en
    # DatabaseError("No se pudo conectar a la BD") usando raise ... from e
    ...

# try:
#     obtener_usuario("u-1")
# except DatabaseError as e:
#     print(str(e))
#     print(e.__cause__)


# ============================================================================
# EJERCICIO 6 — MEDIO — Validación con múltiples excepciones propias
# ============================================================================
seccion("EJERCICIO 6 — MEDIO — Validación con múltiples excepciones propias")

# Formulario de registro con tres reglas de negocio distintas.

class ValidacionError(Exception):
    ...

class EmailInvalidoError(ValidacionError):
    ...

class ContraseñaDemasiadoCortaError(ValidacionError):
    ...

class EdadMinimaError(ValidacionError):
    ...

def validar_registro(email, password, edad):
    # Lanza EmailInvalidoError si no hay "@" en email
    # Lanza ContraseñaDemasiadoCortaError si len(password) < 8
    # Lanza EdadMinimaError si edad < 18
    ...

# Prueba los tres casos por separado
# for email, password, edad in (("sin-arroba", "12345678", 25), ("ana@mail.com", "123", 25), ("ana@mail.com", "12345678", 15)):
#     try:
#         validar_registro(email, password, edad)
#     except ValidacionError as e:
#         print(f"{type(e).__name__}: {e}")


# ============================================================================
# EJERCICIO 7 — AVANZADO — re-raise sin alterar el traceback
# ============================================================================
seccion("EJERCICIO 7 — AVANZADO — re-raise sin alterar el traceback")

# Middleware de logging genérico para cualquier función de la app.

def procesar_con_log(func, *args):
    # try: ejecuta func(*args) y devuelve el resultado
    # except Exception as e: imprime "[LOG] {type(e).__name__}: {e}" y
    # relanza con "raise" (sin argumento) para conservar el traceback original
    ...

def funcion_que_falla(x):
    return 10 / x  # ZeroDivisionError si x == 0

# try:
#     procesar_con_log(funcion_que_falla, 0)
# except ZeroDivisionError as e:
#     print("Traceback conservado, error final:", e)


# ============================================================================
# EJERCICIO 8 — AVANZADO — add_note(): enriquecer con contexto adicional
# ============================================================================
seccion("EJERCICIO 8 — AVANZADO — add_note(): enriquecer con contexto adicional")

# Worker que procesa pedidos en lote; si uno falla, hay que saber cuál.

class PedidoError(Exception):
    ...

def procesar_pedido_individual(pedido):
    if pedido["stock"] <= 0:
        raise PedidoError(f"Sin stock para {pedido['producto']}")

def procesar_lote(pedidos):
    # Itera sobre pedidos con su índice; si procesar_pedido_individual falla,
    # captura la excepción, añade dos notas con e.add_note() (id del pedido
    # e índice en el lote) y relánzala
    ...

# pedidos = [
#     {"id": "P-1", "producto": "Ratón", "stock": 5},
#     {"id": "P-2", "producto": "Teclado", "stock": 0},
# ]
# try:
#     procesar_lote(pedidos)
# except PedidoError as e:
#     print(e)
#     print(e.__notes__)


# ============================================================================
# EJERCICIO 9 — EXPERTO — ExceptionGroup y except*
# ============================================================================
seccion("EJERCICIO 9 — EXPERTO — ExceptionGroup y except*")

# API de registro que reporta TODOS los campos inválidos de una vez.

class EmailInvalidoError2(Exception):
    ...

class ContraseñaInvalidaError(Exception):
    ...

class EdadInvalidaError(Exception):
    ...

def validar_formulario(datos: dict):
    # Comprueba email (debe contener "@"), password (len >= 8) y edad
    # (>= 18). Recopila TODOS los errores en una lista, sin parar al
    # primero, y si hay alguno lanza ExceptionGroup("Errores de validación", errores)
    ...

# datos_invalidos = {"email": "sin-arroba", "password": "123", "edad": 10}
# try:
#     validar_formulario(datos_invalidos)
# except* EmailInvalidoError2 as eg:
#     print("Emails:", [str(e) for e in eg.exceptions])
# except* ContraseñaInvalidaError as eg:
#     print("Contraseñas:", [str(e) for e in eg.exceptions])
# except* EdadInvalidaError as eg:
#     print("Edades:", [str(e) for e in eg.exceptions])


# ============================================================================
# EJERCICIO 10 — EXPERTO — Registro centralizado de excepciones
# ============================================================================
seccion("EJERCICIO 10 — EXPERTO — Registro centralizado de excepciones")

# Servidor web simplificado con un manejador global de errores por tipo.

class AppError(Exception):
    ...

class PagoError(AppError):
    ...

class StockError(AppError):
    ...

class ManejadorErrores:
    def __init__(self):
        # Crea un diccionario vacío para mapear tipo_error -> handler
        ...

    def registrar(self, tipo_error, handler):
        # Registra handler(e) para tipo_error
        ...

    def manejar(self, e):
        # Busca el handler más específico para type(e) usando isinstance
        # y lo ejecuta; si no hay ninguno, relanza la excepción (raise)
        ...

# manejador = ManejadorErrores()
# manejador.registrar(PagoError, lambda e: print(f"[PAGO] {e}"))
# manejador.registrar(StockError, lambda e: print(f"[STOCK] {e}"))
# manejador.registrar(AppError, lambda e: print(f"[APP] {e}"))

# for error in (PagoError("tarjeta rechazada"), StockError("sin stock"), AppError("fallo genérico")):
#     manejador.manejar(error)

# try:
#     manejador.manejar(ValueError("no registrado"))
# except ValueError as e:
#     print("Relanzada:", e)


seccion("FIN — completa los ejercicios y compáralos con ejercicios_resueltos.py")
