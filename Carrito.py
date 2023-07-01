class Carrito:

  def __init__(self, name: str, description: str, price: int, category: str,):
    self.name = name
    self.description = description
    self.price = price
    self.category = category

  def show(self):
    return f"""
    Nombre: {self.name}
    Descripcion: {self.description}
    Precio: {self.price}
    Categoria: {self.category} 
    """