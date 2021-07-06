#42 Interfaces : tmbn llamadas GUI, son intermediarios entre programa y usuario
#conformadas por un conjunto d egraficos como ventanas,botones,casillas etc
#librerias para crear GUI:  Tkinter,WxPython,PyQT,PyGTK
#Tkinter es un puente entre py y la libreria TCL/TK

#Estructura de ventana con Tkinter: raiz o ventana, frame y widgets

from tkinter import *

raiz=Tk()
raiz.title("Ventana de pruebas")
raiz.resizable(1,0)  #raiz.resizable(True ,False) , indica que se puede modificar ancho y no largo


#para el icono, usar archivos con extension .ico

raiz.iconbitmap("gato.ico")

raiz.geometry("650x320")

raiz.config(bg="blue")
raiz.mainloop()