"""
================================================================================
 EJERCICIOS RESUELTOS: BUCLES FOR Y WHILE EN PYTHON
 Ejecutar: python3 ejercicios_resueltos.py
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

# SOLUCIÓN
for temperatura in temperaturas:
    print(f"Temperatura: {temperatura}°C")


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# range() con paso
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — range() con paso")

# SOLUCIÓN
for anio in range(2000, 2031, 4):
    print(anio)


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# while con contador
# ──────────────────────────────────────────────
seccion("EJERCICIO 3 — FÁCIL — while con contador")

# SOLUCIÓN
cuenta = 10
while cuenta >= 1:
    print(cuenta)
    cuenta -= 1
print("Despegue!")


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

# SOLUCIÓN
for comentario in comentarios:
    if comentario["spam"]:
        continue
    print(comentario["texto"])


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

# SOLUCIÓN
for plaza in plazas_parking:
    if plaza["libre"]:
        print(f"Plaza libre encontrada: número {plaza['numero']}")
        break


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# else en bucle for
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — else en bucle for")

despensa = ["harina", "huevos", "leche", "mantequilla"]


def comprobar_ingrediente(nombre: str) -> None:
    # SOLUCIÓN
    for ingrediente in despensa:
        if ingrediente == nombre:
            print(f"'{nombre}' ya está en la despensa")
            break
    else:
        print(f"Falta comprar: {nombre}")


comprobar_ingrediente("azucar")
comprobar_ingrediente("huevos")


# ──────────────────────────────────────────────
# EJERCICIO 7 — MEDIO
# while con condición real
# ──────────────────────────────────────────────
seccion("EJERCICIO 7 — MEDIO — while con condición real")

estado_impresoras = ["ocupada", "ocupada", "libre"]

# SOLUCIÓN
indice = 0
impresion_iniciada = False
while indice < len(estado_impresoras) and not impresion_iniciada:
    if estado_impresoras[indice] == "libre":
        print("Impresión iniciada")
        impresion_iniciada = True
    else:
        print("Impresora ocupada, reintentando...")
    indice += 1


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# while True + break (menú)
# ──────────────────────────────────────────────
seccion("EJERCICIO 8 — AVANZADO — while True + break (menú)")

opciones_cajero = ["1. Consultar saldo", "2. Retirar efectivo", "3. Cambiar PIN", "4. Salir"]
entradas = ["1", "9", "2", "4"]

# SOLUCIÓN
indice_entrada = 0
while True:
    eleccion = entradas[indice_entrada]
    indice_entrada += 1

    if eleccion == "4":
        print("Sesión finalizada")
        break
    elif eleccion in ("1", "2", "3"):
        print("Ejecutando:", opciones_cajero[int(eleccion) - 1])
    else:
        print("Opción no válida")


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

# SOLUCIÓN
for fila_idx, fila in enumerate(sensores):
    for columna_idx, valor in enumerate(fila):
        if valor > umbral:
            print(f"Alerta en sensor fila {fila_idx}, columna {columna_idx}: valor {valor}")
            break


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

# SOLUCIÓN
total_abiertos = 0
for ticket in tickets_soporte:
    if ticket["estado"] != "abierto":
        continue
    print(ticket["id"])
    total_abiertos += 1

print(f"Total tickets abiertos: {total_abiertos}")

for ticket in tickets_soporte:
    if ticket["estado"] == "abierto" and ticket["prioridad"] == "alta":
        print(f"Ticket crítico encontrado: ID {ticket['id']}")
        break
else:
    print("Ningún ticket abierto es de prioridad alta")
