import math

'''
Esto es un bloque de comentarios
'''
def main():
    '''
     esta es una function main
    '''
    print("Hello World")
    print("otra instruccion")
    holaSoyUnaVariable = 4
    holaSoyUnaVariable = "Hola de nuevo"
    print(holaSoyUnaVariable)
    miVariable = float(input("Ingresa tu edad: "))
    print(miVariable)


    miCondition = (0!=1) and (2 > 1)

    if miCondition:
        print("Hola")
    else:
        print("Esto es un else")
    
    myInput = int(input("Ingrese el numero de mes"))

    myMonth = month(myInput)

    print(myMonth)

'''
    En otros lenguajes de programacion
    if () {

    }else {

    } 
'''

def month(number):
    '''
     esta es una function que devuelve un texto basado en un
     numero del mes
    '''
    condition = (number > 0) and (number <= 12) # chequeo primero que este dentro de los parametros esperados
    mes = "invalido"
    if condition:
        print("valido")

        if number == 1:
            mes = "Enero"
        elif number == 2:
            mes = "febrero"
        elif number == 3:
            mes = "marzo"
        elif number == 4:
            mes = "abril"
        elif number == 5:
            mes = "mayo"
        elif number == 6:
            mes = "junio"
        elif number == 7:
            mes = "julio"
        elif number == 8:
            mes = "agosto"
        elif number == 9:
            mes = "septiembre"
        elif number == 10:
            mes = "octubre"
        elif number == 11:
            mes = "noviembre"
        elif number == 12:
            mes = "diciembre"
        '''
        No existen en Python
        switch(expression) {
            case x:
                // code block
                break;
            case y:
                // code block
                break;
            default:
                // code block
            }
        '''
    else:
        print("Mes invalido")
    
    return mes


if __name__ == "__main__":
    # execute only if run as a script
    main()