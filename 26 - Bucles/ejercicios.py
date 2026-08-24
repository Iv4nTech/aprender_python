"""
================================================================================
 EJERCICIOS: BUCLES FOR Y WHILE EN PYTHON
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
# for básico sobre lista
# ──────────────────────────────────────────────
seccion("EJERCICIO 1 — FÁCIL — for básico sobre lista")

temperaturas = [21.5, 19.0, 25.3, 30.1, 18.4]

# Imprime cada temperatura con el formato "Temperatura: X°C"
...

# Resultado esperado:
# Temperatura: 21.5°C
# Temperatura: 19.0°C
# Temperatura: 25.3°C
# Temperatura: 30.1°C
# Temperatura: 18.4°C


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# range() con paso
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — range() con paso")

# Usando range(), imprime los años bisiestos entre 2000 y 2030 (ambos
# límites incluidos si corresponde), es decir, los múltiplos de 4.
...

# Resultado esperado: 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028 (uno por línea)


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# while con contador
# ──────────────────────────────────────────────
seccion("EJERCICIO 3 — FÁCIL — while con contador")

# Simula un contador regresivo de lanzamiento: imprime del 10 al 1 y
# luego "Despegue!". Usa while.
...

# Resultado esperado: 10, 9, 8, ..., 1, "Despegue!"


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# continue para filtrar
# ──────────────────────────────────────────────
seccion("EJERCICIO 4 — MEDIO — continue para filtrar")

comentarios = [
    {"autor": "usuario1", "texto": "Buen artículo, gracias", "spam": False},
    {"autor": "bot99", "texto": "Compra seguidores aquí -> link", "spam": True},
    {"autor": "usuario2", "texto": "Muy claro, lo he entendido", "spam": False},
    {"autor": "bot42", "texto": "Gana dinero rápido, escríbeme", "spam": True},
    {"autor": "usuario3", "texto": "Justo lo que buscaba", "spam": False},
]

# Imprime el texto de los comentarios que NO son spam, usando continue
# para saltar los marcados como spam.
...

# Resultado esperado:
# Buen artículo, gracias
# Muy claro, lo he entendido
# Justo lo que buscaba


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# break para búsqueda
# ──────────────────────────────────────────────
seccion("EJERCICIO 5 — MEDIO — break para búsqueda")

plazas_parking = [
    {"numero": 1, "libre": False},
    {"numero": 2, "libre": False},
    {"numero": 3, "libre": True},
    {"numero": 4, "libre": True},
]

# Encuentra e imprime "Plaza libre encontrada: número X" para la primera
# plaza libre, y para la búsqueda con break.
...

# Resultado esperado: Plaza libre encontrada: número 3


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# else en bucle for
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — else en bucle for")

despensa = ["harina", "huevos", "leche", "mantequilla"]


def comprobar_ingrediente(nombre: str) -> None:
    # Busca "nombre" en la despensa con un for. Si no se encuentra, el
    # bloque else debe imprimir "Falta comprar: <nombre>".
    ...


# Pruébalo con "azucar" (no está) y "huevos" (sí está) para ver que el
# else no se ejecuta cuando hay break.
# comprobar_ingrediente("azucar")
# comprobar_ingrediente("huevos")


# ──────────────────────────────────────────────
# EJERCICIO 7 — MEDIO
# while con condición real
# ──────────────────────────────────────────────
seccion("EJERCICIO 7 — MEDIO — while con condición real")

estado_impresoras = ["ocupada", "ocupada", "libre"]

# Recorre estado_impresoras con while: mientras la impresora esté
# "ocupada", imprime "Impresora ocupada, reintentando..." y prueba con
# la siguiente. En cuanto encuentres una "libre", imprime
# "Impresión iniciada" y para.
...

# Resultado esperado:
# Impresora ocupada, reintentando...
# Impresora ocupada, reintentando...
# Impresión iniciada


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# while True + break (menú)
# ──────────────────────────────────────────────
seccion("EJERCICIO 8 — AVANZADO — while True + break (menú)")

opciones_cajero = ["1. Consultar saldo", "2. Retirar efectivo", "3. Cambiar PIN", "4. Salir"]
entradas = ["1", "9", "2", "4"]

# Usa while True para mostrar el menú y "pedir" cada entrada de la lista
# entradas (una por vuelta, en orden). Si la entrada es "4", imprime
# "Sesión finalizada" y sal del bucle. Para "1", "2" o "3", imprime
# "Ejecutando: <opción>". Para cualquier otra, imprime "Opción no válida".
...

# Resultado esperado:
# Ejecutando: 1. Consultar saldo
# Opción no válida
# Ejecutando: 2. Retirar efectivo
# Sesión finalizada


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# Bucles anidados con break interno
# ──────────────────────────────────────────────
seccion("EJERCICIO 9 — AVANZADO — Bucles anidados con break interno")

sensores = [
    [12, 45, 23, 11],
    [34, 67, 89, 21],  # el 89 supera el umbral de 80
    [5, 14, 33, 72],
]
umbral = 80

# Busca el primer valor que supere "umbral". Cuando lo encuentres, imprime
# "Alerta en sensor fila X, columna Y: valor Z" y para solo el bucle
# interno. El bucle externo debe seguir revisando el resto de filas.
...

# Resultado esperado: "Alerta en sensor fila 1, columna 2: valor 89"


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Combinar todo: filtrado + conteo + búsqueda + else
# ──────────────────────────────────────────────
seccion("EJERCICIO 10 — EXPERTO — Combinar todo: filtrado + conteo + búsqueda + else")

tickets_soporte = [
    {"id": 201, "estado": "cerrado", "prioridad": "baja"},
    {"id": 202, "estado": "abierto", "prioridad": "alta"},
    {"id": 203, "estado": "abierto", "prioridad": "media"},
    {"id": 204, "estado": "escalado", "prioridad": "alta"},
    {"id": 205, "estado": "abierto", "prioridad": "alta"},
]

# 1) Imprime el id de todos los tickets en estado "abierto"
#    (usa continue para saltar los demás)
# 2) Cuenta e imprime cuántos tickets abiertos hay en total
# 3) Busca si existe algún ticket abierto de prioridad "alta"; si lo hay,
#    imprime "Ticket crítico encontrado: ID X" y para; si no hay ninguno,
#    el else debe imprimir "Ningún ticket abierto es de prioridad alta"
...

# Resultado esperado:
# 202
# 203
# 205
# Total tickets abiertos: 3
# Ticket crítico encontrado: ID 202
