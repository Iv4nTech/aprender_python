# ============================================================
#   EJERCICIOS PRÁCTICOS: *args y **kwargs (SIN RESOLVER)
#   Casos reales, de fácil a experto. ¡Completa el código!
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1 (FÁCIL) — Calculadora de promedio
# Crea una función `promedio(*args)` que reciba cualquier
# cantidad de números y devuelva su media aritmética.
# Si no recibe números, debe devolver 0 (evita dividir entre 0).
# ------------------------------------------------------------

def promedio(*args):
    pass  # TODO

# print(promedio(10, 20, 30))  # Esperado: 20.0
# print(promedio())            # Esperado: 0


# ------------------------------------------------------------
# EJERCICIO 2 (FÁCIL) — Constructor de perfil de usuario
# Crea `crear_perfil(**kwargs)` que reciba datos de un usuario
# y los imprima en formato "clave: valor", una línea por dato.
# ------------------------------------------------------------

def crear_perfil(**kwargs):
    pass  # TODO

# crear_perfil(nombre='Ana', edad=28, ciudad='Madrid')
# Esperado:
# nombre: Ana
# edad: 28
# ciudad: Madrid


# ------------------------------------------------------------
# EJERCICIO 3 (FÁCIL-MEDIO) — Concatenar rutas
# Crea `unir_ruta(*args)` que una fragmentos de una ruta con "/".
# Ej: unir_ruta('home', 'ivan', 'docs') -> 'home/ivan/docs'
# ------------------------------------------------------------

def unir_ruta(*args):
    pass  # TODO

# print(unir_ruta('home', 'ivan', 'docs'))  # Esperado: home/ivan/docs


# ------------------------------------------------------------
# EJERCICIO 4 (MEDIO) — Función con configuración por defecto
# Crea `enviar_email(destinatario, asunto, **kwargs)`.
# Por defecto: prioridad='normal', copia=None.
# El usuario puede sobrescribir esos valores con kwargs.
# Imprime un resumen del email.
# ------------------------------------------------------------

def enviar_email(destinatario, asunto, **kwargs):
    pass  # TODO

# enviar_email('a@b.com', 'Hola', prioridad='alta')
# Esperado:
# Para: a@b.com | Asunto: Hola | Prioridad: alta | Copia: None


# ------------------------------------------------------------
# EJERCICIO 5 (MEDIO) — El máximo con clave personalizada
# Crea `maximo(*args, clave=None)` que devuelva el mayor elemento.
# Si se pasa `clave` (una función), úsala para comparar.
# Ej: maximo('hola', 'hi', 'buenas', clave=len) -> 'buenas'
# ------------------------------------------------------------

def maximo(*args, clave=None):
    pass  # TODO

# print(maximo(3, 7, 2))                          # Esperado: 7
# print(maximo('hola', 'hi', 'buenas', clave=len)) # Esperado: buenas


# ------------------------------------------------------------
# EJERCICIO 6 (MEDIO-AVANZADO) — Reenvío de argumentos (wrapper)
# Tienes esta función ya hecha:
def registrar_compra(producto, cantidad, precio):
    total = cantidad * precio
    return f'{cantidad}x {producto} = {total}€'

# Crea `compra_con_log(*args, **kwargs)` que imprima
# "LOG: llamando a registrar_compra" y luego REENVÍE todos los
# argumentos a registrar_compra usando unpacking, devolviendo su resultado.
# ------------------------------------------------------------

def compra_con_log(*args, **kwargs):
    pass  # TODO

# print(compra_con_log('pan', cantidad=2, precio=1.5))
# Esperado:
# LOG: llamando a registrar_compra
# 2x pan = 3.0€


# ------------------------------------------------------------
# EJERCICIO 7 (AVANZADO) — Fusionar diccionarios de config
# Crea `fusionar_config(*configs, **overrides)` que:
#  - Reciba varios diccionarios en *configs y los combine (los de
#    la derecha pisan a los de la izquierda).
#  - Aplique encima los **overrides.
# Devuelve el diccionario final.
# ------------------------------------------------------------

def fusionar_config(*configs, **overrides):
    pass  # TODO

# base = {'tema': 'claro', 'idioma': 'es'}
# usuario = {'tema': 'oscuro'}
# print(fusionar_config(base, usuario, fuente='Arial'))
# Esperado: {'tema': 'oscuro', 'idioma': 'es', 'fuente': 'Arial'}


# ------------------------------------------------------------
# EJERCICIO 8 (AVANZADO) — Decorador que mide y registra llamadas
# Crea un decorador `traza` que envuelva cualquier función,
# imprima los *args y **kwargs con que se llamó, ejecute la función
# y muestre el resultado. Debe funcionar con CUALQUIER firma.
# ------------------------------------------------------------

def traza(func):
    def envoltura(*args, **kwargs):
        pass  # TODO: imprime args/kwargs, llama a func, imprime y devuelve resultado
    return envoltura

# @traza
# def multiplicar(a, b):
#     return a * b
# multiplicar(3, b=4)
# Esperado:
# Llamada: multiplicar(3, b=4)
# Resultado: 12


# ------------------------------------------------------------
# EJERCICIO 9 (EXPERTO) — Validador con argumentos keyword-only
# Crea `crear_usuario(nombre, *, email, edad=18, **extra)`.
#  - `email` es OBLIGATORIO y keyword-only (después del *).
#  - `edad` por defecto 18.
#  - Lanza ValueError si la edad es menor de 0.
#  - Guarda cualquier dato extra en `extra`.
# Devuelve un diccionario con todos los datos.
# ------------------------------------------------------------

def crear_usuario(nombre, *, email, edad=18, **extra):
    pass  # TODO

# print(crear_usuario('Iván', email='i@v.com', telefono='600'))
# Esperado: {'nombre': 'Iván', 'email': 'i@v.com', 'edad': 18, 'telefono': '600'}


# ------------------------------------------------------------
# EJERCICIO 10 (EXPERTO) — Mini "pipeline" de funciones
# Crea `aplicar_pipeline(valor, *funciones, **opciones)` que:
#  - Pase `valor` por cada función de *funciones en orden
#    (la salida de una es la entrada de la siguiente).
#  - Si opciones tiene verbose=True, imprime cada paso intermedio.
# Devuelve el valor final.
# ------------------------------------------------------------

def aplicar_pipeline(valor, *funciones, **opciones):
    pass  # TODO

# resultado = aplicar_pipeline(
#     5,
#     lambda x: x + 1,
#     lambda x: x * 2,
#     verbose=True
# )
# Esperado:
# Paso 1: 6
# Paso 2: 12
# print(resultado)  # 12
