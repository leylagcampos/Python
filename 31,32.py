#31 herencia super() , isinstance() devuelve true o false si es instancia de una clase
class Persona():
	def __init__(self,nombre,edad,lugar_residencia):
		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=lugar_residencia

	def descripcion(self):
		print("Nombre: ",self.nombre,"Edad: ",self.edad,"Residencia: ",self.lugar_residencia)


class Empleado(Persona):
	def __init__(self,salario,antiguedad, nombre_empleado,edad_empleado,residencia_empleado):
		#super().__init__("Antonio",55,"España")
		super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):
		super().descripcion()
		print("Salario: ",self.salario,"Antiguedad: ",self.antiguedad)


Dat1=Empleado(1400,5,"Manuel",55,"Colombia")
Dat1.descripcion()

#principio de sustitucion "es siempre un/a", ejm un empleado siempre es una persona,sin embargo una persona no siempre es un empl.
#entonces verificamos:
print(isinstance(Dat1,Empleado))
print(isinstance(Dat1,Persona))


#Aplicando al ejemplo anterior 

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


class VElectricos(Vehiculos):
	def __init__(self,marca,modelo):
		super().__init__(marca, modelo)
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True

#herencia múltiple
class BicicletaElectrica(VElectricos,Vehiculos):
	pass


miBici=BicicletaElectrica("Orbea","19292")


#32 Polimorfismo
#un obj cambia de forma y comportamiento segun el contexto

class Coche():
	def desplazamiento(self):
		print("Me desplazo utilizando 4 ruedad")

class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando 2 ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo utilizando 6 ruedas")

miVehiculo=Moto()
miVehiculo.desplazamiento()

miVehiculo2=Coche()
miVehiculo2.desplazamiento()

#estamos usando el mismo método

miVehiculo3=Camion()
miVehiculo3.desplazamiento()


#usando un método general que llama al metodo correcto segun el objeto que se le da

def desplazamientoVehiculos(vehiculo):  
	vehiculo.desplazamiento()

miVehiculo4=Camion()
desplazamientoVehiculos(miVehiculo4)