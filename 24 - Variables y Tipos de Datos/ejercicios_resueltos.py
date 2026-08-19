"""
================================================================================
 EJERCICIOS RESUELTOS: VARIABLES Y TIPOS DE DATOS EN PYTHON
 Ejecutar: python3 ejercicios_resueltos.py
================================================================================
"""


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ──────────────────────────────────────────────
# EJERCICIO 1 — FÁCIL
# Perfil de usuario con cada tipo básico
# ──────────────────────────────────────────────
# Estás dando de alta el perfil de un nuevo usuario en la base de datos.
# Necesitas una variable de cada tipo básico y comprobar su tipo real.
seccion("EJERCICIO 1 — FÁCIL — Perfil de usuario con cada tipo básico")

# SOLUCIÓN
nombre_usuario = "ana_gomez"
edad = 28
altura_metros = 1.68
es_premium = False
telefono = None

# Resultado esperado: <class 'str'> <class 'int'> <class 'float'> <class 'bool'> <class 'NoneType'>
print(type(nombre_usuario), type(edad), type(altura_metros), type(es_premium), type(telefono))


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Calcular el total de una compra con IVA
# ──────────────────────────────────────────────
# Un cliente compra varias unidades de un producto. Necesitas el total
# sin IVA, el total con el 21% de IVA aplicado, y redondeado a 2 decimales.
seccion("EJERCICIO 2 — FÁCIL — Calcular el total de una compra con IVA")

precio = 19.99
cantidad = 3

# SOLUCIÓN
total = precio * cantidad
total_con_iva = round(total * 1.21, 2)

# Resultado esperado: total=59.97, total_con_iva=72.56
print(f"total={total}, total_con_iva={total_con_iva}")


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Limpiar y validar una URL de configuración
# ──────────────────────────────────────────────
# La URL de una API llega con espacios de más desde un fichero de config
# mal formateado. Hay que limpiarla y comprobar que usa HTTPS.
seccion("EJERCICIO 3 — FÁCIL — Limpiar y validar una URL de configuración")

url_sucia = "  https://api.ejemplo.com/v1/usuarios  "

# SOLUCIÓN
url_limpia = url_sucia.strip()
dominio = url_limpia.split("/")[2]
es_https = url_limpia.startswith("https")

# Resultado esperado: url_limpia='https://api.ejemplo.com/v1/usuarios',
# dominio='api.ejemplo.com', es_https=True
print(f"{url_limpia!r}, {dominio!r}, {es_https}")


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Contar productos repetidos en un log de ventas
# ──────────────────────────────────────────────
# El log de ventas del día trae los productos vendidos sin agrupar.
# Necesitas saber cuántas unidades se vendieron de cada uno, sin usar
# Counter, solo con un diccionario normal.
seccion("EJERCICIO 4 — MEDIO — Contar productos repetidos en un log de ventas")

productos_vendidos = ["manzana", "pera", "manzana", "kiwi", "pera", "pera"]

# SOLUCIÓN
conteo = {}
for producto in productos_vendidos:
    conteo[producto] = conteo.get(producto, 0) + 1

# Resultado esperado: {'manzana': 2, 'pera': 3, 'kiwi': 1}
print(conteo)


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Leer configuración de app sin arriesgarse a un KeyError
# ──────────────────────────────────────────────
# La configuración de la app viene de un fichero externo: algunas claves
# pueden faltar. Acceder con [] directo reventaría la app al arrancar.
seccion("EJERCICIO 5 — MEDIO — Leer configuración de app sin KeyError")

config_app = {"modo_oscuro": True, "idioma": "es"}

# SOLUCIÓN
modo_oscuro = config_app.get("modo_oscuro", False)
idioma = config_app.get("idioma", "en")
notificaciones = config_app.get("notificaciones", True)

# Resultado esperado: True, 'es', True
print(modo_oscuro, idioma, notificaciones)


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# Convertir los inputs de un formulario al tipo numérico correcto
# ──────────────────────────────────────────────
# Los campos de un formulario llegan siempre como texto. Necesitas
# convertir cada uno a int si es un entero, a float si tiene decimales,
# o dejarlo como None si no es convertible, sin que el programa reviente
# con una excepción no controlada.
seccion("EJERCICIO 6 — MEDIO — Convertir los inputs de un formulario al tipo correcto")

valores_formulario = ["42", "3.14", "hola"]

# SOLUCIÓN
resultados = []
for texto in valores_formulario:
    if texto.isdigit():
        resultados.append(int(texto))
    elif texto.replace(".", "", 1).isdigit():
        resultados.append(float(texto))
    else:
        resultados.append(None)

# Resultado esperado: [42, 3.14, None]
print(resultados)


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# Media y máximo de precios con datos sucios
# ──────────────────────────────────────────────
# Una hoja de cálculo exportada trae los precios como texto, y alguna
# celda tiene basura en vez de un número. Hay que ignorarla sin que
# rompa el cálculo de la media y el máximo.
seccion("EJERCICIO 7 — AVANZADO — Media y máximo de precios con datos sucios")

precios_texto = ["12.5", "8", "invalid", "99.99", "0"]

# SOLUCIÓN
precios_validos = [float(p) for p in precios_texto if p.replace(".", "", 1).isdigit()]
media_precios = sum(precios_validos) / len(precios_validos)
maximo_precio = max(precios_validos)

# Resultado esperado: media=30.1225, maximo=99.99
print(f"media={media_precios}, maximo={maximo_precio}")


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Acceso seguro a una respuesta de API anidada
# ──────────────────────────────────────────────
# La respuesta de una API externa trae varios niveles de diccionarios
# anidados, y algunas claves intermedias pueden no existir en absoluto.
# Acceder con [] encadenado reventaría con KeyError o TypeError.
seccion("EJERCICIO 8 — AVANZADO — Acceso seguro a una respuesta de API anidada")

respuesta_api = {
    "usuario": {
        "nombre": "Ana",
        "direccion": {"ciudad": "Madrid"},
    }
}

# SOLUCIÓN
# Cada .get() intermedio devuelve {} si falta el nivel, para que el
# siguiente .get() encadenado no reciba nunca None y no lance TypeError.
pais = respuesta_api.get("usuario", {}).get("direccion", {}).get("pais", "desconocido")
telefono = respuesta_api.get("usuario", {}).get("telefono", "no disponible")

# Resultado esperado: 'desconocido', 'no disponible'
print(pais, telefono)


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# Normalizar cualquier número a float
# ──────────────────────────────────────────────
# Un cálculo de precios recibe valores de fuentes distintas: a veces un
# int, a veces un float, a veces un str con un número, y a veces un tipo
# que no tiene sentido ahí (como una lista). Hay que convertir a float
# los válidos y marcar los demás, sin que el programa se pare.
seccion("EJERCICIO 9 — AVANZADO — Normalizar cualquier número a float")

valores = [10, 3.5, "7", [1, 2]]

# SOLUCIÓN
normalizados = []
for valor in valores:
    if isinstance(valor, bool):
        normalizados.append("tipo no soportado")
    elif isinstance(valor, (int, float, str)):
        normalizados.append(float(valor))
    else:
        normalizados.append("tipo no soportado")

# Resultado esperado: [10.0, 3.5, 7.0, 'tipo no soportado']
print(normalizados)


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Porcentaje de éxito explotando que bool es subclase de int
# ──────────────────────────────────────────────
# Un test A/B ha guardado los resultados de validación de cada usuario
# como una lista de booleanos. Necesitas el porcentaje de éxito, y
# demostrar que sum() sobre bools funciona porque True/False son int.
seccion("EJERCICIO 10 — EXPERTO — Porcentaje de éxito con bool como subclase de int")

resultados_validacion = [True, False, True, True, False]

# SOLUCIÓN
# sum() trata cada True como 1 y cada False como 0 porque bool hereda de int.
porcentaje_con_sum = sum(resultados_validacion) / len(resultados_validacion) * 100

suma_manual = 0
for resultado in resultados_validacion:
    if resultado:
        suma_manual += 1

# Resultado esperado: porcentaje_con_sum=60.0, suma_manual=3
print(f"porcentaje_con_sum={porcentaje_con_sum}, suma_manual={suma_manual}")
