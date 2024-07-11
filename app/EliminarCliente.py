def eliminar_cliente(listaClientes):
    salir = ""
    while salir != "volver":
        print("La lista de clientes actual es la siguiente:")
        print(listaClientes)
        id = input("Introduzca el ID del cliente que desea eliminar. O escriba 'volver' para salir: ")
        if id == "volver":
            return
        encontrado = False
        for cliente in listaClientes:
            if cliente.id == int(id):
                listaClientes.remove(cliente)
                print("Cliente eliminado correctamente")
                encontrado = True
                break
        if not encontrado:
            print("No se ha encontrado ningún cliente con ese ID")
        print("La lista de clientes actualizada es la siguiente:")
        print(listaClientes)
        return listaClientes
