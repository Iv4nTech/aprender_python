
import math


SEP = '─' * 45

print()
print('═' * 45)
print('       GENERADORES EN PYTHON')
print('═' * 45)

# ── 1. Generador básico ──────────────────────────
print(f'\n  1. Hola generador!\n')

def generador():
    yield "hola mundo!"

ge = generador()
print(f'  → {next(ge)}')
try:
    print(next(ge))
except StopIteration:
    print('  ✗ No hay más valores para generar')

print(f'\n{SEP}')

# ── 2. Múltiples valores ─────────────────────────
print(f'\n  2. Generadores con múltiples valores\n')

def generador2():
    yield 1
    yield 2

g = generador2()
print(f'  → {next(g)}')
print(f'  → {next(g)}')

print(f'\n{SEP}')

# ── 3. Forma PRO ─────────────────────────────────
print(f'\n  3. Generadores con múltiples valores\n     y forma PRO de imprimirlos\n')

def generador3():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n

print('  Forma básica (next a next):')
gv = generador3()
print(f'    → {next(gv)}')
print(f'    → {next(gv)}')
print(f'    → {next(gv)}')

print('\n  Forma PRO (for loop):')
for valor in generador3():
    print(f'    → {valor}')

print(f'\n{SEP}\n')

# Generador comprehension, una forma rápida de crear generadores
print(f'  4. Generador comprehension\n')
gen_comp = (x-5 for x in range(5))  
for valor in gen_comp:
    print(f'  → {valor}')

# Sustituir generador por una clase iterable
print(f'\n{SEP}\n')
print(f'  5. Sustituyendo generadores por clases iterables\n')
class Contador:
    def __init__(self, limite):
        self.limite = limite

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.limite:
            valor = self.n
            self.n += 1
            return valor
        else:
            raise StopIteration
        
c = Contador(5)
for numero in c:
    print(f'  → {numero}')

print(f'\n{SEP}\n')

# 6. Solución con generadores que los hace más eficientes
print(f'  6. Solución con generadores que los hace más eficientes\n')
def decorador_tiempo(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'  Tiempo de ejecución: {end - start:.4f} segundos')
        return result
    return wrapper

@decorador_tiempo   
def multiplicar_numero_no_eficiente(n):
    nums = [] # Almacenamos todos los números en memoria
    for i in range(n):
        nums.append(i)
    return math.prod(nums) # Multiplicamos todos los números juntos, lo que puede ser muy lento y consumir mucha memoria
    
def generador_multiplicar_numero_eficiente(n):
    for i in range(n):
        yield i # Generamos cada número uno a uno sin almacenarlos todos en memoria

@decorador_tiempo
def multiplicar_numero_eficiente(n):
    resultado = 1
    for numero in generador_multiplicar_numero_eficiente(n):
        resultado *= numero # Multiplicamos cada número a medida que lo generamos, sin almacenar todos en memoria
    return resultado

print(f'  Multiplicando números del 0 al 999,999 de forma no eficiente:\n')
multiplicar_numero_no_eficiente(1000000)
print('\n')
print(f'  Multiplicando números del 0 al 999,999 de forma eficiente:\n')
multiplicar_numero_eficiente(1000000)

# 7. Convertir a lista para obtener todos los valores de una vez
print(f'\n{SEP}\n')
print(f'  7. Convertir a lista para obtener todos los valores de una vez\n')
def generador_lista(n):
    for i in range(n):
        yield i

gen = generador_lista(10)
print(f'  → Lista: {list(gen)}') # Convertimos el generador a una lista para obtener todos los valores de una vez
