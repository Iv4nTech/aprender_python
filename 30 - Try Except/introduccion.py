"""
================================================================================
 TRY EXCEPT EN PYTHON
 Ejecutar: python3 introduccion.py
================================================================================
"""


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. QUÉ ES UNA EXCEPCIÓN Y POR QUÉ EL PROGRAMA "EXPLOTA"
# ============================================================================
seccion("1. Qué es una excepción y por qué el programa explota")

# Calculadora de descuentos que recibe el precio como texto, tal cual
# llegaría desde un formulario web. Si el usuario escribe algo que no es
# un número, el programa entero se detiene con un traceback que nadie que
# no programe sabría interpretar.
entrada_usuario = "gratis"

try:
    precio = float(entrada_usuario)
    descuento = precio * 0.10
    print(f"Descuento: {descuento}€")
except ValueError as error:
    # Sin este try/except, esto es lo que se vería en la terminal:
    #   Traceback (most recent call last):
    #     File "introduccion.py", line N, in <module>
    #       precio = float(entrada_usuario)
    #   ValueError: could not convert string to float: 'gratis'
    print(f"Traceback simulado -> ValueError: {error}")

# Una excepción es un objeto que Python crea y "lanza" cuando algo va mal
# durante la ejecución. Ese objeto tiene un tipo (ValueError, TypeError...),
# un mensaje descriptivo y un traceback: la pila de llamadas que llevó
# hasta el error. Si nadie la captura, el intérprete la imprime y el
# programa termina ahí mismo, sin ejecutar ni una línea más.


# ============================================================================
# 2. try / except — CAPTURAR EL ERROR Y REACCIONAR
# ============================================================================
seccion("2. try / except — capturar el error y reaccionar")

# Mismo caso que antes, pero el programa ya no explota: informa del
# problema y sigue ejecutándose con las siguientes entradas.
for entrada_usuario in ("19.99", "gratis"):
    try:
        precio = float(entrada_usuario)
        descuento = precio * 0.10
        print(f"Descuento sobre '{entrada_usuario}': {descuento}€")
    except ValueError as error:
        print(f"Entrada inválida '{entrada_usuario}': {error}")


def calcular_descuento_sobre_total(precio, total_ventas):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    return (precio / total_ventas) * 100


# El usuario también podría escribir un precio negativo (validación manual,
# ValueError) o el total de ventas podría ser 0 (ZeroDivisionError al
# calcular el porcentaje). Un solo except no cubre los dos casos: hacen
# falta dos bloques except distintos en el mismo try.
for precio_prueba, total_prueba in ((25.0, 100.0), (-5.0, 100.0), (25.0, 0.0)):
    try:
        porcentaje = calcular_descuento_sobre_total(precio_prueba, total_prueba)
        print(f"Porcentaje sobre el total: {porcentaje}%")
    except ValueError as error:
        print(f"[ValueError] {error}")
    except ZeroDivisionError:
        print("[ZeroDivisionError] El total de ventas no puede ser 0")


# ============================================================================
# 3. else — CÓDIGO QUE SOLO CORRE SI NO HUBO ERROR
# ============================================================================
seccion("3. else — código que solo corre si no hubo error")


def leer_config(nombre):
    if nombre == "missing.cfg":
        raise FileNotFoundError(f"No se encontró '{nombre}'")
    return {"debug": True, "puerto": 8080}


# El código que depende de que la lectura haya ido bien no debería vivir
# dentro del try: si ese código lanza su propio error, quedaría capturado
# por el except como si fuera un fallo de leer_config, ocultando un bug
# distinto. 'else' separa "qué hago si falló" de "qué hago si funcionó".
for nombre_fichero in ("app.cfg", "missing.cfg"):
    try:
        config = leer_config(nombre_fichero)
    except FileNotFoundError as error:
        print(f"  Error: {error}")
    else:
        # solo se ejecuta si leer_config no lanzó nada
        print(f"  Config cargada: {config}")
        print(f"  Puerto: {config['puerto']}")


# ============================================================================
# 4. finally — CÓDIGO QUE CORRE SIEMPRE
# ============================================================================
seccion("4. finally — código que corre siempre")


def abrir_conexion(bd):
    print(f"  Conexión abierta a '{bd}'")
    return {"bd": bd, "abierta": True}


def consultar(conexion, query):
    if query == "SELECT * FROM usuarios_borrados":
        raise RuntimeError("Tabla no existe")
    print(f"  Consulta ejecutada: {query}")
    return [{"id": 1, "nombre": "Ana"}]


def cerrar_conexion(conexion):
    print(f"  Conexión cerrada a '{conexion['bd']}'")


# Si la conexión no se cierra tanto en el caso correcto como en el fallido,
# se queda abierta en el servidor. Con suficientes peticiones así, la base
# de datos se queda sin conexiones libres y empieza a rechazar clientes
# legítimos. 'finally' garantiza el cierre pase lo que pase dentro del try.
for query in ("SELECT * FROM usuarios", "SELECT * FROM usuarios_borrados"):
    conexion = abrir_conexion("produccion")
    try:
        resultado = consultar(conexion, query)
        print(f"  Resultado: {resultado}")
    except RuntimeError as error:
        print(f"  Error en la consulta: {error}")
    finally:
        cerrar_conexion(conexion)
        

# Nota (Python 3.14, PEP 765): usar return/break/continue dentro de un
# finally ahora lanza un SyntaxWarning, porque descarta silenciosamente
# cualquier excepción pendiente del try — un bug clásico y difícil de ver.


# ============================================================================
# 5. raise — LANZAR EXCEPCIONES INTENCIONALMENTE
# ============================================================================
seccion("5. raise — lanzar excepciones intencionalmente")


def validar_edad(edad):
    if not isinstance(edad, int):
        raise TypeError(f"La edad debe ser un entero, no {type(edad).__name__}")
    if edad < 0 or edad > 120:
        raise ValueError(f"Edad fuera de rango: {edad}")
    return edad


# Si la edad no es válida, seguir ejecutando con un dato corrupto es peor
# que parar ahí mismo: cualquier cálculo posterior (facturación, permisos
# por edad...) heredaría el dato incorrecto sin que nadie se entere.
for edad_prueba in (28, "veintiocho", 150):
    try:
        edad_validada = validar_edad(edad_prueba)
        print(f"  Edad válida: {edad_validada}")
    except TypeError as error:
        print(f"  [TypeError] {error}")
    except ValueError as error:
        print(f"  [ValueError] {error}")


def registrar_usuario(datos):
    try:
        edad = validar_edad(datos["edad"])
        print(f"  Usuario registrado con edad {edad}")
    except (TypeError, ValueError) as error:
        print(f"  [LOG] Error de validación: {error}")
        raise   # re-lanza: el llamador decide qué hacer


# El llamador de registrar_usuario decide qué hacer con el fallo (pedir
# de nuevo el formulario, abortar el registro...) — la función de negocio
# solo se encarga de loguear y dejar pasar el error hacia arriba.
try:
    registrar_usuario({"edad": -5})
except ValueError:
    print("  [CALLER] Registro rechazado, se pide al usuario que corrija la edad")


# ============================================================================
# 6. BUENAS PRÁCTICAS — QUÉ CAPTURAR Y QUÉ NO
# ============================================================================
seccion("6. Buenas prácticas — qué capturar y qué no")


def importar_csv(nombre_fichero):
    if nombre_fichero == "no_existe.csv":
        raise FileNotFoundError(f"No se encontró '{nombre_fichero}'")
    if nombre_fichero == "protegido.csv":
        raise PermissionError(f"Sin permisos para leer '{nombre_fichero}'")
    print(f"  Importado: {nombre_fichero}")


# Anti-patrón 1: capturar Exception a ciegas y no hacer nada con el error.
print("Anti-patrón 1 — except Exception: pass")
try:
    importar_csv("no_existe.csv")
except Exception:
    pass   # el error desaparece; nadie sabe qué pasó
print("  (sin salida: el fallo fue silenciado por completo)")

# Anti-patrón 2: capturar demasiado amplio y seguir como si nada.
print("\nAnti-patrón 2 — except Exception sin relanzar")
try:
    importar_csv("protegido.csv")
except Exception as error:
    print(f"  Algo falló: {error}")
    # sin raise: el programa sigue como si la importación hubiera ido bien


def importar_lote(ficheros):
    for fichero in ficheros:
        try:
            importar_csv(fichero)
        except FileNotFoundError as error:
            print(f"  El fichero no existe: {error}")
            # aquí sí tiene sentido no relanzar: informamos y seguimos con el resto
        except PermissionError as error:
            print(f"  Sin permisos para leer el fichero: {error}")
            raise   # este sí lo relanzamos: es un problema del sistema, no del usuario


# Patrón correcto: específico, con una acción distinta por cada caso.
print("\nPatrón correcto — específico y con acción")
try:
    importar_lote(["no_existe.csv", "protegido.csv", "ventas.csv"])
except PermissionError:
    print("  [CALLER] El problema de permisos llegó hasta aquí, se aborta el lote")


# ============================================================================
# 7. EXCEPCIONES BUILT-IN MÁS COMUNES
# ============================================================================
seccion("7. Excepciones built-in más comunes")

precios_dict = {"Teclado": 45.99, "Ratón": 19.99}
lista_precios = [45.99, 19.99]

try:
    int("hola")
except ValueError as error:
    print(f"ValueError -> conversión de tipo inválida: {error}")

try:
    total = "precio" + 5
except TypeError as error:
    print(f"TypeError -> operación entre tipos incompatibles: {error}")

try:
    precios_dict["Monitor"]
except KeyError as error:
    print(f"KeyError -> clave inexistente en diccionario: {error}")

try:
    lista_precios[10]
except IndexError as error:
    print(f"IndexError -> índice fuera de rango en lista: {error}")

try:
    with open("fichero_que_no_existe.txt", "r", encoding="utf-8") as fichero:
        fichero.read()
except FileNotFoundError as error:
    print(f"FileNotFoundError -> fichero que no existe: {error}")

try:
    10 / 0
except ZeroDivisionError as error:
    print(f"ZeroDivisionError -> división por cero: {error}")

try:
    "texto".metodo_que_no_existe()
except AttributeError as error:
    print(f"AttributeError -> atributo inexistente en un objeto: {error}")


seccion("FIN — ya conoces el try/except básico en Python")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
