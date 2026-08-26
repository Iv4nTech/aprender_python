"""
================================================================================
 EJERCICIOS: FUNCIONES EN PYTHON
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
# Descuento sobre el precio de varios productos
# ──────────────────────────────────────────────
seccion("EJERCICIO 1 — FÁCIL — Descuento sobre el precio de varios productos")

productos_carrito = [(59.99, 10), (120.00, 25), (15.50, 5)]


# Define calcular_descuento(precio, porcentaje) que devuelva el precio
# final tras aplicar el descuento (redondea a 2 decimales).
def calcular_descuento(precio, porcentaje):
    ...


# for precio, porcentaje in productos_carrito:
#     print(calcular_descuento(precio, porcentaje))

# Resultado esperado: 53.99, 90.0, 14.72


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Comprobar si una lista de números son pares
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — Comprobar si una lista de números son pares")

numeros = [3, 8, 15, 22, 7, 10]


# Define es_par(numero) que devuelva True si es par y False si no.
def es_par(numero):
    ...


# for numero in numeros:
#     print(numero, es_par(numero))

# Resultado esperado:
# 3 False
# 8 True
# 15 False
# 22 True
# 7 False
# 10 True


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Saludo con valor por defecto
# ──────────────────────────────────────────────
seccion("EJERCICIO 3 — FÁCIL — Saludo con valor por defecto")


# Define saludar(nombre, saludo="Hola") que imprima "<saludo>, <nombre>!"
def saludar(nombre, saludo="Hola"):
    ...


# saludar("Iván")
# saludar("Ana", "Buenos días")

# Resultado esperado:
# Hola, Iván!
# Buenos días, Ana!


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Contar vocales en un texto
# ──────────────────────────────────────────────
seccion("EJERCICIO 4 — MEDIO — Contar vocales en un texto")

frase = "Los datos del pedido no llegaron a tiempo al servidor"


# Define contar_vocales(texto) que devuelva cuántas vocales tiene, contando
# tanto mayúsculas como minúsculas.
def contar_vocales(texto):
    ...


# print(contar_vocales(frase))

# Resultado esperado: 19


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Estadísticas de ventas con return múltiple
# ──────────────────────────────────────────────
seccion("EJERCICIO 5 — MEDIO — Estadísticas de ventas con return múltiple")

ventas_semana = [1200, 950, 1400, 800, 1100]


# Define estadisticas(numeros) que devuelva la tupla (minimo, maximo, media).
def estadisticas(numeros):
    ...


# mini, maxi, media = estadisticas(ventas_semana)
# print(f"Mínimo: {mini}, Máximo: {maxi}, Media: {media}")

# Resultado esperado: Mínimo: 800, Máximo: 1400, Media: 1090.0


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# Aplicar IVA a una lista de precios sin modificar la original
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — Aplicar IVA a una lista de precios sin modificar la original")

precios_sin_iva = [10.0, 25.5, 99.99]


# Define aplicar_iva(precios, iva=0.21) que devuelva una lista NUEVA con
# el IVA aplicado a cada precio, sin tocar la lista original.
def aplicar_iva(precios, iva=0.21):
    ...


# precios_con_iva = aplicar_iva(precios_sin_iva)
# print(precios_sin_iva)
# print(precios_con_iva)

# Resultado esperado:
# [10.0, 25.5, 99.99]
# [12.1, 30.855, 120.9879]


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# Filtrar productos por categoría
# ──────────────────────────────────────────────
seccion("EJERCICIO 7 — AVANZADO — Filtrar productos por categoría")

productos = [
    {"nombre": "Portátil", "categoria": "informatica"},
    {"nombre": "Auriculares", "categoria": "electronica"},
    {"nombre": "Monitor", "categoria": "informatica"},
    {"nombre": "Móvil", "categoria": "electronica"},
]


# Define filtrar_por(lista_dicts, campo, valor) que devuelva solo los
# diccionarios cuyo 'campo' sea igual a 'valor'.
def filtrar_por(lista_dicts, campo, valor):
    ...


# print(filtrar_por(productos, "categoria", "informatica"))

# Resultado esperado:
# [{'nombre': 'Portátil', 'categoria': 'informatica'}, {'nombre': 'Monitor', 'categoria': 'informatica'}]


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Ordenar empleados por ventas
# ──────────────────────────────────────────────
seccion("EJERCICIO 8 — AVANZADO — Ordenar empleados por ventas")

empleados = [
    {"nombre": "Marta", "ventas": 800},
    {"nombre": "Pablo", "ventas": 1500},
    {"nombre": "Nuria", "ventas": 1200},
]


# Define ordenar_por(lista_dicts, campo, descendente=False) que ordene la
# lista de diccionarios por 'campo', usando sorted() con key=.
def ordenar_por(lista_dicts, campo, descendente=False):
    ...


# print(ordenar_por(empleados, "ventas"))
# print(ordenar_por(empleados, "ventas", descendente=True))

# Resultado esperado:
# [{'nombre': 'Marta', 'ventas': 800}, {'nombre': 'Nuria', 'ventas': 1200}, {'nombre': 'Pablo', 'ventas': 1500}]
# [{'nombre': 'Pablo', 'ventas': 1500}, {'nombre': 'Nuria', 'ventas': 1200}, {'nombre': 'Marta', 'ventas': 800}]


# ──────────────────────────────────────────────
# EJERCICIO 9 — EXPERTO
# Pipeline de transformaciones encadenadas
# ──────────────────────────────────────────────
seccion("EJERCICIO 9 — EXPERTO — Pipeline de transformaciones encadenadas")


def limpiar(texto):
    return texto.strip()


def normalizar(texto):
    return texto.lower()


def contar_palabras(texto):
    return len(texto.split())


texto_bruto = "   Python es un LENGUAJE muy   POTENTE y VERSATIL   "


# Define pipeline(datos, *funciones) que aplique cada función de
# 'funciones' en orden, pasando el resultado de una como entrada de la
# siguiente, y devuelva el resultado final.
def pipeline(datos, *funciones):
    ...


# resultado = pipeline(texto_bruto, limpiar, normalizar, contar_palabras)
# print(resultado)

# Resultado esperado: 8


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Memoizar una función lenta con una caché manual
# ──────────────────────────────────────────────
seccion("EJERCICIO 10 — EXPERTO — Memoizar una función lenta con una caché manual")


def es_primo_lento(numero):
    print(f"  (calculando si {numero} es primo...)")
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


# Define memoizar(funcion) que devuelva una nueva función envoltura con una
# caché (dict) por defecto: si el argumento ya está en caché, lo devuelve
# directamente sin volver a llamar a 'funcion'.
def memoizar(funcion):
    ...


# es_primo_memo = memoizar(es_primo_lento)
# print(es_primo_memo(97))
# print(es_primo_memo(97))
# print(es_primo_memo(100))

# Resultado esperado:
# (calculando si 97 es primo...)
# True
# True
# (calculando si 100 es primo...)
# False
# (la segunda llamada con 97 no vuelve a imprimir "(calculando...)")
