#crea un algoritmo para la sucesion de fibonaci.la sucesion de fibonaci es la siguiente serie:
0,1,1,2,3,5,8,13,21,34,55,89
#pista:Empezando por 0 y 1el siguiente numero es la suma de los dos numeros ultimos.

num:int = 12  
numero_a, numero_b = 0, 1
count = 0
while count < num:
    print(numero_a, end=", ")
    numero_a, numero_b = numero_b, numero_a + numero_b
    count += 1