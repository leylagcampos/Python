#67 Filter , funcion de orden superior que permite la programación funcional
'''esta funcion verifica q los elementos de una secuencia cumplen una condición
 devolviendo un iterador con los elementos que cumplen dicha condición'''


def numero_par(num):
 	if num % 2 ==0 :
 		return True


numeros=[17,24,6,22,12,54,98]

print(list(filter(numero_par,numeros)))


#tambien(filter ft lambda):
print(list(filter(lambda numero_impar: numero_impar%2!=0,numeros)))


class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} $ ".format(self.nombre,self.cargo,self.salario)


listaEmpleados=[
Empleado("Juan","Director",78222),
Empleado("Dora","Presidenta",76363),
Empleado("Hugo","CEO",83833),
Empleado("Sonia","Partner",102222),
Empleado("Diana","Jefe de ventas",43394),
Empleado("Rosario","Finanzas",52737),


]

salarios_altos=filter(lambda empleado:empleado.salario>70000,listaEmpleados)


for empleado_salario in salarios_altos:
	print(empleado_salario)