"""
Ejercicio 10 - Pipeline async-style con generadores (productor/consumidor)
===========================================================================
Implementa un sistema de procesamiento de logs en pipeline con 4 etapas:

1. `producir_logs(fichero)`      → genera líneas del fichero
2. `parsear_logs(lineas)`        → parsea cada línea al formato:
                                   {"timestamp": str, "nivel": str, "mensaje": str}
                                   Formato de línea: "2024-01-15 ERROR mensaje aquí"
                                   Descarta líneas que no encajen.
3. `filtrar_nivel(logs, nivel)`  → solo pasa logs del nivel indicado (ej. "ERROR")
4. `formatear_salida(logs)`      → produce strings listos para imprimir:
                                   "[2024-01-15] ERROR: mensaje aquí"

Encadéna las 4 etapas en una función `pipeline_logs(fichero, nivel)`.

Caso real: procesamiento de logs de producción en tiempo real,
           monitorización de errores, alertas automáticas.
           Este patrón escala a millones de líneas sin problema de memoria.
"""

# Tu código aquí

def producir_logs(fichero):
    with open(fichero, "r") as f:
        for linea in f:
            yield linea.strip()

def parsear_logs(lineas):
    for linea in lineas:
        partes = linea.split(" ", 2)
        if len(partes) == 3:
            timestamp, nivel, mensaje = partes
            yield {"timestamp": timestamp, "nivel": nivel, "mensaje": mensaje}

def filtrar_nivel(logs, nivel):
    for log in logs:
        if log["nivel"] == nivel:
            yield log

def formatear_salida(logs):
    for log in logs:
        yield f"[{log['timestamp']}] {log['nivel']}: {log['mensaje']}"

def pipeline_logs(fichero, nivel):
    lineas = producir_logs(fichero)
    logs_parseados = parsear_logs(lineas)
    logs_filtrados = filtrar_nivel(logs_parseados, nivel)
    return formatear_salida(logs_filtrados)
            

# --- Prueba ---
if __name__ == "__main__":
    import tempfile, os

    contenido = """\
2024-01-15 INFO Servidor arrancado
2024-01-15 ERROR Conexión rechazada por timeout
2024-01-15 WARNING Uso de CPU al 85%
línea malformada sin formato
2024-01-15 ERROR Base de datos no responde
2024-01-15 INFO Petición procesada en 120ms
2024-01-15 ERROR Certificado SSL caducado
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
        f.write(contenido)
        ruta = f.name

    print("=== Errores del sistema ===")
    for linea in pipeline_logs(ruta, "ERROR"):
        print(linea)

    os.unlink(ruta)
