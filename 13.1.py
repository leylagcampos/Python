#in
print("AsignaturasOptativas año 2017")
print("Asiganturas optativas: Informática gráfica - Prueba de software - Usabilidad y accesibilidad")
#asignatura=input("Escribe la asignatura escogida:")

opcion=input("Escribe la asignatura escogida:")

# todo a minusculas con lower() , todo a mayusculas upper()
asignatura=opcion.lower()

if asignatura in ("Informática gráfica","prueba de software","Usabilidad y accesibilidad"):
	print("asignatura elegida: "+ asignatura)
else:
	print("asignatura no contemplada")

#probar con pruebas de software