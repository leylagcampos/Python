#51 chekbutton

from tkinter import*

root=Tk()

root.title("EJEMPLO")


Playa=IntVar()
Montania=IntVar()
RuralT=IntVar()

def opcionesViaje():
	opcionEscogida=""
	if Playa.get()==1:
		opcionEscogida+="Playa "

	if Montania.get()==1:
		opcionEscogida+="Montaña "
		
	if RuralT.get()==1:
		opcionEscogida+="RuralTour "

	textoFinal.config(text=opcionEscogida)


foto=PhotoImage(file="loro.png")
Label(root,image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame,text="Elige los destinos: ",width=50).pack()

Checkbutton(frame,text="Playa",variable=Playa,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Montaña",variable=Montania,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Rural tour",variable=RuralT,onvalue=1,offvalue=0,command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()
root.mainloop()