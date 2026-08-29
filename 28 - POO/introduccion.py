"""
================================================================================
 PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
 Ejecutar: python3 introduccion.py
================================================================================
"""


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA QUE RESUELVEN LAS CLASES
# ============================================================================
seccion("1. El problema que resuelven las clases")

# Sin clases: cada usuario es un puñado de variables sueltas.
nombre1 = "Ivan"
email1 = "ivan@email.com"
saldo1 = 150.0

nombre2 = "Luis"
email2 = "luis@email.com"
saldo2 = 320.0

print(f"{nombre1} ({email1}): {saldo1}€")
print(f"{nombre2} ({email2}): {saldo2}€")

# Funciona con 2 usuarios. ¿Y con 300? ¿Cómo escribes una función que
# "deposite dinero en un usuario" si el usuario no es UNA cosa, son tres
# variables sueltas que hay que pasar siempre juntas y en el mismo orden?


def depositar_v1(saldo, cantidad):
    return saldo + cantidad


# Esto obliga a acordarte de qué saldo es de quién, y a pasar nombre y
# email por separado en cada función que los necesite. Nada ata estos tres
# datos entre sí: nada impide mezclar el nombre de un usuario con el saldo
# de otro por error.
saldo1 = depositar_v1(saldo1, 50)
print(f"Nuevo saldo de {nombre1}: {saldo1}€")

# Una clase es un molde que agrupa datos (nombre, email, saldo) y el
# comportamiento que opera sobre ellos (depositar) en una sola unidad.


# ============================================================================
# 2. TU PRIMERA CLASE — SINTAXIS MÍNIMA
# ============================================================================
seccion("2. Tu primera clase — sintaxis mínima")


class Usuario:
    def __init__(self, nombre, email, saldo):
        self.nombre = nombre
        self.email = email
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def __str__(self):
        return f"Usuario({self.nombre}, saldo={self.saldo}€)"


# __init__ se ejecuta automáticamente al crear la instancia: es donde se
# inicializan sus atributos. 'self' es el objeto que se está creando.
u1 = Usuario("Ana", "ana@email.com", 150.0)
u2 = Usuario("Luis", "luis@email.com", 320.0)

# Cada instancia guarda sus propios datos, sin mezclarse con los de otra.
print(f"{u1.nombre}: {u1.saldo}€")
print(f"{u2.nombre}: {u2.saldo}€")

u1.depositar(50)
print(f"{u1.nombre} tras depositar 50: {u1.saldo}€")
print(f"{u2.nombre} sigue igual: {u2.saldo}€")


# ============================================================================
# 3. SELF — QUÉ ES Y POR QUÉ EXISTE
# ============================================================================
seccion("3. self — qué es y por qué existe")

# u1.depositar(50) no es magia: Python lo traduce internamente a esto.
Usuario.depositar(u1, 50)
print(f"{u1.nombre} tras Usuario.depositar(u1, 50): {u1.saldo}€")

# 'self' es simplemente el objeto que llama al método, pasado como primer
# argumento. u1.depositar(50) y Usuario.depositar(u1, 50) son la misma
# llamada; la sintaxis con punto es solo azúcar para no escribir u1 dos
# veces. Por eso todo método de instancia declara 'self' como primer
# parámetro: es el hueco donde Python coloca el objeto automáticamente.


# ============================================================================
# 4. ATRIBUTOS DE CLASE VS ATRIBUTOS DE INSTANCIA
# ============================================================================
seccion("4. Atributos de clase vs atributos de instancia")


class CarritoRoto:
    items = []  # MAL: es un atributo de CLASE, lo comparten todas las instancias

    def agregar(self, producto):
        self.items.append(producto)


c1 = CarritoRoto()
c2 = CarritoRoto()
c1.agregar("leche")
# Bug real: c2 nunca tocó su carrito y sin embargo ve "leche" en su lista,
# porque 'items = []' se creó UNA vez, en la clase, no una vez por carrito.
print(f"Carrito de c1: {c1.items}")
print(f"Carrito de c2 (¡debería estar vacío!): {c2.items}")


class Carrito:
    def __init__(self):
        self.items = []  # BIEN: cada instancia crea su propia lista en __init__

    def agregar(self, producto):
        self.items.append(producto)


c3 = Carrito()
c4 = Carrito()
c3.agregar("pan")
print(f"Carrito de c3: {c3.items}")
print(f"Carrito de c4 (vacío de verdad): {c4.items}")

# Regla práctica: cualquier atributo mutable (lista, dict, set) debe
# inicializarse dentro de __init__, nunca como asignación directa en el
# cuerpo de la clase.


# ============================================================================
# 5. HERENCIA — REUTILIZAR Y EXTENDER
# ============================================================================
seccion("5. Herencia — reutilizar y extender")


class UsuarioAdmin(Usuario):
    def __init__(self, nombre, email, saldo, nivel_acceso):
        super().__init__(nombre, email, saldo)  # reutiliza el __init__ del padre
        self.nivel_acceso = nivel_acceso

    def banear(self, objetivo):
        print(f"{self.nombre} (nivel {self.nivel_acceso}) ha baneado a {objetivo}")

    def __str__(self):
        return f"Admin({self.nombre}, nivel={self.nivel_acceso})"


admin = UsuarioAdmin("Root", "root@empresa.com", 0.0, nivel_acceso=5)
# Métodos heredados de Usuario, sin reescribirlos.
admin.depositar(100)
print(f"{admin.nombre} tiene {admin.saldo}€ tras depositar")
# Método nuevo, solo de UsuarioAdmin.
admin.banear("spam_bot_23")
# __str__ sobrescrito: cambia cómo se muestra un UsuarioAdmin frente a un Usuario normal.
print(admin)

# Sin super().__init__(), 'nombre', 'email' y 'saldo' nunca se asignarían:
# admin.nombre lanzaría AttributeError en cuanto se intentara usar.


# ============================================================================
# 6. isinstance() E issubclass()
# ============================================================================
seccion("6. isinstance() e issubclass()")


def procesar_pago(usuario, cantidad):
    if not isinstance(usuario, Usuario):
        raise TypeError("Se esperaba un Usuario")
    usuario.saldo -= cantidad
    print(f"Pago de {cantidad}€ procesado. Nuevo saldo de {usuario.nombre}: {usuario.saldo}€")


procesar_pago(u1, 30)
# Un UsuarioAdmin también es un Usuario (hereda de él), así que también pasa el check.
procesar_pago(admin, 20)

print("¿UsuarioAdmin es subclase de Usuario?", issubclass(UsuarioAdmin, Usuario))

try:
    procesar_pago("no soy un usuario", 10)
except TypeError as error:
    print(f"Bloqueado antes de tocar ningún saldo: {error}")


# ============================================================================
# 7. CONVENCIÓN DE ATRIBUTOS "PRIVADOS" (_ Y __)
# ============================================================================
seccion("7. Convención de atributos privados (_ y __)")


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial  # "_": convención, no toques esto desde fuera
        self.__pin = "0000"  # "__": name mangling real

    def consultar_saldo(self):
        return self._saldo


cuenta = CuentaBancaria("Marta", 500.0)
# Nada impide leer o modificar '_saldo' directamente: es solo una señal
# para quien lea el código de que es un detalle interno, no una API pública.
print(f"Accediendo a _saldo igualmente: {cuenta._saldo}€")

# '__pin' sí cambia de nombre de verdad: Python lo renombra a '_CuentaBancaria__pin'.
try:
    print(cuenta.__pin)
except AttributeError as error:
    print(f"cuenta.__pin falla: {error}")
print(f"Pero existe como: {cuenta._CuentaBancaria__pin}")

# Ninguna de las dos formas es privacidad real como en otros lenguajes: es
# una convención que Python respeta a medias (name mangling) para evitar
# colisiones de nombres en herencia, no para impedir el acceso.


# ============================================================================
# 8. CLASSMETHOD Y STATICMETHOD
# ============================================================================
seccion("8. classmethod y staticmethod")

# Las facturas de este mes no llegan como argumentos sueltos: llegan como
# filas de un CSV exportado por otro sistema ("F-1002,349.90"). Sin un
# sitio centralizado para convertir ese formato en una Factura, cada
# desarrollador acaba parseando la fila a mano, y es fácil que alguien se
# equivoque separando el número del importe.


class Factura:
    def __init__(self, numero, importe):
        self.numero = numero
        self.importe = importe

    def __str__(self):
        return f"Factura #{self.numero}: {self.importe}€"

    @classmethod
    def desde_fila_csv(cls, fila):
        numero, importe = fila.split(",")
        return cls(numero, float(importe))

    @staticmethod
    def importe_valido(importe):
        return importe > 0


fila_externa = "F-1002,349.90"
factura = Factura.desde_fila_csv(fila_externa)
print(factura)

# @classmethod recibe 'cls' (la propia clase) en vez de 'self' (una
# instancia). Es la forma idiomática de escribir un constructor
# alternativo: Factura.desde_fila_csv(...) siempre construye una Factura
# correctamente, sin repetir la lógica de parseo en cada lugar donde llega
# una fila de este formato.

print(Factura.importe_valido(349.90))
print(Factura.importe_valido(-10))

# @staticmethod no recibe ni 'self' ni 'cls': es una función normal que no
# necesita datos de la instancia ni de la clase, pero que vive dentro de
# Factura porque conceptualmente pertenece ahí (validar un importe es algo
# que gira en torno a una factura, aunque no dependa de ninguna factura en
# concreto). Se llama igual desde la clase o desde una instancia.
print(factura.importe_valido(0))


# ============================================================================
# 9. POLIMORFISMO — MISMO MÉTODO, DISTINTO COMPORTAMIENTO SEGÚN EL OBJETO
# ============================================================================
seccion("9. Polimorfismo — mismo método, distinto comportamiento según el objeto")


# Antipatrón: preguntar el tipo a mano antes de decidir qué hacer.
def resumen_v1(usuario):
    if type(usuario) is UsuarioAdmin:
        return f"[ADMIN] {usuario.nombre} (nivel {usuario.nivel_acceso})"
    else:
        return f"{usuario.nombre} (saldo {usuario.saldo}€)"


print(resumen_v1(u1))
print(resumen_v1(admin))

# Funciona, pero cada tipo nuevo de usuario obliga a añadir una rama más
# aquí. Si mañana aparece UsuarioBaneado y alguien olvida tocar esta
# función, el bug es silencioso: cae en el "else" y muestra algo incorrecto
# sin lanzar ningún error.

# Polimorfismo: el mismo mensaje (str(usuario)) produce un resultado
# distinto según el objeto real, sin que quien llama tenga que preguntar
# nada. Usuario define __str__ y UsuarioAdmin lo sobrescribe (sección 5).
usuarios_variados = [u1, u2, admin]
for usuario in usuarios_variados:
    print(usuario)

# Añadir un tercer tipo de usuario mañana no toca este bucle para nada:
# basta con que ese tipo también implemente __str__.


class ServicioExterno:

    def __init__(self):
        self.saldo = 0.0  

    def depositar(self, cantidad):
            self.saldo += cantidad

    # No hereda de Usuario ni de nada: no comparte ni una línea de código.
    def __str__(self):
        return f"ServicioExterno(cuenta de sistema) {self.saldo}€"


# Duck typing: en Python el polimorfismo no exige un antepasado común como
# en otros lenguajes con interfaces obligatorias. Basta con que el objeto
# tenga el método que se le va a llamar.
for objeto in [u1, admin, ServicioExterno()]:
    objeto.depositar(10) # todos tienen depositar()
    print(objeto.saldo) # todos tienen saldo

# Los otros pilares clásicos de la POO ya han aparecido antes, sin
# nombrarlos: encapsulación (secciones 2 y 7 — agrupar datos y
# comportamiento, y ocultar detalles internos con "_" y "__") y herencia
# (sección 5). El cuarto pilar, abstracción (obligar a las subclases a
# cumplir un contrato), tiene su propio tema dedicado en este repo:
# '16 - ABC (Abstract Base Classes)'.


# ============================================================================
# 10. COMPOSICIÓN VS HERENCIA — CUÁNDO NO HEREDAR
# ============================================================================
seccion("10. Composición vs herencia — cuándo no heredar")

# UsuarioAdmin hereda de Usuario porque un admin ES un usuario (con más
# permisos). Pero ¿qué pasa si el nivel de acceso de alguien puede cambiar
# en caliente (ascender a moderador, degradar a usuario normal)? Con
# herencia eso es imposible: la clase de un objeto ya creado no se puede
# cambiar en tiempo de ejecución.


class Rol:
    def __init__(self, nombre, nivel_acceso):
        self.nombre = nombre
        self.nivel_acceso = nivel_acceso

    def puede_banear(self):
        return self.nivel_acceso >= 5


class UsuarioConRol:
    def __init__(self, nombre, saldo, rol):
        self.nombre = nombre
        self.saldo = saldo
        self.rol = rol  # composición: UsuarioConRol TIENE UN Rol, no ES UN Rol

    def banear(self, objetivo):
        if not self.rol.puede_banear():
            raise PermissionError(f"{self.nombre} no tiene permisos para banear")
        print(f"{self.nombre} ha baneado a {objetivo}")


invitado = UsuarioConRol("Alex", 0.0, Rol("invitado", nivel_acceso=1))
try:
    invitado.banear("troll_99")
except PermissionError as error:
    print(f"Bloqueado: {error}")

# Ascenso en caliente: cambiar el rol del objeto ya creado, sin tocar su clase.
invitado.rol = Rol("moderador", nivel_acceso=5)
invitado.banear("troll_99")

# Con herencia (Usuario -> UsuarioAdmin) esto no tiene solución limpia: no
# se puede "convertir" un Usuario ya creado en UsuarioAdmin sin crear un
# objeto nuevo y copiar todos sus datos. La composición evita ese problema
# porque el rol es solo un atributo más, reemplazable en cualquier momento.
# Regla práctica: hereda cuando la relación es "ES UN" y es fija de por
# vida (un UsuarioAdmin siempre fue y será un Usuario); compón cuando la
# relación es "TIENE UN" y puede cambiar (un rol, una configuración, un
# estado).


seccion("FIN — ya conoces las clases y la POO al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
