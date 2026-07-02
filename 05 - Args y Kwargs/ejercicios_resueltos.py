# ============================================================
#   EJERCICIOS PRÁCTICOS: *args y **kwargs (RESUELTOS)
#   Casos reales, de fácil a experto.
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1 (FÁCIL) — Calculadora de promedio
# Crea una función `promedio(*args)` que reciba cualquier
# cantidad de números y devuelva su media aritmética.
# Si no recibe números, debe devolver 0 (evita dividir entre 0).
# ------------------------------------------------------------

def promedio(*args):
    if args:
        return sum(args) / len(args)
    return 0

print(promedio(10, 20, 30))  # Esperado: 20.0
print(promedio())            # Esperado: 0


# ------------------------------------------------------------
# EJERCICIO 2 (FÁCIL) — Constructor de perfil de usuario
# Crea `crear_perfil(**kwargs)` que reciba datos de un usuario
# y los imprima en formato "clave: valor", una línea por dato.
# ------------------------------------------------------------

def crear_perfil(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
crear_perfil(nombre='Ana', edad=28, ciudad='Madrid')
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
    concadenar = ""
    args_original = args
    args_nueva = args_original + (None,)
    for a, s in zip(args_nueva, args_nueva[1:]):
        if s != None:
            concadenar += a + '/'
        else:
            concadenar += a
    return concadenar
        

print(unir_ruta('home', 'ivan', 'docs', 'hola'))  # Esperado: home/ivan/docs


# ------------------------------------------------------------
# EJERCICIO 4 (MEDIO) — Función con configuración por defecto
# Crea `enviar_email(destinatario, asunto, **kwargs)`.
# Por defecto: prioridad='normal', copia=None.
# El usuario puede sobrescribir esos valores con kwargs.
# Imprime un resumen del email.
# ------------------------------------------------------------

def enviar_email(destinatario, asunto, **kwargs):
    prioridad = kwargs.get('prioridad', 'normal')
    copia = kwargs.get('copia', None)
    print(f'Para: {destinatario} | Asunto: {asunto} | Prioridad: {prioridad} | Copia: {copia}')

enviar_email('a@b.com', 'Hola', prioridad='alta')
# Esperado:
# Para: a@b.com | Asunto: Hola | Prioridad: alta | Copia: None


# ------------------------------------------------------------
# EJERCICIO 5 (MEDIO) — El máximo con clave personalizada
# Crea `maximo(*args, clave=None)` que devuelva el mayor elemento.
# Si se pasa `clave` (una función), úsala para comparar.
# Ej: maximo('hola', 'hi', 'buenas', clave=len) -> 'buenas'
# ------------------------------------------------------------

def maximo(*args, clave=None):
    if not args:
        return None
    if not clave:
        return max(args)
    return max(args, key=clave)

print(maximo(3, 7, 2))                          # Esperado: 7
print(maximo('hola', 'hi', 'buenas', clave=len)) # Esperado: buenas


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
    resultado_compra = registrar_compra(*args, **kwargs)
    print('LOG: llamando a registrar_compra')
    return resultado_compra

print(compra_con_log('pan', cantidad=2, precio=1.5))
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
    resultado = {}
    for c in configs:
        resultado.update(c)
    resultado.update(overrides)
    return resultado

base = {'tema': 'claro', 'idioma': 'es'}
usuario = {'tema': 'oscuro'}
print(fusionar_config(base, usuario, fuente='Arial'))
# Esperado: {'tema': 'oscuro', 'idioma': 'es', 'fuente': 'Arial'}


# ------------------------------------------------------------
# EJERCICIO 8 (AVANZADO) — Decorador que mide y registra llamadas
# Crea un decorador `traza` que envuelva cualquier función,
# imprima los *args y **kwargs con que se llamó, ejecute la función
# y muestre el resultado. Debe funcionar con CUALQUIER firma.
# ------------------------------------------------------------

def traza(func):
    def envoltura(*args, **kwargs):
        partes = [repr(a) for a in args]
        partes += [f'{k}={v}' for k, v in kwargs.items()]
        firma = ', '.join(partes)
        print(f'Llamada: {func.__name__}({firma})')
        resultado = func(*args, **kwargs)
        print(f'Resultado: {resultado}')
        return resultado
    return envoltura

@traza
def multiplicar(a, b):
    return a * b
multiplicar(3, b=4)
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
    if edad < 0:
        raise ValueError('La edad no puede ser negativa')
    usuario = {'nombre': nombre, 'email': email, 'edad': edad}
    usuario.update(extra)   # añadimos los datos extra
    return usuario


print(crear_usuario('Iván', email='i@v.com', telefono='600'))
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
    for i, fn in enumerate(funciones, 1):
        valor = fn(valor)
        if opciones.get('verbose', False):
            print(f'Paso {i}: {valor}')
    return valor

resultado = aplicar_pipeline(
    5,
    lambda x: x + 1,
    lambda x: x * 2,
    verbose=True
)
# Esperado:
# Paso 1: 6
# Paso 2: 12
print(resultado)  # 12