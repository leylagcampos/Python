#45
#Interfaces -entry (en peruano: cuadros para escribir texto)
#sintaxis variablelabel=Label(contenedor,opciones) 

from tkinter import*

raiz=Tk()
miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

miAlias=StringVar()

cuadroTexto=Entry(miFrame)
#cuadroTexto.pack()
#cuadroTexto.place(x=300,y=100)
cuadroTexto.grid(row=0,column=1)
#grid() , row es fila contando desde 0 y desde arriba, column es columnas desde 0 hacia la derecha

cuadroApell=Entry(miFrame)
cuadroApell.grid(row=1,column=1)

cuadroDir=Entry(miFrame)
cuadroDir.grid(row=2,column=1)
cuadroDir.config(fg="red",justify="right") #define el formato de lo que se ecribirá en el cuadro


cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3,column=1)
cuadroPass.config(show="*")




#sticky ubica con los puntos cardinales en inglés, s,n,w,e y las subcoordenadas nw ne se sw

nombrelbl=Label(miFrame,text="Nombre : ")
#nombrelbl.place(x=100,y=100)
nombrelbl.grid(row=0,column=0,sticky="e")



apellidolbl=Label(miFrame,text="Apellido : ")
apellidolbl.grid(row=1,column=0,sticky="e")

dirlbl=Label(miFrame,text="Dirección: ")
dirlbl.grid(row=2,column=0,sticky="e",padx=10,pady=10)

passlbl=Label(miFrame,text="Password: ")
passlbl.grid(row=3,column=0,sticky="e",padx=10,pady=10)


#pady()  y padx()  define la distancia de los margenes del widget con su contenedor


#46 Text y Button
 
#Texto 
txtComentario=Text(miFrame, width=16,height=5)
txtComentario.grid(row=4,column=1,padx=10,pady=10)


Comentariolbl=Label(miFrame,text="Comentarios:")
Comentariolbl.grid(row=4,column=0,sticky="e",padx=10,pady=10)

#barra de desplazamiento
scrollVert=Scrollbar(miFrame,command=txtComentario.yview) #pertenece al txtcomentario y deberia verse en el eje
scrollVert.grid(row=4,column=2,sticky="nsew")

txtComentario.config(yscrollcommand=scrollVert.set)


#Botones

cuadroAlias=Entry(miFrame,textvariable=miAlias)
cuadroAlias.grid(row=5,column=1)
cuadroAlias.config(fg="blue")

Aliaslbl=Label(miFrame,text="Alias: ")
Aliaslbl.grid(row=5,column=0,sticky="e",padx=10,pady=10)


def codigoBoton():
	miAlias.set("Gringasho")

botonEnviar=Button(raiz,text="Enviar: ",command=codigoBoton)
botonEnviar.pack()


raiz.mainloop()