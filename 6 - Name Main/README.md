# `if __name__ == "__main__"` explicado de una vez por todas

## La idea en 3 frases

1. Cada vez que Python carga un archivo `.py`, le regala una variable automática
   llamada `__name__` (no la creas tú, la crea Python).
2. El valor de esa variable depende de **CÓMO** se cargó el archivo:
   - Si lo ejecutas tú directamente (`python archivo.py`) → `__name__` vale `"__main__"`.
   - Si otro archivo lo importa (`import archivo`) → `__name__` vale `"archivo"` (su propio nombre).
3. Por tanto, `if __name__ == "__main__":` significa literalmente:
   **"ejecuta este bloque SOLO si este archivo es el que se lanzó directamente,
   no si alguien me está importando"**.

## El diagrama mental

```
                 ┌─────────────────────────────┐
                 │  Python carga "saludos.py"  │
                 └──────────────┬──────────────┘
                                │
              ¿Cómo se ha cargado el archivo?
                                │
          ┌─────────────────────┴─────────────────────┐
          │                                           │
  python saludos.py                          import saludos
  (TÚ lo ejecutas)                     (OTRO archivo lo importa)
          │                                           │
  __name__ = "__main__"                    __name__ = "saludos"
          │                                           │
  if __name__ == "__main__":               if __name__ == "__main__":
       → True → SÍ se ejecuta                  → False → NO se ejecuta
```

## ¿Por qué existe esto? El problema real

Cuando haces `import saludos`, Python **ejecuta el archivo saludos.py entero**
de arriba a abajo (es la única forma que tiene de saber qué funciones contiene).

Eso significa que si `saludos.py` tiene código "suelto" (prints, llamadas a
funciones...), ese código se ejecutará **sin que tú lo pidieras**, solo por
importarlo. El `if __name__ == "__main__":` es el candado que evita eso.

## Orden recomendado de las carpetas

| Carpeta | Qué demuestra | Cómo ejecutarla |
|---|---|---|
| `01_que_es_name/` | Que `__name__` existe y vale `"__main__"` al ejecutar directo | `python explicacion.py` |
| `02_el_problema/` | Que `import` ejecuta TODO el archivo importado (el problema) | `python app.py` |
| `03_la_solucion/` | El mismo código pero con el candado `if __name__ == "__main__"` | `python app.py` |
| `04_caso_real/` | Cómo se usa en un proyecto de verdad (módulo + programa principal) | `python programa.py` y también `python calculadora.py` |

En cada carpeta, ejecuta los archivos y **lee los prints**: cada print dice
qué archivo lo imprime y por qué, para que sepas en todo momento de dónde
sale cada línea de la salida.

## Resumen final (chuleta)

```python
# mi_modulo.py

def funcion_util():          # Esto SIEMPRE está disponible al importar
    ...

if __name__ == "__main__":   # Esto SOLO corre con: python mi_modulo.py
    funcion_util()           # Zona de pruebas / demo / punto de entrada
```

- Archivo ejecutado directamente → `__name__ == "__main__"` → el bloque corre.
- Archivo importado → `__name__ == "su_nombre"` → el bloque NO corre.
- Dentro del `if` se pone: demos, pruebas rápidas, o el arranque del programa.
- Fuera del `if` se pone: funciones, clases y constantes (lo reutilizable).
