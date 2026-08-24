"""
================================================================================
 VARIABLES Y TIPOS DE DATOS EN PYTHON
 Ejecutar: python3 introduccion.py
================================================================================
"""


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. QUÉ ES UNA VARIABLE Y CÓMO FUNCIONA LA ASIGNACIÓN
# ============================================================================
seccion("1. Qué es una variable y cómo funciona la asignación")

edad_usuario = 32
print("edad_usuario =", edad_usuario)
print(type(edad_usuario))

edad_usuario = "treinta y dos"
print("edad_usuario =", edad_usuario)
print(type(edad_usuario))

nombre, edad, activo = "Iván", 21, True

print(nombre, edad, activo)

errores = advertencias = avisos = 0

print(errores, advertencias, avisos)


# ============================================================================
# 2. TIPOS NUMÉRICOS: int, float
# ============================================================================
seccion("2. Tipos numéricos: int, float")

id_pedido = 8453921
print("id_pedido =", id_pedido)

factorial_50 = 1
for n in range(1, 51):
    factorial_50 *= n   
print("50! =", factorial_50)

precio_a = 0.1
precio_b = 0.2
print(precio_a + precio_b)
print(round(precio_a + precio_b, 2))

unidades = 47 
por_caja = 10
cajas_completas = unidades // por_caja
sobrantes = unidades % por_caja
print("cajas completas:", cajas_completas)
print("unidades sueltas:", sobrantes)

permisos = 0b1011
print(permisos.bit_count())

descuento = float.from_number(15)
print(descuento)

cantidad = int("34444444441214124")
precio_final = round(19.999, 2)
print(cantidad)
print(precio_final)


# ============================================================================
# 3. BOOLEANOS: bool
# ============================================================================
seccion("3. Booleanos: bool")

print(True == 1)
print(False == 0)
print(isinstance(True, int))

carrito_vacio = []
mensaje_error = ""
print(bool(carrito_vacio))
print(bool(mensaje_error))

carrito_con_items = ["teclado"]
print(bool(carrito_con_items))

formulario_valido = len(mensaje_error) == 0 and len(carrito_con_items) > 0
print(formulario_valido)


# ============================================================================
# 4. CADENAS DE TEXTO: str
# ============================================================================
seccion("4. Cadenas de texto: str")

nombre_usuario = "  ivan.gomez  "
print(nombre_usuario)

limpio = nombre_usuario.strip()
print(nombre_usuario)
print(limpio)

usuario_id = 42
mensaje = "Usuario #" + str(usuario_id) + ": " + limpio
print(mensaje)
print(limpio.upper())
print(limpio.lower())
print(limpio.replace(".", "_"))
print(limpio.split("."))

url_api = "https://api.ejemplo.com/v1/usuarios"
print(url_api.startswith("https"))
print(url_api.endswith("/usuarios"))

ruta = "/api/v1/pedidos"
print(ruta.removeprefix("/api/v1"))
print(ruta.removesuffix("/pedidos"))

telefono = "+34577777773"
print(telefono[0])
print(telefono[1:3])
print(telefono[-9:])


# ============================================================================
# 5. LISTAS: list
# ============================================================================
seccion("5. Listas: list")

carrito = ["teclado", "raton"] 
carrito.append("monitor")
carrito.extend(["cable hdmi", "raton"])
carrito.insert(0, "auriculares")
print(carrito)

carrito.remove("raton")
ultimo = carrito.pop()
print(carrito)
print(ultimo)

print(carrito[:2])

errores_formulario = ["email", "contraseña", "codigo_postal"]
copia_ordenada = sorted(errores_formulario)
errores_formulario.sort()
print(copia_ordenada)
print(errores_formulario)
errores_formulario.reverse()
print(errores_formulario)


# ============================================================================
# 6. DICCIONARIOS: dict
# ============================================================================
seccion("6. Diccionarios: dict")

perfil_usuario = {"nombre": "Ivan", "email": "ivan@empresa.com", "rol": "admin"}
print(perfil_usuario)

if "telefono" in perfil_usuario:
    print(perfil_usuario["telefono"])
else:
    print("la clave telefono no existe")

telefono = perfil_usuario.get("telefono", "no proporcionado")
print(telefono)

perfil_usuario.update({"telefono": "600111222", "rol": "editor"})
print(perfil_usuario)

rol_eliminado = perfil_usuario.pop("rol")
print(rol_eliminado)
print(perfil_usuario)

print(list(perfil_usuario.keys()))
print(list(perfil_usuario.values()))
print(list(perfil_usuario.items()))

for clave, valor in perfil_usuario.items():
    print(clave, valor)


# ============================================================================
# 7. MENCIÓN RÁPIDA: tuple Y set
# ============================================================================
seccion("7. Mención rápida: tuple y set")

coordenada_gps = (40.4, -3.7)
print(coordenada_gps)

permisos_usuario = {"leer", "escribir", "escribir"}
print(permisos_usuario)

# Para profundizar, busca los vídeos dedicados a Tuplas y Sets en el canal.


# ============================================================================
# 8. None: EL VALOR VACÍO
# ============================================================================
seccion("8. None: el valor vacío")

campo_opcional = None
print(campo_opcional)
print(type(campo_opcional))
print(campo_opcional == 0)
print(campo_opcional is None)


usuarios_bd = {1: "Iván"}
resultado = usuarios_bd.get(999)
print(resultado)
print(resultado is None)


# ============================================================================
# 9. CONVERSIÓN ENTRE TIPOS (CASTING)
# ============================================================================
seccion("9. Conversión entre tipos (casting)")

print(int("42"))
print(float("19.99"))
print(str(42))
print(bool(0))
print(bool(1))
print(list("abc"))
print(tuple([1, 2, 3]))

texto = "hola"
if texto.isdigit():
    print(int(texto))
else:
    print("no se puede convertir a int")

print(isinstance(True, int))
print(isinstance(19.99, (int, float)))
print(isinstance("hola", (int, float)))


# ============================================================================
# 10. TABLA RESUMEN COMPARATIVA
# ============================================================================
seccion("10. Tabla resumen comparativa")

filas = [
    ("int", "Inmutable", "N/A", "N/A", "edad = 32"),
    ("float", "Inmutable", "N/A", "N/A", "precio = 19.99"),
    ("str", "Inmutable", "Ordenado", "Si", "nombre = 'Iván'"),
    ("bool", "Inmutable", "N/A", "N/A", "activo = True"),
    ("list", "Mutable", "Ordenado", "Si", "carrito = ['a', 'b']"),
    ("tuple", "Inmutable", "Ordenado", "Si", "coord = (40.4, -3.7)"),
    ("dict", "Mutable", "Ordenado", "Claves unicas", "perfil = {'rol': 'admin'}"),
    ("set", "Mutable", "No", "No", "permisos = {'leer'}"),
    ("None", "Inmutable", "N/A", "N/A", "campo = None"),
]

print("Tipo", "Mutabilidad", "Orden", "Duplicados", "Ejemplo real")
for tipo, mutabilidad, orden, duplicados, ejemplo in filas:
    print(tipo, mutabilidad, orden, duplicados, ejemplo)


seccion("FIN — ya conoces variables y tipos de datos al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
