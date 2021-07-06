IMC=18.5


def IMCcalculator(pesoactual,talla):
  r=pesoactual/(talla**2)
  return r


def pesoideal(talla):
	pesoideal=IMC*(talla**2)
	return pesoideal


print("imc que se aspiró en un inicio: ",IMCcalculator(48.0,1.55))
print("tu IMC actual es: ",IMCcalculator(63.1,1.55),"\nentonces tu peso ideal es: ",pesoideal(1.55))


def datosdelpaciente(tup):
  nombre,apellido,edad,peso,talla,imcA,pesoi= tup
  print("Nombre-->",nombre,"\nApellido-->",apellido,"\nEdad-->",edad,"\nPeso actual-->",peso,"Talla-->",talla,"\nImc-->",imcA,"\nPesoideal-->",pesoi)
  


def Verificacion(L):
	v=input("Los datos son correctos?SI/NO:")
	if(v=="SI"):
		tupla=tuple(L)
		return tupla
	else:
		tupla1=("0","0","0","0","0","0","0")
		return tupla1
 



def Diagnostico(nom,apell,edadact,pesoact,tallaact):
	Lista=[nom,apell,edadact,pesoact,tallaact]
	Lista.append(pesoideal(tallaact))
	Lista.insert(5,IMCcalculator(pesoact,tallaact))
	print(Lista[:])
	n=Lista[3]-Lista[6]
	Diccionario={"P1":Verificacion(Lista)}
	print(Diccionario)
	datosdelpaciente(Diccionario["P1"])
	print("Usted debe bajar: " ,n ," KG")


Diagnostico("Leyla","Campos",21,60.5,1.55)