"""
CONCEPTO 02 · if __name__ == "__main__"
El MISMO fichero puede usarse de dos formas:
  - Ejecutado directamente:   python factura.py   ->  __name__ == "__main__"
  - Importado como módulo:    import factura       ->  __name__ == "factura"

CASO REAL: quieres poder ejecutar el fichero para probarlo rápido,
pero que ese código de prueba NO se ejecute cuando otro fichero lo importe.
"""

def total(precio, cantidad):
    return precio * cantidad

# Esta línea SOLO se ejecuta si lanzas el fichero directamente,
# nunca cuando 'factura' es importado por otro módulo.
if __name__ == "__main__":
    print("Ejecutando como SCRIPT. Prueba:", total(10, 3))
