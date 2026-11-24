Introducción:

Espanish Tkinter, también conocido por sus siglas “esptk”, es una librería externa de Python que busca traducir la mayor parte de Tkinter al español, además de simplificar y automatizar gran parte del proceso.
Esptk te permite crear ventanas, textos, botones y otros widgets de forma más simple y rápida, manteniendo la misma filosofía de la librería original.

Este proyecto aspira a ser una alternativa más sencilla para crear aplicaciones de escritorio, utilizando una sintaxis legible en español. Esto puede servir como una herramienta educativa y de aprendizaje para nuevos programadores interesados en desarrollar interfaces gráficas en Python de manera simple y sin complicaciones.

Aunque esta librería puede utilizarse para aprender a manejar elementos visuales, no se limita a ser una herramienta educativa, ya que su nivel de automatización y simplicidad la hacen perfectamente usable en proyectos más ambiciosos y profesionales.

Ejemplo básico de uso:

```python

from modulos import esptk # Importar módulo

# Crear ventana

ventana_de_prueba = esptk.CrearVentana(
    resolucionX=600,
    resolucionY=400,
    titulo="Aplicacion de prueba hecha con esptk"
)

# Crear un texto

texto_de_prueba = esptk.CrearTexto(
    ventana_de_prueba,
    texto="Hola!!! Esto es un texto simple hecho con esptk",
    tamanio_fuente=20,
    iniciarEjecutado=True,
    posicionY=10
)

# crear un botón

boton_de_prueba = esptk.CrearBoton(
    ventana_de_prueba,
    texto="Salir de la app",
    comando_al_presionar=esptk.CerrarVentana,
    comando_argumentos=ventana_de_prueba,
    iniciarEjecutado=True,
    posicionY=10
)

# Ejecutar la ventana

esptk.EjecutarVentana(ventana_de_prueba)
