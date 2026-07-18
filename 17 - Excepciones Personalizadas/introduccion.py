"""
================================================================================
 EXCEPCIONES PERSONALIZADAS EN PYTHON 3.14
 Ejecutar: python3 introduccion.py
================================================================================
"""

import traceback


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA SIN EXCEPCIONES PERSONALIZADAS
# ============================================================================
seccion("1. El problema sin excepciones personalizadas")

# Caso real: un flujo de pago de e-commerce. Cobrar la tarjeta y reducir
# el stock son dos cosas MUY distintas, pero si ambas lanzan la misma
# Exception genérica, el except no puede diferenciarlas.
def procesar_pedido_v1(producto, cantidad, disponible):
    try:
        if cantidad > disponible:
            raise Exception("Pago fallido")  # en realidad es un problema de STOCK
        print(f"  Pago de {cantidad} unidades de '{producto}' realizado con éxito")
    except Exception as e:
        # Este bloque asume que CUALQUIER error aquí es un fallo de tarjeta.
        print(f"  [AVISO AL CLIENTE] Tu pago ha sido rechazado: {e}")

procesar_pedido_v1("Teclado mecánico", 5, 2)

# El cliente ve "tu pago ha sido rechazado", prueba con otra tarjeta y
# sigue fallando, porque el problema real es que NO HAY STOCK, no la
# tarjeta. Soporte recibe tickets de "mi tarjeta no funciona" durante
# días hasta que alguien revisa el código y descubre que el mensaje
# miente. Un except Exception genérico no puede distinguir un problema
# de stock de un problema de pago: ambos parecen lo mismo desde fuera.


# ============================================================================
# 2. JERARQUÍA BASE: AppError Y SUBCLASES DIRECTAS
# ============================================================================
seccion("2. Jerarquía base: AppError y subclases directas")

class AppError(Exception):
    """Excepción base de la aplicación. Todas las demás heredan de esta."""
    pass

class PagoError(AppError):
    pass

class StockError(AppError):
    pass

class AutenticacionError(AppError):
    pass

def operacion(tipo):
    if tipo == "pago":
        raise PagoError("La pasarela de pago rechazó la operación")
    elif tipo == "stock":
        raise StockError("No queda stock suficiente")
    elif tipo == "auth":
        raise AutenticacionError("Token de sesión caducado")

for tipo in ("pago", "stock", "auth"):
    try:
        operacion(tipo)
    except PagoError as e:
        print(f"  [PagoError específico] -> {e}")
    except AppError as e:
        print(f"  [AppError genérico: {type(e).__name__}] -> {e}")

# Ahora sí se puede reaccionar distinto según el nivel de captura:
# except PagoError solo atrapa pagos, except AppError atrapa cualquier
# error de la app (pago, stock, auth...), y except Exception seguiría
# atrapando además errores que ni siquiera son nuestros (bugs, red...).


# ============================================================================
# 3. EXCEPCIONES CON DATOS: AÑADIR ATRIBUTOS PROPIOS
# ============================================================================
seccion("3. Excepciones con datos propios")

# Exception básica solo tiene un mensaje de texto. En producción necesitas
# saber qué pedido falló, qué producto se agotó, con qué código de banco.
class PagoRechazadoError(PagoError):
    def __init__(self, pedido_id: str, motivo: str, codigo_banco: int):
        self.pedido_id = pedido_id
        self.motivo = motivo
        self.codigo_banco = codigo_banco
        super().__init__(f"Pago rechazado para pedido {pedido_id}: {motivo} (código {codigo_banco})")

    def __repr__(self):
        return (f"PagoRechazadoError(pedido_id={self.pedido_id!r}, "
                f"motivo={self.motivo!r}, codigo_banco={self.codigo_banco})")

class StockInsuficienteError(StockError):
    def __init__(self, producto: str, solicitado: int, disponible: int):
        self.producto = producto
        self.solicitado = solicitado
        self.disponible = disponible
        super().__init__(f"Stock insuficiente para '{producto}': solicitado={solicitado}, disponible={disponible}")

try:
    raise PagoRechazadoError("PED-9001", "fondos insuficientes", 51)
except PagoRechazadoError as e:
    print(f"  Pedido: {e.pedido_id} | Motivo: {e.motivo} | Código banco: {e.codigo_banco}")
    print(f"  Mensaje completo: {e}")

try:
    raise StockInsuficienteError("Teclado mecánico", 5, 2)
except StockInsuficienteError as e:
    print(f"  Producto: {e.producto} | Solicitado: {e.solicitado} | Disponible: {e.disponible}")
    if e.disponible > 0:
        print(f"  Sugerencia: ofrecer las {e.disponible} unidades disponibles")

# Con estos atributos, el except ya no solo sabe QUE algo falló, sabe
# EXACTAMENTE qué datos necesita para reaccionar (revertir un pedido
# concreto, ofrecer una alternativa concreta), sin tener que parsear
# el mensaje de texto con regex como se hacía en el punto 1.


# ============================================================================
# 4. raise ... from ...: ENCADENAMIENTO DE EXCEPCIONES
# ============================================================================
seccion("4. raise ... from ...: encadenamiento de excepciones")

# Caso real: el conector a la pasarela de pago (una librería externa)
# lanza un ConnectionError de bajo nivel. La capa de negocio no debe
# dejar que ese detalle de implementación se filtre hacia arriba tal
# cual: lo envuelve en su propia excepción de dominio.
def conectar_pasarela_pago():
    raise ConnectionError("Timeout conectando a pasarela.pagos.com:443")

def cobrar_con_causa(monto):
    try:
        conectar_pasarela_pago()
    except ConnectionError as error_original:
        raise PagoError(f"No se pudo procesar el cobro de {monto}€") from error_original

try:
    cobrar_con_causa(49.99)
except PagoError as e:
    print("  Con 'from error_original':")
    print(f"    str(e): {e}")
    print(f"    e.__cause__: {e.__cause__!r}")

def cobrar_sin_causa(monto):
    try:
        conectar_pasarela_pago()
    except ConnectionError:
        raise PagoError(f"No se pudo procesar el cobro de {monto}€") from None

try:
    cobrar_sin_causa(49.99)
except PagoError as e:
    print("  Con 'from None':")
    print(f"    str(e): {e}")
    print(f"    e.__cause__: {e.__cause__!r}")

# 'from error_original' conserva la causa real en __cause__: útil en logs
# internos para depurar la cadena completa hasta la librería externa.
# 'from None' suprime la causa deliberadamente: úsalo cuando el detalle
# interno (que usamos tal librería, tal protocolo) es irrelevante para
# quien llama, y solo le importa el error de negocio.


# ============================================================================
# 5. try / except / else / finally: EL FLUJO COMPLETO
# ============================================================================
seccion("5. try / except / else / finally: el flujo completo")

def cobrar(pedido):
    if pedido["id"] == "PED-001":
        raise PagoRechazadoError(pedido["id"], "fondos insuficientes", 51)
    print(f"  Cobro de {pedido['importe']}€ realizado")

def reducir_stock(pedido):
    if pedido["id"] == "PED-002":
        raise StockInsuficienteError(pedido["producto"], pedido["cantidad"], 1)
    print(f"  Stock de '{pedido['producto']}' reducido en {pedido['cantidad']} unidades")

def procesar_pedido(pedido):
    print(f"\n  Procesando {pedido['id']}...")
    try:
        cobrar(pedido)
        reducir_stock(pedido)
    except PagoRechazadoError as e:
        print(f"  [ROLLBACK] Revirtiendo reserva de stock para {e.pedido_id}")
        print(f"  [NOTIFICACION] Aviso al cliente: pago rechazado ({e.motivo})")
    except StockInsuficienteError as e:
        print(f"  [ROLLBACK] Liberando el pago ya cobrado")
        print(f"  [SUGERENCIA] '{e.producto}' agotado, ofrecer alternativa")
    except AppError as e:
        print(f"  [LOG] Error de aplicación no contemplado: {e}")
    else:
        print(f"  [OK] Pedido {pedido['id']} confirmado")
        print(f"  [EMAIL] Enviando email de confirmación al cliente")
    finally:
        print(f"  [CLEANUP] Cerrando conexión con la pasarela de pago")

pedido_ok = {"id": "PED-000", "producto": "Ratón inalámbrico", "cantidad": 3, "importe": 25.50}
pedido_pago_rechazado = {"id": "PED-001", "producto": "Monitor 4K", "cantidad": 1, "importe": 349.00}
pedido_sin_stock = {"id": "PED-002", "producto": "Teclado mecánico", "cantidad": 5, "importe": 89.99}

for pedido in (pedido_ok, pedido_pago_rechazado, pedido_sin_stock):
    procesar_pedido(pedido)

# NOTA (PEP 765, Python 3.14): usar return/break/continue dentro de un
# finally es un anti-patrón que SUPRIME en silencio la excepción o el
# valor de retorno del try. Desde Python 3.14 el compilador emite un
# SyntaxWarning para avisarlo en tiempo de compilación.
def bool_return():
    try:
        return True
    finally:
      return False  # SyntaxWarning: 'return' in a 'finally' block

print("\n  bool_return():", bool_return())
# A pesar de que el try devuelve True, finally lo pisa y la función
# devuelve False. finally siempre tiene la última palabra, y aquí la usa
# para tirar el resultado real sin que salte ningún error en runtime.


# ============================================================================
# 6. re-raise Y CUÁNDO NO CAPTURAR
# ============================================================================
seccion("6. re-raise y cuándo no capturar")

def logger_ficticio(mensaje):
    print(f"  [LOG] {mensaje}")

def procesar_pedido_estricto(pedido):
    if pedido["id"] == "PED-666":
        raise PagoRechazadoError(pedido["id"], "tarjeta caducada", 12)
    if pedido["id"] == "PED-777":
        raise StockInsuficienteError("Monitor 4K", 3, 0)
    print(f"  Pedido {pedido['id']} procesado sin incidencias")

def procesar_con_log(pedido):
    try:
        procesar_pedido_estricto(pedido)
    except AppError as e:
        # el middleware NO distingue el subtipo: solo loguea y deja pasar
        logger_ficticio(f"{type(e).__name__}: {e}")
        raise  # re-raise sin argumento: conserva TIPO y traceback originales

# El mismo middleware procesa dos tipos de error distintos. raise no los
# "generaliza" a ninguno común: cada uno sigue siendo exactamente lo que
# era y se puede capturar por su tipo específico fuera del middleware.
for pedido in ({"id": "PED-666"}, {"id": "PED-777"}):
    try:
        procesar_con_log(pedido)
    except PagoRechazadoError as e:
        print(f"  Capturado fuera como PagoRechazadoError: {e}")
    except StockInsuficienteError as e:
        print(f"  Capturado fuera como StockInsuficienteError: {e}")

# Anti-patrón: capturar Exception y NO relanzar. Oculta bugs inesperados.
def procesar_silenciando_todo(pedido):
    try:
        procesar_pedido_estricto(pedido)
    except Exception as e:
        print(f"  Algo falló pero seguimos como si nada: {e}")
        # sin raise: el llamador nunca se entera de que algo fue mal

procesar_silenciando_todo({"id": "PED-666"})
print("  El programa continúa como si el pedido se hubiera procesado bien")

# Esto es peligroso: cualquier código que dependa de que el pedido se
# procesó correctamente actuará sobre datos falsos, y el bug quedará
# invisible hasta que alguien audite manualmente los pedidos.


# ============================================================================
# 7. add_note(): ENRIQUECER EXCEPCIONES YA CAPTURADAS (Python 3.11+)
# ============================================================================
seccion("7. add_note(): enriquecer excepciones ya capturadas")

# Caso real: un worker procesa una lista de pedidos en lote. Cuando uno
# falla, quieres saber qué pedido y en qué posición del lote, sin crear
# una excepción nueva que oculte el tipo original.
def procesar_pedido_lote(pedido):
    if pedido["id"] == "PED-500":
        raise StockInsuficienteError(pedido["producto"], 10, 0)
    print(f"  Pedido {pedido['id']} procesado en el lote")

def procesar_lote(pedidos):
    for indice, pedido in enumerate(pedidos):
        try:
            procesar_pedido_lote(pedido)
        except AppError as e:
            e.add_note(f"Pedido afectado: {pedido['id']}")
            e.add_note(f"Posición en el lote: {indice + 1} de {len(pedidos)}")
            raise

pedidos_lote = [
    {"id": "PED-499", "producto": "Cable USB-C"},
    {"id": "PED-500", "producto": "Monitor 4K"},
]

try:
    procesar_lote(pedidos_lote)
except AppError as e:
    print(f"  Excepción: {type(e).__name__}: {e}")
    print(f"  e.__notes__: {e.__notes__}")
    print("  Traceback estándar (las notas aparecen al final):")
    for linea in traceback.format_exception(type(e), e, e.__traceback__):
        print("   ", linea.rstrip())

# add_note() añade contexto a la excepción ACTUAL, sin perder su tipo ni
# su traceback. Es distinto de 'raise ... from ...' (sección 4), que crea
# una excepción NUEVA con __cause__ apuntando a la original.


# ============================================================================
# 8. ExceptionGroup Y except*: MÚLTIPLES ERRORES A LA VEZ (Python 3.11+)
# ============================================================================
seccion("8. ExceptionGroup y except*: múltiples errores a la vez")

# Caso real: validación de un formulario de registro. Reportar solo el
# primer campo inválido obliga al usuario a corregir uno, reenviar,
# descubrir el siguiente error, reenviar otra vez... Mejor reportarlos
# todos de una vez.
class ValidacionError(AppError):
    pass

class EmailInvalidoError(ValidacionError):
    def __init__(self, email):
        self.email = email
        super().__init__(f"Email inválido: '{email}'")

class ContraseñaDemasiadoCortaError(ValidacionError):
    def __init__(self, password):
        self.password = password
        super().__init__(f"Contraseña demasiado corta ({len(password)} caracteres, mínimo 8)")

class EdadMinimaError(ValidacionError):
    def __init__(self, edad):
        self.edad = edad
        super().__init__(f"Edad no permitida: {edad} (mínimo 18)")

def email_valido(email):
    return "@" in email and "." in email.split("@")[-1]

def password_valida(password):
    return len(password) >= 8

def edad_valida(edad):
    return isinstance(edad, int) and edad >= 18

def validar_formulario(datos):
    errores = []
    if not email_valido(datos["email"]):
        errores.append(EmailInvalidoError(datos["email"]))
    if not password_valida(datos["password"]):
        errores.append(ContraseñaDemasiadoCortaError(datos["password"]))
    if not edad_valida(datos["edad"]):
        errores.append(EdadMinimaError(datos["edad"]))
    if errores:
        raise ExceptionGroup("Errores de validación del formulario", errores)

datos_formulario = {"email": "no-es-un-email", "password": "1234", "edad": 15}

try:
    validar_formulario(datos_formulario)
except* EmailInvalidoError as eg:
    print(f"  Emails inválidos: {[str(e) for e in eg.exceptions]}")
except* ContraseñaDemasiadoCortaError as eg:
    print(f"  Contraseñas inválidas: {[str(e) for e in eg.exceptions]}")
except* EdadMinimaError as eg:
    print(f"  Edades inválidas: {[str(e) for e in eg.exceptions]}")

# except* y except normal NO se pueden mezclar en el mismo try: o el
# try captura con except (una sola excepción) o con except* (un grupo),
# nunca ambos a la vez.


# ============================================================================
# 9. __str__ Y __repr__ EN EXCEPCIONES
# ============================================================================
seccion("9. __str__ y __repr__ en excepciones")

pago_error = PagoRechazadoError("PED-777", "límite de crédito excedido", 33)

# super().__init__(mensaje) en la sección 3 ya deja un str() con sentido:
print("  str(pago_error):", str(pago_error))

# El __repr__ definido junto a la clase (sección 3) es el que se usa en
# logs estructurados: da todos los atributos por separado, no solo el
# mensaje ya formateado.
print("  repr(pago_error):", repr(pago_error))
print("  type(pago_error).__name__:", type(pago_error).__name__)

print("  Uso: str(e) para mensajes al usuario o logs de texto plano,")
print("       repr(e) para logs estructurados y depuración,")
print("       type(e).__name__ para enrutar o clasificar el error por tipo.")


seccion("FIN — ya conoces las excepciones personalizadas al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
