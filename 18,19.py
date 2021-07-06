#18
#continue

for letra in "Python":
	if letra=="h":
		continue
	print("Viendo la letra: "+letra)



nombre="pildoras informaticas"
print(len(nombre))

#da 21 porque tambien cuenta el espacio

contador=0
for i in nombre:
	if i==" ":
		continue
	contador+=1

print(contador)

#pass 

#while True:
 #pass

#class Miclase:
	#pass               para implementar más tarde

#else dentro de for o while,solo funcionara cuando ya no quede mas por recorrer

email=input("Introduce tu email please: ")
for i in email:
	if i=="@":
		arroba=True
		break;

else: 
	arroba=False

print(arroba)


#19 
#Generadores: Estructuras que extraen valores de una función y se alamcenan en objetos iterables(recorribles),estos valores se almacenan de uno en uno.
#Suspension de estado:cuando el generador almacena,permanece en un estado pausado hasta q se solicicta el siguiente
#son más eficientes que las funciones tradicionales,muy utiles con listas de valores infinitos
#existe yield  e incluso un generador puede tener return



#TRADICIONAL
def generePares(Limite):    
	num=1
	miLista=[]
	while num<Limite:
		miLista.append(num*2)
		num+=1

	return miLista

print(generePares(10))


 #GENERADOR
 
def generePares2(limite):   
	num=1
	
	while num<limite:
		yield num*2
		num+=1

devuelvePares=generePares2(10)

#for i in devuelvePares:
	#print(i)

print(next(devuelvePares))
print("other codigo")
print(next(devuelvePares))
print("other codigo")
print(next(devuelvePares))
