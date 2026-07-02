"""
Al IMPORTAR 'factura', su bloque  if __name__ == "__main__"  NO se ejecuta.
Compáralo:  python factura.py   (sí lo ejecuta)  vs  python demo.py (no).
"""
import factura

print("__name__ de factura al importarlo:", factura.__name__)  # -> "factura"
print("Uso su función igualmente:", factura.total(10, 3))
