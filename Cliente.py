class Cliente:
    def __init__(self, name:str , last_name: str, dni: str, email: str, direction:str , cellphone: str):
        self.name = name
        self.last_name = last_name
        self.dni = dni
        self.email = email
        self.direction = direction
        self.cellphone = cellphone

    def show(self):
        return f"""
        Nombre: {self.name}
        Apellido: {self.last_name}
        DNI: {self.dni}
        Email: {self.email}
        Direction: {self.direction} 
        Telefono: {self.cellphone}
        """