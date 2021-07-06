#47 Calculadora: Interfaz 
#48 Calculadora: Definicion de las  funciones para imprimir los numeros
#49 Calculadora: Definicion de las  funciones para las operaciones básicas


from tkinter import*

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

operacion=""
resultado=0
pantallallena=False

#..............Pantalla..........................
numPantalla=StringVar()


pantalla=Entry(miFrame,textvariable=numPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black",fg="#02f288",justify="right")

#*colspan en diseño web, en python es columnspan
#..................Pulsaciones teclado..........................
def numeroPulsado(boton):
	global operacion
	global pantallallena

	if pantallallena:
		numPantalla.set(""+boton)
		pantallallena=False

	else:
		if operacion!="":
			numPantalla.set(boton)
			operacion=""
		else:
			numPantalla.set(numPantalla.get()+boton)



#.......................Funciones para operaciones básicas.........

def suma(num):
	global operacion
	global resultado
	resultado+=int(num)
	operacion="suma"
	numPantalla.set(resultado)

def igual():
	global resultado
	global operacion
	global pantallallena
	numPantalla.set(resultado+int(numPantalla.get()))
	resultado=0
	operacion=""
	pantallallena=True
	


#.........................fila1...............................

boton7=Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/",width=3)
botonDiv.grid(row=2,column=4)

#.......................fila2...................................

boton4=Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonMult=Button(miFrame,text="x",width=3)
botonMult.grid(row=3,column=4)

#.......................fila3...................................

boton1=Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
botonRest=Button(miFrame,text="-",width=3)
botonRest.grid(row=4,column=4)

#.......................fila4...................................

boton0=Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
botonComa=Button(miFrame,text=",",width=3,command=lambda:numeroPulsado(","))
botonComa.grid(row=5,column=2)
botonIgual=Button(miFrame,text="=",width=3,command=lambda:igual())
botonIgual.grid(row=5,column=3)
botonSuma=Button(miFrame,text="+",width=3,command=lambda:suma(numPantalla.get()))
botonSuma.grid(row=5,column=4)




raiz.mainloop()