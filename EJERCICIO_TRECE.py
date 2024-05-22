#vamos a diseñar una calculadora que se enciende y hasta que no tecleamos SAL no se apaga

#Esta calculadora funciona de la siguiente ,manera:
#Recojemos los datos AyB
#Si operacion es uno calcula la raiz cuadrada de la suma AyB
#Si  operacion es 2 calcula A/B.
#Vigilamos que B no sea o...
#Si la operacion es 3 calculamos la siguiente formula:(A*B)/2.5

# While True:

#print("Bienvenido a ala calculadora. para salir,escriba "SAL."")

operacion=input("ingrese el numero de operacion(1,2 o 3):")

if operacion=="SAL":
    print("hasta luego")
    
 #   break

if operacion not in["1","2","3"]:
    print("operacion no valida.por favor,ingrese 1,2,o 3.")

 #   continue

A=float(input("ingrese el valor de A:"))
B=float(input("ingrese el valor de B:"))

if operacion=="1":
    resultado=(A+B)**0,5
elif operacion=="2":
    if B==0:
        print("no se puede dividir por cero.")
#        continue
    resultado=A/B
elif operacion=="3":
    resultado=(A*B)/2.5

print("el resultado es:",resultado)

