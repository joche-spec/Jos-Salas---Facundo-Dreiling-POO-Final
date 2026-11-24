import tkinter as tk

# =========================
# Diccionarios base
# =========================

COLORES = {
    "verde": "green",
    "verdeclaro": "light green",
    "rojo": "red",
    "azul": "blue",
    "amarillo": "yellow",
    "negro": "black",
    "blanco": "white",
    "gris": "gray",
    "grisclaro": "light gray",
    "rosado": "pink",
    "naranja": "orange",
    "violeta": "violet",
    "purpura": "purple",
    "celeste": "sky blue"
}

ESTILOS_FUENTE = {
    "normal": "normal",
    "negrita": "bold",
    "cursiva": "italic",
    "negritacursiva": "bold italic"
}

LADOS = {
    "centro": "top",
    "arriba": "top",
    "abajo": "bottom",
    "izquierda": "left",
    "derecha": "right"
}

# =========================
# Utilidades internas
# =========================

def normalizar(texto):
    return str(texto).lower().replace(" ", "").strip()

def obtener_color(color):
    color = normalizar(color)
    return COLORES.get(color, color)

def aplicar_pack(widget, mostrar, **pack_kwargs):
    if mostrar:
        widget.pack(**pack_kwargs)

def construir_fuente(fuente, tamanio, estilo):
    fuente = fuente or "Arial"
    estilo = ESTILOS_FUENTE.get(normalizar(estilo), "normal")

    if tamanio > 0:
        return (fuente, tamanio, estilo)
    return (fuente, 10, estilo)

def traducir_kwargs(kwargs):
    mapa = {
        "texto": "text",
        "color_fondo": "bg",
        "color_texto": "fg",
        "ancho": "width",
        "alto": "height"
    }

    resultado = {}

    for k, v in kwargs.items():
        k_norm = normalizar(k)
        k_real = mapa.get(k_norm, k)

        if "color" in k_norm:
            v = obtener_color(v)

        resultado[k_real] = v

    return resultado

# =========================
# Ventana
# =========================

def crear_ventana(ancho=0, alto=0, titulo="", color_fondo=""):
    v = tk.Tk()

    if ancho > 0 and alto > 0:
        v.geometry(f"{ancho}x{alto}")

    if titulo:
        v.title(titulo)

    if color_fondo:
        v.configure(bg=obtener_color(color_fondo))

    return v

def ejecutar(ventana):
    ventana.mainloop()

def cerrar(ventana):
    ventana.destroy()

# =========================
# Widgets base
# =========================

def crear_texto(contenedor, texto="", fuente="", tamanio=0, estilo="normal", mostrar=False, **kwargs):
    config = traducir_kwargs(kwargs)

    lbl = tk.Label(contenedor, text=texto, **config)
    lbl.configure(font=construir_fuente(fuente, tamanio, estilo))

    aplicar_pack(lbl, mostrar)
    return lbl

def crear_boton(contenedor, texto="", comando=None, args=None, fuente="", tamanio=0, estilo="normal", mostrar=False, **kwargs):
    config = traducir_kwargs(kwargs)

    if comando:
        if args:
            config["command"] = lambda: comando(*args)
        else:
            config["command"] = comando

    btn = tk.Button(contenedor, text=texto, **config)
    btn.configure(font=construir_fuente(fuente, tamanio, estilo))

    aplicar_pack(btn, mostrar)
    return btn

def crear_entrada(contenedor, mostrar=False, lado="centro", **kwargs):
    config = traducir_kwargs(kwargs)

    entry = tk.Entry(contenedor, **config)

    lado_real = LADOS.get(normalizar(lado), "top")
    aplicar_pack(entry, mostrar, side=lado_real)

    return entry

def crear_frame(contenedor, mostrar=False, **kwargs):
    config = traducir_kwargs(kwargs)
    frame = tk.Frame(contenedor, **config)

    aplicar_pack(frame, mostrar)
    return frame

def crear_canvas(contenedor, mostrar=False, **kwargs):
    config = traducir_kwargs(kwargs)
    canvas = tk.Canvas(contenedor, **config)

    aplicar_pack(canvas, mostrar)
    return canvas

def crear_check(contenedor, variable=None, mostrar=False, **kwargs):
    config = traducir_kwargs(kwargs)

    chk = tk.Checkbutton(contenedor, variable=variable, **config)

    aplicar_pack(chk, mostrar)
    return chk

def crear_menu_opciones(contenedor, variable, opciones, mostrar=False, **kwargs):
    menu = tk.OptionMenu(contenedor, variable, *opciones)

    aplicar_pack(menu, mostrar)
    return menu

# =========================
# Imagen
# =========================

def crear_imagen(contenedor, ruta, mostrar=False, **kwargs):
    config = traducir_kwargs(kwargs)

    try:
        img = tk.PhotoImage(file=ruta)
        lbl = tk.Label(contenedor, image=img, **config)
        lbl._img = img  # evitar garbage collector

        aplicar_pack(lbl, mostrar)
        return lbl
    except Exception as e:
        print(f"Error cargando imagen: {e}")

# =========================
# Variables
# =========================

def variable_texto(valor=""):
    return tk.StringVar(value=valor)

def variable_bool(valor=False):
    return tk.BooleanVar(value=valor)

# =========================
# Utilidades
# =========================

def editar(widget, **kwargs):
    config = traducir_kwargs(kwargs)
    widget.configure(**config)

def mostrar(*widgets, **pack_kwargs):
    for w in widgets:
        w.pack(**pack_kwargs)

def esconder(*widgets):
    for w in widgets:
        w.pack_forget()