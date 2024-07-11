from Cliente import Cliente
def agregar_cliente(listaClientes):
    nombre = input("Introduzca un NOMBRE para el cliente. O escriba 'volver' para salir: ")
    if nombre == "volver":
        return listaClientes

    email = input("Introduca un EMAIL para el cliente. O escriba 'volver' para salir: ")
    if email == "volver":
        return listaClientes

    while "@" not in email:
        email = input("El formato no es correcto. Introduca un EMAIL válido para el cliente. O escriba 'volver' para salir: ")
        if email == "volver":
            return listaClientes
    telefono = ""
    while len(telefono) != 9 or not telefono.isdigit():
        telefono = input("Introduzca un TELÉFONO para el cliente (sólo acepta números sin espacios). O escriba "
                         "'volver' para salir: ")
        if telefono == "volver":
            return listaClientes
        if not telefono.isdigit():
            print("El teléfono solo puede contener números.")
        if len(telefono) != 9:
            print("El teléfono debe tener 9 dígitos.")

    id = len(listaClientes) + 1
    cliente = Cliente(id, nombre, email, telefono)
    listaClientes.append(cliente)
    print("Cliente agregado correctamente")
    print("La lista de clientes actualizada es la siguiente:")
    print(listaClientes)
    return listaClientes
