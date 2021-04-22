import os
from agenda import Agenda
from tabulate import tabulate

option = ""
headers = ["ID", "NOMBRE", "APELLIDO", "EDAD", "TELEFONO", "EMAIL"]
run = Agenda()
while option != "4":
    os.system('cls')
    print("[1]agregar registro")
    print("[2]buscar y editar registro")
    print("[3]ver registros")
    print("[4]salir")

    option = input("opcion:")

    if option == "1":
        os.system('cls')
        print("---REGISTRO---")
        run.agregar_contacto(
                      input("nombre:"),
                      input("apellido:"),
                      eval(input("edad:")),
                      input("telefono:"),
                      input("email:")
                      )
        
        input("Contacto Registrado, presione enter para continuar...")
    elif option == "2":
        """
        select here we select the type of search,
        filtrar is attribute to filter,
        mod is how we want to filter,
        its value is given automatically select have a value.
        """
        select = ""
        while select != "4":
            # graphis option
            os.system('cls')
            print("buscar por:")
            print("  1-nombre")
            print("  2-apellido")
            print("  3-tel")
            print("4-atras")
            
            # selection,type of search
            select = input("seleccionar:")
            if select == "1":
                name = input("ingrese nombre:")
                filtrar = name
                mod = "Nombre"
            elif select == "2":
                last_name = input("ingrese apellido:")
                filtrar = last_name
                mod = "Apellido"
            elif select == "3":
                tel = input("ingrese tel:")
                filtrar = tel
                mod = "Telefono"
            elif select == "4":
                break
            else:
                select = "5"
                print("tecla incorrecta")
                
            if select != "5":
                result = run.buscar(filtrar, mod)
                print(tabulate(result, headers=headers, tablefmt="grid"))
                
                editar = ""
                while editar != "2":
                    print("\n[1]editar [2]atras")
                    editar = input(">>>")    
                # here we use what we filter to be able to edit the field
                    if len(result) > 0 and editar == "1":
                        index = eval(input("ingrese el ID:"))
                        change = input("ingrese su nuevo "+mod+":")
                        run.edit(index, change)
                        result = run.buscar(filtrar, mod)
                        print(tabulate(result, headers=headers,tablefmt="grid"))
                      
                
                    
                    
    elif option == "3":
        os.system('cls')
        data = run.listar()
        print(tabulate(data, headers=headers, tablefmt="grid"))
        input("enter para ir atras...")
    elif option != "4":
        input("selecciono incorrectamente")
