from Persistencia import BaseDeDatosCONEXION
from Modelos import Cliente
from Persistencia.BaseDeDatosCONEXION import BaseDeDatos



def consultar_clientes_bd():
    db = BaseDeDatos()
    query = """
        SELECT id, nombre, apellido 
        FROM Cliente 
        ORDER BY apellido, nombre
    """
    clientes = db.fetch_query(query)
    if clientes:
        return clientes
    else:
        print("No se encontraron clientes.")
        return []


def registrar_cliente(cliente: Cliente):
    db = BaseDeDatos()
    query = '''
        INSERT INTO Cliente (nombre, apellido, direccion, telefono)
        VALUES (?, ?, ?, ?)
    '''
    params = (cliente.nombre, cliente.apellido, cliente.direccion, cliente.telefono)
    if db.execute_query(query, params):
        print("Cliente registrado exitosamente.")
    else:
        print("Error al registrar el cliente.")

def consultar_autos_vendidos(cliente_id):
    db = BaseDeDatos()
    query = """
        SELECT a.vin, a.marca, a.modelo, a.año, a.precio
        FROM Auto a
        JOIN Venta v ON a.vin = v.auto_vin
        WHERE v.cliente_id = ?
    """
    autos = db.fetch_query(query, (cliente_id,))

    # Crear una lista de autos vendidos
    autos_vendidos = []
    if autos:
        for auto in autos:
            autos_vendidos.append({
                'vin': auto[0],
                'marca': auto[1],
                'modelo': auto[2],
                'año': auto[3],
                'precio': auto[4]
            })
    else:
        print("No se encontraron autos vendidos para este cliente.")

    return autos_vendidos