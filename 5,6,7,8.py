#5
#Funciones:bloque de código q funciona como una uunidad realizando un tarea especifica.Pueden devolver valores o no.Pueden tener parámetros /argumentos o no. Se les denominan "métodos" cuando se encuentran definidas dentro de una clase.utilidad: permite reutilizar código.  Sintaxis:  def nombre_funcion(zona de parámetros):   instruciones  return(opcional).
#funciones predefinidas : ya vienen con el lenguaje ejm print()| funciones propias
print("estamos aprendiendo python")


def mensaje():
  print("ee")
  print ("rr")


mensaje()

print("Ejecutando")


mensaje()
#6
#control+rodillo de mouse para hacer zoom.Cntrl + S para guardar y Cntrol+B para compilar


def suma():
	num1=5
	num2=7
	print( num1+num2 )


suma()

suma()

def suma2(numero1,numero2):
	print(numero1+numero2)

suma2(4,6)
suma2(9,8)

def suma3(a,b):
	resultado=a+b
	return resultado

print(suma3(6,7))

almacenar= suma3(7,8)
print(almacenar)    

#python siempre todo es por referencia
#7
#listas (o array):equivale a un array y es una estructura de datos que permite almacenar una gran cantidad de valores, python: permiten guardar diferente tipo de valores y
#se expande dnámicamente añadiendo nuevos elementos.sintaxis:  nombrelista=[ elem1,elem2,...]

miLista=["María","Pepe","Martha","Antonio"]
print(miLista[:])
 # si ponemos miLista[7] indice fuera de rango, si miLista[-2] empieza a leer desde el final y devuelve Martha
print(miLista[-3])

#acceder a Porción,ejm imprimir los 3 primeros
#indice 0  lo incluye, el tercero no esta incluido.
print(miLista[0:3])

#Si obviamos el 0, python lo sobreentiende.ejm imprimir los dos primero.
print(miLista[:2])
#incuye a indice 1,excluye indice 2
print(miLista[1:2])
print(miLista[1:3])
#Acceder a los dos ultimos.Desde indice 2,que lo incluye ,hasta el final
print(miLista[2:])
print(miLista[3:])
print(miLista[1:])

#append -->añade (en el final)
miLista.append("Sandra")
print(miLista[:])
#insert -->añadiendo en un lugar especifico de la lista
miLista.insert(2,"Yuri")
print(miLista[:])
#extend-->Para añadir varios
miLista.extend(["luz","ana","pablo"])
print(miLista[:])

#para imprimir posicion
print(miLista.index("ana"))

#Imprimir si un elemento esta en la lista, devuelve true o false
print("Pepe" in miLista)

#Añadiendo valores de distinto tipo.
#remove -->eliminar valor de la listas

miLista1=["melisa",5,True,32.12,"Firulais"]
miLista1.remove("Firulais")
print(miLista1[:])

print(miLista1[3])

#pop-->eliminar ultimo elemento
#miLista1.extend(["robert","Eduardo",12])
miLista1.pop()
print(miLista1[:])

#Uniedo lista
miListaA=["w",4,24.2,False]
miListaB=["id","a"]
miListaX=miListaA+miListaB
print(miListaX[:])

#Imprimiendo varias veces la misma lista
miListaC=["aa","bb","cd",7]*3
print(miListaC[:])

#8
#Tuplas-->listas inmutable, no se modifican después de su creación.No permiten añadir,eliminar,mover elementos, ni busqueda.(no append,extend,remove,index(solo en ultimas versiones si)).
#si permiten extraer porciones y comprobar si hay un elemento en la tupla.
#ventaja  de la tupla respecto a la lista: son más rápidas, ocupan menos espacio(mayor optimizacion), formatean String (cadenas), Se pueden usar como claves de diccionario(listas no hacen eso)
#sintaxis:  nombreLista=(elem1,elem2,elem3,..), comienza igual con indice 0 a etc

mitupla=("Juan",23,1,1999)
print(mitupla[2])
#list-->para convertir tupla en lista

milist=list(mitupla)
print(milist)
print(mitupla)

#tuple-->convertir lista en tupla
milist1=["maribel",777,"rubi",777]
mytupla=tuple(milist1)
print(mytupla)
print(milist1)

#verificar si está en tupla
print("rubi" in mytupla)
#count-->imprime cuantas veces aparece ese elemento en la tupla
print(mytupla.count(777))
#len-->numero de elementos
print(len(mytupla))

#Tupla unitaria
tuplaunit=("hector",)
print(len(tuplaunit))

#en la tupla los parentesis son opcionales
#Empaquetado de tupla:
mitupla2="fabiola",14,"bottle",True
print(mitupla2)

#Desempaquetado de tupla: asignamos los elementos d ela tupla a respectivas variables
nombre,dia,objeto,casado=mitupla2
print(nombre)
print(dia)
print(objeto)
print(casado)
