"""
================================================================================
 EJERCICIOS: COLLECTIONS EN PYTHON (Counter, defaultdict, namedtuple, deque)
 Ejecutar: python3 ejercicios.py

 Completa cada ejercicio donde encuentres '...' y descomenta los print()
 para comprobar el resultado.
================================================================================
"""

from collections import Counter, defaultdict, namedtuple, deque


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ──────────────────────────────────────────────
# EJERCICIO 1 — FÁCIL
# Counter básico con logs
# ──────────────────────────────────────────────
# Tienes los métodos HTTP registrados en un log de acceso y necesitas
# saber cuántas veces aparece cada uno.
seccion("EJERCICIO 1 — FÁCIL — Counter básico con logs")

metodos_http = ["GET", "POST", "GET", "DELETE", "GET", "POST", "GET"]

# Usa Counter para contar cuántas veces aparece cada método
conteo_metodos = ...

# Resultado esperado: Counter({'GET': 4, 'POST': 2, 'DELETE': 1})
# print(conteo_metodos)


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# most_common() para top errores
# ──────────────────────────────────────────────
# Un endpoint de monitorización recibe códigos de error HTTP y necesitas
# saber cuáles son los 2 más frecuentes para priorizar el arreglo.
seccion("EJERCICIO 2 — FÁCIL — most_common() para top errores")

codigos_error = [404, 500, 404, 403, 404, 500, 200, 404, 500]

# Usa Counter + most_common(2) para obtener los 2 errores más frecuentes
top_errores = ...

# Resultado esperado: [(404, 4), (500, 3)]
# print(top_errores)


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# defaultdict para agrupar
# ──────────────────────────────────────────────
# Tienes una lista de transacciones (categoria, importe) y quieres agrupar
# los importes por categoría para el resumen mensual de gastos.
seccion("EJERCICIO 3 — FÁCIL — defaultdict para agrupar")

transacciones = [
    ("alimentacion", 45.0), ("ocio", 20.0), ("alimentacion", 30.0),
    ("transporte", 15.0), ("ocio", 50.0),
]

# Usa defaultdict(list) para agrupar los importes por categoría
importes_por_categoria = ...

# Resultado esperado:
# {'alimentacion': [45.0, 30.0], 'ocio': [20.0, 50.0], 'transporte': [15.0]}
# print(dict(importes_por_categoria))


# ──────────────────────────────────────────────
# EJERCICIO 4 — FÁCIL
# namedtuple básica
# ──────────────────────────────────────────────
# El catálogo de tu tienda necesita representar productos con campos con
# nombre en vez de tuplas posicionales que nadie recuerda cómo leer.
seccion("EJERCICIO 4 — FÁCIL — namedtuple básica")

# Crea una namedtuple "Producto" con campos: nombre, precio, stock
Producto = ...

# Instancia dos productos y accede a sus campos por nombre
teclado = ...
raton = ...

# Resultado esperado: algo como Producto(nombre='Teclado', precio=49.99, stock=10)
# print(teclado)
# print(raton)
# print(f"El {teclado.nombre} cuesta {teclado.precio}€")


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# Counter.total() y aritmética
# ──────────────────────────────────────────────
# Tu panel de analítica compara las visitas de dos días para detectar
# páginas en tendencia y páginas visitadas en ambos días.
seccion("EJERCICIO 5 — MEDIO — Counter.total() y aritmética")

dia1 = Counter({"home": 120, "about": 45, "contacto": 30})
dia2 = Counter({"home": 95, "about": 60, "blog": 40})

# Total de visitas del día 1 con total()
total_dia1 = ...

# Páginas visitadas en ambos días (intersección &)
paginas_ambos_dias = ...

# Todas las páginas de los dos días combinadas (unión |)
todas_las_paginas = ...

# Resultado esperado:
# total_dia1 = 195
# paginas_ambos_dias = Counter({'home': 95, 'about': 45})
# todas_las_paginas  = Counter({'home': 120, 'about': 60, 'blog': 40, 'contacto': 30})
# print(f"Total día 1: {total_dia1}")
# print(f"Páginas en ambos días: {paginas_ambos_dias}")
# print(f"Todas las páginas: {todas_las_paginas}")


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# namedtuple con _make, _replace y _asdict
# ──────────────────────────────────────────────
# Una consulta a la base de datos de RRHH devuelve filas planas. Necesitas
# convertirlas en registros con nombre, subir el salario de una empleada
# un 10% sin mutar el original, y serializar el resultado a dict.
seccion("EJERCICIO 6 — MEDIO — namedtuple con _make, _replace y _asdict")

Empleado = namedtuple("Empleado", ["id", "nombre", "email", "salario"])

filas_bd = [
    ("E001", "Ana López", "ana@empresa.com", 2800.0),
    ("E002", "Luis Ruiz", "luis@empresa.com", 3200.0),
]

# Usa _make sobre cada fila para construir una lista de Empleado
empleados = ...

# Usa _replace para subir el salario del primer empleado (Ana) un 10%
ana_actualizada = ...

# Usa _asdict() para convertir ana_actualizada a un dict normal
ana_dict = ...

# Resultado esperado:
# empleados[0] = Empleado(id='E001', nombre='Ana López', email='ana@empresa.com', salario=2800.0)
# ana_actualizada.salario = 3080.0000000000005
# ana_dict = {'id': 'E001', 'nombre': 'Ana López', 'email': 'ana@empresa.com', 'salario': 3080.0000000000005}
# print(empleados)
# print(ana_actualizada)
# print(ana_dict)


# ──────────────────────────────────────────────
# EJERCICIO 7 — MEDIO
# deque como cola de tareas
# ──────────────────────────────────────────────
# Un worker procesa tareas en orden de llegada, salvo las urgentes que
# deben colarse al principio de la cola.
seccion("EJERCICIO 7 — MEDIO — deque como cola de tareas")

# Crea una cola vacía con deque
cola_tareas = ...

# Añade estas tareas normales por la derecha (append): "email", "informe", "backup"
# Añade esta tarea urgente por la izquierda (appendleft): "alerta_seguridad"
...

# Procesa (extrae) todas las tareas por la izquierda (popleft) y muestra el orden
# Resultado esperado del orden de procesamiento:
# alerta_seguridad, email, informe, backup
# while cola_tareas:
#     print(cola_tareas.popleft())


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# defaultdict anidado para inventario
# ──────────────────────────────────────────────
# La logística de la empresa necesita saber, por cada almacén, cuánta
# cantidad hay de cada producto, sumando las distintas entradas de stock.
seccion("EJERCICIO 8 — AVANZADO — defaultdict anidado para inventario")

inventario = [
    ("Madrid", "Teclado", 50), ("Barcelona", "Ratón", 30),
    ("Madrid", "Ratón", 20), ("Barcelona", "Teclado", 10),
]

# Usa defaultdict(lambda: defaultdict(int)) para agrupar por almacén
# y sumar cantidades por producto
stock_por_almacen = ...

# Resultado esperado:
# {'Madrid': {'Teclado': 50, 'Ratón': 20}, 'Barcelona': {'Ratón': 30, 'Teclado': 10}}
# print({almacen: dict(productos) for almacen, productos in stock_por_almacen.items()})


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# deque con maxlen para ventana deslizante
# ──────────────────────────────────────────────
# Un monitor de temperatura solo necesita las últimas 5 lecturas para
# calcular la media móvil y detectar picos anómalos.
seccion("EJERCICIO 9 — AVANZADO — deque con maxlen para ventana deslizante")

lecturas = [22.1, 23.4, 21.8, 24.5, 22.9, 25.1, 23.7, 24.2]

# Crea un deque con maxlen=5
buffer_temperaturas = ...

# Por cada lectura: añádela al buffer y muestra el buffer y la media actual
# for lectura in lecturas:
#     ...
#     print(f"buffer={list(buffer_temperaturas)} media={sum(buffer_temperaturas) / len(buffer_temperaturas):.2f}")


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Pipeline completo con Counter + defaultdict + namedtuple
# ──────────────────────────────────────────────
# El equipo comercial necesita un resumen de ventas: cuántas ventas hizo
# cada vendedor, cuánto facturó cada región, y un resumen final por
# vendedor con nombre, número de ventas e importe total.
seccion("EJERCICIO 10 — EXPERTO — Pipeline completo con Counter + defaultdict + namedtuple")

ventas = [
    {"vendedor": "Laura", "producto": "Laptop", "importe": 1200.0, "region": "Norte"},
    {"vendedor": "Pedro", "producto": "Ratón", "importe": 25.0, "region": "Sur"},
    {"vendedor": "Laura", "producto": "Teclado", "importe": 80.0, "region": "Norte"},
    {"vendedor": "Ana", "producto": "Laptop", "importe": 1200.0, "region": "Sur"},
    {"vendedor": "Pedro", "producto": "Laptop", "importe": 1200.0, "region": "Norte"},
    {"vendedor": "Laura", "producto": "Ratón", "importe": 25.0, "region": "Sur"},
]

# Paso 1: Counter con el número de ventas por vendedor
ventas_por_vendedor = ...

# Paso 2: defaultdict(float) con el importe total facturado por región
importe_por_region = ...

# Paso 3: namedtuple ResumenVendedor con campos nombre, num_ventas, importe_total
ResumenVendedor = ...

# Construye un resumen por vendedor combinando los pasos 1 y 2 (a nivel de vendedor)
resumen_vendedores = ...

# Paso 4: vendedor con más ventas y región con más facturación
vendedor_top = ...
region_top = ...

# Resultado esperado:
# ventas_por_vendedor = Counter({'Laura': 3, 'Pedro': 2, 'Ana': 1})
# importe_por_region  = {'Norte': 2480.0, 'Sur': 1250.0}
# vendedor_top = ('Laura', 3)
# region_top = ('Norte', 2480.0)
# print(ventas_por_vendedor)
# print(dict(importe_por_region))
# print(resumen_vendedores)
# print(f"Vendedor con más ventas: {vendedor_top}")
# print(f"Región con más facturación: {region_top}")
