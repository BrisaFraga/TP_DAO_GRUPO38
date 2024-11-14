

from Persistencia.BaseDeDatosCONEXION import BaseDeDatos


def crearTablas():
    # Conectarse a la base de datos usando el Singleton Persistencia
    db = BaseDeDatos().connect()  # Se conectará automáticamente a `data/concesionaria.db`
    cursor = db.cursor()

    # Crear tablas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Auto (
        vin TEXT PRIMARY KEY,
        marca TEXT,
        modelo TEXT,
        año INTEGER,
        precio REAL,
        estado TEXT,
        cliente_id INTEGER NULL,
        FOREIGN KEY(cliente_id) REFERENCES Cliente(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        direccion TEXT,
        telefono TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Venta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        auto_vin TEXT,
        cliente_id INTEGER,
        fecha_venta TEXT,
        vendedor_id INTEGER,
        FOREIGN KEY(auto_vin) REFERENCES Auto(vin),
        FOREIGN KEY(cliente_id) REFERENCES Cliente(id),
        FOREIGN KEY(vendedor_id) REFERENCES Vendedor(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Servicio (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        auto_vin TEXT,
        tipo_servicio TEXT,
        fecha TEXT,
        costo REAL,
        FOREIGN KEY(auto_vin) REFERENCES Auto(vin)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vendedor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        comisiones REAL
    )
    ''')

    db.commit()
    db.close()

if __name__ == '__main__':
    crearTablas()