#52 Menús
#53 ventanas emergentes o mensajes
from tkinter import*
from tkinter import messagebox
root=Tk()

def infoAdicional():
	messagebox.showinfo("Procesador de Leyla","Procesador de textos version 2020")

def avisoLicencia():
	messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def SalirApp():
	#valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
    valor=messagebox.askokcancel("Salir","¿Deseas salir de la aplicación?")
    if valor==True:
    	root.destroy()

def cerrarDoc():
	valor=messagebox.askretrycancel("Reintentar","No es posible cerrar,documento bloqueado")
	if valor==False:
		root.destroy()


barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

archivoMenu=Menu(barraMenu,tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarDoc)
archivoMenu.add_command(label="Salir ",command=SalirApp)


archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cotar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu,tearoff=0)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="About..",command=infoAdicional)


barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edición",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
barraMenu.add_cascade(label="Help",menu=archivoAyuda)
root.mainloop()
