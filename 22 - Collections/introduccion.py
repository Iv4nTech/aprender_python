"""
================================================================================
 COLLECTIONS EN PYTHON (Counter, defaultdict, namedtuple, deque)
 Ejecutar: python3 introduccion.py
================================================================================
"""

from collections import Counter, defaultdict, namedtuple, deque
import time


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA: CONTAR COSAS SIN Counter
# ============================================================================
seccion("1. El problema: contar cosas sin Counter")

logs_peticiones = [
    "/inicio", "/productos", "/inicio", "/carrito", "/productos", "/inicio",
    "/checkout", "/productos", "/inicio", "/carrito", "/productos", "/inicio",
    "/soporte", "/inicio", "/productos",
]

# Sin Counter: hay que comprobar si la clave existe antes de incrementar.
# Olvidar el "if" revienta con KeyError la primera vez que aparece una URL nueva.
conteo_manual = {}
for url in logs_peticiones:
    if url in conteo_manual:
        conteo_manual[url] += 1
    else:
        conteo_manual[url] = 1
print(f"  Conteo manual (dict + if): {conteo_manual}")

# Con Counter: una sola línea, y las claves inexistentes devuelven 0
# en vez de lanzar KeyError.
conteo_urls = Counter(logs_peticiones)
print(f"  Con Counter:               {conteo_urls}")
print(f"  URL nunca vista -> {conteo_urls['/admin']} (no KeyError)")

# Counter también se construye desde un dict ya hecho o desde kwargs.
desde_dict = Counter({"a": 3, "b": 1})
desde_kwargs = Counter(a=3, b=1)
print(f"\n  Counter desde dict:   {desde_dict}")
print(f"  Counter desde kwargs: {desde_kwargs}")

# most_common(n): las N URLs más visitadas, justo lo que pedía el enunciado.
print(f"\n  Top 3 URLs más visitadas: {conteo_urls.most_common(3)}")

# total(): suma de todos los conteos (Added in 3.10). Sin esto, tocaba
# sum(conteo_urls.values()) a mano.
print(f"  Total de peticiones (total()): {conteo_urls.total()}")

# Aritmética entre Counters: comparar tráfico de dos periodos.
trafico_manana = Counter({"/inicio": 50, "/productos": 30, "/carrito": 10})
trafico_tarde = Counter({"/inicio": 20, "/productos": 45, "/soporte": 15})

print(f"\n  Tráfico mañana: {trafico_manana}")
print(f"  Tráfico tarde:  {trafico_tarde}")
print(f"  Suma (+):        {trafico_manana + trafico_tarde}")
print(f"  Resta (-), solo positivos: {trafico_manana - trafico_tarde}")
print(f"  Intersección (&), el mínimo de cada URL: {trafico_manana & trafico_tarde}")
print(f"  Unión (|), el máximo de cada URL:        {trafico_manana | trafico_tarde}")

# Comparaciones ricas (Added in 3.10): útil para detectar si un periodo
# "contiene" a otro (todas sus URLs con al menos el mismo tráfico).
base = Counter({"/inicio": 10, "/productos": 5})
ampliado = Counter({"/inicio": 20, "/productos": 10, "/carrito": 3})
print(f"\n  base <= ampliado -> {base <= ampliado} (ampliado cubre o supera a base en todo)")
print(f"  ampliado <= base -> {ampliado <= base}")


# ============================================================================
# 2. EL PROBLEMA: AGRUPAR DATOS SIN defaultdict
# ============================================================================
seccion("2. El problema: agrupar datos sin defaultdict")

pedidos_csv = [
    ("C001", "Teclado"), ("C002", "Ratón"), ("C001", "Monitor"),
    ("C003", "Teclado"), ("C002", "Auriculares"), ("C001", "Ratón"),
]

# Sin defaultdict: hay que comprobar si el cliente ya tiene lista antes
# de hacer append. Olvidar el "if" revienta con KeyError.
productos_por_cliente_manual = {}
for cliente, producto in pedidos_csv:
    if cliente not in productos_por_cliente_manual:
        productos_por_cliente_manual[cliente] = []
    productos_por_cliente_manual[cliente].append(producto)
print(f"  Agrupado a mano (dict + if): {productos_por_cliente_manual}")

# Con defaultdict(list): la clave se crea sola con una lista vacía la
# primera vez que se usa. Nada de comprobaciones, nada de KeyError.
productos_por_cliente = defaultdict(list)
for cliente, producto in pedidos_csv:
    productos_por_cliente[cliente].append(producto)
print(f"  Con defaultdict(list):       {dict(productos_por_cliente)}")

# defaultdict(int): alternativa ligera a Counter cuando solo quieres sumar,
# sin necesitar most_common(), total() ni la aritmética de Counter.
ventas_region = [("Norte", 100), ("Sur", 50), ("Norte", 30), ("Este", 20)]
total_por_region = defaultdict(int)
for region, importe in ventas_region:
    total_por_region[region] += importe
print(f"\n  defaultdict(int) para sumar: {dict(total_por_region)}")

# defaultdict(set): agrupar evitando duplicados (un cliente que repite
# el mismo producto dos veces no debería contar dos veces en su set).
productos_unicos_cliente = defaultdict(set)
for cliente, producto in pedidos_csv + [("C001", "Teclado")]:  # Teclado repetido
    productos_unicos_cliente[cliente].add(producto)
print(f"  defaultdict(set) sin duplicados: {dict(productos_unicos_cliente)}")

# defaultdict con factory personalizada vía lambda: valor inicial distinto de 0.
saldo_cuentas = defaultdict(lambda: 100.0)  # toda cuenta nueva arranca con 100
saldo_cuentas["cliente_nuevo"] -= 30.0
print(f"\n  defaultdict(lambda: 100.0): {dict(saldo_cuentas)}")

# TRAMPA CRÍTICA: acceder con [] a una clave inexistente LA CREA.
d = defaultdict(list)
print(f"\n  Antes de consultar 'x' con []: {list(d.keys())}")
_ = d["x"]  # esto ya ha creado la clave "x" con lista vacía, aunque no la usemos
print(f"  Después de 'd[\"x\"]' (solo para leer): {list(d.keys())}  <- se creó sola")

# Para comprobar existencia sin crear la clave, usar "in".
print(f"  '\"y\" in d' (no crea nada): {'y' in d}")
print(f"  Claves tras el 'in': {list(d.keys())}")

# .get() NO activa el default_factory: devuelve None si no existe, y no crea nada.
print(f"  d.get('z') (no activa el factory): {d.get('z')}")
print(f"  Claves tras el .get(): {list(d.keys())}")

# Desde 3.9, los dict (y defaultdict) soportan el operador merge | y |=.
extra = {"z": [99]}
fusionado = d | extra
print(f"\n  Merge con | (PEP 584): {dict(fusionado)}")


# ============================================================================
# 3. EL PROBLEMA: TUPLAS SIN NOMBRES
# ============================================================================
seccion("3. El problema: tuplas sin nombres")


def obtener_empleado_de_bd() -> tuple:
    # Simula una fila cruda devuelta por un driver de base de datos.
    return (42, "María García", "maria@empresa.com", 2800.0)


fila = obtener_empleado_de_bd()
# ¿Qué es fila[2]? Hay que ir a mirar la query o la documentación cada vez.
print(f"  Tupla posicional: {fila}")
print(f"  fila[1] = {fila[1]}  (¿nombre? ¿email? sin mirar la query no se sabe)")

# Con namedtuple: mismos datos, pero autoexplicativos y sin overhead
# frente a una tupla normal (sigue siendo inmutable y compatible con índices).
Empleado = namedtuple("Empleado", ["id", "nombre", "email", "salario"])

empleado = Empleado(42, "María García", "maria@empresa.com", 2800.0)
print(f"\n  namedtuple:      {empleado}")
print(f"  Por nombre:      empleado.nombre = {empleado.nombre}")
print(f"  Por índice:      empleado[1] = {empleado[1]}  (ambos funcionan)")

# _make(iterable): construir una namedtuple directamente desde una fila
# de CSV/BD, sin desempaquetar campo a campo a mano.
filas_bd = [
    ("E001", "Ana López", "ana@empresa.com", 2800.0),
    ("E002", "Luis Ruiz", "luis@empresa.com", 3200.0),
]
Trabajador = namedtuple("Trabajador", ["id", "nombre", "email", "salario"])
trabajadores = [Trabajador._make(fila) for fila in filas_bd]
print(f"\n  _make sobre filas de BD: {trabajadores}")

# _replace(): crea una COPIA modificada (la tupla original no muta).
# Desde 3.13, pasar un campo que no existe lanza TypeError (antes ValueError).
ana_con_subida = trabajadores[0]._replace(salario=trabajadores[0].salario * 1.10)
print(f"\n  Original:        {trabajadores[0]}")
print(f"  Tras _replace:   {ana_con_subida}")
try:
    trabajadores[0]._replace(bono=100)
except TypeError as e:
    print(f"  _replace con campo inválido -> TypeError: {e}")

# _asdict(): convertir a dict normal (desde 3.8, ya no OrderedDict) para,
# por ejemplo, serializar a JSON.
print(f"\n  _asdict(): {ana_con_subida._asdict()}")

# _fields: introspección de los nombres de campo declarados.
print(f"  _fields: {Empleado._fields}")

# Parámetro defaults (Added in 3.7): valores por defecto para campos
# opcionales, útil cuando no todos los pedidos tienen descuento aplicado.
Pedido = namedtuple("Pedido", ["id", "importe", "descuento"], defaults=[0.0])
pedido_sin_descuento = Pedido(1, 100.0)
pedido_con_descuento = Pedido(2, 100.0, 5.10)
print(f"\n  namedtuple con defaults: {pedido_sin_descuento}")
print(f"  Sobrescribiendo el default: {pedido_con_descuento}")

print("\n  namedtuple vs dataclass:")
print("    namedtuple: inmutable, compatible con tupla (unpacking, índices),")
print("                sin overhead de memoria. Ideal para filas de datos.")
print("    dataclass:  mutable por defecto, admite métodos propios y")
print("                validación en __post_init__. Ideal para entidades")
print("                de dominio que cambian de estado.")


# ============================================================================
# 4. EL PROBLEMA: INSERTAR/ELIMINAR AL PRINCIPIO DE UNA LISTA
# ============================================================================
seccion("4. El problema: insertar/eliminar al principio de una lista")

# Con una lista, insert(0, ...) y pop(0) son O(n): Python desplaza TODOS
# los elementos restantes. Con una cola de tareas grande, esto mata el
# rendimiento a medida que crece.
N = 20_000

lista_cola = []
inicio = time.perf_counter()
for i in range(N):
    lista_cola.insert(0, i)
duracion_lista = time.perf_counter() - inicio

deque_cola = deque()
inicio = time.perf_counter()
for i in range(N):
    deque_cola.appendleft(i)
duracion_deque = time.perf_counter() - inicio

print(f"  Insertar {N} elementos al principio:")
print(f"    list.insert(0, x):    {duracion_lista:.4f}s  (O(n) cada vez)")
print(f"    deque.appendleft(x):  {duracion_deque:.4f}s  (O(1) cada vez)")

# deque es genérico sobre su tipo de contenido desde 3.9: se puede anotar
# como deque[int], deque[str], etc., igual que list[int].
cola_tareas: deque[str] = deque()
cola_tareas.append("enviar_email")       # entra por la derecha
cola_tareas.append("generar_informe")
cola_tareas.appendleft("tarea_urgente")  # prioridad: entra por la izquierda
print(f"\n  Cola de tareas: {cola_tareas}")
print(f"  Procesando (popleft): {cola_tareas.popleft()}")
print(f"  Cola tras procesar:   {cola_tareas}")

# maxlen: deque de tamaño fijo. Útil para "últimas N lecturas de un sensor":
# el dato más antiguo se descarta automáticamente al llegar uno nuevo.
ultimas_lecturas = deque(maxlen=5)
for temperatura in [22.1, 23.4, 21.8, 24.5, 22.9, 25.1, 23.7]:
    ultimas_lecturas.append(temperatura)
    print(f"  Lectura {temperatura} -> buffer: {list(ultimas_lecturas)}")

# rotate(n): rotar n posiciones (positivo = derecha, negativo = izquierda).
turnos = deque(["Ana", "Luis", "Marta", "Pedro"])
print(f"\n  Turnos: {list(turnos)}")
turnos.rotate(1)
print(f"  Tras rotate(1) (derecha, el último pasa a primero): {list(turnos)}")
turnos.rotate(-2)
print(f"  Tras rotate(-2) (izquierda, dos posiciones): {list(turnos)}")


# ============================================================================
# 5. TABLA RESUMEN — CUÁNDO USAR CADA UNO
# ============================================================================
seccion("5. Tabla resumen: cuándo usar cada uno")

print("""
    Necesitas...                                       Usa...
    -------------------------------------------------  -----------------
    Contar ocurrencias y operar con conteos             Counter
    Agrupar elementos evitando KeyError                 defaultdict
    Tupla con campos con nombre e inmutable              namedtuple
    Cola/pila con operaciones O(1) en ambos extremos     deque
""")

seccion("FIN — ya conoces collections al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
