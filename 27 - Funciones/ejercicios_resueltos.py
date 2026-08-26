"""
================================================================================
 EJERCICIOS RESUELTOS: FUNCIONES EN PYTHON
 Ejecutar: python3 ejercicios_resueltos.py
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


# SOLUCIÓN
def calcular_descuento(precio, porcentaje):
    return round(precio - precio * porcentaje / 100, 2)


for precio, porcentaje in productos_carrito:
    print(calcular_descuento(precio, porcentaje))


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Comprobar si una lista de números son pares
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — Comprobar si una lista de números son pares")

numeros = [3, 8, 15, 22, 7, 10]


# SOLUCIÓN
def es_par(numero):
    return numero % 2 == 0


for numero in numeros:
    print(numero, es_par(numero))


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Saludo con valor por defecto
# ──────────────────────────────────────────────
seccion("EJERCICIO 3 — FÁCIL — Saludo con valor por defecto")


# SOLUCIÓN
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")


saludar("Iván")
saludar("Mario", "Buenos días")


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Contar vocales en un texto
# ──────────────────────────────────────────────
seccion("EJERCICIO 4 — MEDIO — Contar vocales en un texto")

frase = "Los datos del pedido no llegaron a tiempo al servidor"


# SOLUCIÓN
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador


print(contar_vocales(frase))


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Estadísticas de ventas con return múltiple
# ──────────────────────────────────────────────
seccion("EJERCICIO 5 — MEDIO — Estadísticas de ventas con return múltiple")

ventas_semana = [1200, 950, 1400, 800, 1100]


# SOLUCIÓN
def estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)


mini, maxi, media = estadisticas(ventas_semana)
print(f"Mínimo: {mini}, Máximo: {maxi}, Media: {media}")


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# Aplicar IVA a una lista de precios sin modificar la original
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — Aplicar IVA a una lista de precios sin modificar la original")

precios_sin_iva = [10.0, 25.5, 99.99]


# SOLUCIÓN
def aplicar_iva(precios, iva=0.21):
    return [precio * (1 + iva) for precio in precios]


precios_con_iva = aplicar_iva(precios_sin_iva)
print(precios_sin_iva)
print(precios_con_iva)


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


# SOLUCIÓN
def filtrar_por(lista_dicts, campo, valor):
    return [elemento for elemento in lista_dicts if elemento[campo] == valor]


print(filtrar_por(productos, "categoria", "informatica"))


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


# SOLUCIÓN
def ordenar_por(lista_dicts, campo, descendente=False):
    def obtener_valor(elemento):
        return elemento[campo]

    return sorted(lista_dicts, key=obtener_valor, reverse=descendente)


print(ordenar_por(empleados, "ventas"))
print(ordenar_por(empleados, "ventas", descendente=True))


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


# SOLUCIÓN
def pipeline(datos, *funciones):
    resultado = datos
    for funcion in funciones:
        resultado = funcion(resultado)
    return resultado


resultado = pipeline(texto_bruto, limpiar, normalizar, contar_palabras)
print(resultado)


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


# SOLUCIÓN
def memoizar(funcion):
    cache = {}

    def envoltura(argumento):
        if argumento not in cache:
            cache[argumento] = funcion(argumento)
        return cache[argumento]

    return envoltura


es_primo_memo = memoizar(es_primo_lento)
print(es_primo_memo(97))
print(es_primo_memo(97))
print(es_primo_memo(100))
