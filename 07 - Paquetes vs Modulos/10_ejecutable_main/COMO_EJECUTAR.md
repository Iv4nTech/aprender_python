# Lección 10 · Cómo ejecutar

Este NO se lanza con `python demo.py`. Se ejecuta el PAQUETE entero.

Desde esta carpeta (`10_ejecutable_main`):

```bash
python3 -m saludador          # -> 👋 ¡Hola, mundo!
python3 -m saludador Ivan     # -> 👋 ¡Hola, Ivan!
```

Python busca `saludador/__main__.py` y lo ejecuta. Igual que `python -m pip`.
