"""
EJERCICIOS DE SETS - de FÁCIL a EXPERTO
Casos reales (backend / web / data).

Resuelve cada función. Las soluciones están en ejercicios_resueltos.py.
Debajo de cada ejercicio tienes ejemplos de lo que debería devolver.

Consejo: intenta resolver TODO sin mirar las soluciones. Cuando te atasques,
piensa qué operación de conjuntos modela el problema (unión, intersección,
diferencia, pertenencia...).
"""

# =============================================================================
# NIVEL 1 - FÁCIL
# =============================================================================

# --- Ej 1.1: Eliminar duplicados conservando una colección de únicos ---
# Dada una lista de correos (con repetidos), devuelve cuántos correos
# ÚNICOS hay.
def contar_correos_unicos(correos: list[str]) -> int:
    pass
# contar_correos_unicos(["a@x.com", "b@x.com", "a@x.com"]) -> 2


# --- Ej 1.2: ¿Está baneado? ---
# Dada una colección de usuarios baneados y un nombre, indica si está baneado.
# Hazlo de forma EFICIENTE (piensa por qué un set es mejor que una lista).
def esta_baneado(baneados, usuario: str) -> bool:
    pass
# esta_baneado(["u1", "u2"], "u2") -> True


# --- Ej 1.3: Caracteres distintos ---
# Devuelve cuántos caracteres DISTINTOS tiene un texto (ignora mayúsculas).
def caracteres_distintos(texto: str) -> int:
    pass
# caracteres_distintos("Banana") -> 3   (b, a, n)


# =============================================================================
# NIVEL 2 - INTERMEDIO
# =============================================================================

# --- Ej 2.1: Amigos en común ---
# Devuelve el conjunto de amigos que comparten dos usuarios.
def amigos_en_comun(amigos_a: set, amigos_b: set) -> set:
    pass
# amigos_en_comun({"x", "y"}, {"y", "z"}) -> {"y"}


# --- Ej 2.2: Permisos que faltan ---
# Dado lo que tiene un usuario y lo que requiere una acción, devuelve el
# conjunto de permisos que le FALTAN (vacío si los tiene todos).
def permisos_faltantes(usuario: set, requeridos: set) -> set:
    pass
# permisos_faltantes({"leer"}, {"leer", "escribir"}) -> {"escribir"}


# --- Ej 2.3: Análisis de churn ---
# Dados los clientes de dos meses, devuelve una tupla:
# (nuevos, perdidos, fieles).
def analizar_churn(mes_anterior: set, mes_actual: set) -> tuple[set, set, set]:
    pass
# analizar_churn({"a","b"}, {"b","c"}) -> ({"c"}, {"a"}, {"b"})


# --- Ej 2.4: Etiquetas comunes a TODOS los artículos ---
# Dada una lista de sets de tags (uno por artículo), devuelve los tags que
# aparecen en TODOS los artículos.
def tags_comunes(articulos: list[set]) -> set:
    pass
# tags_comunes([{"py","web"}, {"py","db"}, {"py","api"}]) -> {"py"}


# =============================================================================
# NIVEL 3 - AVANZADO
# =============================================================================

# --- Ej 3.1: Recomendación de amigos ---
# Recomienda a un usuario los amigos de sus amigos que él aún NO tiene
# (y excluyéndose a sí mismo).
#   - usuario: nombre del usuario
#   - grafo: dict {nombre: set(amigos)}
def recomendar_amigos(usuario: str, grafo: dict[str, set]) -> set:
    pass
# grafo = {"ana": {"luis"}, "luis": {"ana", "pedro"}, "pedro": {"luis"}}
# recomendar_amigos("ana", grafo) -> {"pedro"}


# --- Ej 3.2: Detección de permisos duplicados en roles ---
# Dado un dict {rol: set(permisos)}, devuelve el conjunto de permisos que
# están en MÁS DE UN rol (permisos "compartidos").
def permisos_compartidos(roles: dict[str, set]) -> set:
    pass
# permisos_compartidos({"admin": {"leer","borrar"}, "editor": {"leer","escribir"}})
#   -> {"leer"}


# --- Ej 3.3: Combinaciones únicas de permisos (frozenset) ---
# Dada una lista de usuarios, cada uno con su set de permisos, devuelve
# cuántas COMBINACIONES distintas de permisos existen.
# Pista: necesitas frozenset.
def combinaciones_distintas(usuarios_permisos: list[set]) -> int:
    pass
# combinaciones_distintas([{"leer"}, {"leer"}, {"leer","escribir"}]) -> 2


# =============================================================================
# NIVEL 4 - EXPERTO
# =============================================================================

# --- Ej 4.1: Deduplicar registros por clave manteniendo el orden ---
# Tienes una lista de dicts (registros) y una clave. Devuelve la lista sin
# registros cuya 'clave' ya haya aparecido antes, MANTENIENDO el orden original.
# (Caso real: limpiar logs/eventos quedándote con la 1ª aparición de cada id.)
def deduplicar_por_clave(registros: list[dict], clave: str) -> list[dict]:
    pass
# deduplicar_por_clave(
#   [{"id":1,"v":"a"}, {"id":2,"v":"b"}, {"id":1,"v":"c"}], "id"
# ) -> [{"id":1,"v":"a"}, {"id":2,"v":"b"}]


# --- Ej 4.2: Control de acceso jerárquico ---
# roles_usuario: set de roles del usuario.
# jerarquia: dict {rol: set(permisos directos)}.
# herencia: dict {rol: set(roles de los que hereda)}.
# Devuelve TODOS los permisos efectivos del usuario, resolviendo la herencia
# (la herencia puede tener varios niveles; cuidado con ciclos).
def permisos_efectivos(roles_usuario: set, jerarquia: dict, herencia: dict) -> set:
    pass
# jerarquia = {"viewer": {"leer"}, "editor": {"escribir"}, "admin": {"borrar"}}
# herencia  = {"editor": {"viewer"}, "admin": {"editor"}}
# permisos_efectivos({"admin"}, jerarquia, herencia)
#   -> {"leer", "escribir", "borrar"}


# --- Ej 4.3: Detección de solapamiento de horarios ---
# Cada reserva es (inicio, fin) en horas enteras [inicio, fin).
# Devuelve True si ALGUNA reserva se solapa con otra.
# Pista: representa cada reserva como un set de "slots" horarios y usa
# intersección / isdisjoint.
def hay_solapamiento(reservas: list[tuple[int, int]]) -> bool:
    pass
# hay_solapamiento([(9, 11), (11, 13)]) -> False
# hay_solapamiento([(9, 12), (11, 13)]) -> True


# --- Ej 4.4: Motor de recomendación por similitud (Jaccard) ---
# Dado un usuario objetivo y un dict {usuario: set(intereses)}, devuelve el
# usuario MÁS parecido según el índice de Jaccard:
#       J(A, B) = |A ∩ B| / |A ∪ B|
# (excluyendo al propio usuario objetivo). Si nadie comparte nada, devuelve None.
def usuario_mas_similar(objetivo: str, intereses: dict[str, set]) -> str | None:
    pass
# intereses = {
#   "ana":  {"python", "ml", "web"},
#   "luis": {"python", "ml"},
#   "eva":  {"cocina"},
# }
# usuario_mas_similar("ana", intereses) -> "luis"


if __name__ == "__main__":
    # Al ejecutar este fichero verás el resultado de tus soluciones.
    # Compáralo con el valor esperado del comentario de cada línea.

    # --- Nivel 1 ---
    print(contar_correos_unicos(["a@x.com", "b@x.com", "a@x.com"]))   # 2
    print(esta_baneado(["u1", "u2"], "u2"))                           # True
    print(caracteres_distintos("Banana"))                            # 3

    # --- Nivel 2 ---
    print(amigos_en_comun({"x", "y"}, {"y", "z"}))                   # {'y'}
    print(permisos_faltantes({"leer"}, {"leer", "escribir"}))       # {'escribir'}
    print(analizar_churn({"a", "b"}, {"b", "c"}))                   # ({'c'}, {'a'}, {'b'})
    print(tags_comunes([{"py", "web"}, {"py", "db"}, {"py", "api"}]))  # {'py'}

    # --- Nivel 3 ---
    grafo = {"ana": {"luis"}, "luis": {"ana", "pedro"}, "pedro": {"luis"}}
    print(recomendar_amigos("ana", grafo))                          # {'pedro'}
    print(permisos_compartidos(
        {"admin": {"leer", "borrar"}, "editor": {"leer", "escribir"}}))  # {'leer'}
    print(combinaciones_distintas([{"leer"}, {"leer"}, {"leer", "escribir"}]))  # 2

    # --- Nivel 4 ---
    print(deduplicar_por_clave(
        [{"id": 1, "v": "a"}, {"id": 2, "v": "b"}, {"id": 1, "v": "c"}], "id"))
    # [{'id': 1, 'v': 'a'}, {'id': 2, 'v': 'b'}]
    jerarquia = {"viewer": {"leer"}, "editor": {"escribir"}, "admin": {"borrar"}}
    herencia = {"editor": {"viewer"}, "admin": {"editor"}}
    print(permisos_efectivos({"admin"}, jerarquia, herencia))
    # {'leer', 'escribir', 'borrar'}
    print(hay_solapamiento([(9, 11), (11, 13)]))                    # False
    print(hay_solapamiento([(9, 12), (11, 13)]))                    # True
    intereses = {
        "ana": {"python", "ml", "web"},
        "luis": {"python", "ml"},
        "eva": {"cocina"},
    }
    print(usuario_mas_similar("ana", intereses))                    # luis
