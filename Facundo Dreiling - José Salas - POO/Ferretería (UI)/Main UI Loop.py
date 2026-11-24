# Imports

from esptk.esptk import *

ui_visible = []

def mostrar_ui():

    if not ui_visible:
        return

    for elemento_ui in ui_visible:
        mostrar(elemento_ui)

def esconder_ui_visible():

    if not ui_visible:
        return

    for elemento_ui in ui_visible:
        esconder(elemento_ui)

    ui_visible.clear()

# Ventana

ventana_principal = crear_ventana(
    ancho=600, 
    alto=400, 
    titulo="Ferretería"
)

# Títulos

titulo_principal = crear_texto(
    contenedor=ventana_principal, 
    texto="Ferretería UI",
    tamanio=24,
    estilo="Negrita",
    mostrar=True
)

crear_ferreteria_titulo = crear_texto(
    contenedor=ventana_principal, 
    texto="Crear ferretería:",
    tamanio=24,
    estilo="Negrita",
    mostrar=True
)

# Menus

def menu_principal():
    esconder_ui_visible()

    boton_1 = crear_boton(
        ventana_principal,
        texto="Crear ferretería",
        comando=crear_ferreteria
    )

    boton_1.comand = crear_ferreteria

    boton_2 = crear_boton(
        ventana_principal,
        texto="Salir",
        comando=lambda: cerrar(ventana_principal)
    )

    ui_visible.append(titulo_principal)
    ui_visible.append(boton_1)
    ui_visible.append(boton_2) 

    mostrar_ui()

def crear_ferreteria():
    esconder_ui_visible()

    contenedor_temporal = crear_frame(
        contenedor=ventana_principal,
        mostrar=True
    )

    campo_1 = crear_entrada(
        contenedor=contenedor_temporal,
        mostrar=True
    )

    campo_2 = crear_entrada(
        contenedor=contenedor_temporal,
        mostrar=True
    )

    boton_volver = crear_boton(
        contenedor=contenedor_temporal,
        texto="Volver",
        comando=lambda: menu_principal(),
    )

    ui_visible.append(crear_ferreteria_titulo)
    ui_visible.append(contenedor_temporal)
    ui_visible.append(campo_1)
    ui_visible.append(campo_2)
    ui_visible.append(boton_volver)

    mostrar_ui()

menu_principal()
ejecutar(ventana_principal)