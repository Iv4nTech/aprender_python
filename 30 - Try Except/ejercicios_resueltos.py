"""
================================================================================
 EJERCICIOS RESUELTOS: TRY EXCEPT EN PYTHON
 Ejecutar: python3 ejercicios_resueltos.py
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


# SOLUCIÓN
def convertir_precio(texto: str) -> float:
    try:
        return float(texto)
    except ValueError:
        print(f"[AVISO] '{texto}' no es un precio válido, usando 0.0")
        return 0.0


print(f"Precio: {convertir_precio('19.99')}")
convertir_precio("gratis")
convertir_precio("")


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Calcular descuento con varios tipos de error
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — Calcular descuento con varios tipos de error")


# SOLUCIÓN
def calcular_descuento(precio, porcentaje):
    if not isinstance(precio, (int, float)) or not isinstance(porcentaje, (int, float)):
        raise TypeError("Los valores deben ser numéricos")
    if not 0 <= porcentaje <= 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return precio / precio * porcentaje


try:
    print(f"Descuento: {calcular_descuento(150.0, 10)}€")
except (TypeError, ValueError, ZeroDivisionError) as e:
    print(f"[{type(e).__name__}] {e}")

try:
    calcular_descuento("150", 10)
except (TypeError, ValueError, ZeroDivisionError) as e:
    print(f"[{type(e).__name__}] {e}")

try:
    calcular_descuento(150.0, 200)
except (TypeError, ValueError, ZeroDivisionError) as e:
    print(f"[{type(e).__name__}] {e}")


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Buscar producto en catálogo
# ──────────────────────────────────────────────
seccion("EJERCICIO 3 — FÁCIL — Buscar producto en catálogo")

catalogo = {
    "Teclado": {"precio": 79.99, "stock": 5},
    "Ratón": {"precio": 29.99, "stock": 0},
}


# SOLUCIÓN
def buscar_producto(catalogo: dict, nombre: str) -> None:
    try:
        producto = catalogo[nombre]
    except KeyError:
        print(f"[ERROR] '{nombre}' no está en el catálogo")
    else:
        print(f"{nombre} — {producto['precio']}€, stock: {producto['stock']}")


buscar_producto(catalogo, "Teclado")
buscar_producto(catalogo, "Monitor")


# ──────────────────────────────────────────────
# EJERCICIO 4 — FÁCIL
# Procesar fichero con cierre garantizado
# ──────────────────────────────────────────────
seccion("EJERCICIO 4 — FÁCIL — Procesar fichero con cierre garantizado")


# SOLUCIÓN
def procesar_fichero(nombre: str) -> None:
    print("Fichero abierto")
    try:
        if nombre.endswith(".txt"):
            raise RuntimeError("Formato incorrecto")
        print("Procesando...")
    except RuntimeError as e:
        print(f"[ERROR] {e}")
    finally:
        print("Fichero cerrado")


procesar_fichero("datos.csv")
procesar_fichero("datos.txt")


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Crear usuario con validación completa
# ──────────────────────────────────────────────
seccion("EJERCICIO 5 — MEDIO — Crear usuario con validación completa")


# SOLUCIÓN
def crear_usuario(nombre: str, email: str, edad) -> dict:
    if not nombre:
        raise ValueError("El nombre no puede estar vacío")
    if "@" not in email:
        raise ValueError(f"Email inválido: '{email}'")
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un entero")
    if not 18 <= edad <= 99:
        raise ValueError(f"Edad fuera de rango: {edad}")
    return {"nombre": nombre, "email": email, "edad": edad}


casos = [
    ("Ana", "ana@ejemplo.com", 28),
    ("", "x@x.com", 30),
    ("Luis", "no-es-un-email", 30),
    ("Marta", "marta@x.com", "treinta"),
    ("Pedro", "pedro@x.com", 150),
]
for nombre, email, edad in casos:
    try:
        print(f"Usuario creado: {crear_usuario(nombre, email, edad)}")
    except (TypeError, ValueError) as e:
        print(f"[{type(e).__name__}] {e}")


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# Cargar configuración con re-raise
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — Cargar configuración con re-raise")


# SOLUCIÓN
def cargar_configuracion(ruta: str) -> dict:
    if ruta == "missing.cfg":
        raise FileNotFoundError(f"Fichero no encontrado: {ruta}")
    if ruta == "protegido.cfg":
        raise PermissionError(f"Sin permisos para leer: {ruta}")
    return {"ok": True}


def arrancar_app(ruta: str) -> dict:
    try:
        return cargar_configuracion(ruta)
    except (FileNotFoundError, PermissionError) as e:
        print(f"[LOG] {type(e).__name__}: {e}")
        raise


for ruta in ("missing.cfg", "protegido.cfg", "app.cfg"):
    try:
        print(f"Config: {arrancar_app(ruta)}")
    except FileNotFoundError:
        print("[ACCION] El fichero de config no existe, usando valores por defecto")
    except PermissionError:
        print("[ACCION] Sin permisos para leer la config, abortando arranque")


# ──────────────────────────────────────────────
# EJERCICIO 7 — MEDIO
# Transferencia bancaria con try/except/else/finally
# ──────────────────────────────────────────────
seccion("EJERCICIO 7 — MEDIO — Transferencia bancaria con try/except/else/finally")


# SOLUCIÓN
def realizar_transferencia(origen: str, destino: str, importe: float) -> None:
    try:
        if importe <= 0:
            raise ValueError(f"Importe inválido: {importe}")
        if origen == destino:
            raise ValueError("El origen y el destino no pueden ser el mismo")
        print(f"  Moviendo {importe}€ de '{origen}' a '{destino}'...")
    except ValueError as e:
        print(f"  [ERROR] {e}")
    else:
        print(f"Transferencia de {importe}€ de '{origen}' a '{destino}' realizada")
    finally:
        print("Auditoría registrada")


realizar_transferencia("ES01", "ES02", 150.0)
realizar_transferencia("ES01", "ES02", -10.0)
realizar_transferencia("ES01", "ES01", 50.0)


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Importar CSV en capas, sin detenerse al primer error
# ──────────────────────────────────────────────
seccion("EJERCICIO 8 — AVANZADO — Importar CSV en capas, sin detenerse al primer error")


# SOLUCIÓN
def parsear_csv(linea: str) -> dict:
    columnas = linea.split(",")
    nombre = columnas[0]
    precio = columnas[1]
    stock = columnas[2]
    return {"nombre": nombre, "precio": float(precio), "stock": int(stock)}


def extraer_producto(linea: str) -> dict:
    try:
        return parsear_csv(linea)
    except ValueError as e:
        raise ValueError(f"ValueError al parsear: {e}") from e
    except IndexError as e:
        raise IndexError(f"IndexError al parsear: {e}") from e


def importar_lineas(lineas: list) -> None:
    for numero, linea in enumerate(lineas, start=1):
        try:
            producto = extraer_producto(linea)
        except (ValueError, IndexError) as e:
            print(f"[ERROR línea {numero}] {e}")
        else:
            print(f"Importado: {producto}")


lineas = ["Teclado,79.99,5", "Ratón,precio_malo,12", "Monitor,349"]
importar_lineas(lineas)


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# Corregir anti-patrones de manejo de errores
# ──────────────────────────────────────────────
seccion("EJERCICIO 9 — AVANZADO — Corregir anti-patrones de manejo de errores")


# SOLUCIÓN
def procesar_pedido(pedido: dict) -> float:
    cantidad = int(pedido["cantidad"])
    precio = float(pedido["precio"])
    return cantidad * precio


def obtener_cliente(clientes: dict, id_cliente) -> dict:
    try:
        return clientes[id_cliente]
    except KeyError as e:
        print(f"[KeyError] Cliente no encontrado: {e}")
        raise


def calcular_iva(precio) -> float:
    if not isinstance(precio, (int, float)):
        raise TypeError(f"El precio debe ser numérico, no {type(precio).__name__}")
    return precio * 0.21


print(f"Total: {procesar_pedido({'cantidad': '3', 'precio': '19.99'})}€")
try:
    procesar_pedido({"cantidad": "tres", "precio": "19.99"})
except (TypeError, ValueError) as e:
    print(f"[{type(e).__name__}] {e}")

clientes = {1: {"nombre": "Ana"}}
print(obtener_cliente(clientes, 1))
try:
    obtener_cliente(clientes, 99)
except KeyError as e:
    print(f"[KeyError] {e}")

print(f"IVA: {calcular_iva(100)}")
try:
    calcular_iva("cien")
except TypeError as e:
    print(f"[TypeError] {e}")


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Sistema de reintentos
# ──────────────────────────────────────────────
seccion("EJERCICIO 10 — EXPERTO — Sistema de reintentos")


# SOLUCIÓN
def con_reintento(func, intentos: int, *args):
    ultima_excepcion = None
    for intento in range(1, intentos + 1):
        try:
            return func(*args)
        except Exception as e:
            ultima_excepcion = e
            if intento < intentos:
                print(f"[REINTENTO {intento}/{intentos}] Reintentando...")
    raise ultima_excepcion


contador = [0]


def llamar_api(url):
    contador[0] += 1
    if contador[0] < 3:
        raise ConnectionError(f"No se pudo conectar tras {contador[0]} intentos")
    return {"status": "ok"}


resultado = con_reintento(llamar_api, 3, "https://api.ejemplo.com")
print(f"Respuesta recibida: {resultado}")


def siempre_falla(url):
    raise ConnectionError("No se pudo conectar tras 3 intentos")


try:
    con_reintento(siempre_falla, 3, "https://api.ejemplo.com")
except ConnectionError as e:
    print(f"[ERROR FINAL] {type(e).__name__}: {e}")
