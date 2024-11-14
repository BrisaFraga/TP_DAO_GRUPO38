class Venta:
    def __init__(self,auto, cliente, fecha_venta,Id_vendedor, id: int=None):
        self.id = id
        self.auto = auto
        self.cliente = cliente
        self.fecha_venta = fecha_venta
        self.vendedor = Id_vendedor