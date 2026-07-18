"""
================================================================================
 EJERCICIOS RESUELTOS: EXCEPCIONES PERSONALIZADAS EN PYTHON
 Casos reales — de fácil a experto
================================================================================

Este fichero está pensado para ejecutarse de principio a fin:

    python3 ejercicios_resueltos.py

Cada ejercicio imprime resultados reales para confirmar que funciona.
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

# SOLUCIÓN
class UsuarioNoEncontradoError(Exception):
    def __init__(self, usuario_id: str):
        self.usuario_id = usuario_id
        super().__init__(f"Usuario '{usuario_id}' no encontrado")

try:
    raise UsuarioNoEncontradoError("u-4821")
except UsuarioNoEncontradoError as e:
    print(e)


# ============================================================================
# EJERCICIO 2 — FÁCIL — Jerarquía de dos niveles
# ============================================================================
seccion("EJERCICIO 2 — FÁCIL — Jerarquía de dos niveles")

# SOLUCIÓN
class InventarioError(Exception):
    ...

class ProductoAgotadoError(InventarioError):
    def __init__(self, producto: str):
        self.producto = producto
        super().__init__(f"Producto '{producto}' agotado")

class ProductoNoExisteError(InventarioError):
    def __init__(self, sku: str):
        self.sku = sku
        super().__init__(f"Producto con SKU '{sku}' no existe")

for excepcion in (ProductoAgotadoError("Teclado"), ProductoNoExisteError("SKU-999")):
    try:
        raise excepcion
    except ProductoAgotadoError as e:
        print("Específico (agotado):", e)
    except InventarioError as e:
        print(f"Genérico ({type(e).__name__}):", e)


# ============================================================================
# EJERCICIO 3 — FÁCIL — Excepción con atributos propios
# ============================================================================
seccion("EJERCICIO 3 — FÁCIL — Excepción con atributos propios")

# SOLUCIÓN
class ArchivoDemasiadoGrandeError(Exception):
    def __init__(self, nombre_archivo: str, tamaño_mb: float, limite_mb: float):
        self.nombre_archivo = nombre_archivo
        self.tamaño_mb = tamaño_mb
        self.limite_mb = limite_mb
        super().__init__(f"El archivo '{nombre_archivo}' pesa {tamaño_mb}MB, límite es {limite_mb}MB")

try:
    raise ArchivoDemasiadoGrandeError("informe.zip", 512.3, 200.0)
except ArchivoDemasiadoGrandeError as e:
    print(e)
    print(e.nombre_archivo, e.tamaño_mb, e.limite_mb)


# ============================================================================
# EJERCICIO 4 — MEDIO — try / except / else / finally
# ============================================================================
seccion("EJERCICIO 4 — MEDIO — try / except / else / finally")

# SOLUCIÓN
def leer_configuracion(contenido_json):
    try:
        config = json.loads(contenido_json)
    except json.JSONDecodeError as e:
        print(f"JSON inválido: {e}")
    else:
        print(f"Configuración cargada: {config}")
    finally:
        print("Operación de lectura finalizada")

leer_configuracion('{"debug": true, "puerto": 8080}')
leer_configuracion('esto no es json')


# ============================================================================
# EJERCICIO 5 — MEDIO — Encadenamiento con raise ... from ...
# ============================================================================
seccion("EJERCICIO 5 — MEDIO — Encadenamiento con raise ... from ...")

# SOLUCIÓN
class DatabaseError(Exception):
    ...

def conectar_db(host):
    raise ConnectionRefusedError("Puerto cerrado")

def obtener_usuario(usuario_id):
    try:
        conectar_db("localhost")
    except ConnectionRefusedError as e:
        raise DatabaseError("No se pudo conectar a la BD") from e

try:
    obtener_usuario("u-1")
except DatabaseError as e:
    print(str(e))
    print(e.__cause__)


# ============================================================================
# EJERCICIO 6 — MEDIO — Validación con múltiples excepciones propias
# ============================================================================
seccion("EJERCICIO 6 — MEDIO — Validación con múltiples excepciones propias")

# SOLUCIÓN
class ValidacionError(Exception):
    ...

class EmailInvalidoError(ValidacionError):
    ...

class ContraseñaDemasiadoCortaError(ValidacionError):
    ...

class EdadMinimaError(ValidacionError):
    ...

def validar_registro(email, password, edad):
    if "@" not in email:
        raise EmailInvalidoError("Email inválido: debe contener '@'")
    if len(password) < 8:
        raise ContraseñaDemasiadoCortaError("Contraseña demasiado corta: mínimo 8 caracteres")
    if edad < 18:
        raise EdadMinimaError("Edad mínima requerida: 18 años")

for email, password, edad in (("sin-arroba", "12345678", 25), ("ana@mail.com", "123", 25), ("ana@mail.com", "12345678", 15)):
    try:
        validar_registro(email, password, edad)
    except ValidacionError as e:
        print(f"{type(e).__name__}: {e}")


# ============================================================================
# EJERCICIO 7 — AVANZADO — re-raise sin alterar el traceback
# ============================================================================
seccion("EJERCICIO 7 — AVANZADO — re-raise sin alterar el traceback")

# SOLUCIÓN
def procesar_con_log(func, *args):
    try:
        return func(*args)
    except Exception as e:
        print(f"[LOG] {type(e).__name__}: {e}")
        raise  # relanza la excepción original sin alterar el traceback

def funcion_que_falla(x):
    return 10 / x  # ZeroDivisionError si x == 0

try:
    procesar_con_log(funcion_que_falla, 0)
except ZeroDivisionError as e:
    print("Traceback conservado, error final:", e)


# ============================================================================
# EJERCICIO 8 — AVANZADO — add_note(): enriquecer con contexto adicional
# ============================================================================
seccion("EJERCICIO 8 — AVANZADO — add_note(): enriquecer con contexto adicional")

# SOLUCIÓN
class PedidoError(Exception):
    ...

def procesar_pedido_individual(pedido):
    if pedido["stock"] <= 0:
        raise PedidoError(f"Sin stock para {pedido['producto']}")

def procesar_lote(pedidos):
    for i, pedido in enumerate(pedidos):
        try:
            procesar_pedido_individual(pedido)
        except PedidoError as e:
            e.add_note(f"ID del pedido: {pedido['id']}")
            e.add_note(f"Índice en lote: {i}")
            raise

pedidos = [
    {"id": "P-1", "producto": "Ratón", "stock": 5},
    {"id": "P-2", "producto": "Teclado", "stock": 0},
]
try:
    procesar_lote(pedidos)
except PedidoError as e:
    print(e)
    print(e.__notes__)


# ============================================================================
# EJERCICIO 9 — EXPERTO — ExceptionGroup y except*
# ============================================================================
seccion("EJERCICIO 9 — EXPERTO — ExceptionGroup y except*")

# SOLUCIÓN
class EmailInvalidoError2(Exception):
    ...

class ContraseñaInvalidaError(Exception):
    ...

class EdadInvalidaError(Exception):
    ...

def validar_formulario(datos: dict):
    errores = []
    if "@" not in datos.get("email", ""):
        errores.append(EmailInvalidoError2("Email inválido: debe contener '@'"))
    if len(datos.get("password", "")) < 8:
        errores.append(ContraseñaInvalidaError("Contraseña inválida: mínimo 8 caracteres"))
    if datos.get("edad", 0) < 18:
        errores.append(EdadInvalidaError("Edad inválida: mínimo 18 años"))
    if errores:
        raise ExceptionGroup("Errores de validación", errores)

datos_invalidos = {"email": "sin-arroba", "password": "123", "edad": 10}
try:
    validar_formulario(datos_invalidos)
except* EmailInvalidoError2 as eg:
    print("Emails:", [str(e) for e in eg.exceptions])
except* ContraseñaInvalidaError as eg:
    print("Contraseñas:", [str(e) for e in eg.exceptions])
except* EdadInvalidaError as eg:
    print("Edades:", [str(e) for e in eg.exceptions])


# ============================================================================
# EJERCICIO 10 — EXPERTO — Registro centralizado de excepciones
# ============================================================================
seccion("EJERCICIO 10 — EXPERTO — Registro centralizado de excepciones")

# SOLUCIÓN
class AppError(Exception):
    ...

class PagoError(AppError):
    ...

class StockError(AppError):
    ...

class ManejadorErrores:
    def __init__(self):
        self.handlers = {}

    def registrar(self, tipo_error, handler):
        self.handlers[tipo_error] = handler

    def manejar(self, e):
        for tipo_error, handler in self.handlers.items():
            if isinstance(e, tipo_error):
                handler(e)
                return
        raise e

manejador = ManejadorErrores()
manejador.registrar(PagoError, lambda e: print(f"[PAGO] {e}"))
manejador.registrar(StockError, lambda e: print(f"[STOCK] {e}"))
manejador.registrar(AppError, lambda e: print(f"[APP] {e}"))

for error in (PagoError("tarjeta rechazada"), StockError("sin stock"), AppError("fallo genérico")):
    manejador.manejar(error)

try:
    manejador.manejar(ValueError("no registrado"))
except ValueError as e:
    print("Relanzada:", e)


seccion("FIN — todos los ejercicios resueltos")
