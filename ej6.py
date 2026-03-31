import os
os.system("cls")

tareas = []

while True:
    os.system("cls")
    print("\n1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    
    opcion = input("\nElige una opción: ").strip()
    
    if opcion == "1":
        os.system("cls")
        descripcion = input("Descripción: ").strip()
        fecha = input("Fecha de vencimiento: ").strip()
        tareas.append({"descripcion": descripcion, "fecha": fecha, "completada": False})
        print("Tarea agregada")
        input("Presiona ENTER para continuar")
    
    elif opcion == "2":
        os.system("cls")

        if not tareas:
            print("No hay tareas")
        else:
            print("\nTareas:")
            i = 1
            for tarea in tareas:
                estado = "✓" if tarea["completada"] else " "
                print(f"{i}. [{estado}] {tarea['descripcion']} - {tarea['fecha']}")
                i += 1
        input("\nPresiona ENTER para continuar")
    
    elif opcion == "3":
        os.system("cls")
        if not tareas:
            print("No hay tareas")
            input("Presiona ENTER para continuar")
        else:
            i = 1
            for tarea in tareas:
                estado = "✓" if tarea["completada"] else " "
                print(f"{i}. [{estado}] {tarea['descripcion']}")
                i += 1
            
            indice = int(input("Número de tarea: ")) - 1
            tareas[indice]["completada"] = True
            print("Tarea completada")
            input("Presiona ENTER para continuar")
    
    elif opcion == "4":
        os.system("cls")
        if not tareas:
            print("No hay tareas")
            input("Presiona ENTER para continuar")
        else:
            i = 1
            for tarea in tareas:
                print(f"{i}. {tarea['descripcion']}")
                i += 1
            
            indice = int(input("Número de tarea a eliminar: ")) - 1
            tareas.pop(indice)
            print("Tarea eliminada")
            input("Presiona ENTER para continuar")
    
    elif opcion == "5":
        break