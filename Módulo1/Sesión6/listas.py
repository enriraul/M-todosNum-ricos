# lista = [e1,e2,e3,e4,e5]
# [0,1,2,3,4]

# lista =[]
# print(lista)
#
#   append(x): Agrega un elemento en la última posición de la lista
#   lista.append(x)
# 
# #

# nPersonas = int(input("Indica cuántas persoans serán ingresadas"))
# pacientes = []

# for i in range(nPersonas):
#     nombre = input("Ingresa tu nombre: ")
#     edad = int(input("Ingresa tu edad: "))
#     alta = input("Se encuentra dado de alta: sí/no")
#     pacientes.append([nombre, edad, alta])

# print(pacientes)



#
# 
#   Métodos más útilizados en listas
# 
# #

# a=[1,2,3,7,5,0,5,2,4]

# len(): devuelve el numero de elementos que tiene una lista
# len(nombreLista)

# for i in range(len(a)):
#     print(a[i])

#
#  insert(i,x): Agrega un elemento x, en la posición i
#   nombreLista.insert(i,x)
# 
# #
# a.insert(0,0)
# print(a)

# b = ['a','b']
#
# a.extend(b)
# 
# #
# a.extend(b)

#
#  remove: elimina un elemento especificado
#  Warning: elimina la primera coincidencia
#  
# #

# b = a.remove(5)

#
# pop: Elimina y retorna la primera coincidencia de la lista
# ValorEliminado = nombreLista.pop(elemento)
# #

# b = a.pop(5)

#
# 
#  index: Retorna la posición de la primera coincidencia 
#  
#  nombreLista.index(elemento)
# #

# posElemento = a.index(2)

#
#  clear = elimina/limpia la lista de todos los elementos
# #
#print(a.clear(),a)

#
#  sort() - ordena de menor a mayor los elementos
#  reverse() - ordena de mayor a menor los elementos
# #

# a.sort()
# a.reverse()
# print(a)

# a = [i/100.0 for i in range(100)]


b = [[1,2],[3,40],[6,5],[8,7]] #Matriz nxm

# for i in range(len(b)):
#     for j in range(len(b[i])):
#         print(b[i][j])

#
#  Solicitar al usuario dos arreglos: 
#  1a Opción: Solicitar el tamaño de la lista. 
#  2a Opción: Implementación de split(). 
# 
# #

# lista = input("Ingrese los datos separandolos por una coma")
# lista = lista.split(',')
# print(lista)

# Solicitar al usuario el tamaño de la lista. 
# Solicitar los datos suficientes para completar 2 listas, e imprimir cada lista por separado

# Tamaño = int(input("Ingresa el tamaño de cada lista: "))
# Listas = []
# for i in range(2): #Número de listas
#     print(f'Datos para la lista número {i+1}')
#     lista_i =[]
#     for j in range(Tamaño): #Tamaño de cada unas listas
#         dato_j = int(input(f"Valor del elemento {j+1}: "))
#         lista_i.append(dato_j)
#     print(lista_i[0:Tamaño])
#     Listas.append(lista_i)

# print(Listas)

Tamaño = int(input("Ingresa el tamaño de cada lista: "))
Listas = []
for i in range(2): #Número de listas
    print(f'Datos para la lista número {i+1}')
    for j in range(Tamaño): #Tamaño de cada unas listas
        dato_j = int(input(f"Valor del elemento {j+1}: "))
        Listas.append(dato_j)


lista1 = Listas[0:Tamaño]
lista2 = Listas[Tamaño:2*Tamaño]
print(lista1, lista2)
