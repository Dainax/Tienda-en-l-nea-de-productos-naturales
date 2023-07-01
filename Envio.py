from Motorizado import Motorizado
from Venta import Venta
from Cliente import Cliente
class Envio():
    def __init__(self, cliente: Cliente, orden: Venta, servicio: str, costo: str, fecha: str):
        self.cliente = cliente
        self.orden = orden
        self.servicio = servicio
        self.costo = costo
        self.fecha = fecha
        
    def show(self):
        return f"""
        Cliente: {self.cliente}
        Orden: {self.orden}
        Servicio de envio: {self.servicio}
        costo: {self.costo}
        fecha: {self.fecha} 
        """
class Delivery(Envio):
    def __init__(self, cliente: Cliente, orden: Venta, servicio: str, costo: str, fecha: str, motorizado: Motorizado):
        super().__init__(cliente, orden, servicio, costo, fecha)
        self.motorizado = motorizado
        
    def show(self):
        return f"""
        Cliente: {self.cliente}
        Orden: {self.orden}
        Servicio de envio: {self.servicio}
        costo: {self.costo}
        fecha: {self.fecha} 
        Motorizado {self.motorizado}
        """