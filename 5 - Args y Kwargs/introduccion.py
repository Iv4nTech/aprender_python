# Args y Kwargs 

# ARGS: Arguments 

def sumar(a, b):
    return a + b
print(sumar(2, 3))  # Salida: 5
# print(sumar(2, 3, 4))  # Error: demasiados argumentos

def sumar(*args):
    return sum(args)
print(sumar(2, 3))  # Salida: 5
print(sumar(2, 3, 4))  # Salida: 9

# Args con otro nombre, por ejemplo patata
def sumar(*patata):
    return sum(patata)
print(sumar(2, 3))  # Salida: 5
print(sumar(2, 3, 4))  # Salida: 9

# Recorrer args
def imprimir_numeros(*args):
    print(type(args))  # Salida: <class 'tuple'>
    print(args)  # Salida: (1, 2, 3)
    for numero in args:
        print(numero)
imprimir_numeros(1, 2, 3)  # Salida:
# 1
# 2
# 3

# KWARGS: Keyword Arguments

#Kwargs usa diccionarios
def imprimir_info(**kwargs):
    print(type(kwargs))  # Salida: <class 'dict'>
    print(kwargs)  # Salida: {'nombre': 'Alice', 'edad': 30}
imprimir_info(nombre='Alice', edad=30)

#Podemos acceder al valor que queramos ya que usan claves
def imprimir_info(**suscribete):
    nombre = suscribete.get('nombre', 'Desconocido')
    edad = suscribete.get('edad', 'Desconocida')
    print(f'Nombre: {nombre}, Edad: {edad}')

imprimir_info(nombre='Bob', edad=30)  # Salida: Nombre: Bob, Edad: 30

# Orden de los argumentos CORRECTO: primero los normales, luego *args y finalmente **kwargs
def ejemplo(a, b, *args, **kwargs):
    print(f'a: {a}, b: {b}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

ejemplo(1, 2, 3, 4, nombre='Charlie', edad=25)

# Orden de los argumentos INCORRECTO

def ejemplo(*args, a, b, **kwargs):
    print(f'a: {a}, b: {b}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

ejemplo(3, 4, a=1, b=2, nombre='Charlie', edad=25)  # Esto funcionará porque a y b se pasan como argumentos de palabra clave

# Pero puede dar error si intentamos pasar a y b como argumentos posicionales
# ejemplo(1, 2, 3, 4, nombre='Charlie', edad=25) # No detectara a y b como argumentos (argumentos posicionales), lo que resultará en un error de tipo porque a y b no se han proporcionado como argumentos de palabra clave.
# ejemplo(a=1, b=2, 3, 4, nombre='Charlie', edad=25)  # Esto dará un eºrror de sintaxis porque los argumentos posicionales no pueden seguir a los argumentos de palabra clave.
# Orden posicionales, kwargs y args

ejemplo(3, 5, nombre="Iván", edad=25, a=1, b=3)

#Args unpacking 
def sumar(a, b, c):
    return a + b + c
numeros = (1, 2, 3)
print(sumar(*numeros))  # Salida: 6

#Kwargs unpacking
def imprimir_info(nombre, edad):
    print(f'Nombre: {nombre}, Edad: {edad}')
info = {'nombre': 'Alice', 'edad': 30}
imprimir_info(**info)  # Salida: Nombre: Alice, Edad: 30