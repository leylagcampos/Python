
#43 
#creacion de frame

from tkinter import *
raiz=Tk()
raiz.title("Ventana de pruebas")
#raiz.resizable(1,0)

raiz.iconbitmap("gato.ico")
#raiz.geometry("650x320")
raiz.config(bg="blue")



raiz.config(bd=45)
raiz.config(relief="groove") 
raiz.config(cursor="pirate") 

#la raiz se adapta a su contenedor

miFrame=Frame()

miFrame.pack()
#miFrame.pack(side="right")
#miFrame.pack(side="left")
#miFrame.pack(side="bottom")
#miFrame.pack(side="left",anchor="n")
#miFrame.pack(side="right",anchor="s")

#miFrame.pack(fill="x")
#miFrame.pack(fill="y",expand="True")

#miFrame.pack(fill="both", expand="True")


miFrame.config(bg="red")
miFrame.config(width="650",height="300")
miFrame.config(bd=35) #grosor borde
miFrame.config(relief="sunken") #tipo de borde,tambien provar groove
miFrame.config(cursor="hand2") #tipo de cursor, tmbn probar  pirate

raiz.mainloop() 