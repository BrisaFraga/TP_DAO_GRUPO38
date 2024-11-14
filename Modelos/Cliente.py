class Cliente:
    def __init__(self,nombre, apellido, direccion, telefono,id:int=None):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.id=id