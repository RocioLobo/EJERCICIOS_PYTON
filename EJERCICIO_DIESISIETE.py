# Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:
# Verificar el saldo de su cuenta.
# Depositar dinero en su cuenta.
# Retirar dinero de su cuenta.
# Salir del programa.
#El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
# Verificar saldo
# Depositar dinero
#Retirar dinero
# Salir

Total=1000
print("vienvenidoal banco\n")
#QUe desea hacer
# Depositar dinero en su cuenta.
# Retirar dinero de su cuenta.
# Salir del programa.
opcion=int(input())
if opcion==1:
    ingreso=float(input("¿cuanto dinero desea ingresar?:"))
    Total+=ingreso
    print(f"tu saldo es de{Total:.2f}")
if opcion==2:
    egreso=float(input("¿cuanto dinero deseas sacar?:"))
    if Total-egreso<0:
        print(f"no tiene mucho dinero tu saldo es de {Total:.2f})
    else:
    total-=egreso
    print(f"tu saldo es de{Total:.2f}")
if opcion==3:



