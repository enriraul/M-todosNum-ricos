#
# 
# 
#       Funciones
# 
#
#
#       def  nombreFuncion (parámetro1, parámetro2, ..., parámetro_n):
# #

def Presentar(nombre, edad):
    #print(f"Hola, me llamo {nombre} y tengo {edad} años")
    #print("Hola, me llamo "+nombre+" y tengo "+str(edad)+" años")
    #print("Hola, me llamo {0} {0}{0} y tengo {1}".format(nombre,edad))
    return "Hola, me llamo "+nombre+" y tengo "+str(edad)+" años"


# nombre = input("Ingresa tu nombre: ")
# edad = int(input("Ingresa tu edad: "))
# presentacion =Presentar(nombre,edad)
# print(presentacion)
#
#   print(cadena)
#   print(f" {} ") f-string
#   print(" {0} {1}".format(variable0,variable1))
# 
# #

def Factorizacion(numero):
    numero_factorial = 1.0
    for i in range(numero):
        numero_factorial = numero_factorial*(i+1)
    return numero_factorial

# print(Factorizacion(10))
# print(Factorizacion(3))
# print(Factorizacion(8))

def Par(numero):
    if(numero%2==0):
        print(f'{numero} es par')
    else:
        print(f'{numero} es impar')
