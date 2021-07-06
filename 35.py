#35
#Paquetes:directorios donde se almacenarán módulos relacionados entre si,
#sirve para organizar y reutilizar módulos, 
#se crea un archivo __init__.py dentro de una carpeta que hará de paquete


from paquete.calculosgenerales import division

division(6,2)


from paquete.calculosgenerales import potencia

potencia(6,2)


from paquete.calculosgenerales import*

resta(6,2)



from paquete.subpaquete.operaciones import*

multiplicar(2,4)