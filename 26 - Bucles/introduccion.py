"""
================================================================================
 BUCLES FOR Y WHILE EN PYTHON
 Ejecutar: python3 introduccion.py
================================================================================
"""


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL BUCLE FOR — ITERAR SOBRE SECUENCIAS
# ============================================================================
seccion("1. El bucle for — iterar sobre secuencias")

# El for de Python no es como el de C: itera sobre los ELEMENTOS de la
# secuencia, no sobre índices numéricos que luego hay que usar para acceder.
pedidos_pendientes = ["pedido-101", "pedido-102", "pedido-103"]

# Antipatrón: viene de otros lenguajes y sobra en Python.
for i in range(len(pedidos_pendientes)):
    print("Procesando (con índice):", pedidos_pendientes[i])

# Forma idiomática: directa, sin índices intermedios que gestionar.
for pedido in pedidos_pendientes:
    print("Procesando:", pedido)

# Si de verdad necesitas el índice (por ejemplo, para numerar), usa enumerate
# en vez de range(len(...)): evita el mismo antipatrón y es más legible.
for numero, pedido in enumerate(pedidos_pendientes, start=1):
    print(f"{numero}. {pedido}")


# ============================================================================
# 2. RANGE() — CUANDO SÍ NECESITAS NÚMEROS
# ============================================================================
seccion("2. range() — cuando sí necesitas números")

# range() sirve para repetir N veces o generar progresiones numéricas,
# no para recorrer una lista (para eso ya vale el for directo de arriba).
for intento in range(3):
    print("Repetición número:", intento)

# range(inicio, fin, paso): fin nunca se incluye.
for numero in range(0, 10, 2):
    print("Par:", numero)

# range no es una lista: es un iterable perezoso, no guarda los números en
# memoria de golpe. range(1_000_000) ocupa lo mismo que range(3).
print(type(range(1_000_000)))
print(list(range(5)))


def peticion_http(intento: int) -> bool:
    # Simula una API que falla las dos primeras veces y responde a la tercera.
    return intento >= 2


# Caso real: reintentar una petición HTTP fallida hasta un máximo de veces.
max_reintentos = 5
for intento in range(max_reintentos):
    if peticion_http(intento):
        print(f"Petición OK en el intento {intento + 1}")
        break
    print(f"Intento {intento + 1} fallido, reintentando...")


# ============================================================================
# 3. BREAK Y CONTINUE — CONTROLAR EL FLUJO DENTRO DEL BUCLE
# ============================================================================
seccion("3. break y continue — controlar el flujo dentro del bucle")

usuarios = [
    {"nombre": "ana", "rol": "editor"},
    {"nombre": "luis", "rol": "lector"},
    {"nombre": "eva", "rol": "admin"},
    {"nombre": "marc", "rol": "admin"},
]

# break: encontrado el primer admin, no tiene sentido seguir mirando el resto.
for usuario in usuarios:
    if usuario["rol"] == "admin":
        print("Primer admin encontrado:", usuario["nombre"])
        break

facturas = [
    {"id": 1, "estado": "pagada"},
    {"id": 2, "estado": "pendiente"},
    {"id": 3, "estado": "pagada"},
    {"id": 4, "estado": "pendiente"},
]

# continue: saltar las facturas ya pagadas y procesar solo las pendientes.
for factura in facturas:
    if factura["estado"] == "pagada":
        continue
    print("Reclamando pago de la factura:", factura["id"])


# ============================================================================
# 4. CLÁUSULA ELSE EN BUCLES — LA CARACTERÍSTICA QUE NADIE TE ENSEÑA
# ============================================================================
seccion("4. Cláusula else en bucles")

# El else de un for/while se ejecuta SOLO si el bucle terminó SIN break.
# No es un if/else: es "qué pasa si nunca encontré lo que buscaba".
stock = ["camiseta", "pantalon", "zapatillas"]


def buscar_producto(nombre: str) -> None:
    for producto in stock:
        if producto == nombre:
            print(f"'{nombre}' encontrado en stock")
            break
    else:
        print(f"'{nombre}' sin stock disponible")


buscar_producto("pantalon")  # hay break -> el else NO se ejecuta
buscar_producto("chaqueta")  # no hay break -> el else SÍ se ejecuta


# ============================================================================
# 5. EL BUCLE WHILE — REPETIR HASTA QUE UNA CONDICIÓN CAMBIE
# ============================================================================
seccion("5. El bucle while — repetir hasta que una condición cambie")

# for: sabes de antemano cuántas iteraciones hay (una secuencia, un range).
# while: no lo sabes, depende de algo que ocurre durante el propio bucle.
credenciales_correctas = ("admin", "1234")
intentos_login = [("admin", "0000"), ("admin", "1111"), ("admin", "1234")]

intentos = 0
acceso_concedido = False
while intentos < 3 and not acceso_concedido:
    usuario, clave = intentos_login[intentos]
    if (usuario, clave) == credenciales_correctas:
        acceso_concedido = True
        print("Acceso concedido")
    else:
        print("Credenciales incorrectas")
    # Si se olvida esta línea, "intentos" nunca cambia y el bucle no termina
    # nunca: un bucle infinito real que colgaría el proceso de login.
    intentos += 1

if not acceso_concedido:
    print("Cuenta bloqueada tras 3 intentos")


# ============================================================================
# 6. WHILE TRUE + BREAK — EL PATRÓN DO-WHILE DE PYTHON
# ============================================================================
seccion("6. while True + break — el patrón do-while de Python")

# Python no tiene do-while nativo. Cuando el cuerpo debe ejecutarse al menos
# una vez antes de poder evaluar la condición de salida, se usa este patrón.
opciones = ["1. Ver pedidos", "2. Crear pedido", "3. Salir"]
entradas_simuladas = ["1", "9", "2", "3"]
entrada_actual = 0

while True:
    for opcion in opciones:
        print(opcion)
    eleccion = entradas_simuladas[entrada_actual]
    entrada_actual += 1
    print("Opción elegida:", eleccion)

    if eleccion == "3":
        print("Hasta luego")
        break
    elif eleccion in ("1", "2"):
        print("Ejecutando:", opciones[int(eleccion) - 1])
    else:
        print("Opción no válida")


# ============================================================================
# 7. BUCLES ANIDADOS — Y CUÁNDO NO USARLOS
# ============================================================================
seccion("7. Bucles anidados — y cuándo no usarlos")

# Tabla de multiplicar: útil para entender la estructura de un for dentro
# de otro for. El bucle interno completa todas sus vueltas por cada vuelta
# del bucle externo.
for fila in range(1, 4):
    for columna in range(1, 4):
        print(f"{fila} x {columna} = {fila * columna}", end="  ")
    print()

# Caso real: por cada cliente (bucle externo, "fila") revisar los productos
# de su pedido (bucle interno, "columna") en busca de un artículo retirado
# del mercado por seguridad.
pedidos_por_cliente = {
    "ana": ["taza", "camiseta", "auriculares-x200"],
    "luis": ["zapatillas", "mochila"],
    "eva": ["cargador", "auriculares-x200", "funda"],
}
productos_retirados = ["auriculares-x200"]

# break en un bucle anidado solo rompe el bucle MÁS INTERNO: en cuanto un
# cliente tiene un producto retirado dejamos de mirar el resto de SUS
# productos, pero el bucle externo sigue revisando a los demás clientes.
for cliente, productos in pedidos_por_cliente.items():
    for producto in productos:
        if producto in productos_retirados:
            print(f"Aviso para {cliente}: el producto '{producto}' ha sido retirado")
            break
    print(f"{cliente}: revisión de su pedido completada")

# El coste real de este patrón es O(clientes x productos_por_cliente). Con
# tres clientes no se nota, pero con datos de producción crece muy rápido.
n_clientes = 10_000
productos_por_cliente = 20
print(
    f"Con {n_clientes:,} clientes y {productos_por_cliente} productos cada uno: "
    f"{n_clientes * productos_por_cliente:,} comparaciones en el peor caso"
)


seccion("FIN — ya conoces los bucles FOR y WHILE al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
