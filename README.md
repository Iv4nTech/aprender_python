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

### 7 · Paquetes vs Módulos

<img src="./miniaturas/paquetesvsmodulos.jpg" alt="Paquetes vs Módulos en Python" width="480">

¿Cómo se organizan los proyectos grandes? Un **módulo** es un archivo `.py` y un **paquete** es una carpeta con `__init__.py` que agrupa varios módulos. Aprenderás a importar con notación de puntos, a diseñar una API pública limpia con `__all__`, los imports relativos y trucos profesionales como los *namespace packages*. La clave para pasar de scripts sueltos a proyectos de verdad.

📂 [`7 - Paquetes vs Modulos`](./7%20-%20Paquetes%20vs%20Modulos)

---

### 8 · Context Managers

<img src="./miniaturas/context-managers.jpg" alt="Context Managers en Python" width="480">

El famoso `with open(...)` no es magia: es un **context manager**. Aprenderás a gestionar recursos (archivos, conexiones, bloqueos) de forma segura, garantizando que siempre se liberen aunque algo falle. Incluso crearás los tuyos propios. Código robusto de nivel profesional.

📂 [`8 - Context Managers`](./8%20-%20Context%20Managers)

---

### 9 · Generadores

<img src="./miniaturas/generadores.jpg" alt="Generadores en Python" width="480">

¿Trabajar con millones de datos sin agotar la memoria? Los **generadores** producen valores *bajo demanda*, uno a uno, en lugar de cargarlo todo a la vez. Con `yield` desbloquearás un nivel superior de eficiencia y elegancia.

📂 [`9 - Generadores`](./9%20-%20Generadores)

---

### 10 · Dunder Methods

<img src="./miniaturas/method_dunder.jpg" alt="Dunder Methods en Python" width="480">

Los **métodos mágicos** (o *dunder methods*, por el doble guion bajo en `__metodo__`) son los que Python llama por detrás cuando usas `+`, `==`, `len()`, `print()` o un `for`. Definiéndolos, tus propios objetos se comportan como los tipos nativos: podrás sumarlos, compararlos, iterarlos o imprimirlos a tu gusto. El broche de oro: el nivel más alto de personalización en la programación orientada a objetos.

📂 [`10 - Dunder Methods`](./10%20-%20Dunder%20Methods)

---

### 11 · Closures

<img src="./miniaturas/closures.jpg" alt="Closures en Python" width="480">

Una función que se lleva una **"mochila"** con las variables del lugar donde nació y las recuerda para siempre, aunque ese lugar ya no exista. Los **closures** te permiten fabricar funciones a medida, mantener estado sin usar clases y entender de una vez la regla LEGB. Son, además, la base directa sobre la que se construyen los decoradores.

📂 [`11 - Closures`](./11%20-%20Closures)

---

### 12 · Async / Await

<img src="./miniaturas/async-await.jpg" alt="Async y Await en Python" width="480">

¿Y si, mientras tu programa **espera** una descarga o una consulta a la base de datos, pudiera ir avanzando otras diez tareas? Con `async`/`await` escribes código **concurrente** con un solo hilo: descargas que pasan de 5 segundos a 1, colas de trabajo con varios *workers* y control fino con `TaskGroup`, `Semaphore` y `timeout`. El salto que separa a un script que espera de uno que rinde.

📂 [`12 - Async Await`](./12%20-%20Async%20Await)

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
