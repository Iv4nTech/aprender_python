# ============================================================
# EJERCICIOS RESUELTOS: FUNCIONES LAMBDA EN PYTHON
# ============================================================

# ──────────────────────────────────────────────
# EJERCICIO 1 — FÁCIL
# Filtrar usuarios mayores de edad
# ──────────────────────────────────────────────

usuarios = [
    {"nombre": "Ana", "edad": 17},
    {"nombre": "Carlos", "edad": 25},
    {"nombre": "Marta", "edad": 16},
    {"nombre": "Pedro", "edad": 30},
    {"nombre": "Lucía", "edad": 18},
]

mayores = list(filter(lambda u: u["edad"] >= 18, usuarios))
print("Ejercicio 1:", mayores)


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Ordenar productos por precio en un e-commerce
# ──────────────────────────────────────────────

productos = [
    {"nombre": "Teclado", "precio": 45.99},
    {"nombre": "Monitor", "precio": 299.99},
    {"nombre": "Ratón", "precio": 19.99},
    {"nombre": "Auriculares", "precio": 89.99},
    {"nombre": "Webcam", "precio": 59.99},
]

productos_ordenados = sorted(productos, key=lambda p: p["precio"])
print("\nEjercicio 2:", productos_ordenados)


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL-MEDIO
# Aplicar descuento a todos los productos de una campaña
# ──────────────────────────────────────────────

precios = [100, 250, 75, 430, 89, 320]

precios_con_descuento = list(map(lambda p: round(p * 0.80, 2), precios))
print("\nEjercicio 3:", precios_con_descuento)


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Normalizar emails de una base de datos sucia
# ──────────────────────────────────────────────

emails_sucios = [
    "  ANA@GMAIL.COM  ",
    "CARLOS@hotmail.com",
    "  marta@YAHOO.ES",
    "PEDRO@empresa.com  ",
]

emails_limpios = list(map(lambda e: e.strip().lower(), emails_sucios))
print("\nEjercicio 4:", emails_limpios)


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Ranking de empleados por rendimiento
# ──────────────────────────────────────────────

empleados = [
    {"nombre": "Laura",   "depto": "Ventas",    "ventas": 15000},
    {"nombre": "Marcos",  "depto": "Marketing", "ventas": 9000},
    {"nombre": "Sara",    "depto": "Ventas",    "ventas": 22000},
    {"nombre": "Diego",   "depto": "Marketing", "ventas": 13000},
    {"nombre": "Elena",   "depto": "Ventas",    "ventas": 18000},
    {"nombre": "Tomás",   "depto": "Marketing", "ventas": 7500},
]

# La clave es una tupla: (depto ASC, -ventas para invertir el orden)
ranking = sorted(empleados, key=lambda e: (e["depto"], -e["ventas"]))
print("\nEjercicio 5:")
for e in ranking:
    print(f"  {e['depto']:<12} {e['nombre']:<8} {e['ventas']}")


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO-DIFÍCIL
# Pipeline de procesamiento de pedidos
# ──────────────────────────────────────────────

pedidos = [
    {"id": 1, "estado": "entregado",  "importe": 120.5},
    {"id": 2, "estado": "pendiente",  "importe": 340.0},
    {"id": 3, "estado": "entregado",  "importe": 89.99},
    {"id": 4, "estado": "cancelado",  "importe": 210.0},
    {"id": 5, "estado": "entregado",  "importe": 450.75},
    {"id": 6, "estado": "pendiente",  "importe": 60.0},
]

importes_entregados = sorted(
    map(lambda p: p["importe"],
        filter(lambda p: p["estado"] == "entregado", pedidos)),
    reverse=True
)
print("\nEjercicio 6:", importes_entregados)


# ──────────────────────────────────────────────
# EJERCICIO 7 — DIFÍCIL
# Calcular el revenue total con reduce()
# ──────────────────────────────────────────────

from functools import reduce

transacciones = [
    {"concepto": "Suscripción Pro",  "monto": 29.99,  "estado": "completada"},
    {"concepto": "Compra única",     "monto": 149.00, "estado": "completada"},
    {"concepto": "Renovación",       "monto": 29.99,  "estado": "fallida"},
    {"concepto": "Upgrade plan",     "monto": 59.99,  "estado": "completada"},
    {"concepto": "Compra única",     "monto": 89.00,  "estado": "fallida"},
    {"concepto": "Suscripción Pro",  "monto": 29.99,  "estado": "completada"},
]

revenue_total = reduce(
    lambda acc, t: acc + t["monto"],
    filter(lambda t: t["estado"] == "completada", transacciones),
    0
)
print(f"\nEjercicio 7 — Revenue total: {revenue_total:.2f}€")


# ──────────────────────────────────────────────
# EJERCICIO 8 — DIFÍCIL
# Sistema de validación de datos con lambdas como reglas
# ──────────────────────────────────────────────

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

# Aplica la lambda del campo correspondiente sobre el valor del campo
resultado_validacion = {campo: reglas[campo](valor) for campo, valor in datos_usuario.items()}
print("\nEjercicio 8:", resultado_validacion)


# ──────────────────────────────────────────────
# EJERCICIO 9 — EXPERTO
# Motor de transformación de registros CSV
# ──────────────────────────────────────────────

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

# reduce aplica cada lambda en orden, pasando el resultado anterior como input
def apply_pipeline(elemento, pipeline):
    return reduce(lambda acc, fn: fn(acc), pipeline, elemento)

registros = list(map(lambda fila: apply_pipeline(fila, transformaciones), filas_csv))
print("\nEjercicio 9:")
for r in registros:
    print(" ", r)


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Dispatcher de eventos con lambdas como handlers
# ──────────────────────────────────────────────

class EventDispatcher:
    def __init__(self):
        self._handlers = {}

    def on(self, evento, handler):
        if evento not in self._handlers:
            self._handlers[evento] = []
        self._handlers[evento].append(handler)

    def emit(self, evento, payload):
        # Usa map() para ejecutar todos los handlers; list() fuerza la evaluación
        list(map(lambda h: h(payload), self._handlers.get(evento, [])))


dispatcher = EventDispatcher()

dispatcher.on("usuario_registrado", lambda p: print(f"[EMAIL] Bienvenido, {p['nombre']}!"))
dispatcher.on("usuario_registrado", lambda p: print(f"[LOG]   Nuevo usuario: {p['email']}"))
dispatcher.on("compra_realizada",   lambda p: print(f"[EMAIL] Gracias por tu compra de {p['importe']}€"))
dispatcher.on("compra_realizada",   lambda p: print(f"[STOCK] Reducir stock del producto {p['producto']}"))

print("\nEjercicio 10:")
dispatcher.emit("usuario_registrado", {"nombre": "Lucía", "email": "lucia@email.com"})
dispatcher.emit("compra_realizada",   {"importe": 59.99, "producto": "Auriculares BT"})
