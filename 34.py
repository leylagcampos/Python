#34 
#Módulos.para organizar y reutilizar nuestro código.Son archivos con extension .py o .pyc(python compilado)


import funcmat

funcmat.sumar(23,12)
funcmat.restar(4,1)

#otra forma 

from funcmat import  sumar
sumar(44,33)


#para usar todo  de funcmat
from funcmat import*

sumar(3,4)
producto(3,9)






from vehiculos import*

miCoche=Vehiculos("Mazda","MX5")

miCoche.estado()
