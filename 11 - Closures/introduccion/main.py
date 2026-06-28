
# ════════════════════════════════════════════════════════════════
#   CLOSURES EN PYTHON  ·  guía didáctica
# ════════════════════════════════════════════════════════════════
#
#   LA IDEA EN UNA FRASE
#   --------------------
#   Un closure es una función que se lleva una "mochila" con las
#   variables del sitio donde nació, y las sigue recordando aunque
#   ese sitio ya haya desaparecido.
#
#   LA ANALOGÍA DE LA MOCHILA 🎒
#   ----------------------------
#   Imagina que entras a una sala (una función), metes algo en una
#   mochila y, al salir, te llevas la mochila contigo. La sala se
#   cierra, las luces se apagan... pero tú sigues teniendo lo que
#   guardaste dentro. Eso es exactamente un closure: la función
#   "sale" con su mochila de variables.
#
#   FUENTES OFICIALES usadas en esta guía:
#     · Glosario:            https://docs.python.org/es/3/glossary.html
#     · Ámbitos y nonlocal:  https://docs.python.org/es/3/tutorial/classes.html
#     · Modelo de datos:     https://docs.python.org/es/3/reference/datamodel.html
#     · FAQ de programación:  https://docs.python.org/3/faq/programming.html
# ════════════════════════════════════════════════════════════════

SEP = '─' * 60

print()
print('═' * 60)
print('       CLOSURES EN PYTHON')
print('═' * 60)


# ── 1. Primero: ¿dónde "viven" las variables? ────────────────────
print('\n  1. Cada variable vive en un sitio (namespace)\n')

mensaje = 'soy de fuera'

def funcion():
    mensaje = 'soy de dentro'     # variable DISTINTA, vive en la función
    print(f'  → dentro: {mensaje}')

funcion()
print(f'  → fuera:  {mensaje}      (no se ha tocado)')

print(f'\n{SEP}')


# ── 2. ¿Cómo busca Python un nombre? La regla LEGB ───────────────
print('\n  2. La regla LEGB (el orden de búsqueda)\n')

# Fuente (tutorial de clases): cuando Python necesita una variable la
# busca en este orden, de dentro hacia fuera:
#
#   L  Local      → la función actual
#   E  Enclosing  → la función que la envuelve   ← ¡aquí viven los closures!
#   G  Global     → el archivo / módulo
#   B  Built-in   → lo que trae Python (print, len, range...)

x = 'soy Global'

def externa():
    x = 'soy Enclosing'
    def interna():
        # interna no tiene 'x' propia → sube un nivel y encuentra la de externa
        print(f'  → interna usa: {x!r}')
    interna()

externa()

print(f'\n{SEP}')


# ── 3. El nacimiento de un closure ───────────────────────────────
print('\n  3. Una función que devuelve otra función\n')

# El truco: una función interna usa una variable de la externa y la
# externa la DEVUELVE (sin llamarla). Esa variable es la "mochila".

def fabrica_de_saludos(idioma):
    def saludar(nombre):
        return f'{idioma}, {nombre}!'   # 'idioma' viene de la mochila
    return saludar                       # devolvemos la función, no la llamamos

en_espanol = fabrica_de_saludos('Hola')
en_ingles  = fabrica_de_saludos('Hello')

print(f'  → {en_espanol("Ivan")}')
print(f'  → {en_ingles("Ivan")}')
print('    (cada función recuerda SU idioma, aunque la fábrica ya terminó)')

print(f'\n{SEP}')


# ── 4. Abrir la mochila y mirar dentro ───────────────────────────
print('\n  4. Mirando el closure por dentro\n')

# Python guarda la mochila en atributos reales.
#   func.__code__.co_freevars  → nombres que recuerda
#   func.__closure__           → tupla de "celdas" (la mochila)
#   celda.cell_contents        → el valor dentro de cada celda

print(f'  → recuerda:    {en_espanol.__code__.co_freevars}')
print(f'  → guardó esto: {en_espanol.__closure__[0].cell_contents!r}')

print(f'\n{SEP}')


# ── 5. Leer está permitido, ESCRIBIR necesita nonlocal ───────────
print('\n  5. nonlocal: poder MODIFICAR la mochila\n')

# Si no se declara nonlocal, esas variables serán
# de solo lectura; un intento de escribir creará una NUEVA variable
# local. Por eso, para un contador con memoria, necesitas 'nonlocal'.

def crear_contador():
    cuenta = 0
    def incrementar():
        nonlocal cuenta          # "quiero ESCRIBIR en la de fuera"
        cuenta += 1
        return cuenta
    return incrementar

clic = crear_contador()
print(f'  → {clic()}, {clic()}, {clic()}   (mantiene su estado entre llamadas)')

print(f'\n{SEP}')


# ── 6. global vs nonlocal (no confundir) ─────────────────────────
print('\n  6. nonlocal vs global\n')

#   global   → reasigna una variable del MÓDULO (el archivo entero)
#   nonlocal → reasigna una variable de la FUNCIÓN que envuelve

print('  → nonlocal apunta UN nivel hacia fuera (la función contenedora)')
print('  → global salta hasta el nivel del archivo')

print(f'\n{SEP}')


# ── 7. La trampa más famosa: el "late binding" ───────────────────
print('\n  7. El error clásico en bucles (late binding)\n')

# La mochila guarda la VARIABLE, no una foto del valor. Si creas
# varias funciones en un bucle, todas comparten la misma variable
# y acaban viendo su ÚLTIMO valor.

mal = [lambda: i for i in range(3)]
print(f'  ✗ Mal:  {[f() for f in mal]}   (queríamos 0, 1, 2)')

# SOLUCIÓN: capturar el valor con un argumento
# por defecto, que SÍ se congela en el momento de crear la función.
bien = [lambda i=i: i for i in range(3)]
print(f'  ✓ Bien: {[f() for f in bien]}')

# ── Lo mismo SIN lambdas, con def normal (para verlo claro) ──────
# Una lambda es solo una función sin nombre. Aquí está traducido:

print('\n  Lo mismo desglosado con funciones normales:\n')

# MAL: cada función hace 'return i' mirando la VARIABLE de fuera.
mal_def = []
for i in range(3):
    def funcion():        # no recibe nada
        return i          # mira la i de fuera (se lee al LLAMAR)
    mal_def.append(funcion)
# Al acabar el bucle, i vale 2 → las tres devuelven 2
print(f'  ✗ Mal:  {[f() for f in mal_def]}   (i de fuera, vale 2 al final)')

# BIEN: cada función guarda SU propio i con un valor por defecto.
bien_def = []
for i in range(3):
    def funcion(i=i):     # i=i congela el valor de AHORA mismo
        return i          # devuelve su propio i (su "foto")
    bien_def.append(funcion)
print(f'  ✓ Bien: {[f() for f in bien_def]}   (cada función guarda su valor)')

# AÚN MÁS CLARO: una función fábrica que recibe el número.
def crear_funcion(numero):    # recibe el número
    def funcion():
        return numero         # cada función tiene SU propio 'numero'
    return funcion

fabrica = [crear_funcion(i) for i in range(3)]
print(f'  ✓ Fábrica: {[f() for f in fabrica]}   (cada llamada crea su caja)')

print(f'\n{SEP}')


# ── 8. ¿Para qué sirve esto en la vida real? ─────────────────────
print('\n  8. Closures = la base de los decoradores\n')

# Un decorador es, literalmente, un closure que envuelve otra función.
# Lo que aprendas aquí es la base directa del tema de Decoradores.

def registrar(func):
    def envoltorio(*args, **kwargs):
        print(f'    → ejecutando {func.__name__}()')   # 'func' es la mochila
        return func(*args, **kwargs)
    return envoltorio

@registrar
def comprar(producto):
    return f'Comprado: {producto}'

print(f'  → {comprar("teclado")}')

# ── ¿Qué hacen *args y **kwargs en el envoltorio? ────────────────
# Es lo que más confunde. Hay DOS momentos distintos:
#
#   def envoltorio(*args, **kwargs):     ① RECOGER  (empaquetar)
#       return func(*args, **kwargs)     ② REENVIAR (desempaquetar)
#
# ① En la DEFINICIÓN: el envoltorio dice "acepto lo que sea".
#    *args  agrupa los argumentos sueltos en una tupla.
#    **kwargs agrupa los argumentos con nombre en un diccionario.
# ② En la LLAMADA a func: los abre y se los pasa TAL CUAL a la
#    función original. Así el decorador sirve para CUALQUIER función.

# Recordatorio: @registrar es lo mismo que  comprar = registrar(comprar)
# Por eso al llamar comprar(...) en realidad llamas al envoltorio(...).

@registrar
def comprar_detallado(producto, cantidad, urgente=False):
    return f'{cantidad}x {producto} (urgente={urgente})'

# Al llamar:   comprar_detallado("teclado", 2, urgente=True)
#   envoltorio RECOGE →  args = ("teclado", 2)   kwargs = {"urgente": True}
#   func(*args, **kwargs) →  comprar_detallado("teclado", 2, urgente=True)
print(f'  → {comprar_detallado("teclado", 2, urgente=True)}')

print(f'\n{SEP}\n')
print('  RESUMEN')
print('  · Closure = función interna + su "mochila" de variables.')
print('  · Sirve para recordar configuración y mantener estado.')
print('  · Para modificar la mochila: nonlocal.')
print('  · Cuidado con crear closures dentro de bucles.')
print('═' * 60)
print()
