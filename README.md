# TP_DAO_GRUPO38
Sistema de Gestión de Venta de Autos

Descripción

Este proyecto es un sistema de gestión para una concesionaria de autos que permite manejar el inventario de vehículos, registrar clientes y ventas, gestionar servicios post-venta, y generar reportes de rendimiento. Con este sistema, la concesionaria podrá optimizar el proceso de ventas, realizar un seguimiento efectivo de sus vehículos y analizar sus datos de ventas y servicios.


Objetivo:
Desarrollar un sistema que permita a la concesionaria:

-Manejar el inventario de autos disponibles para la venta.
-Registrar clientes y sus compras.
-Llevar un control de los servicios post-venta.
-Generar reportes detallados sobre las ventas y el desempeño.



-Requerimientos

Clases principales:

.Auto: Contiene información sobre el vehículo, como código VIN, marca, modelo, año, precio, estado (nuevo/usado), y cliente asociado en caso de venta.

.Cliente: Contiene los datos personales de los clientes, como ID, nombre, apellido, dirección y teléfono.

.Venta: Registra los detalles de cada venta, incluyendo el ID de venta, el auto vendido, el cliente, la fecha de venta y el vendedor.

.Servicio: Define los servicios post-venta realizados a los vehículos, indicando el ID del servicio, tipo (mantenimiento, reparación), fecha y costo.

.Vendedor: Contiene la información de los vendedores, incluyendo su ID, nombre, apellido y comisiones.




-Operaciones Principales

.Registro de Autos: Permite agregar nuevos autos al inventario.

.Registro de Clientes: Permite registrar nuevos clientes en el sistema.

.Registro de Ventas: Permite registrar la venta de un auto y asignar la comisión correspondiente al vendedor.

.Registro de Servicios: Permite registrar servicios de mantenimiento o reparación para autos ya vendidos.

.Consulta de Autos Vendidos: Permite consultar los autos vendidos a un cliente específico.

.Consulta de Servicios: Permite consultar los servicios realizados a un auto específico.

.Reportes:

  -Listar todas las ventas realizadas en un período de tiempo.
  
  -Generar un reporte de ingresos totales por ventas de autos y servicios post-venta.
  
  -Generar un reporte de los autos más vendidos por marca.




-Dificultad Extra

.Validaciones:

  Asegurar que un auto no pueda ser vendido dos veces.
  
  Permitir que los servicios solo puedan asociarse a autos ya vendidos.

.Implementación de Reportes Avanzados:

  Gráfico de torta que muestre la distribución de ventas por marca.
  
  Gráfico de líneas que presente los ingresos mensuales.





-Instalar dependencias:

Para el buen funcionamiento del proyecto, se deben instalar las siguientes bibliotecas de Python:

pandas: Para el manejo de datos.


dearpygui: Para la interfaz gráfica.

matplotlib: Para la generación de gráficos.

reportlab: Para la creación de reportes en PDF.

sqlite3: Para la gestión de la base de datos del sistema.



-Uso

Registro de datos: Registra autos, clientes y vendedores en el sistema.

Registrar ventas y servicios: Realiza el registro de ventas y servicios post-venta.

Consultar datos: Consulta los autos vendidos y los servicios realizados.

Generar reportes: Obtén reportes de ventas e ingresos y visualiza los gráficos para análisis de rendimiento.

