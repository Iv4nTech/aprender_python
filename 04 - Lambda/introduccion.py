# Ejemplo 1: Diferencia entre función normal y función lambda

# Función normal
def suma(a, b):
    return a + b
# Función lambda
suma_lambda = lambda a, b: a + b

# Uso de ambas funciones
print("Suma con función normal:", suma(3, 5))  # Output: 8
print("Suma con función lambda:", suma_lambda(3, 5))  # Output: 8

# Ejemplo 2: Uso de lambda sin almacenarla en una variable

print("Producto con función lambda:", (lambda a, b: a * b)(3, 5))  # Output: 15

#Ejemplo 3: Pasando como parámetro a otra función e al contrario

# Función que recibe la función lambda como parámetro
def aplicar_operacion(a, b, operacion):
    return operacion(a, b)

# Usando la función lambda como parámetro
resultado = aplicar_operacion(10, 5, lambda x, y: x - y)
print("Resultado de la resta con función lambda:", resultado)  # Output: 5

def aplicar_suma(a, b):
    return a + b

resultado = (lambda a, b: aplicar_suma(a, b))(2, 4)
lambda_funcion = lambda x, y: x + y
resultado = (lambda a, b: lambda_funcion(a, b))(2, 4)
print("Resultado de la suma lambda aprovechando una función existente normal:", resultado)  # Output: 6

# Ejemplo 4: Lambda con valores por defecto

lambda_con_default = lambda a, b=10: a + b
print("Suma con valor por defecto (b=10):", lambda_con_default(5))  # Output: 15
print("Suma con ambos valores:", lambda_con_default(5, 3))  # Output: 8

# Ejemplo 5: Lambda con *args y **kwargs

lambda_con_args = lambda *args: sum(args)
print("Suma de varios números con *args:", lambda_con_args(1, 2, 3, 4))  # Output: 10

lambda_con_kwargs = lambda **kwargs: sum(kwargs.values())
print("Suma de valores con **kwargs:", lambda_con_kwargs(a=1, b=2, c=3))  # Output: 6

# Ejemplo 6: Lambda más de un valor de retorno

lambda_multireturn = lambda a, b: (a + b, a * b)
suma, producto = lambda_multireturn(3, 4)
print("Suma:", suma)  # Output: 7
print("Producto:", producto)  # Output: 12

# Ejemplo 7: Lambda con filter() y map()

numeros = [1, 2, 3, 4, 5, 6]
# Filtrar números pares usando filter() y lambda
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", numeros_pares)  # Output: [2, 4, 6] 

# Elevar al cuadrado cada número usando map() y lambda
cuadrados = map(lambda x: x ** 2, numeros)
print(cuadrados)
print("Cuadrados de los números:", cuadrados)  # Output: [1, 4, 9, 16, 25, 36]