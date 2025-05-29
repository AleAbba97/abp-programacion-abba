clientes = {}

def agregar_cliente():
    apellido = input ("Ingrese Apellido: ")
    nombre = input("Ingrese Nombre o Razón social: ")
    dni = input("Ingrese dni: ")
    email = input("Ingrese email: ")
    telefono = int(input("Ingrese su telefono: "))
    if dni in clientes:
        print("❌ Ya existe un cliente con ese  DNI")
    else:
        clientes[dni] = {
            'Apellido': apellido, 
            'Nombre': nombre, 
            'Email': email, 
            'Telefono': telefono
        }
        print("✅ Cliente agregado con éxito.")    

def modificar_cliente():
    print("=== Modificar cliente ===")
    dni = input("Ingrese el DNI del cliente a modificar: ").strip()

    if dni in clientes:
        cliente = clientes[dni]
        print(f"Cliente actual: {cliente}")
        
        nuevo_apellido = input("Nuevo apellido (dejar vacío para mantener): ").strip()
        nuevo_nombre = input("Nuevo nombre o razón social (dejar vacío para mantener): ").strip()
        nuevo_email = input("Nuevo email (dejar vacío para mantener): ").strip()
        nuevo_telefono = input("Nuevo teléfono (dejar vacío para mantener): ").strip()

        if nuevo_apellido:
            cliente['Apellido'] = nuevo_apellido
        if nuevo_nombre:
            cliente['Nombre'] = nuevo_nombre
        if nuevo_email:
            cliente['Email'] = nuevo_email
        if nuevo_telefono:
            cliente['Telefono'] = nuevo_telefono
        print("✅ Cliente modificado con éxito.")
    else:
        print("❌ No se encontró un cliente con ese DNI.")

def eliminar_cliente():
    print("=== Eliminar cliente ===")
    dni = input("Ingrese el DNI del cliente a eliminar: ").strip()

    if dni in clientes:
        confirmacion = input(f"¿Está seguro de eliminar a {clientes[dni]['Nombre']} {clientes[dni]['Apellido']}? (s/n): ").lower()
        if confirmacion == 's':
            del clientes[dni]
            print("✅ Cliente eliminado.")
        else:
            print("❎ Operación cancelada.")
    else:
        print("❌ No se encontró un cliente con ese DNI.")

def ver_clientes():
    print("=== Lista de Clientes ===")
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for dni, datos in clientes.items():
            apellido = datos.get('Apellido', '[Sin Apellido]')
            nombre = datos.get('Nombre', '[Sin Nombre]')
            email = datos.get('Email', '[Sin Email]')
            telefono = datos.get('Telefono', '[Sin Teléfono]')
            print(f"DNI: {dni} | Apellido: {apellido} | Nombre: {nombre} | Email: {email} | Teléfono: {telefono}")