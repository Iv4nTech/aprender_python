"""
Las 3 formas de importar un módulo (todas válidas, elige según el caso):
"""

# 1) Importar el módulo entero -> accedes con el prefijo: calculadora.xxx
import calculadora
print(calculadora.sumar(2, 3))

# 2) Importar nombres concretos -> los usas directamente
from calculadora import aplicar_iva
print(aplicar_iva(100))

# 3) Importar con alias -> útil para nombres largos o evitar choques
import calculadora as calc
print(calc.aplicar_iva(50, tasa=0.10))
