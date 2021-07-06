#12 
#no existe switch en python
edad=-7

#if 0<edad<100:print("Edad correcta")
#else: 	print("edad incorrecta")


salario_presidente=int(input("Introduce salario del presidente"))
print("salario presidente:"+ str(salario_presidente))

#imprime solo strings


salario_dir=int(input("Introduce salario dir"))
print("salario dir:"+ str(salario_dir))



salario_jefe=int(input("Introduce salario jefe area"))
print("salario jefe area:"+ str(salario_jefe))


salario_adm=int(input("Introduce salario administrativo"))
print("salario administrativo:"+ str(salario_adm))

if salario_adm<salario_jefe<salario_dir<salario_presidente:
	print("todo funciona")
else:
	print("algo anda mal")