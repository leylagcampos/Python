#27 parámetros, 
#estado inicial def __init__(self) eso se hace con un constructor:metodo que le da estado inicial a los objetos pertenecientes a una clase
#28
#encapsular __ : proteger propiedades y metodos para que no se pueda manipular desde fuera de la clase
class Coche():
	def __init__(self):
		self.__largochasis=250
		self.__anchochasis=120
		self.__ruedas=4
		self.__enMarcha=False


	def Frenar(self):
		pass 

	def Arrancar(self,arrancamos):
		self.__enMarcha=arrancamos

		if(self.__enMarcha):
			chequeo=self.__chequeo_interno()


		if(self.__enMarcha and chequeo):
			return "El auto está en marcha"

		elif(self.__enMarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo,no podemos arrancar"

		else:
			return "auto detenido"
		
	def Estado(self):
		print("El coche tiene ", self.__ruedas," ruedas .Un ancho de ", self.__anchochasis, "  y un largo de ", self.__largochasis)

	def __chequeo_interno(self):      #vamos a encapsular el método
		print("realizando chequeo interno")
		self.gasolina="ok"
		self.aceite="ok"  #probar con "mal"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False

#chequeo antes de arrancar

miCoche= Coche() 
print(miCoche.Arrancar(True))
miCoche.Estado()

print("---------A continuacion creamos el 2do objeto----------")


miCoche2=Coche()
print(miCoche2.Arrancar(False))
miCoche2.__ruedas=2  #es incorrecto, cuando lo encapsulo sigue con su valor de 4, de lo contrario muestra 2
miCoche2.Estado()
#print(miCoche2.__chequeo_interno())  no funcionará porque esta encapsulado