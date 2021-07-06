#33 Metodos de cadenas
#upper() -->mayusculas
#lower()-->minusculas
#capitalize()-->primera letra en mayuscula
#count()-->contar cuantas veces aparece una letra o cadena dentro de una frase
#find()-->representa  indice o pos donde aparece un caracter o grupo de carateres dentro de un texto
#isdigit()--> bota true o false si el texto introducido es un digito(numericos)
#isalum()-->lo mismo pero si es alfanumerico
#isalpha()--> lo mismo solo si hay solo letras
#split()-->separa palabras utilizando espacios
#strip()-->borrar espacio sobrante al principio y al final
#replace()-->cambia una letra o palabra por otra
#rfind()-->representa  indice o pos donde aparece un caracter o grupo de carateres dentro de un texto contando desde atras

nombreUsuario=input("Introduce tu nombre de usuario: ")
print("El nombre es ",nombreUsuario.upper())
print("El nombre es ",nombreUsuario.lower())
print("El nombre es ",nombreUsuario.capitalize())

edad=input("Introduce la edad : ")
#print(edad.isdigit())

while(edad.isdigit()==False):
	print("Porfavor, ingrese un numero")
	edad=input("Introduce la edad : ")

if(int(edad)<18):
	print("Menor de edad, no puede pasar")
else:
	print("Pase ")