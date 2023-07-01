from Cliente import Cliente
from Desglose import Desglose
class Venta():
    def __init__(self, cliente: Cliente, compras: list, metpago: str, metenvio: str, factura: Desglose, fecha: str):
        self.cliente = cliente
        self.compras = compras
        self.metpago = metpago
        self.metenvio = metenvio
        self.factura = factura
        self.fecha = fecha
        
    def show(self):
        return f"""
        -----------------------------
        Cliente: {self.cliente.show()}    
        ----------------------------- 
        metodo de pago : {self.metpago}
        -----------------------------
        metodo de envio: {self.metenvio}
        -----------------------------
        factura:
        -----------------------------
        {self.factura.show()} 
        -----------------------------
        fecha: {self.fecha}
        """