
def buscar_cliente(listaClientes):
    busqueda = ""
    caracteristica = ""
    while busqueda != "volver":
        print("Introduzca el filtro de búsqueda: ")
        print("Por ID - 1")
        print("Por nombre - 2")
        print("Por email - 3")
        print("Por teléfono - 4")
        print("Escriba 'volver' para volver: ")
        filtro = input()
        if(filtro == "volver"):
            return
        if(filtro != "1" and filtro != "2" and filtro != "3" and filtro != "4"):
            print("Opción no válida")
            continue
        print("Introduzca el valor de búsqueda: ")
        if filtro == "1":
            caracteristica = "id"
        elif filtro == "2":
            caracteristica = "nombre"
        elif filtro == "3":
            caracteristica = "email"
        elif filtro == "4":
            caracteristica = "telefono"

        busqueda = input()
        busqueda = busqueda.lower()
        encontrado = False
        for cliente in listaClientes:
            if busqueda in getattr(cliente, caracteristica).__str__().lower():
                print(cliente)
                encontrado = True
        if not encontrado and busqueda != "volver":
            print("No se ha encontrado ningún cliente con esos datos")