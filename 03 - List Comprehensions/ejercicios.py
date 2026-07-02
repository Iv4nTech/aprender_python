# ============================================================
# EJERCICIOS DE LIST COMPREHENSIONS (de fácil a experto)
# Resuelve cada ejercicio usando SOLO list comprehensions.
# ============================================================


# --- Ejercicio 1 (Fácil) ---
# Tienes una lista de números. Crea una nueva lista con el cuadrado de cada número.
numeros = [1, 2, 3, 4, 5, 6]
# cuadrados = ...


# --- Ejercicio 2 (Fácil) ---
# A partir de la lista de nombres, crea una lista con cada nombre en MAYÚSCULAS.
nombres = ["ana", "luis", "marta", "pedro"]
# nombres_mayus = ...


# --- Ejercicio 3 (Fácil) ---
# De la lista de números, quédate solo con los números pares.
valores = [10, 15, 22, 33, 40, 51, 60]
# pares = ...


# --- Ejercicio 4 (Medio) ---
# Tienes los precios de un carrito. Aplica un 10% de descuento SOLO a los productos
# que cuesten más de 50 euros. El resto se quedan igual.
precios = [20, 75, 100, 45, 200]
# precios_finales = ...


# --- Ejercicio 5 (Medio) ---
# A partir de una frase, devuelve una lista con la longitud de cada palabra.
frase = "aprender list comprehensions es muy util"
# longitudes = ...


# --- Ejercicio 6 (Medio) ---
# Tienes una lista de temperaturas en Celsius. Conviértelas a Fahrenheit (C * 9/5 + 32),
# pero solo incluye las que superen los 0 grados Celsius.
celsius = [-5, 0, 10, 25, -10, 37]
# fahrenheit = ...


# --- Ejercicio 7 (Difícil) ---
# Tienes una lista de listas (notas de varios alumnos). Aplánala para obtener
# una única lista con todas las notas.
notas_por_alumno = [[8, 9, 7], [5, 6, 4], [10, 9, 8]]
# todas_las_notas = ...


# --- Ejercicio 8 (Difícil) ---
# Tienes una lista de diccionarios con productos. Crea una lista con los nombres
# de los productos que tengan stock (stock > 0).
inventario = [
    {"nombre": "teclado", "stock": 5},
    {"nombre": "raton", "stock": 0},
    {"nombre": "monitor", "stock": 3},
    {"nombre": "webcam", "stock": 0},
]
# disponibles = ...


# --- Ejercicio 9 (Experto) ---
# Tienes dos listas: productos y sus precios. Genera una lista de strings con el
# formato "producto: precioEUR", pero solo para los productos cuyo precio sea >= 100.
productos = ["portatil", "cargador", "funda", "tablet"]
precios_prod = [800, 25, 15, 300]
# etiquetas = ...


# --- Ejercicio 10 (Experto) ---
# Tienes una matriz (lista de listas). Devuelve su transpuesta usando list comprehensions
# anidadas (las filas se convierten en columnas y viceversa).
matriz = [[1, 2, 3], [4, 5, 6]]
# transpuesta = ...
