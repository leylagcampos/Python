#9 Diccionarios
#Permiten almacenar valores de distinto tipo, incluso listas y otros diccionarios.Los datos se alamacenan asociados a una clave (asociación clave:valor) clave unica .EL orden a la hora de almacenar es indiferente.
midicionario={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","España":"Madrid"}
print(midicionario["Francia"])
print(midicionario)
#agregar a un dic.ya creado
midicionario["Italia"]="Lisboa"
print(midicionario)
#sobreescribir
midicionario["Italia"]="Roma"
print(midicionario)
#Borrar de un dicc.
del midicionario["Reino Unido"]
print(midicionario)

midicionario2={"Alemania":"Berlín",23:"Jordan","Mosqueteros":3}
print(midicionario2)


# tupla para asignar clave a valores
mitupla=["España","Francia","RU","Alemania"]
midicionario3={mitupla[0]:"Madrid",mitupla[1]:"París",mitupla[2]:"Londres",mitupla[3]:"Berlín"}
print(midicionario3)
#Guardar un tupla entera como diccionario, tambien guardar diccionario dentro de otro
midicionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"TEMPORADAS":[1991,1992,1993,1996,1997,1998]}}
print(midicionario4["Equipo"])
print(midicionario4["anillos"])

#keys,values, len

print(midicionario4.keys())
print(midicionario4.values())
print(len(midicionario4))

#10Estructuras de control de flujo:Condicionales
#if

print("programa de evaluacion de notas")
#input() espera un valor por teclado

##nota_alumno=input()
def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

##print(evaluacion(int(nota_alumno)))

#tools>>sublimerepl>>python>>python-Run current file


#11 Condicionales if else, elif(equivale a else if  de otros lenguajes de prog.)
print("Verificacion")

edad=int(input("Introduce tu edad"))
if edad<18 :
  print("no puedes pasar")

elif edad>100:
    print("edad incorrecta")
else:
  print("puedes pasar")

print("programa finalizado")

