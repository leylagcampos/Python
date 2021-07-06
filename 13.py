#13
#operadores  de comparacion, logicos: and or,in
print("Porgrana de becas 2017")
dist_escuela=int(input("introduce distancia a la escuela en km:"))
print(dist_escuela)

numero_hmn=int(input("introduce el numero de hermanos en el centro:"))
print(numero_hmn)

salario_familiar=int(input("introduce salario anual bruto:"))
print(salario_familiar)

if dist_escuela>40 and numero_hmn>2 or salario_familiar<=20000:
	print("tiene derecho a beca")
else:
	print("no tiene derecho a beca")