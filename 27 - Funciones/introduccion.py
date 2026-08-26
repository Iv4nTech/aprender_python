"""
================================================================================
 FUNCIONES EN PYTHON
 Ejecutar: python3 introduccion.py
================================================================================
"""


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA DEL CÓDIGO REPETIDO
# ============================================================================
seccion("1. El problema del código repetido")

# Producto 1: teclado mecánico
precio_base = 49.99
iva = 0.21
precio_final = precio_base * (1 + iva)
print(f"Teclado: {precio_base}€ + IVA = {precio_final:.2f}€")

# Producto 2: monitor
precio_base = 219.00
iva = 0.21
precio_final = precio_base * (1 + iva)
print(f"Monitor: {precio_base}€ + IVA = {precio_final:.2f}€")

# Producto 3: ratón
precio_base = 15.50
iva = 0.21
precio_final = precio_base * (1 + iva)
print(f"Ratón: {precio_base}€ + IVA = {precio_final:.2f}€")

# Esto es lo que pasa cuando no usas funciones: el mismo cálculo copiado y
# pegado tres veces. Si mañana cambia el tipo de IVA, hay que tocar el
# código en tres sitios distintos, y es fácil olvidarse de alguno.


# ============================================================================
# 2. LA MISMA LÓGICA COMO FUNCIÓN
# ============================================================================
seccion("2. La misma lógica como función")


def calcular_precio_con_iva(precio_base, iva):
    precio_final = precio_base * (1 + iva)
    return precio_final


# La misma lógica de arriba, pero escrita una sola vez y llamada tres veces.
print(f"Teclado: {calcular_precio_con_iva(49.99, 0.21):.2f}€")
print(f"Monitor: {calcular_precio_con_iva(219.00, 0.21):.2f}€")
print(f"Ratón: {calcular_precio_con_iva(15.50, 0.21):.2f}€")

# Tres conceptos mínimos: 'def' declara la función, 'precio_base' e 'iva'
# son sus parámetros, y 'return' es lo que la función entrega al terminar.


# ============================================================================
# 3. PARÁMETROS CON VALOR POR DEFECTO
# ============================================================================
seccion("3. Parámetros con valor por defecto")


def formatear_precio(precio, moneda="€", decimales=2):
    return f"{precio:.{decimales}f}{moneda}"


# Sin tocar los opcionales, usa los valores por defecto.
print(formatear_precio(49.99))
# Sobreescribiendo solo la moneda.
print(formatear_precio(49.99, "$"))
# Sobreescribiendo moneda y decimales.
print(formatear_precio(49.99, "$", 0))

# Orden obligatorio: los parámetros con valor por defecto van SIEMPRE
# después de los obligatorios. Esto daría error de sintaxis:
#   def formatear_precio(moneda="€", precio): ...
# porque Python no sabría a qué parámetro corresponde un argumento
# posicional si los opcionales van antes que los obligatorios.


# ============================================================================
# 4. ARGUMENTOS POSICIONALES VS KEYWORD
# ============================================================================
seccion("4. Argumentos posicionales vs keyword")

# Posicionales: el orden importa, y sin mirar la firma no se sabe qué es qué.
print(formatear_precio(19.99, "USD", 0))

# Keyword: se nombra cada argumento, el orden deja de importar y el código
# se lee sin tener que recordar la posición de cada parámetro.
print(formatear_precio(19.99, decimales=0, moneda="USD"))

# En funciones con dos o más parámetros del mismo tipo (aquí, dos strings
# o un precio y varios ajustes) usar keyword args evita bugs silenciosos:
# pasar "USD" donde se esperaba el número de decimales no daría error,
# simplemente el resultado sería incorrecto.


# ============================================================================
# 5. RETURN MÚLTIPLE (Y LA TRAMPA DE NO PONER RETURN)
# ============================================================================
seccion("5. Return múltiple (y la trampa de no poner return)")


def analizar_lista(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    media = sum(numeros) / len(numeros)
    return minimo, maximo, media


ventas_semana = [1200, 950, 1400, 800, 1100]
# Python permite devolver varios valores separados por comas: en realidad
# es una tupla, y se puede desempaquetar directamente al llamarla.
minimo, maximo, media = analizar_lista(ventas_semana)
print(f"Mínimo: {minimo}, Máximo: {maximo}, Media: {media:.2f}")


def analizar_lista_rota(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    media = sum(numeros) / len(numeros)
    # Falta el return: los cálculos se hacen pero nunca salen de la función.


resultado = analizar_lista_rota(ventas_semana)
# Sin 'return' explícito, toda función de Python devuelve None. No es un
# error, no lanza ninguna excepción: simplemente el resultado se pierde,
# y el bug solo se nota más adelante, cuando algo intenta usar 'resultado'.
print("Sin return, la función devuelve:", resultado)


# ============================================================================
# 6. SCOPE: VARIABLES LOCALES VS GLOBALES
# ============================================================================
seccion("6. Scope: variables locales vs globales")

intentos = 0  # contador global, fuera de cualquier función


def procesar_login(usuario, clave):
    intentos = 0  # variable LOCAL: aunque se llame igual, es una caja distinta
    intentos += 1
    print(f"  (dentro de la función) intentos: {intentos}")
    return usuario == "admin" and clave == "1234"


procesar_login("admin", "0000")
procesar_login("admin", "1234")
# La variable local 'intentos' de dentro de la función no ha tocado para
# nada a la variable global de fuera: siguen siendo cosas distintas.
print("(fuera de la función) intentos sigue siendo:", intentos)

# La tentación aquí es usar 'global intentos' dentro de la función para que
# el contador persista entre llamadas. NO lo hagas: acopla la función a una
# variable externa concreta, la vuelve impredecible según el orden en que
# se llame y muy difícil de testear de forma aislada. La alternativa
# correcta es pasar el valor como parámetro y devolver el nuevo valor:


def registrar_intento(intentos_previos):
    return intentos_previos + 1


intentos = registrar_intento(intentos)
intentos = registrar_intento(intentos)
print("intentos actualizado explícitamente:", intentos)


# ============================================================================
# 7. FUNCIONES COMO ARGUMENTOS (FIRST-CLASS FUNCTIONS)
# ============================================================================
seccion("7. Funciones como argumentos (first-class functions)")

productos = [
    {"nombre": "Teclado", "precio": 45.99},
    {"nombre": "Monitor", "precio": 299.99},
    {"nombre": "Ratón", "precio": 19.99},
]


def obtener_precio(producto):
    return producto["precio"]


# sorted() recibe la función 'obtener_precio' como argumento, SIN llamarla
# (sin paréntesis): es sorted() quien la llama, una vez por elemento, para
# saber por qué valor ordenar. En Python las funciones son valores como
# cualquier otro y se pueden pasar de una función a otra.
productos_ordenados = sorted(productos, key=obtener_precio)
for producto in productos_ordenados:
    print(f"{producto['nombre']}: {producto['precio']}€")


# ============================================================================
# 8. DOCSTRINGS
# ============================================================================
seccion("8. Docstrings")


def calcular_precio_con_iva(precio_base, iva=0.21):
    """Calcula el precio final de un producto aplicando IVA.

    precio_base: precio sin impuestos, en euros.
    iva: tipo de IVA a aplicar (0.21 = 21%, valor por defecto en España).
    """
    return precio_base * (1 + iva)


# El docstring no es un comentario cualquiera: Python lo guarda como parte
# de la función, y herramientas como help() lo muestran automáticamente.
help(calcular_precio_con_iva)
print(f"Resultado: {calcular_precio_con_iva(100):.2f}€")


seccion("FIN — ya conoces las funciones al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
