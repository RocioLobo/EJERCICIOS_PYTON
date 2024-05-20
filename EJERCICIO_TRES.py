# Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla todos los numeros impares desde 1 hasta ese numero separados por comas.

num=int(input("escriba un numero entero:"))

if num <0:
    print("no se permiten numeros negativos")
else:
    for i in range(1,num+1,2):
        print(i, end=",")
