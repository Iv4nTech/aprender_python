# 🐍 Aprender Python

Una colección de proyectos prácticos para dominar Python paso a paso, **ordenados de menor a mayor dificultad**. Cada carpeta contiene una introducción al concepto, ejercicios para practicar y sus soluciones.

> El objetivo no es solo leer teoría, sino *escribir código*. Cada tema incluye ejercicios resueltos y sin resolver para que aprendas haciendo.

---

## 📚 Contenido

### 1 · Tuplas

<img src="./miniaturas/tuplas.jpg" alt="Tuplas en Python" width="480">

Las tuplas son colecciones **ordenadas e inmutables**: una vez creadas, no cambian. Son perfectas para representar datos que no deberían modificarse (coordenadas, fechas, registros) y, al ser inmutables, son más rápidas y seguras que las listas. Tu primer paso para entender cómo Python organiza la información.

📂 [`1 - Tuplas`](./1%20-%20Tuplas)

---

### 2 · Sets

<img src="./miniaturas/sets.jpg" alt="Sets en Python" width="480">

¿Necesitas eliminar duplicados al instante o comprobar si un elemento existe a toda velocidad? Los **sets** (conjuntos) son tu herramienta. Además, te dan operaciones matemáticas como unión, intersección y diferencia con una sintaxis elegante. Descubre por qué son uno de los secretos mejor guardados para escribir código limpio.

📂 [`2 - Sets`](./2%20-%20Sets)

---

### 3 · List Comprehensions

<img src="./miniaturas/list-comprehensions.jpg" alt="List Comprehensions en Python" width="480">

Convierte cinco líneas de bucles en una sola, legible y eficiente. Las **list comprehensions** son una de las características más queridas de Python: te permiten crear y transformar listas de forma expresiva. Aprenderás a pensar "al estilo Python" y tu código nunca volverá a ser el mismo.

📂 [`3 - List Comprehensions`](./3%20-%20List%20Comprehensions)

---

### 4 · Lambda

<img src="./miniaturas/lambda.jpg" alt="Funciones Lambda en Python" width="480">

Funciones tan pequeñas que caben en una sola línea y no necesitan nombre. Las funciones **lambda** brillan cuando las combinas con `map`, `filter` y `sorted`, permitiéndote escribir lógica potente de forma concisa. Una puerta de entrada al mundo de la programación funcional.

📂 [`4 - Lambda`](./4%20-%20Lambda)

---

### 5 · Args y Kwargs

<img src="./miniaturas/args-kwargs.jpg" alt="Args y Kwargs en Python" width="480">

¿Y si una función pudiera aceptar cualquier número de argumentos? Con `*args` y `**kwargs` creas funciones **flexibles y reutilizables** que se adaptan a lo que necesites. Es la base para entender cómo funcionan muchas librerías profesionales por dentro.

📂 [`5 - Args y Kwargs`](./5%20-%20Args%20y%20Kwargs)

---

### 6 · Name Main

<img src="./miniaturas/name-main.jpg" alt="if __name__ == __main__ en Python" width="480">

`if __name__ == "__main__":` aparece en casi todos los scripts profesionales… ¿pero sabes *por qué*? Aquí entenderás cómo Python distingue entre ejecutar un archivo directamente o importarlo como módulo, una pieza clave para organizar proyectos reales.

📂 [`6 - Name Main`](./6%20-%20Name%20Main)

---

### 7 · Context Managers

<img src="./miniaturas/context-managers.jpg" alt="Context Managers en Python" width="480">

El famoso `with open(...)` no es magia: es un **context manager**. Aprenderás a gestionar recursos (archivos, conexiones, bloqueos) de forma segura, garantizando que siempre se liberen aunque algo falle. Incluso crearás los tuyos propios. Código robusto de nivel profesional.

📂 [`7 - Context Managers`](./7%20-%20Context%20Managers)

---

### 8 · Generadores

<img src="./miniaturas/generadores.jpg" alt="Generadores en Python" width="480">

¿Trabajar con millones de datos sin agotar la memoria? Los **generadores** producen valores *bajo demanda*, uno a uno, en lugar de cargarlo todo a la vez. Con `yield` desbloquearás un nivel superior de eficiencia y elegancia. El broche de oro para tu dominio de Python.

📂 [`8 - Generadores`](./8%20-%20Generadores)

---

## 🚀 Cómo empezar

```bash
# Clona el repositorio
git clone <url-del-repositorio>

# Entra en el tema que quieras aprender
cd "1 - Tuplas"

# Ejecuta la introducción
python introduccion.py
```

Cada carpeta sigue la misma estructura: un archivo de **introducción**, **ejercicios** para resolver y sus **soluciones**. ¡Empieza por el número 1 y avanza a tu ritmo!
