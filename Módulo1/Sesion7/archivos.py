#f = open(DireccionArchivo, modo)
#   Modo:
#       'r' Lectura, debe existir el archivo.  No vamos a poder 
#           hacer actualizaciones o modificaciones a los datos 
#           del archivo
#       'w' Escritura, crea o sobreescribimos archivo. 
#
#       'a' Los nuevos valores/datos son agregados en la última línea. 
#           Si no existe, se crea.
#
#       'r+' Lectura y Escritura, no podemos eliminar elementos
# 
##
def CargarDatos(nombreArchivo):
    dato=[]
    f = open(nombreArchivo,'r', encoding='utf-8')
    for linea in f:
        dato_linea = linea.replace('\n','').split(',')
        dato_linea[2] = int(dato_linea[2])
        dato.append(dato_linea)
    f.close()
    return dato

def EscribirDatos(nombreArchivo, datos):
    f = open(nombreArchivo,'a',encoding='utf-8')
    for dato in datos:
        cadena = dato[0]+","+dato[1]+","+str(dato[2])+","+dato[3]+"\n"
        f.write(cadena)
    f.close()



#f.write(cadena)


#Bubblesort

# def CargarDatos(nombreArchivo):
#     with open(nombreArchivo,'r', encoding='utf-8') as f:
        # contenido = f.read()
        # print(contenido)
        # for linea in f:
        #     print(type(linea.strip()))
        # lineas = f.readlines()
        # print(lineas)

# datos = CargarDatos("datos.txt")
# EscribirDatos("datos_prueba.txt",datos)


def BubbleSort1(datos):

    for i in range(len(datos)-1):
        for j in range(i+1,len(datos)):
            if datos[i] > datos[j]:
                datos[i],datos[j] = datos[j],datos[i]
                # aux = datos[i]
                # datos[i] = datos[i+j]
                # datos[i+j]= aux
    return datos
print(BubbleSort1([1,5,8,2,7,5,0,10,4,6,3]))


# def Ordenar(datos):
#     for i in range(len(datos)-1):
#         for j in range(i+1,len(datos)):
#             if datos[i][2] > datos[j][2]:


# clientes=  [[nombre, apellido, edad],...,[nombre, apellido, edad]]
#sort(clientes, key=lambda, cliente: cliente[2])