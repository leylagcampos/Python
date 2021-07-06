#37 Archivos externos . objetivo: persistencia de datos, luego podemos  hacer manejo de archivos externos y trabajar con bdd's
#Fases para manejar archivos externos : creacion,apertura,manipulacion y cierre.
#uso de io

from io import open
#open(nombre de archivo ,modo) 
#lectura(r),escritura("w") append ("a")


archivo_texto=open("archivopython.txt","w")
frase="Lindo dia\n jueves"
#abrimos con write
archivo_texto.write(frase)
archivo_texto.close()



archivo_texto=open("archivopython.txt","r")
#leemos con read
texto=archivo_texto.read()
archivo_texto.close()
print(texto)


#readlines para convertir en una lista manipulable

archivo_texto=open("archivopython.txt","r")
lineas_Texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_Texto)
print(lineas_Texto[1])

#abrir el archivo en modo agregar con append
archivo_texto=open("archivopython.txt","a")
archivo_texto.write("\n holi")
archivo_texto.close()
