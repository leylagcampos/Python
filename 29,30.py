#29
#Herencia: englobar en una clase padre(superclase) las propiedades y metodos en comun de otras clases 
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


class Furgoneta(Vehiculos):
	def carga(self,cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"



class Moto(Vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	#sobreescitura de métodos

	def estado(self):
		print("Marca: ", self.marca,"\nModelo: ", self.modelo,"\nEn marcha: ", self.enMarcha,"\nAcelerando: ", 
		self.acelera, "\nFrenando: ", self.frena,"\n",self.hcaballito)




#clase indep
class VElectricos():
	def __init__(self):
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True




miMoto=Moto("Honda","CBR")

miMoto.caballito()  
miMoto.estado()   #llama al metodo estado de la clase moto



miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


#herencia múltiple
class BicicletaElectrica(VElectricos,Vehiculos):
	pass

#miBici=BicicletaElectrica("Orvea","HC1030") 
 #siempre da preferencia  a la primera clase que indique, en ese caso velectrico que tiene 0 argumentos

miBici=BicicletaElectrica()