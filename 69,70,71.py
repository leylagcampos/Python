#69 Expresiones regulares(regex) : son una secuencia de caracteres que forman un patron de búsqueda
'''sirven para el trabajo y procesamiento de texto, ejm:buscar un texto que se ajusta a un formato
determinado,buscar si existe o no una cadena de caracteres dentro de un texto,contar el numero de coincidncias dentro de un texto,etc.
match(),search(),findall(),finditer(),group(),start(),end(),span()'''
import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de programación"

print(re.search("aprender",cadena)) #lo encuentra
print(re.search("tu y yo",cadena))

textoBuscar="aprender"

if re.search(textoBuscar,cadena) is not None:
	print("He encontrado 1 texto")
else:
	print("No encuentro el texto")


textoencontrado=re.search(textoBuscar,cadena)
print(textoencontrado.start()) # dice el numero de caracter  donde empieza
print(textoencontrado.end()) # dice el numero de caracter  donde finaliza
print(textoencontrado.span()) # las dos anteriores a la vez

textoBuscar2="Python"
print(len(re.findall(textoBuscar2,cadena))) 
'''devueve logitud de la lista donde dice muchas veces "Python, 
q seria al final las veces que aparece esa palabra en el texto'''

#70 Metacaracteres(carcater comodín),anclas y clases de caracteres


listaNombres=[ 'Santiago Gómez',
               'Maria Martín',
               'Santiago Martín',
               'Fernando Tapia']


for elemento in listaNombres:
	if re.findall('^Santiago',elemento) :
		print(elemento)


for elemento in listaNombres:
	if re.findall('Martín$',elemento) :
		print(elemento)




listaDominio=['http://facebook.com','http://facebook.es','www.chocochispas.co'
,"www.line.ar","m.okchicas.pe",'m.okchicos.pe',"www.chocóchispas.co"]
for elemento in listaDominio:
	if re.findall('^http',elemento) :
		print(elemento)


for elemento in listaDominio:
	if re.findall('.ar$',elemento) :
		print(elemento)


for elemento in listaDominio:
	if re.findall('[n]',elemento) :
		print(elemento)


for elemento in listaDominio:
	if re.findall('m.okchic[oa]s.pe',elemento) :
		print(elemento)

for elemento in listaDominio:
	if re.findall('www.choc[oó]chispas.co',elemento) :
		print(elemento)


#71 con rangos

listaAmigosdJuan=['Ana','Pedro','María','Rosa','Sandra','Celia']

for elemento in listaAmigosdJuan:
	if re.findall('[o-t]',elemento) :
		print(elemento)

print("---------otro ejemplo --------")
for elemento in listaAmigosdJuan:
	if re.findall('^[O-T]',elemento) :
		print(elemento)


print("---------otro ejemplo --------")
for elemento in listaAmigosdJuan:
	if re.findall('[o-t]$',elemento) :
		print(elemento)



listaLugares=['Ma1','Se.1','Ma2','Ba1','Ma3','Va1','Va2','Ma4','MaA',
'Ma5','MaB','MaC','Se:3','Se9']

print("---------otro ejemplo --------")
for elemento in listaLugares:
	if re.findall('Ma[0-3]',elemento) :
		print(elemento)

print("---------otro ejemplo --------")
for elemento in listaLugares:
	if re.findall('Ma[^0-3]',elemento) :
		print(elemento)

print("---------otro ejemplo --------")
for elemento in listaLugares:
	if re.findall('Ma[0-3A-B]',elemento) :
		print(elemento)


print("---------otro ejemplo --------")
for elemento in listaLugares:
	if re.findall('Se[.:]',elemento) :
		print(elemento)