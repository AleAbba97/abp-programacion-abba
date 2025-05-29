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
from clientes import agregar_cliente, modificar_cliente, eliminar_cliente, ver_clientes

def agregar_destino():
    print("""Nuevo Destino:
    Ciudad:
    Pais:
    Costo base del viaje: 
    """)

def modificar_destino():
    print(">>> Función: Modificando un destino existente...")

def eliminar_destino():
    print(">>> Función: Eliminando un destino...")

def ver_destinos():
    print(">>> Función: Mostrando la lista de destinos...")

def gestionar_ventas():
    print(">>> Ingrese su numero de venta: ")
    print (" Su venta se encuentra: (Activa/Desactiva)")

def consultar_ventas():
    print("Ingrese numero de venta:")
    print("La venta pertenece al cuit: (numero de cuil) y es al destino (destino)")

def boton_arrepentimiento():
    print("Usted posee la posibilidad de reembolsar su viaje, tiene 60 dias habiles para realizarlo.")

def ver_reporte_general():
    print(">>> Función: Generando reporte general...")

def acerca_del_sistema():
    print(">>> Información: SkyRoute v1.0 - Sistema de Gestión de Pasajes.")
    print(">>> Desarrollado por [Tu Nombre/Equipo].")
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
            gestionar_ventas()
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