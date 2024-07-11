import AgregarCliente
import EliminarCliente
import BuscarCliente
import ListarClientes
import listaClientes
from Cliente import Cliente

print("==============================================")
print("Sistema de Gestión de Clientes")
print("==============================================")
print("1. Agregar un cliente")
print("2. Eliminar un cliente")
print("3. Buscar un cliente")
print("4. Listar todos los clientes")
print("5. Salir")
print("==============================================")

listaClientes = listaClientes.listaClientes
def salir():
    print("Saliendo del sistema")
    return


opciones = {
    "1": lambda: AgregarCliente.agregar_cliente(listaClientes),
    "2": lambda: EliminarCliente.eliminar_cliente(listaClientes),
    "3": lambda: BuscarCliente.buscar_cliente(listaClientes),
    "4": lambda: ListarClientes.listar_clientes(listaClientes),
    "5": salir
}

opcion = input("Elija una opción: ")

while opcion != "5":
    funcion = opciones.get(opcion, lambda: print("Opción no válida"))
    funcion()
    print("==============================================")
    print("Sistema de Gestión de Clientes")
    print("==============================================")
    print("1. Agregar un cliente")
    print("2. Eliminar un cliente")
    print("3. Buscar un cliente")
    print("4. Listar todos los clientes")
    print("5. Salir")
    print("==============================================")
    opcion = input("Elija una opción: ")
