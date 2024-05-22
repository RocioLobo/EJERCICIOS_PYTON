#Tenemos la pantalla del movil bloqueada.partiendo de un PIN_SECRETO,intentaremos desbloquear la pantalla Tenemos hasta 3 intentos.Simula el proceso con pyton.En caso de acceder,lanza al usuario login correcto.Sino,llamando a la policia.
i=0
while i<3:
      usuario=input("ingrese su nombre de usuario")
      i=i +1
      if str(usuario)=="rocio":
            print("USUARIO CORRECTO")
            clave=input("ingrese su clave")
            if str(clave)=="linda":
                  print("login correcto")
                  break
            else:
                  print("CLAVE INCORRECTA")
                  if    i==3:
                        print("llamando a la policia")
                        break
      else:
            print("USUARIO INCORRECTO")
            if    i==3:
                  print("INTENTOS AGOTADOS")