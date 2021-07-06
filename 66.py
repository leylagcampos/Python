#66 Funciones lambda

#todo lo q se had con lambda se uede hacer de forma normal, pero no viceversa

'''def area_triangulo(base, altura):
	return (base*altura)/2

print(area_triangulo(5,7))

triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(9,6)

print(triangulo1)
print(triangulo2) '''

#----------------------------------------------------------------------------
#funcion lambda

area_triangulo=lambda base, altura:(base*altura)/2

triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(9,6)

print(triangulo1)
print(triangulo2) 
#----------------------------------------------------------------------------
import math 
#al_cubo=lambda numero: numero**3

#al_cubo=lambda numero: math.pow(numero,3)

al_cubo=lambda numero: pow(numero,3)

print(al_cubo(2))

#---------------------------------------------------------------------------
destacar_valor=lambda comision:"¡s/.{}! ".format(comision)

comision_Ana=15589
print(destacar_valor(comision_Ana))