#Escriba un programa que pregunte cuantos numeros se van introducir, pida los esos numeros (que puedan ser decimales)y calcule su suma, mostrar por terminal la suma de los numeros introducidos.

print ("¿Cuántos valores va a introducir?")
num= int(input())

suma=0
for numero in range(1,num+1):
    print ('Escribe el numero %s'% str(numero))
    nN=float(input())
    suma= suma+nN
print ('La suma de los %s numeros introducidos es %s' % (str(num),str(suma)))