"""
EJERCICIOS DE SETS - SOLUCIONES
Soluciones (resueltas por el usuario y verificadas con el bloque de tests
del final). Cada una incluye una breve nota del PORQUÉ se resuelve así.
"""

# =============================================================================
# NIVEL 1 - FÁCIL
# =============================================================================

def contar_correos_unicos(correos: list[str]) -> int:
    # set() elimina duplicados; len() cuenta los únicos.
    return len(set(correos))


def esta_baneado(baneados, usuario: str) -> bool:
    # 'in' busca el usuario en la colección.
    # Nota: si 'baneados' ya fuera un set, esta comprobación sería O(1);
    # con lista es O(n). Para muchas llamadas, conviene recibir un set.
    return usuario in baneados


def caracteres_distintos(texto: str) -> int:
    # Pasamos a minúsculas y metemos en un set: cuenta caracteres únicos.
    return len(set(texto.lower()))


# =============================================================================
# NIVEL 2 - INTERMEDIO
# =============================================================================

def amigos_en_comun(amigos_a: set, amigos_b: set) -> set:
    # Intersección: lo que está en ambos.
    return amigos_a & amigos_b


def permisos_faltantes(usuario: set, requeridos: set) -> set:
    # Diferencia: lo requerido que el usuario NO tiene.
    return requeridos - usuario


def analizar_churn(mes_anterior: set, mes_actual: set) -> tuple[set, set, set]:
    nuevos = mes_actual - mes_anterior      # están ahora pero no antes
    perdidos = mes_anterior - mes_actual    # estaban antes pero no ahora
    fieles = mes_actual & mes_anterior      # están en ambos
    return tuple([nuevos, perdidos, fieles])


def tags_comunes(articulos: list[set]) -> set:
    if not articulos:          # lista vacía -> no hay tags comunes
        return set()
    # Intersección acumulada de todos los sets.
    comunes = articulos[0]
    for a in articulos[1:]:
        comunes &= a
    return comunes


# =============================================================================
# NIVEL 3 - AVANZADO
# =============================================================================

def recomendar_amigos(usuario: str, grafo: dict[str, set]) -> set:
    amigos_usuario = grafo.get(usuario, set())
    amigos_del_amigo = set()
    for amigo in amigos_usuario:
        amigos_del_amigo |= grafo.get(amigo, set())   # amigos de mis amigos
    # Quito a los que ya son mis amigos y a mí mismo.
    return amigos_del_amigo - amigos_usuario - {usuario}


def permisos_compartidos(roles: dict[str, set]) -> set:
    vistos_una_vez = set()
    repe = set()
    for p in roles.values():
        repe |= p & vistos_una_vez
        vistos_una_vez |= p
    return repe


def combinaciones_distintas(usuarios_permisos: list[set]) -> int:
    # Un set no puede contener sets, pero SÍ frozensets (son hashables).
    # Así deduplicamos grupos enteros de permisos.
    return len({frozenset(p) for p in usuarios_permisos})


# =============================================================================
# NIVEL 4 - EXPERTO
# =============================================================================

def deduplicar_por_clave(registros: list[dict], clave: str) -> list[dict]:
    vistos = set()             # set = control rápido de claves ya vistas (O(1))
    resultado = []             # lista = resultado en orden original
    for reg in registros:
        valor = reg[clave]
        if valor not in vistos:
            vistos.add(valor)
            resultado.append(reg)
    return resultado


def permisos_efectivos(roles_usuario: set, jerarquia: dict, herencia: dict) -> set:
    permisos = set()
    visitados = set()                  # evita ciclos infinitos
    por_procesar = list(roles_usuario)
    while por_procesar:
        rol = por_procesar.pop()
        if rol in visitados:
            continue
        visitados.add(rol)
        permisos |= jerarquia.get(rol, set())          # permisos directos
        por_procesar.extend(herencia.get(rol, set()))  # roles heredados
    return permisos


def hay_solapamiento(reservas: list[tuple[int, int]]) -> bool:
    ocupadas = set()
    for i, f in reservas:
        reserva_set = set(range(i, f))           # franjas: (9,12) -> {9,10,11}
        if not reserva_set.isdisjoint(ocupadas):  # comparte alguna -> solapa
            return True
        ocupadas |= reserva_set
    return False


def usuario_mas_similar(objetivo: str, intereses: dict[str, set]) -> str | None:
    mis_intereses = intereses[objetivo]
    mejor_usuario = None
    mejor_score = 0.0
    for usuario, otros in intereses.items():
        if usuario == objetivo:
            continue
        union = mis_intereses | otros
        if not union:
            continue
        jaccard = len(mis_intereses & otros) / len(union)
        if jaccard > mejor_score:
            mejor_score = jaccard
            mejor_usuario = usuario
    return mejor_usuario


# =============================================================================
# EJECUCIÓN DE EJEMPLOS
# =============================================================================
if __name__ == "__main__":
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