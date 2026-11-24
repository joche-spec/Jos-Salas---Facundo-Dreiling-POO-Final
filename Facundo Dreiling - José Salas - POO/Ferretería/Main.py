from Clases.Clases import *

ferreteria = None

def MenuPrincipal():
    while True:
        try:

            eleccion = int(input(
                "Ingrese una opción:\n"
                "1) Crear ferretería\n"
                "0) Salir\n"
                ">>> "
            ))

            if eleccion == 1:
                CrearFerreteria()

            elif eleccion == 0:
                return

            else:
                print("Elección fuera de rango.")

        except ValueError:
            print("Intente de nuevo")

def CrearFerreteria():
    global ferreteria

    print("Crear Ferretería")

    print("---\n")

    while True:
        try:

            nombre = input("Ingrese el nombre de la ferretería: ")
            direccion = input("Ingrese la dirección de la ferretería: ")

            ferreteria = Ferreteria(nombre, direccion, [])

            print(
                "¡Ferretería lista!\n"
                f"Nombre: {ferreteria.nombre}\n"
                f"Dirección: {ferreteria.direccion}"
            )

            AdministrarFerreteria()

        except ValueError:
            print("Intente de nuevo")

def AdministrarFerreteria():
    global ferreteria
    
    print("Crear Ferretería/Administrar Ferretería")

    print("---\n")

    while True:
        try:

            eleccion = int(input(
                "Administrar ferretería:\n"
                "1) Ver nombre y dirección\n"
                "2) Ver inventario\n"
                "3) Gestionar nombre/dirección\n"
                "4) Gestionar inventario\n"
                "0) Volver\n"
                ">>> "
            ))

            if eleccion == 1:

                print(
                    f"Nombre: {ferreteria.GetNombre()}\n"
                    f"Dirección: {ferreteria.GetDireccion()}\n"
                )

                input("Presione enter para seguir...")

                print("---\n")

            elif eleccion == 2:
                ferreteria.MostrarInventario()

            elif eleccion == 3:

                print("Crear Ferretería/Administrar Ferretería/Gestionar nombre y dirección")

                print("---\n")

                nombre = input("Ingrese el nombre de la ferretería: ")
                direccion = input("Ingrese la dirección de la ferretería: ")

                ferreteria.SetNombre(nombre)
                ferreteria.SetDireccion(direccion)

            elif eleccion == 4:
                AdministrarInventario()

            elif eleccion == 0:
                MenuPrincipal()

            else:
                print("Elección fuera de rango.")

        except ValueError:
            print("Intente de nuevo")

def AdministrarInventario():
    print("Crear Ferretería/Administrar Ferretería/Gestionar inventario")

    print("---\n")

    while True:
        try:

            eleccion = int(input(
                "Gestionar inventario:\n"
                "1) Agregar herramienta\n"
                "2) Quitar herramienta\n"
                "0) Volver\n"
                ">>> "
            ))

            if eleccion == 1:
                AgregarHerramienta()

            if eleccion == 2:
                QuitarHerramienta()

            elif eleccion == 0:
                AdministrarFerreteria()

            else: 
                print("Elección fuera de rango.")

        except ValueError:
            print("Intente de nuevo")

def AgregarHerramienta():
    global ferreteria
    
    print("Crear Ferretería/Administrar Ferretería/Gestionar inventario/Agregar herramienta")

    print("---\n")

    nombre = input("Ingrese el nombre de la herramienta: ")
    funcion = input("Ingrese la función de la herramienta: ")

    herramienta = Herramienta(nombre, funcion)

    ferreteria.AgregarHerramienta(herramienta)

    AdministrarInventario()

def QuitarHerramienta():
    global ferreteria
    
    print("Crear Ferretería/Administrar Ferretería/Gestionar inventario/Quitar herramienta")

    print("---\n")

    nombre = input("Ingrese el nombre de la herramienta: ")

    ferreteria.QuitarHerramienta(nombre)

    AdministrarInventario()

MenuPrincipal()