#24 POO
#programacion orientada a procedimientos(fortran,cobol): deseventajas= unidades de codigo muy grandes,son complejas de decifrar,poco reutilizables,si existe un fallo probablemente el programa caiga,aparicion de codigo spagueti(flujo que sube baja regresa ),dificil de depurar.
#programacion orientado a objetos(c´´,java,visualnet): consiste en trasladar la naturaleza de los objetos de la vida real al codigo de programacion.los objetos tienen un estado, un comportamiento(que puede hacer?) y unas propiedades.ejm un coche puede estar estacionado,propiedades :color,peso,.., comportamiento :puede frenar, acelerar.
#propiedades son atributos .  Ventajas de poo : programas dividido en trozos,partes,modulos o clases(modularizacion).muy reutilizable.herencia.el programa continuara funcionando si existe fallo(excepciones).encapsulamiento.
#POO diccionary: clase, objeto,ejemplar e instancia de clase,modularizar,encapsulamiento,herencia,polimorfismos

#25
#Clase:modelo donde se redactan las caracteristicas comunes de un grupo de objetos ejm:chasis y 4 ruedas de un coche
#Instancia:ejemplar(sinonimo) perteneciente a una clase ejm:coches de diferente fabricante, tienen en comun las 4 ruedas y chasis, pero varia en su peso,color, etc que son sus propias caracteristicas.
#Modularizacion: un programa  puede estar compuesto de varias clases,permite reutilizar trozos de codigo.se conectan mediante métodos de acceso
#Encapsulación: para que nadie sepa del funcionamiento de una de las clases, que no sea accesible
#obejtos tienen propiedades y comportamientos, nomenclatura del punto coche.color="rojo" ,   coche.gira()
 
#26


class Coche():
	largochasis=250
	anchochasis=120
	ruedas=4
	enMarcha=False
	def Frenar(self):
		pass 

	def Arrancar(self):
		self.enMarcha=True  #miCoche.enmarcha=True 

	def Estado(self):
		if(self.enMarcha):
			return "El auto está en marcha"
		else:
			return "auto detenido"
		

#por defecto viene pass porque no hace nada esta funcion,y seguir ejecutando el resto
miCoche= Coche()     #intanciando(ejemplarizar) una clase, no se usa new como en otro leng.de programacion
print("El largo del coche es :" , miCoche.largochasis)
print("El coche tiene " , miCoche.ruedas, " ruedas")
miCoche.Arrancar()
print(miCoche.enMarcha)
print(miCoche.Estado())