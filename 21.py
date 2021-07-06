#21 Excepciones1 
#errores que ocurren durante la ejecucion del programa,durante la ejecucion ocurre algo inesperado
#manejo o control de excepciones: para que la_ ejecucion _del programa continue
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	try:
		return num1/num2
	except ZeroDivisionError:       #si no puede dividir y el error coincide con esto, continuara la ejecucion y el programa no caera
		print("No se puede dividir entre 0")
		return "Operación errónea"
	

while True:
	try:
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))
		break

	except ValueError:
		print("Los valores introducidos no son correctos.Intentalo denuevo")  #capturando mas excepci0nes


operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")


#probar division entre 0, o entrar otro tipo de valor como strings en vez de numeros