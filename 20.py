#20 
#yield from :simplifica el codigo de los generadores en caso de usar bucles anidados , similar a matrices en otros codigos

def devuelve_ciudades(*ciudades):#* que va recibir un numero indeterminado de elementos y lo recibe en forma de tupla
 for elemento in ciudades:
 	for subelemento in elemento:
 		yield subelemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#Con yield from=

def devuelve_ciudades2(*ciudades):#* que va recibir un numero indeterminado de elementos y lo recibe en forma de tupla
 for elemento in ciudades:
 	#for subelemento in elemento:
 		yield from elemento

ciudades_devueltas=devuelve_ciudades2("Madrid","Barcelona","Bilbao","Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))