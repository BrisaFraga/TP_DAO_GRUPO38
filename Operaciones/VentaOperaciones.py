from Persistencia import BaseDeDatosCONEXION
from Modelos import Venta
from Persistencia.BaseDeDatosCONEXION import BaseDeDatos


def obtener_ingresos_mensuales_ventas():
    db = BaseDeDatos()
    query = '''
            SELECT strftime('%Y-%m', fecha), SUM(Auto.precio)
            FROM Venta
            INNER JOIN Auto ON Venta.auto_vin = Auto.vin
            GROUP BY strftime('%Y-%m', fecha)
        '''
    resultados = db.fetch_query(query)
    db.close()
    return resultados

def obtener_ingresos_mensuales_servicios():
    db = BaseDeDatos()
    query = '''
            SELECT strftime('%Y-%m', fecha), SUM(costo)
            FROM Servicio
            GROUP BY strftime('%Y-%m', fecha)
        '''
    resultados = db.fetch_query(query)
    db.close()
    return resultados

def obtener_ventas_por_marca():
    db = BaseDeDatos()
    query = '''
            SELECT Auto.marca
            FROM Venta
            INNER JOIN Auto ON Venta.auto_vin = Auto.vin
        '''
    resultados = db.fetch_query(query)
    db.close()
    return resultados
def registrar_venta(venta: Venta):
    db = BaseDeDatos()

    # Comprobar si el auto ya tiene un cliente asignado
    auto_cliente_query = '''
        SELECT cliente_id FROM Auto WHERE vin = ?
    '''
    auto = db.fetch_query(auto_cliente_query, (venta.auto,))

    # Verificar si el auto ya ha sido vendido
    if auto and auto[0][0] is not None:
        print("El auto ya ha sido vendido a otro cliente.")
        return False

    # Registrar la venta e intentar actualizar el cliente en la tabla Auto
    registrar_venta_query = '''
        INSERT INTO Venta (auto_vin, cliente_id, fecha_venta, vendedor_id)
        VALUES (?, ?, ?, ?)
    '''
    update_auto_query = '''
        UPDATE Auto SET cliente_id = ? WHERE vin = ?
    '''

    try:
        if db.execute_query(registrar_venta_query, (venta.auto, venta.cliente, venta.fecha_venta, venta.vendedor)):
            db.execute_query(update_auto_query, (venta.cliente, venta.auto))
            print("Venta registrada exitosamente.")
            return True
    except Exception as e:
        print(f"Error al registrar la venta: {e}")
        return False


def ventas_por_periodo(fecha_inicio, fecha_fin):
    db = BaseDeDatos()
    query = '''
        SELECT * FROM Venta WHERE fecha_venta BETWEEN ? AND ?
    '''
    ventas = db.fetch_query(query, (fecha_inicio, fecha_fin))

    if not ventas:
        print("No se encontraron ventas en el periodo especificado.")

    return ventas


def autos_mas_vendidos_por_marca():
    db = BaseDeDatos()
    query = '''
        SELECT marca, modelo, COUNT(*) AS cantidad
        FROM Venta
        JOIN Auto ON Venta.auto_vin = Auto.vin
        WHERE Auto.cliente_id IS NOT NULL  -- Solo contar autos vendidos
        GROUP BY marca, modelo
        ORDER BY marca, cantidad DESC
    '''

    resultados = db.fetch_query(query, ())

    # Procesar resultados para obtener el modelo más vendido por marca
    autos_mas_vendidos = {}
    for marca, modelo, cantidad in resultados:
        if marca not in autos_mas_vendidos or autos_mas_vendidos[marca][1] < cantidad:
            autos_mas_vendidos[marca] = (modelo, cantidad)

    return autos_mas_vendidos
