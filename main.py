from datetime import datetime

import dearpygui.dearpygui as dpg
from Operaciones import AutoOperaciones
from Operaciones import ClienteOperaciones
from Operaciones import VentaOperaciones
from Operaciones import ServicioOperaciones
from Operaciones import ReportesOperaciones
from Modelos.Auto import Auto
from Modelos.Cliente import Cliente
from Modelos.Servicio import Servicio
from Modelos.Venta import Venta



#----------------------mensaje de error o exito
def mostrar_mensaje(titulo, mensaje):
# Elimina la ventana de mensaje anterior si existe
    if dpg.does_item_exist("mensaje_popup"):
        dpg.delete_item("mensaje_popup")
        # Calcula la posición central de la pantalla
    viewport_width = dpg.get_viewport_client_width()
    viewport_height = dpg.get_viewport_client_height()
    window_width = 300
    window_height = 150
    window_x = (viewport_width - window_width) // 2
    window_y = (viewport_height - window_height) // 2

    # Crea una nueva ventana de mensaje modal como un popup
    with dpg.window(label=titulo, modal=True, show=True, tag="mensaje_popup", width=window_width, height=window_height, pos=(window_x, window_y), no_move=True, no_resize=True, no_close=True):
        dpg.add_text(mensaje)
        dpg.add_button(label="Aceptar", callback=lambda: dpg.delete_item("mensaje_popup"))

'''
def mostrar_mensaje(titulo, mensaje):
    # Elimina la ventana de mensaje anterior si existe
    if dpg.does_item_exist("mensaje_window"):
        print("Eliminando ventana de mensaje anterior...")
        dpg.delete_item("mensaje_window")
        print("Ventana de mensaje anterior eliminada.")

    # Calcula la posición central de la pantalla
    viewport_width = dpg.get_viewport_client_width()
    viewport_height = dpg.get_viewport_client_height()
    window_width = 300
    window_height = 150
    window_x = (viewport_width - window_width) // 2
    window_y = (viewport_height - window_height) // 2

    # Crea una nueva ventana de mensaje modal
    print("Creando nueva ventana de mensaje...")
    with dpg.window(label=titulo, modal=True, show=True, tag="mensaje_window", width=window_width, height=window_height, pos=(window_x, window_y), no_move=True, no_resize=True, no_close=True):
        dpg.add_text(mensaje)
        dpg.add_button(label="Aceptar", callback=lambda: dpg.delete_item("mensaje_window"))
    print("Nueva ventana de mensaje creada.")
'''

#----------------------- PUNTO 1 -----------------------------

def registrar_autos():
    if not dpg.does_item_exist("registro_autos_window"):
        # Ajustar la ventana al 100% del tamaño de la pantalla
        ancho_pantalla = dpg.get_viewport_client_width()
        alto_pantalla = dpg.get_viewport_client_height()

        with dpg.window(label="Registro de Autos", modal=True, show=True, tag="registro_autos_window",
                        width=ancho_pantalla, height=alto_pantalla, pos=(0, 0)):
            dpg.add_input_text(label="VIN", tag="vin_input")
            dpg.add_input_text(label="Marca", tag="marca_input")
            dpg.add_input_text(label="Modelo", tag="modelo_input")
            dpg.add_input_float(label="Precio", tag="precio_input")
            dpg.add_input_int(label="Año", tag="año_input")
            dpg.add_combo(label="Estado", items=["NUEVO", "USADO"], tag="estado_input")  # Menú desplegable para el estado

            dpg.add_button(label="Registrar Auto", callback=registrar_auto_callback)
            dpg.add_button(label="Cerrar", callback=lambda: dpg.hide_item("registro_autos_window"))
    else:
        dpg.show_item("registro_autos_window")



def registrar_auto_callback():
    vin = dpg.get_value("vin_input")
    marca = dpg.get_value("marca_input")
    modelo = dpg.get_value("modelo_input")
    precio = dpg.get_value("precio_input")
    anio = dpg.get_value("año_input")  # Obtener el año del input
    estado = dpg.get_value("estado_input")  # Obtener el valor del campo estado
#vin, marca, modelo, año, precio, estado

    if not all([vin, marca, modelo, precio, anio,estado]):  # Asegúrate de validar también el año

        mostrar_mensaje("Error", "Por favor, complete todos los campos.")
        print("Por favor, completa todos los campos.")
        return

    auto = Auto(vin, marca, modelo, anio,precio,estado)
    try:
        AutoOperaciones.registrar_auto(auto)
        print("Auto registrado exitosamente.")
        mostrar_mensaje("Éxito", "Auto registrado exitosamente.")

        limpiar_camposAuto()  # Limpiar campos después de registrar

    except ValueError as e:
        mostrar_mensaje("Error",f"Error al registrar el auto: {e}")

        print(f"Error al registrar el auto: {e}")

    # Verificar si la ventana existe antes de ocultarla
    if dpg.does_item_exist("registro_autos_window"):
        dpg.hide_item("registro_autos_window")  # Cerrar la ventana después de registrar

def limpiar_camposAuto():
    # Limpiar todos los campos de entrada
    dpg.set_value("vin_input", "")
    dpg.set_value("marca_input", "")
    dpg.set_value("modelo_input", "")
    dpg.set_value("precio_input", 0.0)
    dpg.set_value("año_input", 0)  # Limpiar campo de año
    dpg.set_value("estado_input", "")  # Limpiar campo de estado


#----------------------- PUNTO 2 -----------------------------
def registrar_clientes():
    if not dpg.does_item_exist("registro_clientes_window"):
        ancho_pantalla = dpg.get_viewport_client_width()
        alto_pantalla = dpg.get_viewport_client_height()

        with dpg.window(label="Registro de Clientes", tag="registro_clientes_window", modal=True, show=True,
                        width=ancho_pantalla, height=alto_pantalla, pos=(0, 0)):
            dpg.add_input_text(label="Nombre", tag="nombre_input")
            dpg.add_input_text(label="Apellido", tag="apellido_input")
            dpg.add_input_text(label="Dirección", tag="direccion_input")
            dpg.add_input_text(label="Teléfono", tag="telefono_input")
            dpg.add_button(label="Registrar Cliente", callback=registrar_cliente_callback)
            dpg.add_button(label="Cerrar", callback=lambda: dpg.hide_item("registro_clientes_window"))
    else:
        dpg.show_item("registro_clientes_window")
def registrar_cliente_callback():
    nombre = dpg.get_value("nombre_input")
    apellido = dpg.get_value("apellido_input")
    direccion = dpg.get_value("direccion_input")
    telefono = dpg.get_value("telefono_input")

    if not all([nombre, apellido, direccion, telefono]):
        print("Por favor, completa todos los campos.")
        return

    cliente = Cliente(nombre, apellido, direccion, telefono)
    ClienteOperaciones.registrar_cliente(cliente)
    print("Cliente registrado exitosamente.")

    dpg.hide_item("registro_clientes_window")  # Asegúrate de que esto sea correcto

#----------------------- PUNTO 3 -----------------------------
def registrar_ventas():
    if not dpg.does_item_exist("registro_ventas_window"):
        ancho_pantalla = dpg.get_viewport_client_width()
        alto_pantalla = dpg.get_viewport_client_height()

        with dpg.window(label="Registro de Ventas", modal=True, show=True, tag="registro_ventas_window",
                        width=ancho_pantalla, height=alto_pantalla, pos=(0, 0)):
            dpg.add_input_text(label="VIN del auto", tag="vin_venta_input")
            dpg.add_input_int(label="ID del cliente", tag="cliente_id_input")
            dpg.add_input_text(label="Fecha de venta (YYYY-MM-DD)", tag="fecha_venta_input")
            dpg.add_input_int(label="ID del vendedor", tag="vendedor_id_input")
            dpg.add_button(label="Registrar Venta", callback=registrar_venta_callback)
            dpg.add_button(label="Cerrar", callback=lambda: dpg.hide_item("registro_ventas_window"))
    else:
        dpg.show_item("registro_ventas_window")
def registrar_venta_callback():
    auto_vin = dpg.get_value("vin_venta_input")
    cliente_id = dpg.get_value("cliente_id_input")
    fecha_venta = dpg.get_value("fecha_venta_input")
    vendedor_id = dpg.get_value("vendedor_id_input")

    if not all([auto_vin, cliente_id, fecha_venta, vendedor_id]):
        print("Por favor, completa todos los campos.")
        mostrar_mensaje("Error","Por favor, complete todos los campos.")

        return

    venta = Venta(auto_vin, cliente_id, fecha_venta, vendedor_id)
    try:
        VentaOperaciones.registrar_venta(venta)
        mostrar_mensaje("Exito","Venta registrada con exito.")

        print("Venta registrada exitosamente.")
    except ValueError as e:
        mostrar_mensaje("Error",f"Error al registrar la venta: {e}")

        print(f"Error al registrar la venta: {e}")

    dpg.hide_item("registro_ventas_window")

#----------------------- PUNTO 4 -----------------------------
def registrar_servicios():
    if not dpg.does_item_exist("registro_servicios_window"):
        ancho_pantalla = dpg.get_viewport_client_width()
        alto_pantalla = dpg.get_viewport_client_height()

        with dpg.window(label="Registro de Servicios", modal=True, show=True, tag="registro_servicios_window",
                        width=ancho_pantalla, height=alto_pantalla, pos=(0, 0)):
            dpg.add_input_text(label="VIN del auto", tag="vin_servicio_input")
            dpg.add_combo(label="Tipo de servicio", items=["MANTENIMIENTO", "REPARACION"], tag="tipo_servicio_input")  # Menú desplegable para el estado

            dpg.add_input_text(label="Fecha del servicio (YYYY-MM-DD)", tag="fecha_servicio_input")
            dpg.add_input_float(label="Costo del servicio", tag="costo_servicio_input")
            dpg.add_button(label="Registrar Servicio", callback=registrar_servicio_callback)
            dpg.add_button(label="Cerrar", callback=lambda: dpg.hide_item("registro_servicios_window"))
    else:
        dpg.show_item("registro_servicios_window")


def registrar_servicio_callback():
    auto_vin = dpg.get_value("vin_servicio_input")
    tipo_servicio = dpg.get_value("tipo_servicio_input")
    fecha = dpg.get_value("fecha_servicio_input")
    costo = dpg.get_value("costo_servicio_input")

    if not all([auto_vin, tipo_servicio, fecha, costo]):
        print("Por favor, completa todos los campos.")
        mostrar_mensaje("Error","Por favor, completa todos los campos.")

        return

    try:
        costo = float(costo)  # Asegúrate de que el costo sea un número
    except ValueError:
        print("El costo debe ser un número válido.")
        mostrar_mensaje("Error","El costo debe ser un número válido.")

        return

    # Crear una nueva instancia de Servicio sin el id
    servicio = Servicio(auto_vin, tipo_servicio, fecha, costo)

    try:
        ServicioOperaciones.registrar_servicio(servicio)
        print("Servicio registrado exitosamente.")
        mostrar_mensaje("Exito","Servicio registrado exitosamente.")

        # Limpiar campos después de registrar, si es necesario
    except ValueError as e:
        mostrar_mensaje("Error",f"Error al registrar el servicio: {e}")

        print(e)


    # Verificar si la ventana existe antes de ocultarla
    if dpg.does_item_exist("registro_servicios_window"):
        dpg.hide_item("registro_servicios_window")


#----------------------- PUNTO 5 -----------------------------
def obtener_lista_clientes():
    clientes = ClienteOperaciones.consultar_clientes_bd()
    if not clientes:
        return []  # Retornar lista vacía si no hay clientes

    # Formatear la lista de clientes para el combo
    clientes_formateados = []
    for cliente in clientes:
        try:
            # Verificar que tengamos todos los datos necesarios
            if len(cliente) >= 3 and all(x is not None for x in cliente[:3]):
                cliente_formateado = (
                    cliente[0],  # ID
                    f"{cliente[1]} {cliente[2]} (ID: {cliente[0]})"  # Nombre formateado
                )
                clientes_formateados.append(cliente_formateado)
        except Exception as e:
            print(f"Error al formatear cliente {cliente}: {e}")
            continue

    return clientes_formateados

def consultar_autos_vendidos():
    # Si la ventana ya existe, la oculta
    if dpg.does_item_exist("consulta_autos_vendidos_window"):
        dpg.show_item("consulta_autos_vendidos_window")  # Mostrar si ya existe
        return

    # Obtener lista de clientes
    clientes = obtener_lista_clientes()
    nombres_clientes = [cliente[1] for cliente in clientes]
    ids_clientes = [cliente[0] for cliente in clientes]

    # Obtener el tamaño de la pantalla para ajustar la ventana al 100%
    ancho_pantalla = dpg.get_viewport_client_width()
    alto_pantalla = dpg.get_viewport_client_height()

    # Crear la ventana a pantalla completa
    with dpg.window(label="Consulta de Autos Vendidos",
                    tag="consulta_autos_vendidos_window",
                    modal=True,
                    show=True,
                    width=ancho_pantalla,
                    height=alto_pantalla,
                    pos=(0, 0)):
        # Agregar combo de clientes
        dpg.add_text("Seleccione un cliente:")
        dpg.add_combo(
            items=nombres_clientes,  # Texto visible en el combo
            tag="combo_clientes",
            width=300,
            default_value=nombres_clientes[0] if nombres_clientes else "",
            callback=lambda s: consulta_autos_callback(ids_clientes[nombres_clientes.index(dpg.get_value(s))])
        )

        # Botón de cerrar
        dpg.add_button(
            label="Cerrar",
            callback=lambda: dpg.hide_item("consulta_autos_vendidos_window")
        )
def consulta_autos_callback(id_cliente):
    try:
        autos = ClienteOperaciones.consultar_autos_vendidos(id_cliente)

        # Primero, eliminar cualquier tabla existente
        if dpg.does_item_exist("tabla_autos"):
            dpg.delete_item("tabla_autos")

        if autos:
            # Crear una tabla
            with dpg.table(tag="tabla_autos", header_row=True,
                           borders_outerH=True, borders_outerV=True,
                           borders_innerH=True, borders_innerV=True,
                           parent="consulta_autos_vendidos_window"):

                # Definir columnas
                dpg.add_table_column(label="VIN")
                dpg.add_table_column(label="Marca")
                dpg.add_table_column(label="Modelo")
                dpg.add_table_column(label="Año")
                dpg.add_table_column(label="Precio")

                # Añadir filas
                for auto in autos:
                    with dpg.table_row():
                        dpg.add_text(str(auto['vin']))  # VIN
                        dpg.add_text(str(auto['marca']))  # Marca
                        dpg.add_text(str(auto['modelo']))  # Modelo
                        dpg.add_text(str(auto['año']))  # Año
                        dpg.add_text(str(auto['precio']))  # Precio
        else:
            # Si no hay autos, mostrar un mensaje en la tabla
            with dpg.table(tag="tabla_autos", header_row=True,
                           parent="consulta_autos_vendidos_window"):
                dpg.add_table_column(label="Mensaje")
                with dpg.table_row():
                    dpg.add_text("No se encontraron autos vendidos para este cliente.")

    except ValueError as e:
        # Manejar errores mostrando un mensaje en la tabla
        if dpg.does_item_exist("tabla_autos"):
            dpg.delete_item("tabla_autos")

        with dpg.table(tag="tabla_autos", header_row=True,
                       parent="consulta_autos_vendidos_window"):
            dpg.add_table_column(label="Error")
            with dpg.table_row():
                dpg.add_text(str(e))






#----------------------- PUNTO 6  ver esta linea-----------------------------


def consultar_servicios():
    # Si la ventana ya existe, la oculta
    if dpg.does_item_exist("consulta_servicios_window"):
        dpg.show_item("consulta_servicios_window")  # Mostrar si ya existe
        return

    # Crear la ventana para consultar servicios
    ancho_pantalla = dpg.get_viewport_client_width()
    alto_pantalla = dpg.get_viewport_client_height()

    with dpg.window(label="Consulta de Servicios",
                    tag="consulta_servicios_window",
                    modal=True,
                    show=True,
                    width=ancho_pantalla,
                    height=alto_pantalla,
                    pos=(0, 0)):
        dpg.add_input_text(label="VIN del auto", tag="vin_auto_consulta_input")
        dpg.add_button(label="Consultar", callback=consulta_servicios_callback)
        dpg.add_button(label="Cerrar", callback=lambda: dpg.hide_item("consulta_servicios_window"))

def consulta_servicios_callback():
    vin_auto = dpg.get_value("vin_auto_consulta_input")
    servicios = ServicioOperaciones.consultar_servicios_auto(vin_auto)

    # Eliminar tabla existente si ya existe
    if dpg.does_item_exist("tabla_servicios"):
        dpg.delete_item("tabla_servicios")

    if servicios:
        # Crear una tabla para mostrar los servicios
        with dpg.table(tag="tabla_servicios", header_row=True,
                       borders_outerH=True, borders_outerV=True,
                       borders_innerH=True, borders_innerV=True,
                       parent="consulta_servicios_window"):

            # Definir columnas
            dpg.add_table_column(label="ID")
            dpg.add_table_column(label="Tipo de Servicio")
            dpg.add_table_column(label="Fecha")
            dpg.add_table_column(label="Costo")

            # Añadir filas
            for servicio in servicios:
                with dpg.table_row():
                    dpg.add_text(str(servicio['id']))  # ID
                    dpg.add_text(str(servicio['tipo_servicio']))  # Tipo de Servicio
                    dpg.add_text(str(servicio['fecha']))  # Fecha
                    dpg.add_text(str(servicio['costo']))  # Costo

    else:
        # Si no hay servicios, mostrar mensaje en la tabla
        with dpg.table(tag="tabla_servicios", header_row=True,
                       parent="consulta_servicios_window"):
            dpg.add_table_column(label="Mensaje")
            with dpg.table_row():
                dpg.add_text("No se encontraron servicios para este vehículo.")






#----------------------- PUNTO 7 -----------------------------


def mostrar_fechas_ventas(sender, app_data):
    print("Botón 'Listar todas las ventas' clickeado")  # Debugging
    # Comprobar si la ventana ya existe
    if not dpg.does_item_exist("fechas_ventas_window"):
        ancho_pantalla = dpg.get_viewport_client_width()
        alto_pantalla = dpg.get_viewport_client_height()
        ahora = datetime.now()

        # Formato actual de la fecha
        fecha_actual = ahora.strftime("%Y-%m-%d")  # Formato de fecha año/mes/día

        # Crear la ventana modal para seleccionar las fechas
        with dpg.window(label="Seleccionar Periodo de Ventas", modal=True, show=True,
                        tag="fechas_ventas_window", width=ancho_pantalla // 2, height=alto_pantalla // 3,
                        pos=(ancho_pantalla // 4, alto_pantalla // 3)):
            dpg.add_text("Ingrese el periodo de ventas:")

            # Campos para ingresar las fechas de inicio y fin
            with dpg.group(horizontal=True):
                dpg.add_text("Fecha de inicio:")
                # Campo de texto para ingresar la fecha manualmente
                dpg.add_input_text(
                    tag="fecha_inicio_input",
                    default_value=fecha_actual,  # Usar fecha actual en formato año/mes/día
                    width=200
                )

            with dpg.group(horizontal=True):
                dpg.add_text("Fecha de fin:")
                # Campo de texto para ingresar la fecha manualmente
                dpg.add_input_text(
                    tag="fecha_fin_input",
                    default_value=fecha_actual,  # Usar fecha actual en formato año/mes/día
                    width=200
                )

            # Botón para generar el reporte
            dpg.add_button(label="Listar Ventas", callback=listar_ventas_callback)

            # Botón para cerrar la ventana
            dpg.add_button(label="Cerrar", callback=lambda: dpg.hide_item("fechas_ventas_window"))
    else:
        dpg.show_item("fechas_ventas_window")


def listar_ventas_callback(sender, app_data):
    fecha_inicio = dpg.get_value("fecha_inicio_input")
    fecha_fin = dpg.get_value("fecha_fin_input")

    # Verificar que las fechas no estén vacías
    if fecha_inicio and fecha_fin:
        ventas = ReportesOperaciones.generar_reporte_ventas_por_periodo(fecha_inicio, fecha_fin)
        print("Ventas en el periodo:")
        for venta in ventas:
            print(venta)
    else:
        print("Por favor, ingrese ambas fechas.")




def ingresos_callback():
    ingresos_ventas, ingresos_servicios = ReportesOperaciones.generar_reporte_ingresos_totales()
    print(f"Ingresos totales por ventas de autos: {ingresos_ventas}")
    print(f"Ingresos totales por servicios: {ingresos_servicios}")

def autos_mas_vendidos_callback():
    autos_mas_vendidos = ReportesOperaciones.generar_reporte_autos_mas_vendidos_por_marca()
    print("Autos más vendidos por marca:")
    for fila in autos_mas_vendidos:
        print(f"Marca: {fila[0]}, Cantidad Vendida: {fila[1]}")


def reporte_ventas_por_marca_callback():
    ReportesOperaciones.generar_reporte_ventas_por_marca()
    print("Reporte de ventas por marca generado exitosamente.")

def reporte_ingresos_mensuales_callback():
    ReportesOperaciones.generar_grafico_lineas()
    print("Reporte de ingresos mensuales generado exitosamente.")


#----------------------- MENU PRINCIPAL -----------------------------
def crear_menu():
    # Crear la ventana del menú principal
    with dpg.window(label="Menú Principal", width=dpg.get_viewport_client_width(), height=dpg.get_viewport_client_height()):
        with dpg.menu_bar():
            with dpg.menu(label="Registro"):
                dpg.add_menu_item(label="Registro de Autos", callback=registrar_autos)
                dpg.add_menu_item(label="Registro de Clientes", callback=registrar_clientes)
                dpg.add_menu_item(label="Registro de Ventas", callback=registrar_ventas)
                dpg.add_menu_item(label="Registro de Servicios", callback=registrar_servicios)
            with dpg.menu(label="Consulta"):
                dpg.add_menu_item(label="Autos Vendidos", callback=consultar_autos_vendidos)
                dpg.add_menu_item(label="Servicios", callback=consultar_servicios)
            with dpg.menu(label="Reportes"):
                # Submenú dentro de Reportes
                with dpg.menu(label="Generar Reportes"):
                    dpg.add_menu_item(label="Listar todas las ventas realizadas en un periodo de tiempo",
                                       callback=mostrar_fechas_ventas)
                    dpg.add_menu_item(label="Generar un reporte de ingresos totales", callback=ingresos_callback)
                    dpg.add_menu_item(label="Autos más vendidos por marca", callback=autos_mas_vendidos_callback)
                    dpg.add_menu_item(label="Generar reporte de ventas por marca", callback=reporte_ventas_por_marca_callback)
                    dpg.add_menu_item(label="Generar reporte de ingresos mensual", callback=reporte_ingresos_mensuales_callback)
                dpg.add_menu_item(label="Salir", callback=lambda: dpg.stop_dearpygui())

def main():
    dpg.create_context()
    dpg.create_viewport(title='Sistema de Gestion de Autos', width=800, height=600)
    crear_menu()  # Llama a crear_menu después de establecer el viewport

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()