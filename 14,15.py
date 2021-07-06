#14 Estructuras de control:Bucles
#Bucle determindos (sabemos cuanto va a repetirse) indeterminado (depende de la ejecucion del programa)
#Bulce for .Sintaxis= for variable in elemento a recorrer lista texto o rango :

for i in [1,2,3]:
	print("Hola") 

for estaciones in ["primavera","verano","otoño","invierno"]:
	print(estaciones)


#15    Recorrer strings, tipo range, notaciones especiales con print

# end imprimir como un espacio que no existe
for i in ["pildoras","informaticas", 3]:
	print("holi",end=" ")

#imprimir la misma cantidad de caracteres que hay en el elemento a recorrer
for i in "juan@pildorasinformaticas.es":
	print("Hi", end="")



email=False
miEmail=input("Introduce tu direccion email: ")

for i in miEmail:
	if(i=="@"):
	 email=True

#if email==True   se sobreentiende  verdadero  en    if email:
if email:
	print("email correcto")
else:
	print("email incorrecto ")



#entrara dos veces  si encuentra arroba y punto
contador=0
miEmail=input("Introduce tu direccion email: ")
for i in miEmail:
	if(i=="@" or i=="."):
	 contador=contador+1

if contador==2:
	print("email correcto")
else:
	print("email incorrecto ")

#crea una lista que va del 0 al cuatro
for i in range(5):
	print(i)