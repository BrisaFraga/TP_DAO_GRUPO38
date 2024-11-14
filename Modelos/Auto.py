class Auto:
    def __init__(self, vin, marca, modelo, año, precio, estado, cliente_id=None):
        self.vin = vin
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.estado = estado
        self.cliente_id = cliente_id  # Asegúrate de incluir este atributo
