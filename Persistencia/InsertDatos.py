from Persistencia.BaseDeDatosCONEXION import BaseDeDatos


def insertar_datos():
    try:
        db = BaseDeDatos().connect('concesionaria.db')
        cursor = db.cursor()

        # Insertar 10 Clientes
        cursor.executemany(''' 
        INSERT INTO Cliente (nombre, apellido, direccion, telefono)
        VALUES (?, ?, ?, ?)
        ''', [
            ('Brian', 'Silvestri', '123 Calle Principal', '231456789'),
            ('Maria', 'Gonzalez', '456 Avenida Central', '987654321'),
            ('Luis', 'Fernandez', '789 Calle Secundaria', '456123789'),
            ('Ana', 'Torres', '159 Avenida Norte', '654789321'),
            ('Carlos', 'Hernandez', '258 Calle Este', '321654987'),
            ('Sofia', 'Martinez', '369 Avenida Oeste', '159753468'),
            ('Fernando', 'Ruiz', '753 Calle Nueva', '753951852'),
            ('Julia', 'Pérez', '951 Avenida Vieja', '852369741'),
            ('Diego', 'Cruz', '357 Calle 10', '147258369'),
            ('Elena', 'Sanchez', '159 Avenida 11', '963852741'),
        ])

        # Insertar 10 Vendedores
        cursor.executemany('''
        INSERT INTO Vendedor (nombre, apellido, comisiones)
        VALUES (?, ?, ?)
        ''', [
            ('Juan', 'Perez', 5000.0),
            ('Laura', 'Martinez', 7500.0),
            ('Luis', 'Gomez', 4000.0),
            ('Carla', 'Morales', 6500.0),
            ('Javier', 'Vega', 7000.0),
            ('Sofia', 'Lopez', 5500.0),
            ('Andres', 'Hernandez', 6000.0),
            ('Lucia', 'Fernandez', 4800.0),
            ('Mateo', 'Santos', 5300.0),
            ('Valentina', 'Reyes', 7200.0),
        ])

        # Insertar 10 Autos
        cursor.executemany('''
        INSERT INTO Auto (vin, marca, modelo, año, precio, estado, cliente_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', [
            ('001', 'Honda', 'Civic', 2020, 20000.0, 'disponible', 1),
            ('002', 'Toyota', 'Corolla', 2021, 22000.0, 'disponible', 2),
            ('003', 'Ford', 'F-150', 2019, 30000.0, 'vendido', 3),
            ('004', 'Chevrolet', 'Malibu', 2018, 19000.0, 'disponible', 4),
            ('005', 'Nissan', 'Altima', 2022, 24000.0, 'disponible', 5),
            ('006', 'Hyundai', 'Elantra', 2021, 18000.0, 'vendido', 6),
            ('007', 'Kia', 'Forte', 2020, 17000.0, 'disponible', 7),
            ('008', 'Volkswagen', 'Jetta', 2021, 23000.0, 'disponible', 8),
            ('009', 'Subaru', 'Impreza', 2023, 26000.0, 'disponible', 9),
            ('010', 'Mazda', '3', 2019, 19000.0, 'vendido', 10),
        ])

        # Insertar 10 Ventas
        cursor.executemany('''
        INSERT INTO Venta (auto_vin, cliente_id, fecha_venta, vendedor_id)
        VALUES (?, ?, ?, ?)
        ''', [
            ('002', 2, '2024-10-31', 1),
            ('003', 3, '2024-10-15', 2),
            ('001', 1, '2024-10-10', 3),
            ('004', 4, '2024-10-05', 1),
            ('005', 5, '2024-10-01', 2),
            ('006', 6, '2024-09-28', 3),
            ('007', 7, '2024-09-25', 1),
            ('008', 8, '2024-09-20', 2),
            ('009', 9, '2024-09-15', 3),
            ('010', 10, '2024-09-10', 1),
        ])

        # Insertar 10 Servicios
        cursor.executemany('''
        INSERT INTO Servicio (auto_vin, tipo_servicio, fecha, costo)
        VALUES (?, ?, ?, ?)
        ''', [
            ('001', 'MANTENIMIENTO', '2024-10-15', 100.0),
            ('002', 'MANTENIMIENTO', '2024-10-20', 150.0),
            ('003', 'REPARACION', '2024-10-01', 200.0),
            ('004', 'MANTENIMIENTO', '2024-09-28', 75.0),
            ('005', 'REPARACION', '2024-09-10', 120.0),
            ('006', 'REPARACION', '2024-08-15', 250.0),
            ('007', 'REPARACION', '2024-08-10', 80.0),
            ('008', 'MANTENIMIENTO', '2024-08-05', 300.0),
            ('009', 'REPARACION', '2024-07-25', 100.0),
            ('010', 'MANTENIMIENTO', '2024-07-15', 150.0),
        ])

        db.commit()
    except Exception as e:
        print(f"Error al insertar datos: {e}")
    finally:
        db.close()


if __name__ == '__main__':
    insertar_datos()  # Inserta los datos