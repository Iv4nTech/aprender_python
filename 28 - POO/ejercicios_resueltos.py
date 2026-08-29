"""
================================================================================
 EJERCICIOS RESUELTOS: PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
 Ejecutar: python3 ejercicios_resueltos.py
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


# SOLUCIÓN
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def disponible(self):
        return self.stock > 0


teclado = Producto("Teclado", 45.99, 3)
raton = Producto("Ratón", 19.99, 0)
print(teclado.disponible())
print(raton.disponible())


# ──────────────────────────────────────────────
# EJERCICIO 2 — FÁCIL
# Rectángulo con área y perímetro
# ──────────────────────────────────────────────
seccion("EJERCICIO 2 — FÁCIL — Rectángulo con área y perímetro")


# SOLUCIÓN
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)


r = Rectangulo(4, 5)
print(r.area())
print(r.perimetro())


# ──────────────────────────────────────────────
# EJERCICIO 3 — FÁCIL
# Cuenta bancaria sin saldo negativo
# ──────────────────────────────────────────────
seccion("EJERCICIO 3 — FÁCIL — Cuenta bancaria sin saldo negativo")


# SOLUCIÓN
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad


cuenta = CuentaBancaria("Elena", 100.0)
cuenta.depositar(50)
cuenta.retirar(30)
cuenta.retirar(1000)  # no hace nada, no hay fondos suficientes
print(cuenta.saldo)


# ──────────────────────────────────────────────
# EJERCICIO 4 — MEDIO
# Playlist con duración total
# ──────────────────────────────────────────────
seccion("EJERCICIO 4 — MEDIO — Playlist con duración total")


# SOLUCIÓN
class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar(self, cancion):
        self.canciones.append(cancion)

    def eliminar(self, titulo):
        self.canciones = [c for c in self.canciones if c["titulo"] != titulo]

    def duracion_total(self):
        return sum(c["segundos"] for c in self.canciones)


playlist = Playlist("Focus")
playlist.agregar({"titulo": "Intro", "segundos": 120})
playlist.agregar({"titulo": "Flow", "segundos": 240})
playlist.agregar({"titulo": "Outro", "segundos": 90})
playlist.eliminar("Outro")
print(playlist.duracion_total())


# ──────────────────────────────────────────────
# EJERCICIO 5 — MEDIO
# La trampa del atributo de clase mutable
# ──────────────────────────────────────────────
seccion("EJERCICIO 5 — MEDIO — La trampa del atributo de clase mutable")


# Versión con el bug: 'jugadores' es un atributo de CLASE compartido.
class EquipoRoto:
    jugadores = []

    def fichar(self, jugador):
        self.jugadores.append(jugador)


equipo_a = EquipoRoto()
equipo_b = EquipoRoto()
equipo_a.fichar("Rodri")
print(equipo_b.jugadores)  # bug: contiene "Rodri" sin haberlo fichado


# SOLUCIÓN: mover 'jugadores' a __init__ para que sea de instancia.
class Equipo:
    def __init__(self):
        self.jugadores = []

    def fichar(self, jugador):
        self.jugadores.append(jugador)


equipo_c = Equipo()
equipo_d = Equipo()
equipo_c.fichar("Pedri")
print(equipo_d.jugadores)


# ──────────────────────────────────────────────
# EJERCICIO 6 — MEDIO
# Empleado y Gerente con herencia
# ──────────────────────────────────────────────
seccion("EJERCICIO 6 — MEDIO — Empleado y Gerente con herencia")


# SOLUCIÓN
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def bonus(self):
        return self.salario * 0.20


gerente = Gerente("Sara", 3000.0, "Ventas")
print(gerente.bonus())


# ──────────────────────────────────────────────
# EJERCICIO 7 — AVANZADO
# Cadena de herencia: Vehiculo -> Coche -> CocheElectrico
# ──────────────────────────────────────────────
seccion("EJERCICIO 7 — AVANZADO — Cadena de herencia: Vehiculo -> Coche -> CocheElectrico")


# SOLUCIÓN
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def descripcion(self):
        return f"Vehículo {self.marca}"


class Coche(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

    def descripcion(self):
        return f"Coche {self.marca} de {self.puertas} puertas"


class CocheElectrico(Coche):
    def __init__(self, marca, puertas, autonomia_km):
        super().__init__(marca, puertas)
        self.autonomia_km = autonomia_km

    def descripcion(self):
        return (
            f"Coche eléctrico {self.marca} de {self.puertas} puertas, "
            f"{self.autonomia_km} km de autonomía"
        )


v = Vehiculo("Genérica")
c = Coche("Toyota", 5)
ce = CocheElectrico("Tesla", 4, 500)
print(v.descripcion())
print(c.descripcion())
print(ce.descripcion())


# ──────────────────────────────────────────────
# EJERCICIO 8 — AVANZADO
# Descuento con isinstance() según tipo de cliente
# ──────────────────────────────────────────────
seccion("EJERCICIO 8 — AVANZADO — Descuento con isinstance() según tipo de cliente")


# SOLUCIÓN
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


class ClienteVIP(Cliente):
    pass


def calcular_descuento(cliente):
    if isinstance(cliente, ClienteVIP):
        return 0.10
    return 0.0


normal = Cliente("Iván")
vip = ClienteVIP("Marta")
print(calcular_descuento(normal))
print(calcular_descuento(vip))


# ──────────────────────────────────────────────
# EJERCICIO 9 — AVANZADO
# Numeración automática de facturas con atributo de clase
# ──────────────────────────────────────────────
seccion("EJERCICIO 9 — AVANZADO — Numeración automática de facturas con atributo de clase")


# SOLUCIÓN
class Factura:
    contador = 0

    def __init__(self, importe):
        self.importe = importe
        Factura.contador += 1
        self.numero = Factura.contador


f1 = Factura(100.0)
f2 = Factura(250.0)
f3 = Factura(80.0)
print(f1.numero, f2.numero, f3.numero)


# ──────────────────────────────────────────────
# EJERCICIO 10 — EXPERTO
# Tienda completa con inventario
# ──────────────────────────────────────────────
seccion("EJERCICIO 10 — EXPERTO — Tienda completa con inventario")


# SOLUCIÓN
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def productos_disponibles(self):
        return [p for p in self.productos if p.disponible()]

    def aplicar_descuento(self, porcentaje):
        for producto in self.productos:
            producto.precio -= producto.precio * porcentaje / 100


tienda = Tienda()
tienda.agregar_producto(Producto("Teclado", 50.0, 3))
tienda.agregar_producto(Producto("Ratón", 20.0, 0))
tienda.agregar_producto(Producto("Monitor", 200.0, 5))

print(tienda.buscar("Ratón").nombre)
print(tienda.buscar("Webcam"))
print([p.nombre for p in tienda.productos_disponibles()])

tienda.aplicar_descuento(10)
print([p.precio for p in tienda.productos])
