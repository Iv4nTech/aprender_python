"""
'vieja_funcion' no existe como def, pero __getattr__ la intercepta:
lanza un DeprecationWarning y devuelve la nueva. El código viejo sigue vivo.
"""
import warnings
warnings.simplefilter("always")  # para que el aviso se vea siempre en la demo

import libreria

print(libreria.nueva_funcion())

# Acceder a 'vieja_funcion' dispara el aviso de deprecación... pero funciona:
funcion = libreria.vieja_funcion
print(funcion())
