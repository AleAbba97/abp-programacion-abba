# ventas.py

ventas = []

def crear_venta(clientes, destinos):
    print("=== Crear Venta ===")
    id_venta = len(ventas) + 1

    if not clientes:
        print("❌ No hay clientes registrados.")
        return
    if not destinos:
        print("❌ No hay destinos registrados.")
        return

    print("Clientes disponibles:")
    for dni, datos in clientes.items():
        print(f"DNI: {dni} | Nombre: {datos['Nombre']} {datos['Apellido']}")

    dni_cliente = input("Ingrese el DNI del cliente: ").strip()
    if dni_cliente not in clientes:
        print("❌ Cliente no encontrado.")
        return
    cliente = clientes[dni_cliente]

    print("Destinos disponibles:")
    for id_destino, datos in destinos.items():
        print(f"ID: {id_destino} | País: {datos['Pais']} | Ciudad: {datos['Ciudad']}")

    try:
        id_destino = int(input("Ingrese el ID del destino: "))
        if id_destino not in destinos:
            print("❌ Destino no encontrado.")
            return
    except ValueError:
        print("❌ ID inválido.")
        return

    destino = destinos[id_destino]

    nueva_venta = {
        'ID': id_venta,
        'Cliente_DNI': dni_cliente,
        'Nombre': cliente['Nombre'],
        'Apellido': cliente['Apellido'],
        'Destino': f"{destino['Ciudad']}, {destino['Pais']}"
    }

    ventas.append(nueva_venta)
    print("✅ Venta registrada con éxito.")

def consultar_ventas():
    print("=== Ventas Registradas ===")
    if not ventas:
        print("No hay ventas registradas.")
    else:
        for venta in ventas:
            print(f"ID: {venta['ID']} | Cliente: {venta['Nombre']} {venta['Apellido']} (DNI: {venta['Cliente_DNI']}) | Destino: {venta['Destino']}")
