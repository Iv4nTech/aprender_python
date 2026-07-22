"""
================================================================================
 EJERCICIOS RESUELTOS: JSON EN PYTHON
 Casos reales — de fácil a experto
================================================================================

Este fichero está pensado para ejecutarse de principio a fin:

    python3 ejercicios_resueltos.py

Cada ejercicio imprime resultados reales para confirmar que funciona.
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

config_app = {
    "puerto": 8080,
    "debug": False,
    "region": "eu-west-1",
    "reintentos_maximos": 3,
}

# SOLUCIÓN
config_json = json.dumps(config_app)
config_recuperada = json.loads(config_json)
tipo_puerto = type(config_recuperada["puerto"])

print(config_json)
print(config_recuperada)
print(f"Tipo de 'puerto' tras loads: {tipo_puerto}")


# ============================================================================
# EJERCICIO 2 — FÁCIL — Leer y actualizar un fichero usuarios.json
# ============================================================================
seccion("EJERCICIO 2 — FÁCIL — Leer y actualizar un fichero usuarios.json")

with open("usuarios.json", "w", encoding="utf-8") as f:
    json.dump(
        {"usuarios": [{"nombre": "Ana"}, {"nombre": "Luis"}, {"nombre": "Marta"}]},
        f,
    )

# SOLUCIÓN
with open("usuarios.json", encoding="utf-8") as f:
    datos_usuarios = json.load(f)
total_usuarios = len(datos_usuarios["usuarios"])

datos_usuarios["total"] = total_usuarios
with open("usuarios.json", "w", encoding="utf-8") as f:
    json.dump(datos_usuarios, f)

with open("usuarios.json", encoding="utf-8") as f:
    print(json.load(f))


# ============================================================================
# EJERCICIO 3 — FÁCIL — Guardar productos con acentos correctamente
# ============================================================================
seccion("EJERCICIO 3 — FÁCIL — Guardar productos con acentos correctamente")

productos = [
    {"nombre": "Ratón inalámbrico", "precio": 25.50, "stock": 12},
    {"nombre": "Teclado mecánico", "precio": 89.99, "stock": 5},
    {"nombre": "Cámara web HD", "precio": 45.00, "stock": 0},
]

# SOLUCIÓN
with open("productos.json", "w", encoding="utf-8") as f:
    json.dump(productos, f, indent=2, ensure_ascii=False)

with open("productos.json", encoding="utf-8") as f:
    print(f.read())


# ============================================================================
# EJERCICIO 4 — MEDIO — parse_respuesta_api tolerante a errores
# ============================================================================
seccion("EJERCICIO 4 — MEDIO — parse_respuesta_api tolerante a errores")

# SOLUCIÓN
def parse_respuesta_api(texto: str):
    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        return None

respuesta_valida = '{"pedido_id": "PED-100", "estado": "confirmado"}'
respuesta_rota = '{"pedido_id": "PED-101", "estado": }'

print(parse_respuesta_api(respuesta_valida))
print(parse_respuesta_api(respuesta_rota))


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

# SOLUCIÓN
pedidos = json.loads(respuesta_pedidos)["pedidos"]
total_enviados = sum(p["importe"] for p in pedidos if p["estado"] == "enviado")

print(f"Total en pedidos enviados: {total_enviados}")


# ============================================================================
# EJERCICIO 6 — MEDIO — Serializar un datetime con default=
# ============================================================================
seccion("EJERCICIO 6 — MEDIO — Serializar un datetime con default=")

evento = {"tipo": "usuario_registrado", "cuando": datetime(2024, 1, 15, 10, 30, 0)}

# SOLUCIÓN
def default_fecha(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Objeto de tipo {type(obj).__name__} no es serializable a JSON")

evento_json = json.dumps(evento, default=default_fecha)

print(evento_json)


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

# SOLUCIÓN
def reconstruir_fecha(dct):
    if "fecha_creacion" in dct:
        dct["fecha_creacion"] = datetime.fromisoformat(dct["fecha_creacion"])
    return dct

datos = json.loads(respuesta_pedidos_con_fecha, object_hook=reconstruir_fecha)
for pedido in datos["pedidos"]:
    print(pedido["id"], type(pedido["fecha_creacion"]), pedido["fecha_creacion"])


# ============================================================================
# EJERCICIO 8 — AVANZADO — Clase Config con persistencia automática
# ============================================================================
seccion("EJERCICIO 8 — AVANZADO — Clase Config con persistencia automática")

# SOLUCIÓN
class Config:
    DEFAULTS = {"tema": "claro", "idioma": "es"}

    def __init__(self, ruta="config_app.json"):
        self._ruta = ruta
        if os.path.exists(ruta):
            with open(ruta, encoding="utf-8") as f:
                self._datos = json.load(f)
        else:
            self._datos = dict(self.DEFAULTS)

    def __getitem__(self, clave):
        return self._datos[clave]

    def __setitem__(self, clave, valor):
        self._datos[clave] = valor

    def guardar(self):
        with open(self._ruta, "w", encoding="utf-8") as f:
            json.dump(self._datos, f, indent=2)

config = Config("config_app_test.json")
print(config["tema"])
config["tema"] = "oscuro"
config.guardar()
config2 = Config("config_app_test.json")
print(config2["tema"])
os.remove("config_app_test.json")


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

# SOLUCIÓN
def default_factura(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Objeto de tipo {type(obj).__name__} no es serializable a JSON")

facturas_json = json.dumps(facturas, default=default_factura)

print(facturas_json)
print(json.loads(facturas_json)[0]["lineas"])


# ============================================================================
# EJERCICIO 10 — EXPERTO — Pipeline de limpieza de datos tolerante a errores
# ============================================================================
seccion("EJERCICIO 10 — EXPERTO — Pipeline de limpieza de datos tolerante a errores")

registros_entrada = [
    {"nombre": "ANA GARCÍA", "fecha_nacimiento": "1995-06-10", "_id_interno": "u1"},
    {"nombre": "Luis Pérez", "fecha_nacimiento": "1988-11-23", "_id_interno": "u2"},
    {"nombre": "MARTA ruiz"},  # sin fecha_nacimiento: debe registrarse como error
]
with open("datos_entrada.json", "w", encoding="utf-8") as f:
    json.dump(registros_entrada, f, ensure_ascii=False)

# SOLUCIÓN
def transformar_registro(registro: dict) -> dict:
    nacimiento = date.fromisoformat(registro["fecha_nacimiento"])
    hoy = date.today()
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
    limpio = {k: v for k, v in registro.items() if not k.startswith("_")}
    limpio["nombre"] = limpio["nombre"].lower()
    limpio["edad"] = edad
    return limpio

def pipeline_limpieza(ruta_entrada: str, ruta_salida: str):
    with open(ruta_entrada, encoding="utf-8") as f:
        registros = json.load(f)

    limpios = []
    errores = []
    for indice, registro in enumerate(registros):
        try:
            limpios.append(transformar_registro(registro))
        except KeyError as e:
            errores.append({"indice": indice, "registro": registro, "motivo": f"falta el campo {e}"})

    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(limpios, f, indent=2, ensure_ascii=False)

    return errores

resultado = pipeline_limpieza("datos_entrada.json", "datos_limpios.json")
with open("datos_limpios.json", encoding="utf-8") as f:
    print(json.load(f))
print("Errores:", resultado)


for fichero in ("usuarios.json", "productos.json", "datos_entrada.json", "datos_limpios.json"):
    if os.path.exists(fichero):
        os.remove(fichero)

seccion("FIN — 10/10 ejercicios resueltos")
