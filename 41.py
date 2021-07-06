#41 Guardado Permanente

import pickle

class Persona:
	def __init__(self,nombre,genero,edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una Persona nueva con el nombre de ", self.nombre)
     #los sgte convierte en cadena de texto la informacion 
	def __str__(self):
		return "{} {} {}".format(self.nombre,self.genero,self.edad)




class ListaPersonas:
	personas=[]

	def __init__(self):
		ListadeP=open("ficheroExterno","ab+")
		ListadeP.seek(0)

		try:
			self.personas=pickle.load(ListadeP)
			print("Se cargaron {} personas del fichero externo ".format(len(self)))

		except:
			print("El fichero está vacio")

		finally:
			ListadeP.close()
			del(ListadeP)

	def agregarPersonas(self,p):
		self.personas.append(p)
		self.guardarPersonasenFicheroExt()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)


	def guardarPersonasenFicheroExt(self):
		ListadeP=open("ficheroExterno","wb")
		pickle.dump(self.personas,ListadeP)
		ListadeP.close()
		del(ListadeP)

	def mostrarInfoFicheroExt(self):
		print("La informacion del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)

miLista=ListaPersonas()
persona1=Persona("Dora","Femenino",5)
miLista.agregarPersonas(persona1)
miLista.mostrarInfoFicheroExt()

#p=Persona("Sandra","Femenino",29)
#miLista.agregarPersonas(p)


