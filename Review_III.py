#Review III
class Persona():

	def __init__(self,nombre,pesokg,alturacm,edad,sexo):
		self.peso=pesokg
		self.altura=alturacm
		self.edad=edad
		self.__nombre=nombre
		self.sexo=sexo

	def Reporte(self):
		print("hola ",self.__nombre," actualmente tienes ",self.edad ," años,mides ",self.altura," y pesas ",self.peso) 



class TasaMetabólicaBasal(Persona):
    calorias1=0
    calorias2=0
    calorias3=0

    def HarrisBenedict(self):
    	if self.sexo=="F":
    		self.calorias1=665+(9.6 * self.peso)+(1.85* self.altura)-(4.7* self.edad)

    	elif self.sexo=="M":
    		self.calorias1=66.5+(13.8*self.peso)+(5*self.altura)-(6.8 * self.edad)

    def MifflinStJeor(self):
    	if self.sexo=="F":
    		self.calorias2=(10* self.peso)+(6.25* self.altura)-(5* self.edad)-161
    	elif self.sexo=="M":
    		self.calorias2=(10*self.peso)+(6.25*self.altura)-(5* self.edad)+ 5

    def OMS(self):
    	 self.calorias3=(14.7*self.peso)+496  #completar aqui y las por nivel de actividad

    def Reporte1(self):
    	print("Según HarrisBenedict deberías consumir: ",self.calorias1,", segun Mifflin :",
    		self.calorias2*1.2," , según la OMS :",self.calorias3, " calorias")








Persona1=TasaMetabólicaBasal("Leyla",55,1.55,21,"F")
Persona1.HarrisBenedict()
Persona1.MifflinStJeor()
Persona1.OMS()
Persona1.Reporte()
Persona1.Reporte1()