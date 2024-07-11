class Cliente:
    def __init__(self, id, nombre, email, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def get_nombre(self, nombre):
        return self.nombre

    def get_email(self, email):
        return self.email

    def get_telefono(self, telefono):
        return self.telefono

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_email(self, email):
        self.email = email

    def set_telefono(self, telefono):
        self.telefono = telefono

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}\n"

    # Esto permite que al llamar a un objeto de tipo Cliente, éste se vea como un string en lugar de su representación en memoria
    def __repr__(self):
        return self.__str__()
