def mostrar_menu_principal():
    """Muestra el menú principal del sistema."""
    menu = """
Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes

1. Gestionar Clientes
2. Gestionar Destinos
3. Gestionar Ventas
4. Consultar Ventas
5. Botón de Arrepentimiento
6. Ver Reporte General
7. Acerca del Sistema
8. Salir

"""
    print(menu)

def mostrar_submenu_clientes():
    """Gestión de clientes."""
    submenu = """
--- Gestionar Clientes ---
1. Agregar Cliente
2. Modificar Cliente
3. Eliminar Cliente
4. Ver Clientes
5. Volver al Menú Principal
-----------------------------------
"""
    print(submenu)

def mostrar_submenu_destinos():
    """Gestión de destinos."""
    submenu = """
--- Gestionar Destinos ---
1. Agregar Destino
2. Modificar Destino
3. Eliminar Destino
4. Ver Destinos
5. Volver al Menú Principal
-----------------------------------
"""
    print (submenu)
from clientes import agregar_cliente, modificar_cliente, eliminar_cliente, ver_clientes, clientes
from destinos import agregar_destino, modificar_destino, eliminar_destino, ver_destinos, destinos
from ventas import crear_venta, consultar_ventas, ventas

def boton_arrepentimiento():
    print("Usted posee la posibilidad de reembolsar su viaje, tiene 60 días hábiles para realizarlo.")  
    if not ventas:
        print("❌ No hay ventas registradas.")
        return
    print("Las ventas realizadas son:")
    for venta in ventas:
        print(f"ID: {venta['ID']} | Cliente: {venta['Nombre']} {venta['Apellido']} (DNI: {venta['Cliente_DNI']}) | Destino: {venta['Destino']}")
        id_a_borrar = int(input("Ingrese el ID de la venta que desea anular (o 0 para cancelar): "))
    if id_a_borrar == 0:
        print("❎ Operación cancelada.")
        return
    for venta in ventas:
        if venta['ID'] == id_a_borrar:
            confirmacion = input(f"¿Está seguro de anular la venta de {venta['Nombre']} a {venta['Destino']}? (s/n): ").strip().lower()
            if confirmacion == 's':
                ventas.remove(venta)
                print("✅ Venta anulada con éxito.")
            else:
                print("❎ Anulación cancelada.")
            return
    print("❌ No se encontró una venta con ese ID.")
def ver_reporte_general():
    print(">>> Función: Generando reporte general...")

def acerca_del_sistema():
    print(">>> Información: SkyRoute v1.0 - Sistema de Gestión de Pasajes.")
    print(">>> Desarrollado por Buen Codigo.")
    print(">>> ¡Gracias por usar nuestro sistema!")

def Gestiones():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Ingrese una opción del menú principal: ")

        if opcion_principal == '1':
            while True:
                mostrar_submenu_clientes()
                opcion_clientes = input("Ingrese una opción del submenú de clientes: ")
                if opcion_clientes == '1':
                    agregar_cliente()
                elif opcion_clientes == '2':
                    modificar_cliente()
                elif opcion_clientes == '3':
                    eliminar_cliente()
                elif opcion_clientes == '4':
                    ver_clientes()
                elif opcion_clientes == '5':
                    print("Volviendo al menú principal...")
                    break  
                else:  
                    print("Opción inválida. Por favor, intente de nuevo.")

        elif opcion_principal == '2':
            while True:
                mostrar_submenu_destinos()
                opcion_destinos = input("Ingrese una opción del submenú de destinos: ")
                if opcion_destinos == '1':
                    agregar_destino()
                elif opcion_destinos == '2':
                    modificar_destino()
                elif opcion_destinos == '3':
                    eliminar_destino()
                elif opcion_destinos == '4':
                    ver_destinos()
                elif opcion_destinos == '5':
                    print("Volviendo al menú principal...")
                    break 
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")
        elif opcion_principal == '3':
            crear_venta(clientes, destinos)
        elif opcion_principal == '4':
            consultar_ventas()
        elif opcion_principal == '5':
            boton_arrepentimiento()
        elif opcion_principal == '6':
            ver_reporte_general()
        elif opcion_principal == '7':
            acerca_del_sistema()
        elif opcion_principal == '8':
            print("¡Gracias por usar SkyRoute! Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
 
        if opcion_principal != '8': 
            input("\nPresione Enter para continuar")
            print("\n" * 2) 
Gestiones()