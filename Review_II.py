#Review II

Celular=int(input("Ingrese su número de celular:"))
Email=input("Escriba su email más usado: ")
EmailFormato=Email.lower()

print("Ubicación: LIMA - CALLAO- PROVINCIA")
Ubicación=input("Escriba la ubicación escogida").upper()

if Ubicación in ("LIMA","CALLAO","PROVINCIA"):
	print("Escogió: "+ Ubicación)

print("Número de celular de este paciente es : "+ str(Celular))




for clavehoy in ["7","Colombia","2020"]:
	print("W" + clavehoy  ,end=" ")





confirmacion=False

while(confirmacion==False):
	f=0
	for i in str(Celular):
	 f=f+1              #contador de digitos
	 if f==1:
	 	PrimerDig=i
	 else:
	 	continue



	if f==9  and PrimerDig=="9":
		print("Es un número de celular")
		confirmacion=True
	else:
		print("No es un número de celular")
		Celular=int(input("Ingrese denuevo su número de celular:"))






contador=0

for i in EmailFormato:
	if(i=="@" or i=="."):
	 contador=contador+1

if contador==2:
	print("email correcto")
else:
	print("email incorrecto ")



def GenerarCitas(dia):
	
	while dia<30 :
		yield dia+7
		dia+=7
		




devuelveproximascitas=GenerarCitas(12)
print("Futuras citas en este mes:")
print(next(devuelveproximascitas))
print("pause")
print(next(devuelveproximascitas))


def codigoPaciente(*datos):
	for elem in datos:
	 yield from elem

codigo=codigoPaciente(str(Celular),Ubicación,EmailFormato)

print(next(codigo))
next(codigo)
next(codigo)
next(codigo)
next(codigo)
next(codigo)
next(codigo)
next(codigo)
print(next(codigo))