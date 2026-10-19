# if(condicion):
#     if(condicion2):
#
# for(i):
#     for(j):
#
# while():
#     while():

#
#   Transacciones de banco:
#   Creación de su propia cuenta: saldo_inicial
#   Depositar dinero
#   Retirar dinero
# #

def Depositar(saldo_usuario,deposito):
    if(deposito<0):
        print('El monto que desea depositar no es válido')
    else:
        saldo_usuario += deposito
    return saldo_usuario

def Retirar(saldo_usuario,retiro):
    transaccion = False
    if(retiro<0):
        print('El monto que desea retirar no es válido')
    else:
        if(saldo_usuario>= retiro):
            saldo_usuario -=  retiro
            transaccion = True
        else:
            print("No contamos con el monto necesario para realizar dicho retiro")
    return saldo_usuario,transaccion


saldo_usuario = float(input("Ingresa el monto inicial a tu cuenta"))
mensaje= """
Indique qué proceso desea realizar
1.- Depositar
2.- Retirar
3.- Salir
"""
while(True):
    print(mensaje)
    decision = int(input('Indica el número de la acción que deseas realizar: '))
    if(decision ==1):
        deposito = float(input("Ingrese el monto a depositar: "))
        saldo_usuario = Depositar(saldo_usuario,deposito)
        print(f'El monto: {deposito} ha sido depositado, tu saldo actual es de {saldo_usuario}')
    elif(decision == 2):
        retiro = float(input("Ingrese el monto a retirar: "))
        saldo_usuario,transaccion = Retirar(saldo_usuario, retiro)
        if(transaccion):
            print(f'El monto: {retiro} ha sido retirado, tu saldo actual es de {saldo_usuario}')
        else:
            print(f'No se pudo efectuar tu solicitud, tu saldo actual es de {saldo_usuario}')
    elif(decision ==3):
        break
    else:
        print("La acción que desea realizar no es válida")

