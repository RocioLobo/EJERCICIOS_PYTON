#Escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo como el de la imagen adjunta.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

num= int(input("ingrese un numero entero positivo:"))
for i in range(1,num,2):
    print("")
    for j in range(i,0,-2):
        print(j, end=" ")