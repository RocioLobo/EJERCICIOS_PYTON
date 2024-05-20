#Escriba un programa que pregunte cuantos numeros se van a introducir, pida esos numeros y escriba cuantos negativos a introducido.

print ('Cuantos numeros desea introducir?')
numN=int(input())

contadorneg=0
for numero in range(1,numN+1):
    print ('Escriba el numero %s'% str(numero))
    nNumeros=float(input())
    if nNumeros<0:
        contadorneg=contadorneg+1
        
print ('Ha escrito %s numeros negativos.'% str(contadorneg))