#73 Decoradores

''' Funciones que a su vez añaden funcionalidades a otras funciones, de ahi el termino "decora"
porque les añaden funcionalidades

Estructura de un decorador:
3 funciones A, B, C  donde A recibe  como parametro a B  para devolver C

el decorador siempre devuelve una función
//funcion A
def función_decorador(función):  //funcion B
  def función_interna():  //funcion C
    #codigo de la funcion interna
  return funcion_interna

'''



#decorador sirve para agregar las misma funcionalidades a varias funciones

def funcion_decoradora(funcion_parametro):
	def funcion_interior(*argumentos,**kwargs):
		#Acciones adicionales que decoran
		print("Vamos a realizar un cálculo :  ")
		funcion_parametro(*argumentos,**kwargs)
		print("Hemos terminado el cálculo")
	return funcion_interior




@funcion_decoradora
def suma():
  print(15+20)


@funcion_decoradora
def resta():
	print(90-30)



@funcion_decoradora
def multip(num1,num2):
  print(num1*num2)


@funcion_decoradora
def potencia(base,exponente):
	print(pow(base,exponente))

@funcion_decoradora
def operacionb(a,b,c):
	print((a+b)*c)


suma()
resta()
multip(2,5)
operacionb(2,3,3)
potencia(2,5)

potencia(base=4,exponente=3)  #con clave  **kwargs