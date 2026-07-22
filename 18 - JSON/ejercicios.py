"""
================================================================================
 EJERCICIOS: JSON EN PYTHON
 Casos reales — de fácil a experto
================================================================================

Este fichero está pensado para ejecutarse de principio a fin:

    python3 ejercicios.py

Completa cada ejercicio donde encuentres "..." y descomenta los print()
para comprobar el resultado.
================================================================================
"""

import json
import os
from datetime import datetime, date
from decimal import Decimal


def seccion(titulo: str) -> None:
    """Pequeño helper para imprimir cabeceras y que la salida sea legible."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# EJERCICIO 1 — FÁCIL — dumps y loads con una config de app
# ============================================================================
seccion("EJERCICIO 1 — FÁCIL — dumps y loads con una config de app")

# Una app de e-commerce arranca leyendo esta config desde variables Python.
config_app = {
    "puerto": 8080,
    "debug": False,
    "region": "eu-west-1",
    "reintentos_maximos": 3,
}

# Usa json.dumps() para convertir config_app a un string JSON
config_json = ...

# Usa json.loads() para volver a convertirlo en un dict de Python
config_recuperada = ...

# Comprueba si "puerto" (int) sigue siendo int tras el viaje de ida y vuelta
tipo_puerto = ...

# print(config_json)
# print(config_recuperada)
# print(f"Tipo de 'puerto' tras loads: {tipo_puerto}")

# Resultado esperado: tipo_puerto es <class 'int'> (los VALORES sí conservan
# tipo; son las CLAVES las que siempre se convierten a str, no los valores)


# ============================================================================
# EJERCICIO 2 — FÁCIL — Leer y actualizar un fichero usuarios.json
# ============================================================================
seccion("EJERCICIO 2 — FÁCIL — Leer y actualizar un fichero usuarios.json")

# Setup: se crea el fichero usuarios.json para este ejercicio.
with open("usuarios.json", "w", encoding="utf-8") as f:
    json.dump(
        {"usuarios": [{"nombre": "Ana"}, {"nombre": "Luis"}, {"nombre": "Marta"}]},
        f,
    )

# Usa json.load() para leer usuarios.json y cuenta cuántos usuarios tiene
# la lista "usuarios"
datos_usuarios = ...
total_usuarios = ...

# Añade una key "total" al dict con ese número y guarda el fichero de
# nuevo (sobrescribiéndolo) con json.dump()
...

# with open("usuarios.json", encoding="utf-8") as f:
#     print(json.load(f))

# Resultado esperado: {'usuarios': [...], 'total': 3}


# ============================================================================
# EJERCICIO 3 — FÁCIL — Guardar productos con acentos correctamente
# ============================================================================
seccion("EJERCICIO 3 — FÁCIL — Guardar productos con acentos correctamente")

productos = [
    {"nombre": "Ratón inalámbrico", "precio": 25.50, "stock": 12},
    {"nombre": "Teclado mecánico", "precio": 89.99, "stock": 5},
    {"nombre": "Cámara web HD", "precio": 45.00, "stock": 0},
]

# Guarda productos en "productos.json" con json.dump(), usando indent=2
# y ensure_ascii=False para que los acentos se guarden legibles
...

# with open("productos.json", encoding="utf-8") as f:
#     print(f.read())

# Resultado esperado: el fichero contiene "Ratón", "Cámara" tal cual,
# sin secuencias de escape á ni similares


# ============================================================================
# EJERCICIO 4 — MEDIO — parse_respuesta_api tolerante a errores
# ============================================================================
seccion("EJERCICIO 4 — MEDIO — parse_respuesta_api tolerante a errores")

# Escribe parse_respuesta_api(texto: str) que haga json.loads(texto) y
# devuelva None (sin lanzar excepción) si el texto no es JSON válido
def parse_respuesta_api(texto: str):
    ...

respuesta_valida = '{"pedido_id": "PED-100", "estado": "confirmado"}'
respuesta_rota = '{"pedido_id": "PED-101", "estado": }'

# print(parse_respuesta_api(respuesta_valida))
# print(parse_respuesta_api(respuesta_rota))

# Resultado esperado: {'pedido_id': 'PED-100', 'estado': 'confirmado'} y None


# ============================================================================
# EJERCICIO 5 — MEDIO — Filtrar y sumar pedidos enviados de una API
# ============================================================================
seccion("EJERCICIO 5 — MEDIO — Filtrar y sumar pedidos enviados de una API")

respuesta_pedidos = json.dumps({
    "pedidos": [
        {"id": "PED-1", "estado": "enviado", "importe": 45.00},
        {"id": "PED-2", "estado": "pendiente", "importe": 89.99},
        {"id": "PED-3", "estado": "enviado", "importe": 120.50},
        {"id": "PED-4", "estado": "cancelado", "importe": 30.00},
        {"id": "PED-5", "estado": "enviado", "importe": 15.25},
    ]
})

# Parsea respuesta_pedidos con json.loads(), filtra los pedidos con
# estado "enviado" y suma su importe total
pedidos = ...
total_enviados = ...

# print(f"Total en pedidos enviados: {total_enviados}")

# Resultado esperado: Total en pedidos enviados: 180.75


# ============================================================================
# EJERCICIO 6 — MEDIO — Serializar un datetime con default=
# ============================================================================
seccion("EJERCICIO 6 — MEDIO — Serializar un datetime con default=")

evento = {"tipo": "usuario_registrado", "cuando": datetime(2024, 1, 15, 10, 30, 0)}

# Escribe una función default_fecha(obj) que convierta un datetime a su
# string ISO 8601 con obj.isoformat(), y lánzala con json.dumps(evento, default=...)
def default_fecha(obj):
    ...

evento_json = ...

# print(evento_json)

# Resultado esperado: {"tipo": "usuario_registrado", "cuando": "2024-01-15T10:30:00"}


# ============================================================================
# EJERCICIO 7 — AVANZADO — object_hook para reconstruir fechas
# ============================================================================
seccion("EJERCICIO 7 — AVANZADO — object_hook para reconstruir fechas")

respuesta_pedidos_con_fecha = json.dumps({
    "pedidos": [
        {"id": "PED-10", "fecha_creacion": "2024-02-01T09:00:00"},
        {"id": "PED-11", "fecha_creacion": "2024-02-02T14:15:00"},
    ]
})

# Escribe reconstruir_fecha(dct) para usar como object_hook: si el dict
# tiene la key "fecha_creacion", conviértela con datetime.fromisoformat()
def reconstruir_fecha(dct):
    ...

# datos = json.loads(respuesta_pedidos_con_fecha, object_hook=reconstruir_fecha)
# for pedido in datos["pedidos"]:
#     print(pedido["id"], type(pedido["fecha_creacion"]), pedido["fecha_creacion"])

# Resultado esperado: cada fecha_creacion es un objeto <class 'datetime.datetime'>


# ============================================================================
# EJERCICIO 8 — AVANZADO — Clase Config con persistencia automática
# ============================================================================
seccion("EJERCICIO 8 — AVANZADO — Clase Config con persistencia automática")

# Crea la clase Config que:
# - en __init__(self, ruta="config_app.json") intenta cargar ese fichero
#   con json.load(); si no existe, usa los defaults {"tema": "claro", "idioma": "es"}
# - permite modificar valores como si fuera un dict: config["tema"] = "oscuro"
#   (usa __getitem__ y __setitem__ sobre un dict interno self._datos)
# - tiene un método guardar() que escribe self._datos en self._ruta con
#   json.dump(indent=2)
class Config:
    def __init__(self, ruta="config_app.json"):
        ...

    def __getitem__(self, clave):
        ...

    def __setitem__(self, clave, valor):
        ...

    def guardar(self):
        ...

# config = Config("config_app_test.json")
# print(config["tema"])
# config["tema"] = "oscuro"
# config.guardar()
# config2 = Config("config_app_test.json")
# print(config2["tema"])
# os.remove("config_app_test.json")

# Resultado esperado: 'claro', luego 'oscuro' (persistido y releído del disco)


# ============================================================================
# EJERCICIO 9 — AVANZADO — Facturas anidadas con datetime y Decimal
# ============================================================================
seccion("EJERCICIO 9 — AVANZADO — Facturas anidadas con datetime y Decimal")

facturas = [
    {
        "numero": "F-001",
        "fecha": datetime(2024, 3, 1, 12, 0, 0),
        "importe": Decimal("199.99"),
        "lineas": [{"concepto": "Licencia anual", "importe": Decimal("199.99")}],
    },
    {
        "numero": "F-002",
        "fecha": datetime(2024, 3, 5, 9, 30, 0),
        "importe": Decimal("49.50"),
        "lineas": [{"concepto": "Soporte técnico", "importe": Decimal("49.50")}],
    },
]

# Escribe default_factura(obj) que maneje TANTO datetime (-> isoformat())
# COMO Decimal (-> float()), y sirve para serializar la estructura anidada
def default_factura(obj):
    ...

facturas_json = ...

# print(facturas_json)
# print(json.loads(facturas_json)[0]["lineas"])  # confirma que el JSON es válido

# Resultado esperado: JSON válido con fechas como string ISO y Decimal como number


# ============================================================================
# EJERCICIO 10 — EXPERTO — Pipeline de limpieza de datos tolerante a errores
# ============================================================================
seccion("EJERCICIO 10 — EXPERTO — Pipeline de limpieza de datos tolerante a errores")

# Setup: datos_entrada.json con registros de usuarios, algunos con campos
# internos "_id_interno" que hay que eliminar, y uno con datos incompletos
registros_entrada = [
    {"nombre": "ANA GARCÍA", "fecha_nacimiento": "1995-06-10", "_id_interno": "u1"},
    {"nombre": "Luis Pérez", "fecha_nacimiento": "1988-11-23", "_id_interno": "u2"},
    {"nombre": "MARTA ruiz"},  # sin fecha_nacimiento: debe registrarse como error
]
with open("datos_entrada.json", "w", encoding="utf-8") as f:
    json.dump(registros_entrada, f, ensure_ascii=False)

# Escribe transformar_registro(registro: dict) -> dict que:
# - pone "nombre" en minúsculas
# - calcula "edad" a partir de "fecha_nacimiento" (usa date.today() y
#   date.fromisoformat()), asumiendo el cumpleaños ya pasado este año
# - elimina cualquier key que empiece por "_"
# - lanza KeyError si falta "fecha_nacimiento" (deja que el pipeline lo capture)
def transformar_registro(registro: dict) -> dict:
    ...

# Escribe el pipeline: lee datos_entrada.json, aplica transformar_registro
# a cada registro (saltando y registrando en una lista "errores" los que
# fallen), y guarda los registros válidos en datos_limpios.json
def pipeline_limpieza(ruta_entrada: str, ruta_salida: str):
    ...

# resultado = pipeline_limpieza("datos_entrada.json", "datos_limpios.json")
# with open("datos_limpios.json", encoding="utf-8") as f:
#     print(json.load(f))
# print("Errores:", resultado)

# Resultado esperado: 2 registros limpios (ana garcía, luis pérez) con
# "edad" calculada y sin "_id_interno"; 1 error registrado para "MARTA ruiz"


for fichero in ("usuarios.json", "productos.json", "datos_entrada.json", "datos_limpios.json"):
    if os.path.exists(fichero):
        os.remove(fichero)

seccion("FIN — completa los ejercicios y compáralos con ejercicios_resueltos.py")
