# ============================================================
# EJERCICIOS: FUNCIONES LAMBDA EN PYTHON
# Casos reales — de fácil a experto
# ============================================================

# ──────────────────────────────────────────────
# EJERCICIO 1 — FÁCIL
# Filtrar usuarios mayores de edad
# ──────────────────────────────────────────────
# Tienes una app con usuarios registrados. Necesitas mostrar
# solo los que son mayores de edad para acceder a cierto contenido.

usuarios = [
    {"nombre": "Ana", "edad": 17},
    {"nombre": "Carlos", "edad": 25},
    {"nombre": "Marta", "edad": 16},
    {"nombre": "Pedro", "edad": 30},
    {"nombre": "Lucía", "edad": 18},
]

# Usa filter() + lambda para obtener solo los mayores de edad (>= 18)
mayores = ...

# Resultado esperado: Ana y Marta fuera, el resto dentro
# print(mayores)


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Ordenar productos por precio en un e-commerce
# ──────────────────────────────────────────────
# Tu tienda online necesita mostrar los productos de menor a mayor precio.

productos = [
    {"nombre": "Teclado", "precio": 45.99},
    {"nombre": "Monitor", "precio": 299.99},
    {"nombre": "Ratón", "precio": 19.99},
    {"nombre": "Auriculares", "precio": 89.99},
    {"nombre": "Webcam", "precio": 59.99},
]

# Usa sorted() + lambda para ordenar por precio ascendente
productos_ordenados = ...

# print(productos_ordenados)


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL-MEDIO
# Aplicar descuento a todos los productos de una campaña
# ──────────────────────────────────────────────
# Es el Black Friday. Todos los precios tienen un 20% de descuento.
# Necesitas generar la lista de precios con descuento aplicado.

precios = [100, 250, 75, 430, 89, 320]

# Usa map() + lambda para aplicar el 20% de descuento a cada precio
# Redondea a 2 decimales dentro del lambda
precios_con_descuento = ...

# Resultado esperado: [80.0, 200.0, 60.0, 344.0, 71.2, 256.0]
# print(list(precios_con_descuento))


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Normalizar emails de una base de datos sucia
# ──────────────────────────────────────────────
# Recibes datos de usuarios con emails en distintos formatos (mayúsculas,
# espacios, etc.). Tienes que limpiarlos y estandarizarlos.

emails_sucios = [
    "  ANA@GMAIL.COM  ",
    "CARLOS@hotmail.com",
    "  marta@YAHOO.ES",
    "PEDRO@empresa.com  ",
]

# Usa map() + lambda para: eliminar espacios y convertir a minúsculas
emails_limpios = ...

# Resultado esperado: ['ana@gmail.com', 'carlos@hotmail.com', 'marta@yahoo.es', 'pedro@empresa.com']
# print(list(emails_limpios))


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Ranking de empleados por rendimiento
# ──────────────────────────────────────────────
# RRHH necesita ordenar a los empleados primero por departamento (A-Z)
# y dentro de cada departamento, por ventas de mayor a menor.

empleados = [
    {"nombre": "Laura",   "depto": "Ventas",    "ventas": 15000},
    {"nombre": "Marcos",  "depto": "Marketing", "ventas": 9000},
    {"nombre": "Sara",    "depto": "Ventas",    "ventas": 22000},
    {"nombre": "Diego",   "depto": "Marketing", "ventas": 13000},
    {"nombre": "Elena",   "depto": "Ventas",    "ventas": 18000},
    {"nombre": "Tomás",   "depto": "Marketing", "ventas": 7500},
]

# Usa sorted() + lambda con clave compuesta (tupla) para ordenar
# por departamento ASC y ventas DESC
ranking = ...

# print(ranking)


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO-DIFÍCIL
# Pipeline de procesamiento de pedidos
# ──────────────────────────────────────────────
# Tienes pedidos de una tienda. Necesitas en una sola cadena:
# 1. Filtrar solo los pedidos entregados
# 2. Extraer únicamente el importe de cada pedido
# 3. Ordenar los importes de mayor a menor

pedidos = [
    {"id": 1, "estado": "entregado",  "importe": 120.5},
    {"id": 2, "estado": "pendiente",  "importe": 340.0},
    {"id": 3, "estado": "entregado",  "importe": 89.99},
    {"id": 4, "estado": "cancelado",  "importe": 210.0},
    {"id": 5, "estado": "entregado",  "importe": 450.75},
    {"id": 6, "estado": "pendiente",  "importe": 60.0},
]

# Encadena filter() + map() + sorted() usando lambdas para obtener
# los importes de pedidos entregados, ordenados de mayor a menor
importes_entregados = ...

# Resultado esperado: [450.75, 120.5, 89.99]
# print(importes_entregados)


# ──────────────────────────────────────────────
# EJERCICIO 7 — DIFÍCIL
# Calcular el revenue total con reduce()
# ──────────────────────────────────────────────
# Necesitas calcular el total de ingresos de una lista de transacciones,
# pero solo contando las que han sido completadas (no las fallidas).

from functools import reduce

transacciones = [
    {"concepto": "Suscripción Pro",  "monto": 29.99,  "estado": "completada"},
    {"concepto": "Compra única",     "monto": 149.00, "estado": "completada"},
    {"concepto": "Renovación",       "monto": 29.99,  "estado": "fallida"},
    {"concepto": "Upgrade plan",     "monto": 59.99,  "estado": "completada"},
    {"concepto": "Compra única",     "monto": 89.00,  "estado": "fallida"},
    {"concepto": "Suscripción Pro",  "monto": 29.99,  "estado": "completada"},
]

# Paso 1: filtra solo las completadas con filter() + lambda
# Paso 2: usa reduce() + lambda para sumar todos los montos
revenue_total = ...

# Resultado esperado: 268.97
# print(f"Revenue total: {revenue_total:.2f}€")


# ──────────────────────────────────────────────
# EJERCICIO 8 — DIFÍCIL
# Sistema de validación de datos con lambdas como reglas
# ──────────────────────────────────────────────
# Tienes un formulario de registro. Las reglas de validación están
# definidas como lambdas y se aplican dinámicamente sobre el input.

reglas = {
    "nombre":    lambda v: len(v) >= 2,
    "email":     lambda v: "@" in v and "." in v.split("@")[-1],
    "password":  lambda v: len(v) >= 8 and any(c.isdigit() for c in v),
    "edad":      lambda v: isinstance(v, int) and v >= 18,
}

datos_usuario = {
    "nombre":   "Al",
    "email":    "alicia@gmail.com",
    "password": "segura",
    "edad":     22,
}

# Usa un dict comprehension + lambda (ya definidas en reglas) para
# obtener un dict con los campos y si pasan o no la validación:
# {"nombre": False, "email": True, "password": False, "edad": True}
resultado_validacion = ...

# print(resultado_validacion)


# ──────────────────────────────────────────────
# EJERCICIO 9 — EXPERTO
# Motor de transformación de registros CSV
# ──────────────────────────────────────────────
# Recibes filas de un CSV como strings. Necesitas construir un pipeline
# configurable de transformaciones usando una lista de lambdas que se
# aplican en secuencia sobre cada fila.

filas_csv = [
    "  001 ; Juan García ; 35 ; Madrid  ",
    "  002 ; ana LÓPEZ ; 28 ; barcelona  ",
    "  003 ; CARLOS ruiz ; 41 ; Valencia  ",
]

transformaciones = [
    lambda fila: fila.strip(),
    lambda fila: fila.split(";"),
    lambda partes: [p.strip() for p in partes],
    lambda partes: {"id": partes[0], "nombre": partes[1].title(), "edad": int(partes[2]), "ciudad": partes[3].capitalize()},
]

# Implementa la función apply_pipeline que aplica cada transformación
# de la lista en orden sobre un elemento, usando reduce()
def apply_pipeline(elemento, pipeline):
    ...

registros = ...  # aplica apply_pipeline a cada fila de filas_csv con map()

# Resultado esperado:
# [
#   {'id': '001', 'nombre': 'Juan García', 'edad': 35, 'ciudad': 'Madrid'},
#   {'id': '002', 'nombre': 'Ana López',   'edad': 28, 'ciudad': 'Barcelona'},
#   {'id': '003', 'nombre': 'Carlos Ruiz', 'edad': 41, 'ciudad': 'Valencia'},
# ]
# print(registros)


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Dispatcher de eventos con lambdas como handlers
# ──────────────────────────────────────────────
# Estás construyendo un sistema de notificaciones. Los handlers de
# cada tipo de evento son lambdas registradas dinámicamente.
# El dispatcher debe ejecutar todos los handlers del evento recibido.

class EventDispatcher:
    def __init__(self):
        self._handlers = {}

    def on(self, evento, handler):
        # Registra un handler (lambda) para un tipo de evento.
        # Si el evento ya tiene handlers, añade el nuevo a la lista.
        ...

    def emit(self, evento, payload):
        # Ejecuta todos los handlers registrados para el evento,
        # pasando payload como argumento. Si no hay handlers, no hace nada.
        ...


dispatcher = EventDispatcher()

# Registra handlers con lambdas:
dispatcher.on("usuario_registrado", lambda p: print(f"[EMAIL] Bienvenido, {p['nombre']}!"))
dispatcher.on("usuario_registrado", lambda p: print(f"[LOG]   Nuevo usuario: {p['email']}"))
dispatcher.on("compra_realizada",   lambda p: print(f"[EMAIL] Gracias por tu compra de {p['importe']}€"))
dispatcher.on("compra_realizada",   lambda p: print(f"[STOCK] Reducir stock del producto {p['producto']}"))

# Al emitir un evento, deben ejecutarse todos sus handlers en orden:
dispatcher.emit("usuario_registrado", {"nombre": "Lucía", "email": "lucia@email.com"})
dispatcher.emit("compra_realizada",   {"importe": 59.99, "producto": "Auriculares BT"})

# Output esperado:
# [EMAIL] Bienvenido, Lucía!
# [LOG]   Nuevo usuario: lucia@email.com
# [EMAIL] Gracias por tu compra de 59.99€
# [STOCK] Reducir stock del producto Auriculares BT
