from Persistencia import BaseDeDatosCONEXION
from Modelos import Servicio
from Persistencia.BaseDeDatosCONEXION import BaseDeDatos



def registrar_servicio(servicio: Servicio):
    db = BaseDeDatos()

    # Verificar el estado del auto
    auto_estado_query = '''
            SELECT cliente_id FROM Auto WHERE vin = ?
        '''
    auto_estado = db.fetch_query(auto_estado_query, (servicio.auto,))

    # Verificar si el auto está vendido
    if not auto_estado or auto_estado[0][0] is None:
        print("El servicio debe estar asociado a un auto vendido.")
        return False

    # Registrar el servicio
    registrar_servicio_query = '''
            INSERT INTO Servicio (auto_vin, tipo_servicio, fecha, costo)
            VALUES (?, ?, ?, ?)
        '''
    params = (servicio.auto, servicio.tipo_servicio, servicio.fecha, servicio.costo)

    if db.execute_query(registrar_servicio_query, params):
        print("Servicio registrado exitosamente.")
        return True
    else:
        print("Error al registrar el servicio.")
        return False



def consultar_servicios_auto(vin):
    db = BaseDeDatos()
    query = """
        SELECT s.id, s.tipo_servicio, s.fecha, s.costo
        FROM Servicio s
        JOIN Auto a ON s.auto_vin = a.vin
        WHERE a.vin = ?
    """
    servicios = db.fetch_query(query, (vin,))

    # Crear una lista de servicios realizados
    servicios_realizados = []
    if servicios:
        for servicio in servicios:
            servicios_realizados.append({
                'id': servicio[0],
                'tipo_servicio': servicio[1],
                'fecha': servicio[2],
                'costo': servicio[3]
            })
    else:
        print("No se encontraron servicios para este auto.")

    return servicios_realizados  # Devuelve la lista de servicios realizados
