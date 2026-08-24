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

precios = [12.5, 8.0, 23.99, 5.5, 17.0]

# Imprime cada precio con el formato "Precio: X€"
...

# Resultado esperado:
# Precio: 12.5€
# Precio: 8.0€
# Precio: 23.99€
# Precio: 5.5€
# Precio: 17.0€


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# range() con paso
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — range() con paso")

# Usando range(), imprime todos los números pares del 0 al 20 inclusive
...

# Resultado esperado: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 (uno por línea)


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

transacciones = [150, -30, 200, -50, 80, -10, 300]

# Imprime solo las transacciones positivas (ingresos), usando continue
# para saltar los negativos.
...

# Resultado esperado: 150, 200, 80, 300 (uno por línea)


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# break para búsqueda
# ──────────────────────────────────────────────
seccion("EJERCICIO 5 — MEDIO — break para búsqueda")

emails = ["user@gmail.com", "admin@empresa.com", "info@empresa.com", "soporte@empresa.com"]

# Encuentra e imprime el primer email del dominio @empresa.com y para
# la búsqueda con break.
...

# Resultado esperado: admin@empresa.com


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# else en bucle for
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — else en bucle for")

productos_en_stock = ["camiseta", "pantalon", "zapatillas"]


def buscar(nombre: str) -> None:
    # Busca "nombre" con un for. Si no se encuentra, el bloque else debe
    # imprimir "Producto no disponible".
    ...


# Pruébalo buscando "chaqueta" (no está) y "camiseta" (sí está) para ver
# que el else no se ejecuta cuando hay break.
# buscar("chaqueta")
# buscar("camiseta")


# ──────────────────────────────────────────────
# EJERCICIO 7 — MEDIO
# while con condición real
# ──────────────────────────────────────────────
seccion("EJERCICIO 7 — MEDIO — while con condición real")

usuario_correcto = "admin"
clave_correcta = "1234"
intentos_login = [("admin", "wrong"), ("user", "1234"), ("admin", "1234")]

# Itera sobre intentos_login con while o for simulando los intentos.
# Imprime "Acceso concedido" o "Credenciales incorrectas" según cada
# intento, y para al primer acceso correcto.
...

# Resultado esperado:
# Credenciales incorrectas
# Credenciales incorrectas
# Acceso concedido


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# while True + break (menú)
# ──────────────────────────────────────────────
seccion("EJERCICIO 8 — AVANZADO — while True + break (menú)")

opciones_menu = ["1. Ver pedidos", "2. Crear pedido", "3. Salir"]
entradas = ["1", "2", "5", "3"]

# Usa while True para mostrar el menú y "pedir" cada entrada de la lista
# entradas (una por vuelta, en orden). Si la entrada es "3", imprime
# "Hasta luego" y sal del bucle. Para "1" o "2", imprime
# "Ejecutando: <opción>". Para cualquier otra, imprime "Opción no válida".
...

# Resultado esperado:
# Ejecutando: 1. Ver pedidos
# Ejecutando: 2. Crear pedido
# Opción no válida
# Hasta luego


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

# 1) Imprime el importe de todos los pedidos en estado "pendiente"
#    (usa continue para saltar los demás)
# 2) Calcula e imprime el importe total de pedidos pendientes
# 3) Busca si existe algún pedido pendiente con importe superior a 100€;
#    si lo hay, imprime "Pedido prioritario encontrado: ID X" y para;
#    si no hay ninguno, el else debe imprimir
#    "Ningún pedido supera el umbral prioritario"
...

# Resultado esperado:
# 120.5
# 89.9
# Total pendiente: 210.4
# Pedido prioritario encontrado: ID 2
