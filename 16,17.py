#16
#range, notacion especial f ,contar del 5 termina en el 49 y va ir de 3 en tres
for i in range(5,50,3):
	print(f"valor de la variable {i}")

valido=False
email=input("introduce tu mail: ")
for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido:
	print("email correcto")
else:
	print("email incorreto")

#17 
#Bucle while .Sintaxis= while condicion: instrucciones

j=1
while j<=10:
	print("Ejecucion" + str(j))
	j=j+1
print("Se terminó la ejecución")


edad=int(input("Introduce tu edad: "))
while edad<5 or edad>100 :
	print("edad incorrecta .intentalo denuevo")
	edad=int(input("introduce tu edad please: "))

print("Gracias Puedes pasar")
print("edad del postulante: " + str(edad))




import math
print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero porfavor: "))
intentos=0

while numero<0:
	print("no se puede hallar raiz de un numero negativo")

	if intentos==2:
		print("Has consumido demasiados intentos.Finalizo el programa")
		break; #nos sacara del programa
	numero=int(input("Introduce un numero porfavor: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de "+ str(numero)+ " es "+ str(solucion))

