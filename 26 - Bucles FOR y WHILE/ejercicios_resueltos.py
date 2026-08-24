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

precios = [12.5, 8.0, 23.99, 5.5, 17.0]

# SOLUCIÓN
for precio in precios:
    print(f"Precio: {precio}€")


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# range() con paso
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — range() con paso")

# SOLUCIÓN
for numero in range(0, 21, 2):
    print(numero)


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

transacciones = [150, -30, 200, -50, 80, -10, 300]

# SOLUCIÓN
for movimiento in transacciones:
    if movimiento < 0:
        continue
    print(movimiento)


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# break para búsqueda
# ──────────────────────────────────────────────
seccion("EJERCICIO 5 — MEDIO — break para búsqueda")

emails = ["user@gmail.com", "admin@empresa.com", "info@empresa.com", "soporte@empresa.com"]

# SOLUCIÓN
for email in emails:
    if email.endswith("@empresa.com"):
        print(email)
        break


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# else en bucle for
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — else en bucle for")

productos_en_stock = ["camiseta", "pantalon", "zapatillas"]


def buscar(nombre: str) -> None:
    # SOLUCIÓN
    for producto in productos_en_stock:
        if producto == nombre:
            print(f"'{nombre}' encontrado")
            break
    else:
        print("Producto no disponible")


buscar("chaqueta")
buscar("camiseta")


# ──────────────────────────────────────────────
# EJERCICIO 7 — MEDIO
# while con condición real
# ──────────────────────────────────────────────
seccion("EJERCICIO 7 — MEDIO — while con condición real")

usuario_correcto = "admin"
clave_correcta = "1234"
intentos_login = [("admin", "wrong"), ("user", "1234"), ("admin", "1234")]

# SOLUCIÓN
indice = 0
acceso = False
while indice < len(intentos_login) and not acceso:
    usuario, clave = intentos_login[indice]
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido")
    else:
        print("Credenciales incorrectas")
    indice += 1


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# while True + break (menú)
# ──────────────────────────────────────────────
seccion("EJERCICIO 8 — AVANZADO — while True + break (menú)")

opciones_menu = ["1. Ver pedidos", "2. Crear pedido", "3. Salir"]
entradas = ["1", "2", "5", "3"]

# SOLUCIÓN
indice_entrada = 0
while True:
    eleccion = entradas[indice_entrada]
    indice_entrada += 1

    if eleccion == "3":
        print("Hasta luego")
        break
    elif eleccion in ("1", "2"):
        print("Ejecutando:", opciones_menu[int(eleccion) - 1])
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
# Combinar todo: validación + búsqueda + else
# ──────────────────────────────────────────────
seccion("EJERCICIO 10 — EXPERTO — Combinar todo: validación + búsqueda + else")

pedidos = [
    {"id": 1, "estado": "enviado", "importe": 45.0},
    {"id": 2, "estado": "pendiente", "importe": 120.5},
    {"id": 3, "estado": "cancelado", "importe": 30.0},
    {"id": 4, "estado": "pendiente", "importe": 89.9},
    {"id": 5, "estado": "enviado", "importe": 200.0},
]

# SOLUCIÓN
total_pendiente = 0.0
for pedido in pedidos:
    if pedido["estado"] != "pendiente":
        continue
    print(pedido["importe"])
    total_pendiente += pedido["importe"]

print(f"Total pendiente: {total_pendiente}")

for pedido in pedidos:
    if pedido["estado"] == "pendiente" and pedido["importe"] > 100:
        print(f"Pedido prioritario encontrado: ID {pedido['id']}")
        break
else:
    print("Ningún pedido supera el umbral prioritario")
