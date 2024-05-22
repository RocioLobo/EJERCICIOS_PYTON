#Desarollara una lista en pyton que permita gestionar una lista de tareas pendientes.El programa debe cumplir con los siguientes requisitos:
#Debe permitir agregar nuevas tareas a la lista.
#Debe permitir marcar tareas como completadaslo que las eliminara de la lista de tareas pendientes.
#Debe proporcionar un menu interactivo que permitira al usurio seleccionar entre las opciones anteriores y salir del programa. el menu debe presentar las siguientes opciones.
#Agregar tarea
#Marcar tarea como completada.
#mostrar tareas.
#salir

lista_de_tareas={}
#Debe permitir agregar nuevas tareas a la lista.
def agregar_tareas():
    tarea=input("ingrese la nueva tarea:")
    nuevo_id=len(lista_de_tareas) +1
    nueva_tarea={"tarea":tarea,"completada":False}
    lista_de_tareas[nuevo_id]=nueva_tarea
    print("tarea agregada a la lista.")

# Marcar tarea como completada.
def marcar_completada():
    tarea_id=int(input("ingrese el numero de tarea que desea marcar como completada:"))
    if tarea_id in lista_de_tareas:
        lista_de_tareas[tarea_id]["completada"]= True
        print("tarea marcada como completada.")
    else:
        print("tarea no encontrada.")

#mostrar tareas.
def mostrar_lista():
    print("\n lista de tareas:")
    for tarea_id,tarea_info in lista_de_tareas.items():
        tarea=tarea_info["tarea"]
        completada=tarea_info["completada"]
#Estado de tareas completadas o pendientes.
estado ="completada" if "completada" else "pendiente"
print(f"{tarea_id}.{tarea}-{estado}")

#menu principal
while True:
    print("\nmenutareas.")
    print("1.Agregar tarea")
    print("2.marcar tarea como completada")
    print("3.mostrar lista de tareas")
    print("4.salir")

#Debe proporcionar un menu interactivo que permitira al usurio seleccionar entre las opciones anteriores y salir del programa.
opcion=input("seleccione una opcion:")
if opcion=="1":
    agregar-tarea()
elif opcion=="2":
    marcar_completada()
elif opcion=="3":
    mostrar_lista()
elif opcion=="4":
    print("saliendo del programa.")
#    break
else:
    print("opcion no valida. por favor,seleccione una opcion valida.")




