"""
INTRODUCCIÓN A LOS SETS EN PYTHON
De cero a experto.

Estructura del fichero (sigue el guion del video):
  1.  ¿Qué es un set y cómo se crea?
  2.  El superpoder nº1: no hay duplicados
  3.  El superpoder nº2: pertenencia ultra rápida (set vs lista)
  4.  Mutar un set: add, update, remove, discard, pop, clear
  5.  Operaciones de conjuntos: unión, intersección, diferencia...
  6.  Comparar conjuntos: subset, superset, disjoint
  7.  Set comprehensions
  8.  frozenset (el set inmutable)
  9.  Qué se puede meter en un set (hashables) y qué no
  10. Casos reales (backend / web / data)
"""

# =============================================================================
# 1. ¿QUÉ ES UN SET Y CÓMO SE CREA?
# =============================================================================
# Un set es una colección NO ordenada, SIN duplicados y MUTABLE.

vacio = set()              # ¡OJO! {} es un dict vacío, no un set
numeros = {1, 2, 3, 4}
mixto = {1, "hola", 3.14, True}
print(vacio)
print(numeros)
print(mixto)

# Desde otra colección:
lista = [1, 2, 2, 3, 3, 3]
desde_lista = set(lista)   # {1, 2, 3}
print(desde_lista)

desde_texto = set("banana")  # {'b', 'a', 'n'}
print(desde_texto)


# =============================================================================
# 2. EL SUPERPODER Nº1: NO HAY DUPLICADOS
# =============================================================================
emails = [
    "ana@gmail.com",
    "luis@gmail.com",
    "ana@gmail.com",
    "marta@gmail.com",
    "luis@gmail.com",
]

unicos = set(emails)
print(unicos)
print(len(emails), "->", len(unicos))

# El truco de 1 línea para eliminar duplicados de una lista:
sin_duplicados = list(set(emails))
print(sin_duplicados)


# =============================================================================
# 3. EL SUPERPODER Nº2: BÚSQUEDA ULTRA RÁPIDA (set vs lista)
# =============================================================================
# En una LISTA, "x in lista" recorre elemento por elemento  -> O(n)
# En un SET,   "x in set"   salta directo al elemento        -> O(1)

usuarios_baneados_lista = ["user1", "user2", "user3"]
usuarios_baneados_set = {"user1", "user2", "user3"}

print("user2" in usuarios_baneados_lista)
print("user2" in usuarios_baneados_set)

# Demostración de velocidad:
import time

grande_lista = list(range(1_000_000))
grande_set = set(grande_lista)
objetivo = 999_999

t0 = time.perf_counter()
objetivo in grande_lista
t_lista = time.perf_counter() - t0

t0 = time.perf_counter()
objetivo in grande_set
t_set = time.perf_counter() - t0

print(f"Lista: {t_lista:.6f}s")
print(f"Set:   {t_set:.6f}s")
print(f"El set es ~{t_lista / t_set:.0f} veces más rápido")


# =============================================================================
# 4. MUTAR UN SET
# =============================================================================
permisos = {"leer"}

permisos.add("escribir")              # añade un elemento
permisos.update({"borrar", "admin"})  # añade varios (acepta cualquier iterable)
print(permisos)
permisos.update(["exportar"], ("importar",))
print(permisos)

permisos.remove("admin")    # quita; lanza KeyError si no existe
permisos.discard("noexiste")  # quita; NO lanza error si no existe (más seguro)

algo = permisos.pop()       # quita y devuelve un elemento "cualquiera"
print("Saqué:", algo)

copia = permisos.copy()     # copia superficial
print(copia)
copia.add('hola mundo!')
print(copia)
print(permisos)
permisos.clear()          # lo vacía entero
print(permisos)


# =============================================================================
# 5. OPERACIONES DE CONJUNTOS (el corazón de los sets)
# =============================================================================
frontend = {"ana", "luis", "marta"}
backend = {"luis", "marta", "pedro", "sofia"}

# UNIÓN -> todos, sin repetir
print(frontend | backend)
print(frontend.union(backend))

# INTERSECCIÓN -> los que están en AMBOS
print(frontend & backend)
print(frontend.intersection(backend))

# DIFERENCIA -> en frontend pero NO en backend
print(frontend - backend)
print(frontend.difference(backend))
print(backend - frontend)

# DIFERENCIA SIMÉTRICA -> en uno o en otro, pero NO en ambos
print(frontend ^ backend)
print(frontend.symmetric_difference(backend))

# --- Versiones "in-place" ---
# OJO a la diferencia:
#   frontend | backend   -> crea y devuelve un set NUEVO (no toca frontend)
#   frontend |= backend  -> MODIFICA frontend directamente (no crea uno nuevo)
# Es lo mismo que  x = x + 1  vs  x += 1, pero con conjuntos.

# |=  union in-place  (equivale a .update)
equipo = {"ana", "luis"}
equipo |= {"marta", "pedro"}     # equipo ahora: {"ana","luis","marta","pedro"}
print(equipo)
equipo.update({"sofia"})         # misma operación con método
print(equipo)

# &=  intersección in-place  (equivale a .intersection_update)
activos = {"ana", "luis", "marta", "pedro"}
con_sesion = {"luis", "marta", "hugo"}
activos &= con_sesion            # me quedo SOLO con los que están en ambos
print(activos)                   # {"luis", "marta"}

# -=  diferencia in-place  (equivale a .difference_update)
permisos_rol = {"leer", "escribir", "borrar"}
permisos_revocados = {"borrar"}
permisos_rol -= permisos_revocados   # quito los revocados del set original
print(permisos_rol)              # {"leer", "escribir"}

# ^=  diferencia simétrica in-place  (equivale a .symmetric_difference_update)
seleccion = {"a", "b", "c"}
toggle = {"c", "d"}
seleccion ^= toggle              # quita los comunes, añade los nuevos (toggle)
print(seleccion)                 # {"a", "b", "d"}

# ¿Por qué usar in-place? Es más eficiente: no crea un set nuevo en memoria.
# Útil cuando vas acumulando en un set dentro de un bucle.
todos_los_tags = set()
for articulo in [{"py", "web"}, {"py", "db"}, {"api"}]:
    todos_los_tags |= articulo   # voy acumulando sin crear sets intermedios
print(todos_los_tags)


# =============================================================================
# 6. COMPARAR CONJUNTOS
# =============================================================================
permisos_usuario = {"leer", "escribir"}
permisos_requeridos = {"leer"}
permisos_admin = {"leer", "escribir", "borrar"}

# ¿requeridos está contenido en usuario?  (subconjunto)
print(permisos_requeridos <= permisos_usuario)   # True
print(permisos_requeridos.issubset(permisos_usuario))

# ¿usuario contiene a requeridos?  (superconjunto)
print(permisos_usuario >= permisos_requeridos)   # True
print(permisos_usuario.issuperset(permisos_requeridos))

# < y > son subconjunto/superconjunto ESTRICTO (no iguales)
print(permisos_usuario < permisos_admin)         # True

# ¿no comparten NADA?
print({"a", "b"}.isdisjoint({"c", "d"}))         # True


# =============================================================================
# 7. SET COMPREHENSIONS
# =============================================================================
# Como las list comprehensions pero con {} -> resultado sin duplicados.
cuadrados = {x * x for x in range(-3, 4)}      # {0, 1, 4, 9}
dominios = {e.split("@")[1] for e in emails}   # dominios únicos
print(cuadrados)
print(dominios)


# =============================================================================
# 8. frozenset: EL SET INMUTABLE
# =============================================================================
# Igual que un set pero NO se puede modificar -> es hashable.
# Esto permite usarlo como clave de dict o como elemento de otro set.
roles = frozenset({"leer", "escribir"})
print(roles)
# roles.add("x")  # AttributeError

# Un set NO puede contener sets (no son hashables), pero SÍ frozensets:
combos_permisos = {
    frozenset({"leer"}),
    frozenset({"leer", "escribir"}),
}
print(combos_permisos)


# =============================================================================
# 9. ¿QUÉ SE PUEDE METER EN UN SET? (HASHABLES)
# =============================================================================
# Solo objetos INMUTABLES/hashables: int, str, float, bool, tuple, frozenset.
ok = {1, "a", (1, 2), 3.5}
print(ok)

# Esto FALLA porque las listas y los dicts son mutables (no hashables):
# malo = {[1, 2], {3, 4}}   # TypeError: unhashable type: 'list'

# Truco: para "meter" una lista en un set, conviértela en tupla primero.
lista = [10, 20]
coordenadas_visitadas = set()
coordenadas_visitadas.add(tuple(lista))
coordenadas_visitadas.add(tuple(lista))   # duplicado ignorado
print(coordenadas_visitadas)


# =============================================================================
# 10. CASOS REALES 
# =============================================================================

# --- 10.1 Backend: ¿el usuario tiene los permisos requeridos? ---
def puede_acceder(permisos_usuario: set, permisos_requeridos: set) -> bool:
    return permisos_requeridos <= permisos_usuario

print(puede_acceder({"leer", "escribir"}, {"leer"}))            # True
print(puede_acceder({"leer"}, {"leer", "escribir", "borrar"}))  # False

# Qué permisos le FALTAN al usuario:
faltan = {"leer", "escribir", "borrar"} - {"leer"}
print("Le faltan:", faltan)


# --- 10.2 Redes sociales: amigos en común y recomendaciones ---
amigos_ana = {"luis", "marta", "pedro"}
amigos_luis = {"marta", "pedro", "sofia", "ana"}

en_comun = amigos_ana & amigos_luis
recomendar_a_ana = (amigos_luis - amigos_ana) - {"ana"}
print("Amigos en común:", en_comun)
print("Recomendar a Ana:", recomendar_a_ana)


# --- 10.3 Seguridad / logs: IPs únicas que atacaron hoy ---
peticiones = ["8.8.8.8", "1.1.1.1", "8.8.8.8", "9.9.9.9", "1.1.1.1"]
ips_unicas = set(peticiones)
lista_negra = {"9.9.9.9", "6.6.6.6"}
print("IPs sospechosas detectadas:", ips_unicas & lista_negra)


# --- 10.4 Data cleaning: comparar dos datasets ---
clientes_enero = {"c1", "c2", "c3", "c4"}
clientes_febrero = {"c3", "c4", "c5", "c6"}

nuevos = clientes_febrero - clientes_enero      # captados en febrero
perdidos = clientes_enero - clientes_febrero    # churn
fieles = clientes_enero & clientes_febrero      # se quedaron
print("Nuevos:", nuevos, "| Perdidos:", perdidos, "| Fieles:", fieles)


# --- 10.5 Validación de tags sin duplicar ---
def normalizar_tags(tags: list[str]) -> set[str]:
    return {t.strip().lower() for t in tags if t.strip()}

print(normalizar_tags([" Python", "python ", "SETS", "  ", "Sets"]))
