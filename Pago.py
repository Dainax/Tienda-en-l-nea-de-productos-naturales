from Venta import Venta
from Cliente import Cliente
from Desglose import Desglose
class Pago():
    def __init__(self, cliente: Cliente, factura: Desglose, divisa: str, tipo: str, fecha:str ):
        self.cliente = cliente
        self.factura = factura
        self.divisa = divisa
        self.tipo = tipo
        self.fecha = fecha
        
    def show(self):
        return f"""
        Cliente: {self.cliente.show()}
        Monto: {self.factura.show()}
        Moneda del pago: {self.divisa}
        Tipo de pago: {self.tipo} 
        Fecha:: {self.fecha}
        """
