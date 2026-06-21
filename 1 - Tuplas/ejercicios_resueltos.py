"""
================================================================================
 EJERCICIOS DE TUPLAS — SOLUCIONES COMENTADAS
================================================================================

Mismas tareas que 'ejercicios.py', resueltas.
Ejecuta para ver el resultado de cada ejercicio y verificar que pasan los tests:

    python3 ejercicios_resueltos.py
================================================================================
"""

from collections import namedtuple


# ----------------------------------------------------------------------------
# EJERCICIO 1  ⭐  — Coordenada GPS
# Contexto: una API de mapas te pide siempre devolver la posición como una
# tupla inmutable (lat, lon) para que nadie la modifique por accidente.
# Tarea: crea y devuelve la tupla (lat, lon).
# ----------------------------------------------------------------------------
def crear_coordenada(lat: float, lon: float) -> tuple:
    return lat, lon


# ----------------------------------------------------------------------------
# EJERCICIO 2  ⭐  — Swap de configuración
# Contexto: en un sistema de failover necesitas intercambiar el servidor
# primario y el secundario sin variable temporal.
# Tarea: devuelve (secundario, primario) usando desempaquetado de tuplas.
# ----------------------------------------------------------------------------
def intercambiar(primario: str, secundario: str) -> tuple:
    return secundario, primario


# ----------------------------------------------------------------------------
# EJERCICIO 3  ⭐  — Min, max y media en una pasada
# Contexto: dashboard de métricas. Recibes lecturas de un sensor y debes
# devolver las tres estadísticas como una sola tupla.
# Tarea: devuelve (minimo, maximo, media). La media como float.
# ----------------------------------------------------------------------------
def resumen_sensor(lecturas: tuple) -> tuple:
    return min(lecturas), max(lecturas), sum(lecturas) / len(lecturas)


# ----------------------------------------------------------------------------
# EJERCICIO 4  ⭐⭐  — Parsear cabecera y filas
# Contexto: lees un CSV ya troceado en filas (lista de tuplas). La primera
# fila es la cabecera y el resto son datos.
# Tarea: devuelve una tupla (cabecera, lista_de_filas_de_datos).
# Usa desempaquetado con *.
# ----------------------------------------------------------------------------
def separar_cabecera(filas: list) -> tuple:
    cabecera, *datos = filas
    return cabecera, datos


# ----------------------------------------------------------------------------
# EJERCICIO 5  ⭐⭐  — Tarifa por ruta con tupla como clave
# Contexto: motor de precios de vuelos. El precio depende de (origen, destino).
# Tarea: dado un diccionario de tarifas y una ruta (origen, destino),
# devuelve el precio, o -1.0 si la ruta no existe.
# ----------------------------------------------------------------------------
def precio_ruta(tarifas: dict, origen: str, destino: str) -> float:
    return tarifas.get((origen, destino), -1)


# ----------------------------------------------------------------------------
# EJERCICIO 6  ⭐⭐  — Contar votos y encontrar al ganador
# Contexto: recuento electoral. Recibes una tupla de votos (nombres repetidos).
# Tarea: devuelve una tupla (ganador, num_votos) del más votado.
# En caso de empate, gana el que aparece primero al recorrer el conjunto único.
# Pista: tupla.count() es tu amigo.
# ----------------------------------------------------------------------------
def ganador_votacion(votos: tuple) -> tuple:
    nombres_unicos = set(votos)
    ganador = ("", -1)
    for n in nombres_unicos:
        num_votos = votos.count(n)
        if num_votos > ganador[1]:
            ganador = n, num_votos
    return ganador


# ----------------------------------------------------------------------------
# EJERCICIO 7  ⭐⭐⭐  — Agrupar transacciones por (usuario, categoría)
# Contexto: analítica de gastos. Recibes una lista de transacciones, cada una
# es una tupla (usuario, categoria, importe). Debes sumar el importe total
# por cada par (usuario, categoria).
# Tarea: devuelve un dict { (usuario, categoria): total }.
# ----------------------------------------------------------------------------
def agrupar_gastos(transacciones: list) -> dict:
    totales = {}
    for usuario, categoria, importe in transacciones:
        clave = (usuario, categoria)
        totales[clave] = totales.get(clave, 0.0) + importe
    return totales


# ----------------------------------------------------------------------------
# EJERCICIO 8  ⭐⭐⭐  — Ranking ordenando por varias claves
# Contexto: tabla de clasificación de un torneo. Cada jugador es una tupla
# (nombre, puntos, diferencia_goles). Hay que ordenar por puntos DESC y,
# a igualdad de puntos, por diferencia_goles DESC.
# Tarea: devuelve la lista ordenada de tuplas.
# Pista: ordena por una tupla de claves negadas, o usa reverse con cuidado.
# ----------------------------------------------------------------------------
def clasificacion(jugadores: list) -> list:
    return sorted(jugadores, key=lambda j: (-j[1], -j[2]))


# ----------------------------------------------------------------------------
# EJERCICIO 9  ⭐⭐⭐⭐  — Registro inmutable con namedtuple
# Contexto: capa de dominio de una app de RRHH. Quieres un registro de
# empleado inmutable, legible y con un método que devuelva una COPIA con
# el salario actualizado (sin mutar el original).
# Tarea:
#   - Crea un namedtuple llamado 'Empleado' con campos: nombre, salario, dpto.
#   - Implementa subir_salario(empleado, pct) que devuelva una copia nueva
#     con el salario incrementado un 'pct' por ciento.
# ----------------------------------------------------------------------------
Empleado = namedtuple('Empleado', ['nombre', 'salario', 'dpto'])

def subir_salario(empleado, pct: float):
    return empleado._replace(salario=empleado.salario * (1 + pct / 100))


# ----------------------------------------------------------------------------
# EJERCICIO 10  ⭐⭐⭐⭐  — Detectar colisiones en un tablero (set de tuplas)
# Contexto: motor de un juego por turnos. Tienes las posiciones (x, y) de
# varias unidades. Dos unidades colisionan si ocupan la misma celda.
# Tarea: dada una lista de posiciones (tuplas (x, y)), devuelve una tupla
# (hay_colision, celdas_repetidas) donde:
#   - hay_colision es bool
#   - celdas_repetidas es un set con las celdas ocupadas por más de una unidad
# Pista: las tuplas son hashables -> puedes meterlas en un set y contarlas.
# ----------------------------------------------------------------------------
def detectar_colisiones(posiciones: list) -> tuple:
    vistas = set()
    repetidas = set()
    for celda in posiciones:
        if celda in vistas:
            repetidas.add(celda)
        else:
            vistas.add(celda)
    return (len(repetidas) > 0, repetidas)


# ============================================================================
#  DEMO — imprime lo que devuelve cada ejercicio (para ir viendo el resultado)
# ============================================================================
def _mostrar(num, descripcion, funcion):
    """Ejecuta una función ya sin argumentos y muestra su resultado o el error."""
    try:
        resultado = funcion()
        print(f"  Ej {num:>2} | {descripcion:<28} -> {resultado!r}")
    except Exception as e:
        print(f"  Ej {num:>2} | {descripcion:<28} -> ❌ {type(e).__name__}: {e}")


def _mostrar_resultados():
    print("\n" + "=" * 70)
    print("  RESULTADOS DE CADA EJERCICIO")
    print("=" * 70)

    _mostrar(1, "crear_coordenada(40.41,-3.7)", lambda: crear_coordenada(40.41, -3.70))
    _mostrar(2, "intercambiar('db1','db2')", lambda: intercambiar("db1", "db2"))
    _mostrar(3, "resumen_sensor((10,20,30))", lambda: resumen_sensor((10, 20, 30)))
    _mostrar(4, "separar_cabecera(filas)",
             lambda: separar_cabecera([("id", "nombre"), (1, "Ana"), (2, "Luis")]))
    _mostrar(5, "precio_ruta(MAD->BCN)",
             lambda: precio_ruta({("MAD", "BCN"): 49.99}, "MAD", "BCN"))
    _mostrar(6, "ganador_votacion(...)",
             lambda: ganador_votacion(("A", "B", "A", "C", "A", "B")))
    _mostrar(7, "agrupar_gastos(...)", lambda: agrupar_gastos([
        ("ana", "comida", 10.0), ("ana", "comida", 5.5),
        ("ana", "ocio", 20.0), ("luis", "comida", 8.0)]))
    _mostrar(8, "clasificacion(...)", lambda: clasificacion([
        ("Equipo A", 6, 3), ("Equipo B", 9, 1),
        ("Equipo C", 9, 5), ("Equipo D", 3, 0)]))
    _mostrar(9, "subir_salario(Ana, 10%)",
             lambda: subir_salario(Empleado("Ana", 1000.0, "IT"), 10))
    _mostrar(10, "detectar_colisiones(...)",
             lambda: detectar_colisiones([(0, 0), (1, 1), (0, 0), (2, 2), (1, 1)]))


# ============================================================================
#  TESTS — no toques nada de aquí abajo
# ============================================================================
def _run_tests():
    # 1
    assert crear_coordenada(40.41, -3.70) == (40.41, -3.70)
    assert isinstance(crear_coordenada(0, 0), tuple)

    # 2
    assert intercambiar("db1", "db2") == ("db2", "db1")

    # 3
    assert resumen_sensor((10, 20, 30)) == (10, 30, 20.0)
    assert resumen_sensor((5,)) == (5, 5, 5.0)

    # 4
    filas = [("id", "nombre"), (1, "Ana"), (2, "Luis")]
    cab, datos = separar_cabecera(filas)
    assert cab == ("id", "nombre")
    assert datos == [(1, "Ana"), (2, "Luis")]

    # 5
    tarifas = {("MAD", "BCN"): 49.99, ("MAD", "LON"): 120.5}
    assert precio_ruta(tarifas, "MAD", "BCN") == 49.99
    assert precio_ruta(tarifas, "MAD", "NYC") == -1.0

    # 6
    assert ganador_votacion(("A", "B", "A", "C", "A", "B")) == ("A", 3)
    assert ganador_votacion(("X", "Y", "Y")) == ("Y", 2)

    # 7
    txs = [
        ("ana", "comida", 10.0),
        ("ana", "comida", 5.5),
        ("ana", "ocio", 20.0),
        ("luis", "comida", 8.0),
    ]
    res = agrupar_gastos(txs)
    assert res[("ana", "comida")] == 15.5
    assert res[("ana", "ocio")] == 20.0
    assert res[("luis", "comida")] == 8.0

    # 8
    jugadores = [
        ("Equipo A", 6, 3),
        ("Equipo B", 9, 1),
        ("Equipo C", 9, 5),
        ("Equipo D", 3, 0),
    ]
    esperado = [
        ("Equipo C", 9, 5),
        ("Equipo B", 9, 1),
        ("Equipo A", 6, 3),
        ("Equipo D", 3, 0),
    ]
    assert clasificacion(jugadores) == esperado

    # 9
    assert Empleado is not None, "Debes definir el namedtuple 'Empleado'"
    e = Empleado("Ana", 1000.0, "IT")
    e2 = subir_salario(e, 10)
    assert e2.salario == 1100.0
    assert e.salario == 1000.0, "El original NO debe cambiar (inmutable)"
    assert e2.nombre == "Ana" and e2.dpto == "IT"

    # 10
    pos = [(0, 0), (1, 1), (0, 0), (2, 2), (1, 1)]
    hay, repetidas = detectar_colisiones(pos)
    assert hay is True
    assert repetidas == {(0, 0), (1, 1)}
    hay2, rep2 = detectar_colisiones([(0, 0), (1, 1)])
    assert hay2 is False and rep2 == set()

    print("\n" + "=" * 60)
    print("  ✅  TODAS LAS SOLUCIONES PASAN")
    print("=" * 60)


if __name__ == "__main__":
    _mostrar_resultados()   # primero ves QUÉ devuelve cada ejercicio
    _run_tests()            # luego se comprueba que las respuestas son correctas
