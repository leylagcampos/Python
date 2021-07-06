#68 Map :aplica una función a cada elemento de una lista iterable(listasmtuplas,etc),devolviendo una lista con resultados


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



def comision_calculo(empleado):

	if(empleado.salario<=50000):
		empleado.salario=empleado.salario*1.03

	return empleado


lista_Econcomision=map(comision_calculo,listaEmpleados)

for empleado in lista_Econcomision:
	print(empleado)

