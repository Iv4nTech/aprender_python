# 1. Caso básico: transformar cada elemento (primero la forma tradicional con bucle)
numeros = [1, 2, 3, 4, 5]
dobles_tradicional = []
for n in numeros:
    dobles_tradicional.append(n * 2)

# 1. El mismo resultado con list comprehension (una sola línea)
dobles = [n * 2 for n in numeros]
print(dobles)

# 2. Aplicar una función o método a cada elemento
nombres = ["ana", "luis", "marta"]
nombres_formateados = [nombre.capitalize() for nombre in nombres]
print(nombres_formateados)

# 3. Filtrar con un condicional (if al final): forma tradicional con bucle
edades = [12, 18, 25, 9, 40, 16]
mayores_tradicional = []
for edad in edades:
    if edad >= 18:
        mayores_tradicional.append(edad)

# 3. El mismo filtrado con list comprehension
mayores_de_edad = [edad for edad in edades if edad >= 18]
print(mayores_de_edad)

# 4. Transformar y filtrar a la vez
precios = [10, 25, 5, 80, 3, 50]
precios_con_iva = [precio * 1.21 for precio in precios if precio > 10]
print(precios_con_iva)

# 5. Condicional if/else (operador ternario dentro del comprehension)
temperaturas = [15, 30, 22, 5, 38]
clasificacion = ["calor" if t >= 25 else "frio" for t in temperaturas]
print(clasificacion)

# 6. Varios filtros encadenados
ventas = [120, 340, 50, 890, 200, 30]
ventas_objetivo = [v for v in ventas if v >= 100 if v <= 500]
print(ventas_objetivo)

# 7. Iterar sobre un string (cada carácter es un elemento)
frase = "Hola Mundo"
solo_vocales = [letra for letra in frase if letra.lower() in "aeiou"]
print(solo_vocales)

# 8. For anidados: combinar dos listas (producto de tallas y colores)
tallas = ["S", "M", "L"]
colores = ["rojo", "azul"]
combinaciones = [f"{talla}-{color}" for talla in tallas for color in colores]
print(combinaciones)

# 9. Aplanar una lista de listas (matriz a lista plana)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [valor for fila in matriz for valor in fila]
print(plana)

# 10. List comprehension anidada (lista de listas como resultado)
tabla_multiplicar = [[fila * columna for columna in range(1, 4)] for fila in range(1, 4)]
print(tabla_multiplicar)

# 11. Transponer una matriz (intercambiar filas por columnas)
original = [[1, 2, 3],  
            [4, 5, 6]]
transpuesta = [[fila[i] for fila in original] for i in range(len(original[0]))]
print(transpuesta)

# 12. Usar enumerate para acceder al índice y al valor
productos = ["pan", "leche", "huevos"]
inventario = [f"{i}: {producto}" for i, producto in enumerate(productos, start=1)]
print(inventario)

# 13. Usar zip para recorrer dos listas en paralelo
articulos = ["camiseta", "pantalon", "gorra"]
cantidades = [3, 1, 5]
pedido = [f"{cant}x {art}" for art, cant in zip(articulos, cantidades)]
print(pedido)

# 14. Limpiar y normalizar datos (quitar espacios y pasar a minúsculas)
emails_sucios = ["  Ana@Mail.com ", "LUIS@mail.com", " marta@MAIL.com  "]
emails_limpios = [email.strip().lower() for email in emails_sucios]
print(emails_limpios)

# 15. Extraer un campo de una lista de diccionarios
usuarios = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Luis", "activo": False},
    {"nombre": "Marta", "activo": True},
]
usuarios_activos = [u["nombre"] for u in usuarios if u["activo"]]
print(usuarios_activos)

# 16. Convertir tipos de datos en bloque (strings a enteros)
entradas = ["10", "20", "30", "40"]
valores = [int(x) for x in entradas]
print(valores)

# 17. Combinar condicionales y transformaciones complejas
puntuaciones = [45, 78, 92, 33, 60, 88]
notas = ["aprobado" if p >= 50 else "suspenso" for p in puntuaciones if p > 40]
print(notas)
