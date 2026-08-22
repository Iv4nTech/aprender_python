"""
================================================================================
 CONDICIONALES EN PYTHON
 Ejecutar: python3 introduccion.py
================================================================================
"""


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA SIN CONDICIONALES
# ============================================================================
seccion("1. El problema sin condicionales")

# Un sistema de pedidos que no comprueba nada antes de confirmar.
stock_almacen = {"teclado": 3, "monitor": 0}

pedidos_entrantes = [
    ("teclado", 2),
    ("monitor", 5),
    ("teclado", 4),
]

for producto, cantidad in pedidos_entrantes:
    # Sin condicionales, el código siempre toma el mismo camino: confirmar.
    stock_almacen[producto] -= cantidad
    print(f"Pedido confirmado: {cantidad}x {producto}")

print("Estado final del almacén:", stock_almacen)
# El almacén queda en negativo: se han "vendido" productos que no existían.
# Esto es exactamente lo que un if evitaría: tomar un camino distinto
# según si hay stock suficiente o no.


# ============================================================================
# 2. IF BÁSICO
# ============================================================================
seccion("2. if básico")


def verificar_stock_basico(stock: int, cantidad: int) -> None:
    if stock >= cantidad:
        print("Stock suficiente, se puede confirmar el pedido")
    # Si la condición es False, este bloque no se ejecuta nunca.
    print("verificación terminada")


verificar_stock_basico(stock=3, cantidad=2)
verificar_stock_basico(stock=1, cantidad=5)
# En el segundo caso no se imprime "Stock suficiente": el bloque del if
# se salta por completo cuando la condición es False.


# ============================================================================
# 3. IF / ELSE
# ============================================================================
seccion("3. if / else")


def confirmar_pedido(stock: int, cantidad: int) -> str:
    if stock >= cantidad:
        mensaje = "Pedido confirmado"
    else:
        mensaje = "Sin stock suficiente"
    # else no tiene condición propia: se ejecuta en TODOS los casos
    # restantes, sea cual sea la razón por la que el if no se cumplió.
    return mensaje


print(confirmar_pedido(stock=10, cantidad=4))
print(confirmar_pedido(stock=2, cantidad=4))


# ============================================================================
# 4. IF / ELIF / ELSE
# ============================================================================
seccion("4. if / elif / else")


def calcular_precio(precio_base: float, tipo_cliente: str) -> float:
    if tipo_cliente == "premium":
        return round(precio_base * 0.90, 2)
    elif tipo_cliente == "empleado":
        return round(precio_base * 0.75, 2)
    else:
        return precio_base


print(calcular_precio(100.0, "premium"))
print(calcular_precio(100.0, "empleado"))
print(calcular_precio(100.0, "normal"))


def calcular_precio_con_trampa(precio_base: float, tipo_cliente: str) -> float:
    # La condición más amplia va primero: las específicas nunca se alcanzan.
    if tipo_cliente in ("premium", "empleado", "normal"):
        return precio_base
    elif tipo_cliente == "empleado":
        return round(precio_base * 0.75, 2)
    else:
        return precio_base


print(calcular_precio_con_trampa(100.0, "empleado"))
# Un empleado paga el precio completo: el elif con el descuento del 25%
# nunca se evalúa porque el primer if ya ha capturado el caso.


# ============================================================================
# 5. OPERADORES DE COMPARACIÓN Y LÓGICOS
# ============================================================================
seccion("5. Operadores de comparación y lógicos")

paises_disponibles = ["España", "Portugal", "Francia", "Italia"]


def envio_valido(peso_kg: float, destino: str) -> bool:
    peso_permitido = peso_kg > 0 and peso_kg <= 30
    destino_permitido = destino in paises_disponibles
    return peso_permitido and destino_permitido


print(envio_valido(peso_kg=12.5, destino="España"))
print(envio_valido(peso_kg=45.0, destino="España"))
print(envio_valido(peso_kg=5.0, destino="Alemania"))

pedido_test = {"id": 501, "cliente": None}
print(pedido_test["cliente"] is None)
print(pedido_test["id"] != 0)
print("cliente" not in pedido_test or pedido_test["cliente"] is None)


# ============================================================================
# 6. VALORES TRUTHY Y FALSY
# ============================================================================
seccion("6. Valores truthy y falsy")

carrito_lleno = ["teclado", "monitor"]
carrito_vacio: list[str] = []

if carrito_lleno:
    print("El carrito tiene productos")

if not carrito_vacio:
    print("El carrito está vacío, no se puede pagar")

# La trampa: un carrito puede EXISTIR (no ser None) y aun así estar vacío.
carrito_recibido = []
if carrito_recibido is not None:
    print("El carrito no es None, procesando...")
    if carrito_recibido:
        print("Hay productos que cobrar")
    else:
        print("El carrito existe pero no tiene productos: nada que cobrar")

print(bool(0), bool(0.0), bool(""), bool([]), bool({}), bool(None))
print(bool(1), bool("no vacio"), bool([0]))


# ============================================================================
# 7. EXPRESIÓN TERNARIA (CONDICIONAL EN UNA LÍNEA)
# ============================================================================
seccion("7. Expresión ternaria")


def formatear_estado(estado: str) -> str:
    etiqueta = "ENTREGADO" if estado == "entregado" else estado.upper()
    return f"Pedido: {etiqueta}"


print(formatear_estado("entregado"))
print(formatear_estado("pendiente"))

stock_disponible = 5
cantidad_pedida = 8
print("Stock OK" if stock_disponible >= cantidad_pedida else "Stock insuficiente")

# Cuándo NO usarla: una condición larga en una línea pierde legibilidad.
# Esto es difícil de leer de un vistazo:
resultado_dificil = "premium" if stock_disponible > 0 and cantidad_pedida < 10 and stock_disponible >= cantidad_pedida else "normal"
print(resultado_dificil)
# Mejor un if/else normal cuando la condición ya no cabe en una idea simple.


# ============================================================================
# 8. CONDICIONALES ANIDADOS Y CÓMO EVITARLOS
# ============================================================================
seccion("8. Condicionales anidados y cómo evitarlos")


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


# Funciona, pero cada comprobación añade un nivel de indentación:
# una pirámide que se vuelve difícil de leer con más reglas.


def validar_pedido(pedido: dict) -> str:
    # Cláusulas de guarda: se valida lo que NO cumple y se sale enseguida.
    if pedido["cantidad"] <= 0:
        return "La cantidad debe ser mayor que 0"
    if not pedido["direccion"]:
        return "Falta la dirección de envío"
    if pedido["metodo_pago"] not in ("tarjeta", "paypal"):
        return "Método de pago no soportado"
    # El camino principal queda plano, sin anidar nada.
    return "Pedido válido"


pedido_ok = {"cantidad": 2, "direccion": "Calle Mayor 1", "metodo_pago": "tarjeta"}
pedido_mal = {"cantidad": 0, "direccion": "", "metodo_pago": "bizum"}
print(validar_pedido_anidado(pedido_ok))
print(validar_pedido(pedido_ok))
print(validar_pedido(pedido_mal))


# ============================================================================
# 9. MATCH / CASE (LA ALTERNATIVA MODERNA)
# ============================================================================
seccion("9. match / case")


def gestionar_estado(estado: str) -> str:
    match estado:
        case "pendiente":
            return "Esperando confirmación de pago"
        case "pagado" | "confirmado":
            return "Pago recibido, preparando envío"
        case "enviado":
            return "En camino"
        case "entregado":
            return "Pedido finalizado"
        case _:
            return "Estado desconocido"


for estado_pedido in ("pendiente", "pagado", "enviado", "entregado", "devuelto"):
    print(estado_pedido, "->", gestionar_estado(estado_pedido))

# match también hace destructuring estructural, no solo comparar valores.
evento_webhook = {"tipo": "pago", "importe": 1500, "moneda": "EUR"}

match evento_webhook:
    case {"tipo": "pago", "importe": importe} if importe > 1000:
        print(f"Pago grande de {importe} {evento_webhook['moneda']}: revisión manual")
    case {"tipo": "pago", "importe": importe}:
        print(f"Pago normal de {importe}")
    case _:
        print("Evento no reconocido")

# Nota sobre Python 3.14: los mensajes de SyntaxError son más precisos.
# Por ejemplo, si se escribe un elif después de un else, el intérprete
# señala exactamente esa línea con una flecha en vez de un error genérico.


seccion("FIN — ya conoces los condicionales al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
