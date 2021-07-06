#39 Serialización
#se serializan colecciones  y objetos
#se guarda una collecion  etc en un fichero externo en formato de codigo binario
#para distribuir un objeto py en internet, o guardar una coleecion o dic en almacenamiento externo  o BD
#usamos biblioteca pickle, usando los metodos:
#dump():volcado de datos al fichero binario externo
#load(): carga de los datos al fichero binario externo

import pickle

lista_nom=["Román","Elsa","Nicolas","Isabela"]

#wb:write binary , rb: read binary

fichero_binario=open("ListaNombres","wb")
pickle.dump(lista_nom,fichero_binario)
fichero_binario.close()
del(fichero_binario)


fichero1=open("ListaNombres","rb")
lista1=pickle.load(fichero1)
print(lista1)



#40 serializacion de objetos

class Vehiculos():

	def __init__(self,marca,modelo):
		self.marca=marca
		self.modelo=modelo
		self.enMarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enMarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca,"\nModelo: ", self.modelo,"\nEn marcha: ", self.enMarcha,"\nAcelerando: ", 
		self.acelera, "\nFrenando: ", self.frena)


coche1=Vehiculos("Mazda","MX5")
coche2=Vehiculos("Seat","Leon")
coche3=Vehiculos("Renault","Megane")
coches=[coche1,coche2,coche3]

fichero_Binario=open("losCoches","wb")
pickle.dump(coches,fichero_Binario)
fichero_Binario.close()
del(fichero_Binario)

#recuperando

fichero2=open("losCoches","rb")
misCoches=pickle.load(fichero2)
fichero2.close()

for c in misCoches:
	print(c.estado())