class Motorizado:
    def __init__(self, name: str, last_name: str, cellphone: str):
        self.name = name
        self.last_name = last_name
        self.cellphone = cellphone
        
    def show(self):
        return f"""
        Nombre: {self.name}
        Apellido: {self.last_name}
        Telefono: {self.cellphone}
        """
        