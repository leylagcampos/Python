#23
#Lanzamiento de excepciones:Instruccion Raise.Creación de excepciones propias

def evaluaedad(edad):
	if edad<0:
		raise TypeError("no se permiten edades negativas")  #errores ya contemplados, si no esta contemplado sale error

	if edad <20:
		return "ud muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	elif edad<100:
		return "Cuidate.."

#print(evaluaedad(-55))


import math
def calculaRaiz(num):
	if num<0:
		raise ValueError("Número no puede ser negativo")
	else:
		return math.sqrt(num)

op1=(int(input("Introduce un número: ")))
try:
	print(calculaRaiz(op1))

except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)              

print("Programa terminado")  #continua la ejecucion 