#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la ultima.

palabra=input("igrese una palabra por favor:")

for i in range(len(palabra)-1,-1,-1):
    print(palabra[i])