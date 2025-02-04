# Crear los procedimientos
def suma(num1, num2):
    return(num1 + num2)

def resta(num1, num2):
    return(num1 - num2)

def multiplicacion(num1, num2):
     return(num1 * num2)

def division(num1, num2):
    return(num1 / num2)


#mensaje en la pantalla
def calculadora():
    
    print('seleccione su operacion:')
    print('1  suma')
    print('2  resta')
    print('3  multiplicasion')
    print('4  division')
    
    #lee la seleccion de operacion y los valores
    opcion = input()
    num1 = float(input('escribe el primer numero: '))
    num2 = float(input('escriba el segundo numero: '))
    
    
    #realiza las operaciones
    if opcion == '1':
                 print(f"Resultado: {suma(num1, num2)}")
    elif opcion == '2':
                 print(f"Resultado: {resta(num1, num2)}")
    elif opcion == '3':
                 print(f"Resultado: {multiplicacion(num1, num2)}")
    elif opcion == '4':
                 print(f"Resultado: {division(num1, num2)}")
    else:
         print("Operacion no valida")

#ejecutar la calculadora
calculadora()