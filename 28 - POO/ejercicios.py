"""
================================================================================
 EJERCICIOS: CLASES Y PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
 Ejecutar: python3 ejercicios.py

 Completa cada ejercicio donde encuentres '...' y descomenta los print()
 para comprobar el resultado.
================================================================================
"""


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ──────────────────────────────────────────────
# EJERCICIO 1 — FÁCIL
# Producto con control de stock
# ──────────────────────────────────────────────
seccion("EJERCICIO 1 — FÁCIL — Producto con control de stock")


# Define la clase Producto con atributos nombre, precio y stock (en ese
# orden, recibidos en __init__). Añade el método disponible() que devuelva
# True si stock > 0, False en caso contrario.
class Producto:
    ...


# teclado = Producto("Teclado", 45.99, 3)
# raton = Producto("Ratón", 19.99, 0)
# print(teclado.disponible())
# print(raton.disponible())

# Resultado esperado:
# True
# False


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Rectángulo con área y perímetro
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — Rectángulo con área y perímetro")


# Define la clase Rectangulo con atributos ancho y alto. Añade los métodos
# area() (ancho * alto) y perimetro() (2 * (ancho + alto)).
class Rectangulo:
    ...


# r = Rectangulo(4, 5)
# print(r.area())
# print(r.perimetro())

# Resultado esperado:
# 20
# 18


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Cuenta bancaria sin saldo negativo
# ──────────────────────────────────────────────
seccion("EJERCICIO 3 — FÁCIL — Cuenta bancaria sin saldo negativo")


# Define la clase CuentaBancaria con atributos titular y saldo. Añade
# depositar(cantidad) que suma al saldo, y retirar(cantidad) que resta al
# saldo solo si hay fondos suficientes; si no, no debe modificar el saldo.
class CuentaBancaria:
    ...


# cuenta = CuentaBancaria("Elena", 100.0)
# cuenta.depositar(50)
# cuenta.retirar(30)
# cuenta.retirar(1000)  # no debe hacer nada, no hay fondos
# print(cuenta.saldo)

# Resultado esperado: 120.0


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Playlist con duración total
# ──────────────────────────────────────────────
seccion("EJERCICIO 4 — MEDIO — Playlist con duración total")


# Define la clase Playlist con atributo nombre y una lista de canciones
# (vacía al crearse). Cada canción es un dict con 'titulo' y 'segundos'.
# Métodos: agregar(cancion), eliminar(titulo) (por título) y
# duracion_total() (suma de segundos de todas las canciones).
class Playlist:
    ...


# playlist = Playlist("Focus")
# playlist.agregar({"titulo": "Intro", "segundos": 120})
# playlist.agregar({"titulo": "Flow", "segundos": 240})
# playlist.agregar({"titulo": "Outro", "segundos": 90})
# playlist.eliminar("Outro")
# print(playlist.duracion_total())

# Resultado esperado: 360


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# La trampa del atributo de clase mutable
# ──────────────────────────────────────────────
seccion("EJERCICIO 5 — MEDIO — La trampa del atributo de clase mutable")

# Esta clase tiene un bug: 'jugadores' es un atributo de CLASE, así que lo
# comparten todos los equipos. Compruébalo primero con el código roto...
class EquipoRoto:
    jugadores = []

    def fichar(self, jugador):
        self.jugadores.append(jugador)


# equipo_a = EquipoRoto()
# equipo_b = EquipoRoto()
# equipo_a.fichar("Rodri")
# print(equipo_b.jugadores)  # bug: contiene "Rodri" sin haberlo fichado

# Resultado esperado del bug: ['Rodri']


# ...y ahora define Equipo (correcta) moviendo 'jugadores' a __init__ para
# que cada instancia tenga su propia lista.
class Equipo:
    ...


# equipo_c = Equipo()
# equipo_d = Equipo()
# equipo_c.fichar("Pedri")
# print(equipo_d.jugadores)

# Resultado esperado: []


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# Empleado y Gerente con herencia
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — Empleado y Gerente con herencia")


# Define Empleado con atributos nombre y salario. Define Gerente, que
# hereda de Empleado, añade el atributo departamento (usa super().__init__
# para nombre y salario) y el método bonus() que devuelve el 20% del salario.
class Empleado:
    ...


class Gerente(Empleado):
    ...


# gerente = Gerente("Sara", 3000.0, "Ventas")
# print(gerente.bonus())

# Resultado esperado: 600.0


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# Cadena de herencia: Vehiculo -> Coche -> CocheElectrico
# ──────────────────────────────────────────────
seccion("EJERCICIO 7 — AVANZADO — Cadena de herencia: Vehiculo -> Coche -> CocheElectrico")


# Vehiculo: atributo marca. Método descripcion() -> f"Vehículo {marca}".
# Coche(Vehiculo): añade atributo puertas. Sobrescribe descripcion() ->
# f"Coche {marca} de {puertas} puertas" (usa super().__init__ para marca).
# CocheElectrico(Coche): añade atributo autonomia_km. Sobrescribe
# descripcion() -> f"Coche eléctrico {marca} de {puertas} puertas, "
# f"{autonomia_km} km de autonomía" (usa super().__init__ para marca y puertas).
class Vehiculo:
    ...


class Coche(Vehiculo):
    ...


class CocheElectrico(Coche):
    ...


# v = Vehiculo("Genérica")
# c = Coche("Toyota", 5)
# ce = CocheElectrico("Tesla", 4, 500)
# print(v.descripcion())
# print(c.descripcion())
# print(ce.descripcion())

# Resultado esperado:
# Vehículo Genérica
# Coche Toyota de 5 puertas
# Coche eléctrico Tesla de 4 puertas, 500 km de autonomía


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Descuento con isinstance() según tipo de cliente
# ──────────────────────────────────────────────
seccion("EJERCICIO 8 — AVANZADO — Descuento con isinstance() según tipo de cliente")


# Define Cliente con atributo nombre. Define ClienteVIP(Cliente) sin
# atributos ni métodos nuevos (solo hereda). Define la función
# calcular_descuento(cliente) que devuelva 0.10 si cliente es ClienteVIP,
# 0.0 si es un Cliente normal (usa isinstance()).
class Cliente:
    ...


class ClienteVIP(Cliente):
    ...


def calcular_descuento(cliente):
    ...


# normal = Cliente("Iván")
# vip = ClienteVIP("Marta")
# print(calcular_descuento(normal))
# print(calcular_descuento(vip))

# Resultado esperado:
# 0.0
# 0.1


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# Numeración automática de facturas con atributo de clase
# ──────────────────────────────────────────────
seccion("EJERCICIO 9 — AVANZADO — Numeración automática de facturas con atributo de clase")


# Define Factura con un atributo de CLASE 'contador' que empieza en 0.
# En __init__(self, importe), incrementa Factura.contador en 1 y guarda
# ese valor como self.numero (así cada factura recibe un número único).
class Factura:
    ...


# f1 = Factura(100.0)
# f2 = Factura(250.0)
# f3 = Factura(80.0)
# print(f1.numero, f2.numero, f3.numero)

# Resultado esperado: 1 2 3


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Tienda completa con inventario
# ──────────────────────────────────────────────
seccion("EJERCICIO 10 — EXPERTO — Tienda completa con inventario")


# Reutiliza la clase Producto del ejercicio 1 (nombre, precio, stock).
# Define Tienda con una lista de productos (vacía al crearse). Métodos:
# - agregar_producto(producto): añade un Producto a la lista.
# - buscar(nombre): devuelve el Producto con ese nombre, o None si no existe.
# - productos_disponibles(): devuelve la lista de productos con stock > 0.
# - aplicar_descuento(porcentaje): reduce el precio de todos los productos
#   ese porcentaje (modifica los productos en el sitio).
class Tienda:
    ...


# tienda = Tienda()
# tienda.agregar_producto(Producto("Teclado", 50.0, 3))
# tienda.agregar_producto(Producto("Ratón", 20.0, 0))
# tienda.agregar_producto(Producto("Monitor", 200.0, 5))
#
# print(tienda.buscar("Ratón").nombre)
# print(tienda.buscar("Webcam"))
# print([p.nombre for p in tienda.productos_disponibles()])
#
# tienda.aplicar_descuento(10)
# print([p.precio for p in tienda.productos])

# Resultado esperado:
# Ratón
# None
# ['Teclado', 'Monitor']
# [45.0, 18.0, 180.0]
