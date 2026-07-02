# Lección 11 · Namespace packages (PEP 420) — SIN `__init__.py`

CONCEPTO (AVANZADO): un mismo paquete puede estar REPARTIDO en varias carpetas
distintas del disco. Esto NO se hace con `__init__.py`, sino con *namespace
packages*: carpetas SIN `__init__.py` que comparten el mismo nombre.

Aquí el paquete `extensiones` vive partido en dos sitios:

```
ruta_a/extensiones/audio.py     (NO hay __init__.py)
ruta_b/extensiones/video.py     (NO hay __init__.py)
```

Al poner AMBAS rutas en el path de búsqueda, Python las une en un solo
paquete lógico `extensiones` con `audio` y `video` dentro.

CASO REAL: plugins de terceros. Cada plugin se instala en su propia carpeta,
pero todos aparecen bajo el mismo paquete (p. ej. `import miempresa.plugin_x`).

## Ejecutar

Desde esta carpeta (`11_namespace_package`):

```bash
python3 demo.py
```
