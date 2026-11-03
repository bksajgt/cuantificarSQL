from pathlib import Path

# Usa automáticamente la carpeta donde está este script
carpeta = Path(__file__).resolve().parent

origen = carpeta / "frutas.sql"
destino = carpeta / "frutas_compatible.sql"

buscar = b"_uca1400_ai_ci"
reemplazar = b"_general_ci"

tamano_bloque = 1024 * 1024
pendiente = b""
cambios = 0

if not origen.exists():
    print("No se encontró el archivo:")
    print(origen)
    input("Presiona Enter para cerrar...")
    raise SystemExit

with open(origen, "rb") as entrada, open(destino, "wb") as salida:
    while True:
        bloque = entrada.read(tamano_bloque)

        if not bloque:
            break

        datos = pendiente + bloque

        limite = max(0, len(datos) - len(buscar) + 1)

        procesar = datos[:limite]
        pendiente = datos[limite:]

        cambios += procesar.count(buscar)
        salida.write(procesar.replace(buscar, reemplazar))

    cambios += pendiente.count(buscar)
    salida.write(pendiente.replace(buscar, reemplazar))

print("Proceso terminado.")
print(f"Reemplazos realizados: {cambios}")
print(f"Archivo creado: {destino}")

input("Presiona Enter para cerrar...")