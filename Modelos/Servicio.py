class Servicio:
    def __init__(self, auto, tipo_servicio, fecha, costo, id : id=int):
        self.id = id
        self.auto = auto
        self.tipo_servicio = tipo_servicio
        self.fecha = fecha
        self.costo = costo