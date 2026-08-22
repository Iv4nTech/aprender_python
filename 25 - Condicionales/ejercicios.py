"""
================================================================================
 EJERCICIOS: CONDICIONALES EN PYTHON
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
# Verificar stock antes de confirmar un pedido
# ──────────────────────────────────────────────
# El almacén necesita saber si un pedido se puede confirmar según el
# stock disponible, antes de descontarlo.
seccion("EJERCICIO 1 — FÁCIL — Verificar stock antes de confirmar un pedido")


def verificar_stock(stock: int, cantidad: int) -> str:
    # Devuelve "Pedido confirmado" si hay stock suficiente,
    # o "Sin stock suficiente" en caso contrario
    ...


# Resultado esperado: 'Pedido confirmado', 'Sin stock suficiente'
# print(verificar_stock(10, 4))
# print(verificar_stock(2, 5))


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Precio final según el tipo de cliente
# ──────────────────────────────────────────────
# La tienda aplica descuentos distintos según el tipo de cliente.
seccion("EJERCICIO 2 — FÁCIL — Precio final según el tipo de cliente")


def calcular_precio(precio_base: float, tipo_cliente: str) -> float:
    # premium -> 10% de descuento, empleado -> 25% de descuento,
    # normal -> precio base sin cambios. Redondea a 2 decimales.
    ...


# Resultado esperado: 90.0, 75.0, 100.0
# print(calcular_precio(100.0, "premium"))
# print(calcular_precio(100.0, "empleado"))
# print(calcular_precio(100.0, "normal"))


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Clasificar un pedido como prioritario
# ──────────────────────────────────────────────
# Ciertos números de pedido están marcados como prioritarios y deben
# procesarse antes que el resto.
seccion("EJERCICIO 3 — FÁCIL — Clasificar un pedido como prioritario")

pedidos_prioritarios = [1042, 1077, 1099]


def clasificar_pedido(numero: int, prioritarios: list) -> str:
    # Devuelve "Prioritario" si numero está en prioritarios,
    # o "Estándar" en caso contrario. Usa el operador in.
    ...


# Resultado esperado: 'Prioritario', 'Estándar'
# print(clasificar_pedido(1077, pedidos_prioritarios))
# print(clasificar_pedido(2000, pedidos_prioritarios))


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Calcular el coste de envío según peso y destino
# ──────────────────────────────────────────────
# La logística cobra el envío según el peso del paquete y el destino.
seccion("EJERCICIO 4 — MEDIO — Calcular el coste de envío según peso y destino")


def coste_envio(peso: float, destino: str) -> float:
    # nacional < 5kg -> 3, nacional >= 5kg -> 6
    # europeo < 10kg -> 12, europeo >= 10kg -> 20
    # internacional -> 35 siempre, sea cual sea el peso
    ...


# Resultado esperado: 3, 6, 12, 20, 35
# print(coste_envio(3, "nacional"))
# print(coste_envio(7, "nacional"))
# print(coste_envio(8, "europeo"))
# print(coste_envio(15, "europeo"))
# print(coste_envio(1, "internacional"))


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Aplicar un código de descuento al carrito
# ──────────────────────────────────────────────
# Un código de descuento solo se aplica si el carrito no está vacío y
# supera un mínimo de 50€.
seccion("EJERCICIO 5 — MEDIO — Aplicar un código de descuento al carrito")

codigos_validos = {"DESC10": 0.10, "DESC20": 0.20, "GRATIS_ENVIO": 0.0}


def calcular_total(carrito: list, codigo: str) -> float:
    # Si el carrito está vacío (usa un valor truthy/falsy para comprobarlo),
    # el total es 0. Si el código es válido y el subtotal supera 50€,
    # aplica el descuento correspondiente. Si no, devuelve el subtotal tal cual.
    ...


# Resultado esperado: 81.0, 60, 0
# print(calcular_total([50, 20, 20], "DESC10"))
# print(calcular_total([30, 30], "CODIGO_INVALIDO"))
# print(calcular_total([], "DESC10"))


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# Permisos de un usuario según su rol
# ──────────────────────────────────────────────
# El panel de administración necesita saber qué acciones puede realizar
# cada usuario según su rol y si está activo.
seccion("EJERCICIO 6 — MEDIO — Permisos de un usuario según su rol")


def permisos_usuario(rol: str, activo: bool) -> list:
    # admin activo -> ["leer", "escribir", "eliminar"]
    # editor activo -> ["leer", "escribir"]
    # lector activo -> ["leer"]
    # cualquier rol inactivo -> [] (ninguna acción)
    ...


# Resultado esperado: ['leer', 'escribir', 'eliminar'], ['leer'], []
# print(permisos_usuario("admin", True))
# print(permisos_usuario("lector", True))
# print(permisos_usuario("admin", False))


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# Aplanar validación de pedido con cláusulas de guarda
# ──────────────────────────────────────────────
# Esta función valida un pedido con condicionales anidados. Reescríbela
# usando cláusulas de guarda (early return) en lugar de condicionales
# anidados, para que el camino principal quede plano.
seccion("EJERCICIO 7 — AVANZADO — Aplanar validación de pedido con cláusulas de guarda")


def validar_pedido_anidado(pedido: dict) -> str:
    if pedido["cantidad"] > 0:
        if pedido["direccion"]:
            if pedido["metodo_pago"] in ("tarjeta", "paypal"):
                return "Pedido válido"
            else:
                return "Método de pago no soportado"
        else:
            return "Falta la dirección de envío"
    else:
        return "La cantidad debe ser mayor que 0"


def validar_pedido(pedido: dict) -> str:
    # Reescribe validar_pedido_anidado sin anidamiento, con early return
    ...


# Resultado esperado: 'Pedido válido', 'Falta la dirección de envío'
# print(validar_pedido({"cantidad": 2, "direccion": "Calle Falsa 123", "metodo_pago": "tarjeta"}))
# print(validar_pedido({"cantidad": 1, "direccion": "", "metodo_pago": "tarjeta"}))


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Mensaje de confirmación con expresión ternaria
# ──────────────────────────────────────────────
# El mensaje de confirmación de un pedido cambia de formato según si es
# prioritario y si tiene descuento, pero debe construirse en una sola línea.
seccion("EJERCICIO 8 — AVANZADO — Mensaje de confirmación con expresión ternaria")


def mensaje_pedido(numero: int, producto: str, prioritario: bool, descuento: float) -> str:
    # Mensaje base: f"Pedido #{numero}: {producto}"
    # Si prioritario, antepón "[URGENTE] " al mensaje
    # Si descuento > 0, añade al final f" (ahorro: {descuento}€)"
    # Todo con expresiones ternarias, sin usar if normal
    ...


# Resultado esperado:
# '[URGENTE] Pedido #501: Teclado (ahorro: 5€)'
# 'Pedido #502: Monitor'
# print(mensaje_pedido(501, "Teclado", True, 5))
# print(mensaje_pedido(502, "Monitor", False, 0))


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# Ciclo de vida de un pedido con match/case
# ──────────────────────────────────────────────
# Un pedido solo puede cambiar de estado siguiendo transiciones válidas.
# Intentar enviar un pedido no pagado, por ejemplo, no debe estar permitido.
seccion("EJERCICIO 9 — AVANZADO — Ciclo de vida de un pedido con match/case")


def transicion_estado(estado_actual: str, accion: str) -> str:
    # Transiciones válidas:
    # ("pendiente", "pagar") -> "pagado"
    # ("pagado", "enviar") -> "enviado"
    # ("enviado", "entregar") -> "entregado"
    # (cualquier estado, "cancelar") -> "cancelado", excepto si ya está "entregado"
    # cualquier otra combinación -> "Accion no permitida"
    # Usa match/case sobre la tupla (estado_actual, accion)
    ...


# Resultado esperado: 'pagado', 'Accion no permitida', 'cancelado'
# print(transicion_estado("pendiente", "pagar"))
# print(transicion_estado("pendiente", "enviar"))
# print(transicion_estado("pagado", "cancelar"))


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Clasificar transacciones financieras con match/case
# ──────────────────────────────────────────────
# El sistema antifraude necesita clasificar transacciones según su
# forma de pago y algunas propiedades adicionales.
seccion("EJERCICIO 10 — EXPERTO — Clasificar transacciones financieras con match/case")


def clasificar_transaccion(transaccion: dict) -> str:
    # Usa match con patrones de diccionario (destructuring):
    # {"tarjeta": ..., "importe": importe} con importe > 1000 -> "revision_manual"
    # {"paypal": ...} -> "pago_digital"
    # {"transferencia": ..., "iban": ...} -> "pago_bancario"
    # cualquier otro caso -> "desconocido"
    ...


# Resultado esperado: 'revision_manual', 'pago_digital', 'pago_bancario', 'desconocido'
# print(clasificar_transaccion({"tarjeta": "1234", "importe": 1500}))
# print(clasificar_transaccion({"paypal": "user@email.com", "importe": 50}))
# print(clasificar_transaccion({"transferencia": "SEPA", "iban": "ES9121000418450200051332"}))
# print(clasificar_transaccion({"bizum": "600111222"}))
