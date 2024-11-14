import os
from datetime import datetime
from sqlite3 import Error
from collections import Counter
import matplotlib.pyplot as plt
from Operaciones import VentaOperaciones
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import pandas as pd

from Persistencia.BaseDeDatosCONEXION import BaseDeDatos

def generar_reporte_ventas_por_periodo(fecha_inicio, fecha_fin):
    # Obtener ventas del periodo
    ventas = VentaOperaciones.ventas_por_periodo(fecha_inicio, fecha_fin)

    # Crear la carpeta 'reportes' si no existe
    reportes_folder = os.path.join(os.path.dirname(__file__), '../Reportes')
    os.makedirs(reportes_folder, exist_ok=True)

    # Definir la ruta para el PDF
    reporte_path = os.path.join(reportes_folder, f"reporte_ventas_{fecha_inicio}_a_{fecha_fin}.pdf")

    # Crear el PDF
    doc = SimpleDocTemplate(reporte_path, pagesize=letter)

    # Estilos para el documento
    styles = getSampleStyleSheet()
    elements = []

    # Título
    title = Paragraph(f"VENTAS DEL {fecha_inicio} AL {fecha_fin}", styles['Title'])
    elements.append(title)

    # Crear la tabla de datos
    data = [['ID Venta', 'Auto VIN', 'Cliente ID', 'Fecha de Venta', 'Vendedor ID']]

    # Añadir cada venta a la tabla
    for venta in ventas:
        data.append([venta[0], venta[1], venta[2], venta[3], venta[4]])

    # Estilo de la tabla
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    # Generar el PDF
    doc.build(elements)
    print(f"Reporte generado: {reporte_path}")
    return ventas

def generar_reporte_ingresos_totales():
    db = BaseDeDatos()

    try:
        # Obtener los ingresos por ventas
        ingresos_ventas_query = '''
                SELECT SUM(Auto.precio)
                FROM Venta
                INNER JOIN Auto ON Venta.auto_vin = Auto.vin
            '''
        ingresos_ventas = db.fetch_query(ingresos_ventas_query)
        ingresos_ventas = ingresos_ventas[0][0] if ingresos_ventas and ingresos_ventas[0][0] else 0

        # Obtener los ingresos por servicios
        ingresos_servicios_query = '''
                SELECT SUM(costo)
                FROM Servicio
            '''
        ingresos_servicios = db.fetch_query(ingresos_servicios_query)
        ingresos_servicios = ingresos_servicios[0][0] if ingresos_servicios and ingresos_servicios[0][0] else 0

    except Error as e:
        print(f"Error al obtener ingresos: {e}")
        return None, None
    finally:
        db.close()

    # Crear la carpeta 'reportes' si no existe
    reportes_folder = os.path.join(os.path.dirname(__file__), '../Reportes')
    os.makedirs(reportes_folder, exist_ok=True)

    # Definir la ruta para el PDF
    reporte_path = os.path.join(reportes_folder, "reporte_ingresos_totales.pdf")

    # Crear el PDF
    doc = SimpleDocTemplate(reporte_path, pagesize=letter)

    # Estilos para el documento
    styles = getSampleStyleSheet()
    elements = []

    # Título
    title = Paragraph("Reporte de Ingresos Totales", styles['Title'])
    elements.append(title)

    # Crear la tabla de datos
    data = [
        ['Descripción', 'Ingresos'],
        ['Ventas de Autos', f"${ingresos_ventas:.2f}"],
        ['Servicios', f"${ingresos_servicios:.2f}"],
    ]

    # Estilo de la tabla
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    # Generar el PDF
    doc.build(elements)
    print(f"Reporte generado: {reporte_path}")
    return ingresos_ventas, ingresos_servicios



def generar_reporte_autos_mas_vendidos_por_marca():
    # Obtener los autos más vendidos por marca
    autos = VentaOperaciones.autos_mas_vendidos_por_marca()

    # Crear la carpeta 'reportes' si no existe
    reportes_folder = os.path.join(os.path.dirname(__file__), '../Reportes')
    os.makedirs(reportes_folder, exist_ok=True)

    # Definir la ruta para el PDF
    reporte_path = os.path.join(reportes_folder, "reporte_autos_mas_vendidos_por_marca.pdf")

    # Crear el PDF
    doc = SimpleDocTemplate(reporte_path, pagesize=letter)

    # Estilos para el documento
    styles = getSampleStyleSheet()
    elements = []

    # Título
    title = Paragraph("AUTOS MÁS VENDIDOS POR MARCAS", styles['Title'])
    elements.append(title)

    # Crear la tabla de datos
    data = [['Marca', 'Modelo', 'Cantidad Vendida']]  # Encabezados de la tabla

    # Añadir cada auto a la tabla
    for marca, (modelo, cantidad) in autos.items():
        data.append([marca, modelo, cantidad])

    # Estilo de la tabla
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    # Generar el PDF
    doc.build(elements)
    print(f"Reporte generado: {reporte_path}")

    return autos


def generar_reporte_ventas_por_marca():
    # Obtener los datos de ventas por marca desde el controlador de ventas
    ventas = VentaOperaciones.obtener_ventas_por_marca()

    # Contar las ventas por cada marca
    marcas = [venta[0] for venta in ventas]
    conteo_marcas = Counter(marcas)

    # Crear el gráfico de torta
    labels = conteo_marcas.keys()
    sizes = conteo_marcas.values()
    colors = plt.cm.Paired(range(len(labels)))

    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Ventas por Marca')
    plt.axis('equal')  # Para que el gráfico sea un círculo perfecto

    # Guardar el gráfico de torta como una imagen temporal
    grafico_path = os.path.join(os.path.dirname(__file__), 'temp_grafico_torta.png')
    plt.savefig(grafico_path)
    plt.close()

    # Crear la carpeta 'reportes' si no existe
    reportes_folder = os.path.join(os.path.dirname(__file__), '../Reportes')
    os.makedirs(reportes_folder, exist_ok=True)
    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime("%Y%m%d")

    # Definir la ruta para el PDF con la fecha actual
    reporte_path = os.path.join(reportes_folder, f"reporte_ventas_por_marca_{fecha_actual}.pdf")


    # Crear el PDF
    doc = SimpleDocTemplate(reporte_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Título
    title = Paragraph("Reporte de Distribución de Ventas por Marca", styles['Title'])
    elements.append(title)

    # Añadir el gráfico de torta al PDF
    elements.append(Image(grafico_path, width=6*inch, height=4*inch))

    # Generar el PDF
    doc.build(elements)
    print(f"Reporte generado: {reporte_path}")

    # Eliminar la imagen temporal
    os.remove(grafico_path)

def generar_grafico_lineas():
    # Obtener los datos de ingresos mensuales desde el controlador de ventas
    ventas_mensuales = VentaOperaciones.obtener_ingresos_mensuales_ventas()
    servicios_mensuales = VentaOperaciones.obtener_ingresos_mensuales_servicios()

    # Convertir los datos a DataFrame
    df_ventas = pd.DataFrame(ventas_mensuales, columns=['Mes', 'IngresosVentas'])
    df_servicios = pd.DataFrame(servicios_mensuales, columns=['Mes', 'IngresosServicios'])

    # Unir los DataFrame por el mes
    df_ingresos = pd.merge(df_ventas, df_servicios, on='Mes', how='outer').fillna(0)
    df_ingresos['IngresosTotales'] = df_ingresos['IngresosVentas'] + df_ingresos['IngresosServicios']

    # Crear el gráfico de líneas
    plt.figure(figsize=(12, 8))
    plt.plot(df_ingresos['Mes'], df_ingresos['IngresosTotales'], marker='o', linestyle='-', color='b')
    plt.xlabel('Mes')
    plt.ylabel('Ingresos Totales')
    plt.title('Ingresos Mensuales Totales')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Guardar el gráfico de líneas como una imagen temporal
    grafico_path = os.path.join(os.path.dirname(__file__), 'temp_grafico_lineas.png')
    plt.savefig(grafico_path)
    plt.close()

    # Crear la carpeta 'reportes' si no existe
    reportes_folder = os.path.join(os.path.dirname(__file__), '../Reportes')
    os.makedirs(reportes_folder, exist_ok=True)

    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime("%Y%m%d")

    # Definir la ruta para el PDF con la fecha actual
    reporte_path = os.path.join(reportes_folder, f"reporte_ingresos_mensuales_{fecha_actual}.pdf")

    # Crear el PDF
    doc = SimpleDocTemplate(reporte_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Título
    title = Paragraph("Reporte de Ingresos Mensuales", styles['Title'])
    elements.append(title)

    # Añadir el gráfico de líneas al PDF
    elements.append(Image(grafico_path, width=6 * inch, height=4 * inch))

    # Generar el PDF
    doc.build(elements)
    print(f"Reporte generado: {reporte_path}")