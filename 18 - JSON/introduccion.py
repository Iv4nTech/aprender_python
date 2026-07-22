"""
================================================================================
 JSON EN PYTHON 
 Ejecutar: python3 introduccion.py
================================================================================
"""

import json
import os
import subprocess
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from decimal import Decimal


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA SIN JSON
# ============================================================================
seccion("1. El problema sin JSON")

# Caso real: la config de una app guardada como texto plano casero.
config_texto_plano = "debug=true;puerto=8080;host=localhost;max_conexiones=100"

# Para leerla hay que inventar tu propio parser a mano...
partes = dict(par.split("=") for par in config_texto_plano.split(";"))
print(f"  Config parseada a mano: {partes}")
print(f"  Tipo de 'puerto': {type(partes['puerto']).__name__}")  # sigue siendo str

# El problema aparece el día que otro servicio (un script de deploy en Bash,
# una API en otro lenguaje) necesita leer esta misma config: no hay ningún
# estándar, cada quien inventa su propio formato casero, y "puerto" llega
# como el string "8080" en vez de un número. JSON es un formato de texto
# estándar que cualquier lenguaje sabe leer y que preserva tipos básicos
# (números, booleanos, null) sin que cada proyecto reinvente su parser.


# ============================================================================
# 2. dumps Y loads — DE PYTHON A JSON Y DE VUELTA
# ============================================================================
seccion("2. dumps y loads: de Python a JSON y de vuelta")

# dumps: Python -> string JSON. loads: string JSON -> Python.
config_app = {
    "debug": True,
    "puerto": 8080,
    "host": "localhost",
    "max_conexiones": 100,
    "middleware": None,
    "orígenes_permitidos": ["localhost", "127.0.0.1"],
}

config_json = json.dumps(config_app)
print(f"  json.dumps(config_app):\n  {config_json}")

config_recuperada = json.loads(config_json)
print(f"\n  json.loads(...) de vuelta: {config_recuperada}")

# Tabla de conversión Python -> JSON, todas ejecutables aquí:
print("\n  Tabla de conversión Python -> JSON:")
print(f"    dict  -> object  : {json.dumps({'a': 1})}")
print(f"    list  -> array   : {json.dumps([1, 2, 3])}")
print(f"    tuple -> array   : {json.dumps((1, 2, 3))}")
print(f"    str   -> string  : {json.dumps('hola')}")
print(f"    int   -> number  : {json.dumps(42)}")
print(f"    float -> number  : {json.dumps(3.14)}")
print(f"    True  -> true    : {json.dumps(True)}")
print(f"    None  -> null    : {json.dumps(None)}")

# La trampa: un dict con claves int, al volver de JSON, tiene claves str.
codigos_http = {200: "OK", 404: "No encontrado", 500: "Error interno"}
codigos_json = json.dumps(codigos_http)
codigos_recuperados = json.loads(codigos_json)
print(f"\n  Claves originales: {list(codigos_http.keys())} -> {[type(k).__name__ for k in codigos_http.keys()]}")
print(f"  Claves tras loads: {list(codigos_recuperados.keys())} -> {[type(k).__name__ for k in codigos_recuperados.keys()]}")
# JSON no tiene concepto de "clave entera": las claves de un object SIEMPRE
# son strings. Si buscas codigos_recuperados[200] después de un loads(),
# lanza KeyError aunque codigos_http[200] funcionara perfectamente. Este
# bug aparece constantemente en caches y configs que usan IDs numéricos
# como clave y se guardan/recuperan de JSON sin conversión.
try:
    codigos_recuperados[200]
except KeyError as e:
    print(f"  codigos_recuperados[200] -> KeyError: {e} (hay que usar codigos_recuperados['200'])")


# ============================================================================
# 3. dump Y load — LEER Y ESCRIBIR FICHEROS JSON
# ============================================================================
seccion("3. dump y load: leer y escribir ficheros JSON")

ruta_config = "config.json"

# dump escribe directamente en el stream del fichero, sin construir antes
# el string completo en memoria (importante si la config fuera enorme).
# indent=2 lo hace legible para humanos; ensure_ascii=False evita que los
# acentos se escapen como á, imprescindible en proyectos en español.
with open(ruta_config, "w", encoding="utf-8") as f:
    json.dump(
        {
            "nombre_app": "Panel de Facturación",
            "descripción": "Gestión de pedidos y clientes",
            "debug": False,
            "puerto": 8080,
            "administradores": ["ana@empresa.com", "iván@empresa.com"],
        },
        f,
        indent=2,
        ensure_ascii=False,
    )

with open(ruta_config, encoding="utf-8") as f:
    contenido_crudo = f.read()
print(f"  Contenido real de '{ruta_config}' en disco:\n{contenido_crudo}")

with open(ruta_config, encoding="utf-8") as f:
    config_cargada = json.load(f)
print(f"  json.load(f) devuelve un dict normal: {config_cargada['nombre_app']}")

# Si hubiéramos usado ensure_ascii=True (el valor por defecto), "descripción"
# y "iván@empresa.com" se habrían guardado como "descripción" y
# "iván@empresa.com": técnicamente válido, pero ilegible al abrir el
# fichero a mano y más pesado en bytes por cada acento.


# ============================================================================
# 4. CAPTURAR ERRORES DE PARSING — JSONDecodeError
# ============================================================================
seccion("4. Capturar errores de parsing: JSONDecodeError")

# Caso real: una API externa devuelve una respuesta truncada o corrupta.
# Si no se controla, json.loads() revienta la app entera con un ValueError.
respuesta_api_rota = '{"pedido_id": "PED-001", "estado": "enviado", }'  # coma sobrante

try:
    json.loads(respuesta_api_rota)
except json.JSONDecodeError as e:
    print(f"  JSONDecodeError (es subclase de ValueError: {isinstance(e, ValueError)})")
    print(f"  Mensaje: {e.msg}")
    print(f"  Posición: línea {e.lineno}, columna {e.colno} (offset {e.pos})")


def parse_seguro(texto: str):
    """Patrón de defensa real: nunca dejar que un JSON externo tumbe la app."""
    try:
        return json.loads(texto)
    except json.JSONDecodeError as e:
        print(f"  [parse_seguro] JSON inválido, se ignora: {e.msg} (línea {e.lineno})")
        return None


print("\n  Probando parse_seguro con una respuesta válida y otra rota:")
print(f"    válida -> {parse_seguro('{\"estado\": \"ok\"}')}")
print(f"    rota   -> {parse_seguro(respuesta_api_rota)}")


# ============================================================================
# 5. SERIALIZAR TIPOS QUE JSON NO SOPORTA — default=
# ============================================================================
seccion("5. Serializar tipos que JSON no soporta: default=")

evento_pedido = {"pedido_id": "PED-002", "creado_en": datetime(2024, 1, 15, 10, 30, 0)}

try:
    json.dumps(evento_pedido)
except TypeError as e:
    print(f"  Sin default=, json.dumps() revienta: {e}")


def default_json(obj):
    """Se llama SOLO con los objetos que json no sabe serializar de forma nativa."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Objeto de tipo {type(obj).__name__} no es serializable a JSON")


evento_json = json.dumps(evento_pedido, default=default_json)
print(f"  Con default=default_json: {evento_json}")

# Caso real con dataclass: la API de facturación devuelve importes en Decimal
# para no perder precisión, y las fechas casi siempre son datetime.
@dataclass
class Factura:
    numero: str
    importe: Decimal
    emitida_en: datetime

factura = Factura("F-2024-001", Decimal("149.99"), datetime(2024, 3, 1, 9, 0, 0))
factura_json = json.dumps(asdict(factura), default=default_json)
print(f"  Factura serializada: {factura_json}")


# ============================================================================
# 6. RECONSTRUIR OBJETOS AL DESERIALIZAR — object_hook=
# ============================================================================
seccion("6. Reconstruir objetos al deserializar: object_hook=")

# El inverso del punto anterior: una API de pedidos manda las fechas como
# strings ISO 8601, y queremos que loads() las reconstruya como datetime
# automáticamente, sin tener que recorrer el dict a mano después.
respuesta_api_pedido = json.dumps({
    "pedido_id": "PED-003",
    "creado_en": "2024-01-15T10:30:00",
    "cliente": "Ana García",
})


def reconstruir_fechas(dct):
    if "creado_en" in dct:
        dct["creado_en"] = datetime.fromisoformat(dct["creado_en"])
    return dct


pedido_reconstruido = json.loads(respuesta_api_pedido, object_hook=reconstruir_fechas)
print(f"  pedido['creado_en'] es datetime: {isinstance(pedido_reconstruido['creado_en'], datetime)}")
print(f"  Valor: {pedido_reconstruido['creado_en']!r}")
# object_hook se ejecuta una vez POR CADA object JSON que aparece en el
# documento (incluidos los anidados), así que hay que comprobar qué claves
# tiene cada uno antes de tocarlas, como se hace aquí con el "in".


# ============================================================================
# 7. OPCIONES DE FORMATO PARA PRODUCCIÓN
# ============================================================================
seccion("7. Opciones de formato para producción")

datos_ejemplo = {"puerto": 8080, "debug": True, "host": "localhost"}

print("  Guardar en disco, legible por humanos (indent, ensure_ascii=False, sort_keys):")
print(" ", json.dumps(datos_ejemplo, indent=2, ensure_ascii=False, sort_keys=True))

print("\n  Enviar por red, lo más compacto posible (separators sin espacios):")
print(" ", json.dumps(datos_ejemplo, separators=(",", ":")))

print("\n  Debug rápido en consola (indent más ancho, fácil de leer de un vistazo):")
print(json.dumps(datos_ejemplo, indent=4))

# En una API real, el payload compacto con separators ahorra bytes en cada
# request/response; en un fichero de config que un humano va a editar a
# mano, esos mismos bytes de más en indent=2 son gratis comparados con el
# tiempo que ahorra que sea legible.


# ============================================================================
# 8. python -m json (NOVEDAD PYTHON 3.14)
# ============================================================================
seccion("8. python -m json (novedad Python 3.14)")

# Hasta Python 3.13 había que escribir 'python -m json.tool' para validar
# y pretty-printear un JSON desde la terminal. Desde Python 3.14, el mismo
# comando funciona directamente como 'python -m json' (json.tool queda
# soft-deprecated, sigue funcionando pero ya no hace falta).
resultado = subprocess.run(
    [sys.executable, "-m", "json"],
    input='{"puerto":8080,"debug":true}',
    capture_output=True,
    text=True,
)
print("  $ echo '{\"puerto\":8080,\"debug\":true}' | python -m json")
print(" ", resultado.stdout.replace("\n", "\n  "))


os.remove(ruta_config)


seccion("FIN — ya conoces el módulo json al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
