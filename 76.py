#76 Documentación y pruebas
#doctest

def areaTriangulo(base, altura):
	""" 
	Esta función calcula el área de un triangulo dado su base y altura

    >>> areaTriangulo(3,6)
    'El área del trinagulo es : 9.0'

    >>> areaTriangulo(4,5)
    'El área del trinagulo es : 10.0'

    >>> areaTriangulo(9,3)
    'El área del trinagulo es : 13.5'



	"""
	return "El área del trinagulo es : " + str(( base*altura)/2)


#print(areaTriangulo(2,4))


#rfind es si @esta al final

def compruebaMail(mailUsuario):
	"""
	la función compruebaMail evalúa un mail recibido en busca de la @.Si tiene una @
	es correcto, si tiene más de una @ es incorrecto si la @ está al final es incorrecto


    >>> compruebaMail('juan@cursos.es')
    True

    >>> compruebaMail('juancursos.es@')
    False

    >>> compruebaMail('juancursos.es')
    False

    >>> compruebaMail('juan@cursos@.es')
    False

	"""

	arroba=mailUsuario.count('@')

	if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
	 return False

	else:
	 return True  






import doctest

doctest.testmod()