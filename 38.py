#38 archivoexternosII :manipulación del puntero
from io import open

archivo_texto=open("archivopython2.txt","r")

print(archivo_texto.read())  #puntero al inicio del contenido del txt, y empieza a leer
print(archivo_texto.read())  #cuando termina de leer el puntero se encuentra al final, por lo tanto no imprime nada



#seek()

print("*********Usando seek *********")

archivo_texto.seek(0)      #puntero se regresa al principio
print(archivo_texto.read())  


archivo_texto.seek(9)  #puntero en el caracter de la posicion 9(contando vacios tmbn)  e imprime lo de la pos7 y lo demás 
print(archivo_texto.read())

archivo_texto.seek(0)
print(archivo_texto.read(9)) #lee hasta donde diga que se posicione el puntero,sin lo que este en la pos7 y adelante

#seguir imprimiendo desde donde se quedó
print(archivo_texto.read())


archivo_texto.seek(0) 
#leyendo desde la mitad
archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())


# leer desde la sigueinte linea
archivo_texto.seek(0) 
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())


#LECTURA Y ESCRITURA   r+

archivo_texto1=open("archivopython3.txt","r+")
#archivo_texto1.write("JUGOS")   
#print(archivo_texto1.read()) #no aparece modificado aun
print(archivo_texto1.readlines())


#modificamos  una linea del txt 

archivo_texto1.seek(0) 
lista_texto=archivo_texto1.readlines()
lista_texto[1]="linea insertada \n"

archivo_texto1.seek(0)
archivo_texto1.writelines(lista_texto)
archivo_texto1.close()