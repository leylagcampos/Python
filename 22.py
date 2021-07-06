def divide():
    try:
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el segundo número: ")))
        print("La división es: "+str(op1/op2))

    except ValueError:
    	print("Valor que se ah introducido es erroneo")

    except ZeroDivisionError:
    	print("No se puede dividir entre cero")

    print("Calculo finalizado")

divide()


#solo poner except:  ,es posible y rapido de implementar pero no recomendable:::

def divide2():
    try:
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el segundo número: ")))
        print("La división es: "+str(op1/op2))

    except:
    	print("ha ocurrido un error")

    print("Calculo finalizado")

divide2()

#finally
def divide3():
    try:
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el segundo número: ")))
        print("La división es: "+str(op1/op2))

    except ValueError:
    	print("Valor que se ah introducido es erroneo")

    except ZeroDivisionError:
    	print("No se puede dividir entre cero")

    finally:             #lo que esta dentro de el siempre se ejecuta asi ocurra o no alguna excepcion
     print("Calculo finalizado")

divide3()


#solo poner finally, no va atrapar ninguna excepcion(mostrara errores),sin embargo se ejecuta lo del finally
def divide4():
    try:
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el segundo número: ")))
        print("La división es: "+str(op1/op2))

    finally:          
        print("Calculo finalizado")

divide4()



#try solo(sin except s ni finally) da error