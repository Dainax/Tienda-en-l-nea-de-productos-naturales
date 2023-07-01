class Desglose:
    def __init__(self, subtotal: float, descuento: int, iva: float, igtf: float, total: float ):
        self.subtotal = subtotal
        self.descuento = descuento
        self.iva = iva
        self.igtf = igtf
        self.total = total
        pass
    
    def show(self):
        return f"""
        Subtotal: ${self.subtotal}
        Descuentos: {self.descuento}%
        IVA: 16% - ${self.iva} 
        IGTF: 3% {self.igtf}
        Total: ${self.total}
        """