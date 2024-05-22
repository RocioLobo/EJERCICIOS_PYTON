# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
while True:
    contrasena1:str = input("Escriba su contraseña por favor : ")
    contrasena2:str = input("Escriba de nuevo su contraseña por favor: ")
    if contrasena2 == contrasena1:
        print("Contraseña correcta.")
        break
    else:
        print("contraseña incorrecta. Inténtelo de nuevo.")