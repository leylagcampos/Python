#50 radiobutton

#botonces de seleccion para  preguntas con respuesta unica, ejm: el género

from tkinter import*
root=Tk()

varOpcion=IntVar()

def imprimir():
	#print(varOpcion.get())
	if varOpcion.get()==1:
		etiqueta.config(text="Haz elegido Masculino")
	elif varOpcion.get()==2:
		etiqueta.config(text="Haz elegido Femenino")
	else:
		etiqueta.config(text="No especificaste ninguno")

Radiobutton(root, text="Masculino",variable=varOpcion,value=1,command=imprimir).pack()
Radiobutton(root,text="Femenino",variable=varOpcion,value=2,command=imprimir).pack()
Radiobutton(root,text="Prefiero no decirlo",variable=varOpcion,value=3,command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()