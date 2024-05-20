#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
numero=int(input("digite un numero entero: "))

for i in range(1,11):
    print(f"{i} x{numero} = {i*numero}")