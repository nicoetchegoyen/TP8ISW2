#Calculando el número de iteraciones del algoritmo de Collatz
def collatz(num):
    iteraciones = 0
    
    #Valida que el numero este en el rango de 1 a 1999
    if num < 1 or num > 1999:
        raise ValueError("El número debe estar entre 1 y 1999")
    
    #Aplicar la conjetura de Collatz
    while num != 1:
        if num % 2 == 0:
            num = num // 2  #Si es par se divide entre 2
        else:
            num = 3*num + 1  #Si es impar se multiplica por 3 y se suma 1
        iteraciones += 1
    return iteraciones

#Ingrese un numero entero positivo entre 1 y 1999
i =  1500

try:
    #Intentar convertir la entrada a numero
    i = int(i)
    print("El número de iteraciones para %d es %d\n" % (i, collatz(i)))
except ValueError as e:
    print(f"Error: {e}. Asegúrate de ingresar un número válido.")
except TypeError as e:
    print(f"Error: {e}. Tipo de dato no soportado.")
