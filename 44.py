#44 
#Interfaces -label
#sintaxis variablelabel=Label(contenedor,opciones) 

from tkinter import*
root=Tk()
miFrame=Frame(root,width=500,height=400)
miFrame.pack()


#uso de imagenes --> tkinter usa en formato png y gif 


miImage=PhotoImage(file="loro.png")
Label(miFrame,image=miImage).place(x=0,y=0)


miLabel=Label(miFrame,text="Hola amigos",font=("Comic Sans MS",20))
#miLabel.pack()  #ajusta el contenedor al tamaño del texto
miLabel.place(x=100,y=200)


Label(miFrame,text="ey",fg="blue",font=(20)).place(x=0,y=200)


root.mainloop()

