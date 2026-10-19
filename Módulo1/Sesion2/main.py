#
# 
#  Operadores
# 
# 

# Aritmeticos
#
#   + suma a+b
#   - resta a-b
#   * multiplicación a*b
#   / división a/b
#   % modulo 
#   ** a**b  
# 
# #


#  Operadores Lógicos
# 
#  and  conjunción: Todos los elementos deben ser verdaderos 
#  or disyución: Almenos un elemento debe ser verdadero
#  not negación
# 
# #

#  Operadores comparativos
#  
#  == Igual 
#  != Diferentes/ Desiguales
#  > Mayor que
#  < Menor que
#  >= Mayor o igual
#  <= Menor igual
# 
# #

# print()

# edad = 16

# if (edad>=17):
#     print("Tienes la edad suficiente para comenzar con el trámite")
#     print("recordandote que debes estar acompañad@ de un adulto")
# elif(edad>=18):
#     print("Tienes la edad suficiente para comenzar con el trámite")
# else: 
#     print("No cumples con los requisitos solicitados")

#
#   if(condicional):
#       instrucciones
#   elif(condicional):<
#       instrucciones
#   else:
#       instrucciones 
# #


#
# 
# 
#   for -   ciclo basado en un indice que determina la iteración
#           actual, en este tipo de estructura nosotros conocemos
#            cuantas iteraciones realizaremos
#
#
#   for i in range(n):   i: 0 ->  n-1, +1
# #

#factorial
# N_f(n) = n*n-1*n-2*...*2*1 
# numero = 100
# numero_factorial = 1.0
# for i in range(numero):
#     numero_factorial = numero_factorial*(i+1)
    #print(i+1, numero_factorial)

#print(numero_factorial)


#
#   Arreglos - Listas
#   a = [1,2,3,4,5,6,7,8]    
#   posiciones = [0,1,2,3,4,5,6,7]
# #

# a = [1,"Enrique",3.5,True,'5',6,7,8]

# for i in a:
#     print(i)

#
#       Ciclos While
#       while(condición):
#           instrucciones
# 
# #

#
#   input("")
# #

#
#   Entero int
#   Flotante float
#   Cadenas/textos str
#   Boolean bool
# 
# #

# nombre = input("Ingresa tu nombre")
# print(nombre, type(nombre))
# edad = int(input("Ingresa tu edad"))
# print(edad, type(edad))

numero = int(input("Teclea un numero"))

while(numero!=18):
    numero = int(input("Teclea un numero"))


#
#   Vamos a solicitar al usuario un numero personas
#   
#   Solicitar: Nombre, edad, nacionalidad
#   Imprimir la información  
# 
# #