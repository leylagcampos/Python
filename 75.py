#75 Documentación

from modulo import funcmat

class Areas:

 """Esta clase se calcula las areas de diferentes figuras geométricas"""
 def areaCuadrado(lado):
 	 """ Calcula el área de un cuadrado elevando al cuadrado el lado pasado por parámetro"""
 	 return "El área del cuadrado es: "+ str(lado+lado)

 def areaTriangulo(base,altura):
	 """Calcula el área del triangulo utilizando los parámetros base y altura"""
	 return "El área del triangulo es : "+ str((base*altura)/2)


print(Areas.areaTriangulo(2,7))
print("----------------------------")
help(Areas)
print("----------------------------")
help(Areas.areaTriangulo)
print("----------------------------")
print(Areas.areaCuadrado.__doc__)
print("----------------------------")
print(Areas.areaCuadrado(3))
print("----------------------------")
help(Areas.areaCuadrado)


help(funcmat)





