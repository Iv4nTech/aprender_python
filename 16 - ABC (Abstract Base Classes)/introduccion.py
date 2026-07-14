"""
================================================================================
 ABC — ABSTRACT BASE CLASSES EN PYTHON 3.14
 Ejecutar: python3 introduccion.py
================================================================================
"""

from abc import ABC, abstractmethod
from collections.abc import Sequence, Mapping, Iterable, Callable


def seccion(titulo: str) -> None:
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)


# ============================================================================
# 1. EL PROBLEMA SIN ABC
# ============================================================================
seccion("1. El problema sin ABC")

# Caso real: un sistema de notificaciones con varios canales (email, SMS,
# push). Cada canal debe implementar enviar(). Sin un contrato explícito,
# nada obliga a hacerlo.
class NotificadorSinContrato:
    def enviar(self, mensaje):
        pass  # no hace nada: ni error, ni aviso

class NotificadorEmail(NotificadorSinContrato):
    def enviar(self, mensaje):
        print(f"  [EMAIL] {mensaje}")

class NotificadorSMS(NotificadorSinContrato):
    def enviar(self, mensaje):
        print(f"  [SMS] {mensaje}")

class NotificadorPush(NotificadorSinContrato):
    pass  # el desarrollador se olvidó de implementar enviar()

canales = [NotificadorEmail(), NotificadorSMS(), NotificadorPush()]
for canal in canales:
    canal.enviar("Tu pedido #4821 ha sido enviado")

# El canal Push no lanza ningún error: simplemente no envía nada.
# En producción esto significa que los usuarios dejan de recibir avisos
# push y NADIE se entera hasta que llegan quejas. El bug está ahí desde
# el día 1, pero solo se descubre cuando ya ha hecho daño real.
# Esto es justo lo que ABC va a resolver: fallar pronto, al instanciar,
# no en silencio, meses después, en producción.


# ============================================================================
# 2. PRIMERA ABC: @abstractmethod
# ============================================================================
seccion("2. Primera ABC: @abstractmethod")

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        ...

# Intentar instanciar la ABC directamente falla.
try:
    Notificador()
except TypeError as e:
    print("Notificador() ->", type(e).__name__, "->", e)

class NotificadorEmail(Notificador):
    def enviar(self, mensaje):
        print(f"  [EMAIL] {mensaje}")

class NotificadorSMS(Notificador):
    def enviar(self, mensaje):
        print(f"  [SMS] {mensaje}")

NotificadorEmail().enviar("Factura de julio disponible")
NotificadorSMS().enviar("Tu código de verificación es 8271")

# Ahora reproducimos el mismo error del punto 1: un canal Push sin enviar().
class NotificadorPush(Notificador):
    pass

try:
    NotificadorPush()
except TypeError as e:
    print("NotificadorPush() ->", type(e).__name__, "->", e)

# LA DIFERENCIA CLAVE: este error salta al INSTANCIAR la clase, es decir,
# en el arranque de la app o en los tests de CI. Ya no llega a producción.


# ============================================================================
# 3. @abstractmethod CON MÚLTIPLES MÉTODOS
# ============================================================================
seccion("3. Múltiples métodos abstractos")

# Caso real: conectores de almacenamiento en la nube. Cada proveedor debe
# saber subir() Y descargar() archivos; si falta uno, el conector es inútil
# a medias y puede provocar pérdida de datos si nadie se da cuenta a tiempo.
class AlmacenamientoCloud(ABC):
    @abstractmethod
    def subir(self, ruta_local, ruta_remota):
        ...

    @abstractmethod
    def descargar(self, ruta_remota, ruta_local):
        ...

class AlmacenamientoS3(AlmacenamientoCloud):
    def subir(self, ruta_local, ruta_remota):
        print(f"  S3: subiendo {ruta_local} -> s3://{ruta_remota}")

    def descargar(self, ruta_remota, ruta_local):
        print(f"  S3: descargando s3://{ruta_remota} -> {ruta_local}")

class AlmacenamientoAzure(AlmacenamientoCloud):
    def subir(self, ruta_local, ruta_remota):
        print(f"  Azure: subiendo {ruta_local} -> blob://{ruta_remota}")

    def descargar(self, ruta_remota, ruta_local):
        print(f"  Azure: descargando blob://{ruta_remota} -> {ruta_local}")

s3 = AlmacenamientoS3()
s3.subir("backup.zip", "backups/backup.zip")
s3.descargar("backups/backup.zip", "restaurado.zip")

azure = AlmacenamientoAzure()
azure.subir("backup.zip", "backups/backup.zip")

# Un conector a medio implementar (falta descargar) no se puede instanciar.
# Sin ABC, este bug solo aparecería el día que alguien necesite RESTAURAR
# un backup y descubra que no puede... cuando ya es una emergencia.
class AlmacenamientoFTP(AlmacenamientoCloud):
    def subir(self, ruta_local, ruta_remota):
        print(f"  FTP: subiendo {ruta_local} -> {ruta_remota}")

try:
    AlmacenamientoFTP()
except TypeError as e:
    print("AlmacenamientoFTP() ->", type(e).__name__, "->", e)


# ============================================================================
# 4. PROPIEDADES ABSTRACTAS CON @property
# ============================================================================
seccion("4. Propiedades abstractas")

# Caso real: planes de suscripción de una app SaaS. Cada plan define un
# límite de proyectos, y ese límite se consulta constantemente en el
# código (paywalls, alertas, validaciones) como si fuera un simple dato,
# no como una llamada a método.
class PlanSuscripcion(ABC):
    @property
    @abstractmethod
    def limite_proyectos(self):
        ...

class PlanBasico(PlanSuscripcion):
    @property
    def limite_proyectos(self):
        return 3

class PlanPro(PlanSuscripcion):
    @property
    def limite_proyectos(self):
        return 50

def puede_crear_proyecto(plan, proyectos_actuales):
    # Se lee como una propiedad, SIN paréntesis: plan.limite_proyectos.
    return proyectos_actuales < plan.limite_proyectos

basico = PlanBasico()
pro = PlanPro()
print("Plan básico, límite:", basico.limite_proyectos)
print("¿Puede crear el 4º proyecto con plan básico?", puede_crear_proyecto(basico, 3))
print("¿Puede crear el 4º proyecto con plan pro?", puede_crear_proyecto(pro, 3))

# Si limite_proyectos fuera un método normal, cada subclase podría "olvidar"
# ponerlo (@abstractmethod) o el equipo podría mezclar attributos sueltos
# (self.limite = 3) con propiedades, generando inconsistencia en la API
# pública. La propiedad abstracta OBLIGA a que todas las subclases expongan
# el dato con la misma interfaz.


# ============================================================================
# 5. isinstance() Y issubclass() CON ABCs
# ============================================================================
seccion("5. isinstance() y issubclass()")

email = NotificadorEmail()
print("isinstance(email, Notificador):", isinstance(email, Notificador))
print("issubclass(NotificadorEmail, Notificador):", issubclass(NotificadorEmail, Notificador))

# Caso real: un GestorNotificaciones que recibe canales desde config (o un
# plugin externo) y debe rechazar cualquier objeto que no cumpla el
# contrato ANTES de intentar usarlo, no al primer fallo en producción.
class GestorNotificaciones:
    def __init__(self):
        self._canales = []

    def registrar_canal(self, canal):
        if not isinstance(canal, Notificador):
            raise TypeError(f"{canal!r} no es un Notificador válido")
        self._canales.append(canal)

    def difundir(self, mensaje):
        for canal in self._canales:
            canal.enviar(mensaje)

gestor = GestorNotificaciones()
gestor.registrar_canal(NotificadorEmail())
gestor.registrar_canal(NotificadorSMS())
gestor.difundir("Mantenimiento programado esta noche")

try:
    gestor.registrar_canal("no soy un canal")
except TypeError as e:
    print("registrar_canal('texto') ->", type(e).__name__, "->", e)

# La utilidad real: si isinstance(x, Notificador) da True, tienes la
# GARANTÍA de que x.enviar() existe y funciona, porque si no lo
# implementara no se habría podido instanciar (sección 2). Con una clase
# normal, isinstance solo te dice el tipo; con una ABC, además te da la
# garantía del contrato. Por eso este patrón —validar con isinstance antes
# de usar un objeto externo— es tan común en sistemas de plugins, colas de
# eventos o cualquier API que reciba objetos de fuera.


# ============================================================================
# 6. __subclasshook__: REGISTRAR CLASES EXTERNAS
# ============================================================================
seccion("6. register(): clases externas sin herencia")

# Caso real: integras el SDK de Slack de un tercero. No puedes tocar su
# código (viene de una librería instalada con pip), pero ya tiene un
# método enviar() con la firma correcta. Quieres tratarlo como un
# Notificador más, sin reescribir el SDK.
class SlackSDK:
    """Simula una clase de una librería externa que no conoce tu ABC."""
    def enviar(self, mensaje):
        print(f"  [SLACK] {mensaje}")

Notificador.register(SlackSDK)

slack = SlackSDK()
print("isinstance(slack, Notificador):", isinstance(slack, Notificador))
gestor.registrar_canal(slack)          # el gestor lo acepta sin problema
gestor.difundir("Nuevo despliegue en producción")

# ADVERTENCIA: register() solo marca el tipo, NO obliga a implementar nada.
# Si SlackSDK no tuviera enviar(), isinstance() diría True igualmente y el
# error solo aparecería al llamar al método (vuelve el problema del punto 1,
# pero ahora escondido detrás de un isinstance que decía que todo iba bien).
# Úsalo solo cuando confíes en que la clase externa cumple el contrato.


# ============================================================================
# 7. ABCs DE LA LIBRERÍA ESTÁNDAR (collections.abc)
# ============================================================================
seccion("7. ABCs de collections.abc")

print("isinstance([1,2,3], Sequence):", isinstance([1, 2, 3], Sequence))
print("isinstance({}, Mapping):", isinstance({}, Mapping))
print("isinstance((1,2), Iterable):", isinstance((1, 2), Iterable))
print("isinstance(len, Callable):", isinstance(len, Callable))

# Caso real: un historial de pedidos que quieres poder recorrer con for,
# indexar con [], hacer len(), y usar "in" — es decir, que se comporte
# como una secuencia nativa de Python, sin reinventar todos esos métodos.
# Sequence exige solo __len__ y __getitem__: el resto (index, count,
# __contains__, __iter__, __reversed__, slicing) llega GRATIS como mixin.
class HistorialPedidos(Sequence):
    def __init__(self):
        self._pedidos = []

    def registrar(self, pedido):
        self._pedidos.append(pedido)

    def __len__(self):
        return len(self._pedidos)

    def __getitem__(self, indice):
        return self._pedidos[indice]

historial = HistorialPedidos()
historial.registrar("Pedido #101")
historial.registrar("Pedido #102")
historial.registrar("Pedido #103")

print("isinstance(historial, Sequence):", isinstance(historial, Sequence))
print("len(historial):", len(historial))
print("historial[0]:", historial[0])
print("'Pedido #102' in historial:", "Pedido #102" in historial)   # __contains__ gratis
for pedido in historial:                                            # __iter__ gratis
    print("  ", pedido)

# Esto demuestra por qué las ABCs de stdlib son contratos implícitos MUY
# usados: cualquier objeto tuyo que implemente el mínimo exigido se vuelve
# compatible con todo el ecosistema de Python (bucles for, unpacking,
# funciones que esperan una Sequence, etc.) sin escribir código extra.


# ============================================================================
# 8. MÉTODOS CONCRETOS EN UNA ABC: PATRÓN TEMPLATE METHOD
# ============================================================================
seccion("8. Métodos concretos: Template Method")

# Caso real: un pipeline ETL (Extract-Transform-Load), muy habitual en
# ingeniería de datos. El ORDEN de los pasos es siempre el mismo
# (extraer -> transformar -> cargar), pero el CONTENIDO de cada paso
# depende de la fuente de datos concreta.
class PipelineETL(ABC):
    # Método concreto: ya viene implementado, las subclases lo heredan gratis.
    def ejecutar(self):
        datos_crudos = self.extraer()
        datos_limpios = self.transformar(datos_crudos)
        self.cargar(datos_limpios)

    @abstractmethod
    def extraer(self):
        ...

    @abstractmethod
    def transformar(self, datos):
        ...

    @abstractmethod
    def cargar(self, datos):
        ...

class PipelineVentasCSV(PipelineETL):
    def extraer(self):
        print("  Leyendo ventas.csv...")
        return [100, 250, 75]

    def transformar(self, datos):
        print("  Aplicando IVA del 21%...")
        return [round(v * 1.21, 2) for v in datos]

    def cargar(self, datos):
        print(f"  Insertando en tabla ventas: {datos}")

class PipelineUsuariosAPI(PipelineETL):
    def extraer(self):
        print("  Llamando a la API de usuarios...")
        return ["ana@mail.com", "LUIS@MAIL.COM "]

    def transformar(self, datos):
        print("  Normalizando emails...")
        return [e.strip().lower() for e in datos]

    def cargar(self, datos):
        print(f"  Insertando en tabla usuarios: {datos}")

PipelineVentasCSV().ejecutar()
PipelineUsuariosAPI().ejecutar()

# Patrón Template Method: la ABC define el ALGORITMO (ejecutar), cada
# pipeline concreto solo rellena los HUECOS (extraer/transformar/cargar).
# Ventaja real: si mañana el ETL necesita, por ejemplo, medir el tiempo
# de cada ejecución o enviar una alerta si falla, lo añades UNA vez en
# ejecutar() y todos los pipelines existentes lo heredan sin tocarlos.


# ============================================================================
# 9. TABLA COMPARATIVA FINAL
# ============================================================================
seccion("9. ABC vs herencia normal vs duck typing vs Protocol")

# ABC (abc.ABC):
#   - Contrato EXPLÍCITO y forzado: falla al instanciar si falta un método.
#   - Requiere herencia (o register() para relajar eso).
#   - Ideal cuando el contrato es parte del diseño: canales de notificación,
#     conectores de almacenamiento, drivers de base de datos, plugins.
#
# Herencia normal (sin abstractmethod):
#   - Ningún contrato: el error aparece en tiempo de ejecución, tarde,
#     como el NotificadorPush "mudo" de la sección 1.
#   - Solo sirve si controlas todo el código y confías en no olvidarte nada.
#
# Duck typing ("si camina como pato y grazna como pato..."):
#   - Sin ningún contrato ni chequeo: simplemente se usa el método y ya.
#   - Rápido y flexible, pero los errores se descubren muy tarde.
#
# typing.Protocol (structural typing):
#   - Contrato IMPLÍCITO verificado por el TYPE CHECKER (mypy), no en runtime.
#   - No requiere herencia ni registro: si el objeto tiene los métodos, vale.
#   - Ideal para librerías donde no controlas las clases de quien las usa.
#
# Regla práctica:
#   - Diseñas una jerarquía propia con contrato fuerte  -> ABC.
#   - Quieres flexibilidad total y controlas el contexto -> duck typing.
#   - Quieres contrato verificado por el linter, sin herencia -> Protocol.


seccion("FIN — ya conoces las ABC al 100%")
print("Siguiente paso: abre 'ejercicios.py' y ponte a prueba.")
