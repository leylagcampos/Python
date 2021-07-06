Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hola mundo")
hola mundo
>>> # prompt >>>
... 
>>> #instruccion es una linea de codigo, no hay punto y coma, con enter se ejecuta.
... 
>>> print("hola alumnos");print("bye mundo")
hola alumnos
bye mundo
>>> #no es una practica recomendable
... 
>>> mi_nombre="mi nombre es paulina"
>>> mi_nombre
'mi nombre es paulina'
>>> mi_nombre="mi nombre es\juan"
>>> 
>>> mi_nombre
'mi nombre es\\juan'
>>> mi_nombre=" mi nombre es \  juan"
>>> mi_nombre
' mi nombre es \\  juan'
>>> a=0
>>> for i in range(6):
... a+=1
  File "<stdin>", line 2
    a+=1
    ^
IndentationError: expected an indented block
>>> for i in range(6):  a+=1 print(a)
  File "<stdin>", line 1
    for i in range(6):  a+=1 print(a)
                                 ^
SyntaxError: invalid syntax
>>> for i in range(6):
...  a+=1  ; print(a)
... 
1
2
3
4
5
6
>>> 