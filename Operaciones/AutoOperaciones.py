from Persistencia import BaseDeDatosCONEXION
from Modelos import Auto
from Persistencia.BaseDeDatosCONEXION import BaseDeDatos



def registrar_auto(auto: Auto):
        db = BaseDeDatos()
        query = '''
            INSERT INTO Auto (vin, marca, modelo, año, precio, estado, cliente_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        params = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado, auto.cliente_id)
        if db.execute_query(query, params):
            print("Auto registrado exitosamente.")
        else:
            print("Error al registrar el auto.")

