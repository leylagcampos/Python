#72 math() busca desde el principio, search no

import re

nombre1="Daniel Fernandez"
nombre2="Jenny López"
nombre3="daniel Vidal"
nombre4="Mara Gutierres"
nombre5="Dara Torres"

cadena1="Felicia Herrera"
cadena2="738282"
cadena3="b81819"


if re.match("Jenny",nombre2):
   print("Hemos encontrado el nombre")

else:
 print("No lo hemos encontrado")




if re.match("Daniel",nombre3,re.IGNORECASE): 
   print("Hemos encontrado el nombre")

else:
 print("No lo hemos encontrado")

#con ignorecase se ingnora si primera letra es mayuscula o minuscula


if re.match(".ara",nombre5,re.IGNORECASE):
   print("Hemos encontrado el nombre")

else:
 print("No lo hemos encontrado")




if re.match("\d",cadena1):
   print("Hemos encontrado el numero")

else:
 print("No  hemos encontrado el numero")




if re.match("\d",cadena2):
   print("Hemos encontrado el numero")

else:
 print("No  hemos encontrado el numero")



#search()



if re.search("López",nombre2):
   print("Hemos encontrado el apellido")

else:
 print("No  hemos encontrado el apellido")



cod1="ksbdnbsdcksbsdcm91nbnmn"
cod2="jkdsk jdkejjd jde91ji jndn"
cod3="nde hjedj jdekd"


if re.search("91",cod2):
	print("Hemos encontrado el codigo")

else:
	print("no hay codigo uu")