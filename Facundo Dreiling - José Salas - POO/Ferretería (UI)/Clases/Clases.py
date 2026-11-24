def Minimizar(texto:str):
    return texto.replace(" ", "").lower().strip()

class Herramienta():

# Init

    def __init__(self, nombre, funcion):
        self.nombre = nombre
        self.funcion = funcion

# Setters

    def SetNombre(self, nombre):
        self.nombre = nombre

    def SetFuncion(self, funcion):
        self.funcion = funcion

# Getters

    def GetNombre(self):
        return self.nombre

    def GetFuncion(self):
        return self.funcion

    def UsarHerramienta(self):

        print(
            f"Usando herramienta: {self.nombre}.\n"
            f"Su función es: {self.funcion}"
        )

class Ferreteria():

# Init

    def __init__ (
            self, 
            nombre:str, 
            direccion:str, 
            inventario:list[Herramienta]
    ):
        self.nombre = nombre
        self.direccion = direccion
        self.inventario = inventario

# Setters

    def SetNombre(self, nombre):
        self.nombre = nombre

    def SetDireccion(self, direccion):
        self.direccion = direccion

# Getters

    def GetNombre(self):
        return self.nombre
    
    def GetDireccion(self):
        return self.direccion
    
    def GetInventario(self):
        return self.inventario

    def AgregarHerramienta(self, herramienta:Herramienta):

        self.inventario.append(herramienta)
        print("Herramienta ya añadida al inventario.")

    def QuitarHerramienta(self, nombre_herramienta:str):

        if not self.inventario:
            print("No hay inventario disponible.")
            pass

        encontrado = False

        for herramienta in self.inventario:

            if Minimizar(nombre_herramienta) == Minimizar(herramienta.nombre):

                encontrado = True

                print(f"Herramienta {herramienta.nombre} removida del inventario.")
                self.inventario.remove(herramienta)
                break

        if not encontrado:
            print(f"No se encontró la herramienta {nombre_herramienta} en el inventario.")

    def MostrarInventario(self):

        if not self.inventario:
            print("No hay inventario disponible.")
            pass

        i = 0

        print("---\n")

        for herramienta in self.inventario:

            i += 1
            print(
                f"Herramieta {i}: {herramienta.nombre}\n"
                f"Función: {herramienta.funcion}\n"
            )

        input("Presione enter para seguir...")

        print("---\n")