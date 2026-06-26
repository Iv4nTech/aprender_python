"""
CONCEPTO 09 · Imports RELATIVOS dentro de un paquete
El punto significa "desde aquí mismo":
    from . import algo        -> hermano (mismo paquete)
    from .modulo import X     -> de un módulo hermano
    from ..utils import Y     -> SUBIR un nivel (paquete padre)

CASO REAL: módulos profundos que necesitan utilidades del paquete padre,
sin escribir la ruta absoluta completa (más fácil de mover/renombrar).

⚠️ OJO: los imports relativos SOLO funcionan si el fichero se ejecuta
COMO PARTE DEL PAQUETE (importado), no lanzando el fichero suelto.
Por eso este se prueba desde demo.py, no con 'python facturacion.py'.
"""
from ..utils import formatear_precio   # sube a 'proyecto' y entra en utils


def factura(importe):
    return f"Factura: {formatear_precio(importe)}"
