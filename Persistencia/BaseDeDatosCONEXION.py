import sqlite3
from sqlite3 import Connection, Error
import os

class BaseDeDatos:
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BaseDeDatos, cls).__new__(cls)
            cls._instance._connection = None
            cls._instance.cursor = None
        return cls._instance

    def connect(self, db_name: str = 'concesionaria.db') -> Connection:
        """
        Establece la conexión a la base de datos, guardándola en la carpeta `data`.
        Returns:
            Connection: Objeto de conexión a la base de datos
        """
        if self._connection is None:
            # Crear la carpeta `data` si no existe
            data_folder = os.path.join(os.path.dirname(__file__), '../data')
            os.makedirs(data_folder, exist_ok=True)

            # Ruta completa de la base de datos
            db_path = os.path.join(data_folder, db_name)

            try:
                self._connection = sqlite3.connect(db_path)
                self.cursor = self._connection.cursor()
                print("Conexión a la base de datos establecida.")
            except Error as e:
                print(f"Error al conectar a la base de datos: {e}")
                self._connection = None
                self.cursor = None
        return self._connection

    def test_connection(self):
        """Verifica y establece la conexión si no existe."""
        if not self._connection:
            self.connect()

    def execute_query(self, query: str, parameters: tuple = ()) -> bool:
        """
        Ejecuta una consulta SQL que modifica la base de datos.
        Args:
            query (str): Consulta SQL a ejecutar
            parameters (tuple): Parámetros para la consulta
        Returns:
            bool: True si la consulta se ejecutó correctamente, False en caso contrario
        """
        try:
            self.test_connection()
            self.cursor.execute(query, parameters)
            self._connection.commit()
            return True
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return False

    def fetch_query(self, query: str, parameters: tuple = ()) -> list:
        """
        Ejecuta una consulta SQL que obtiene datos de la base de datos.
        Args:
            query (str): Consulta SQL a ejecutar
            parameters (tuple): Parámetros para la consulta
        Returns:
            list: Resultados de la consulta o lista vacía en caso de error
        """
        try:
            self.test_connection()
            self.cursor.execute(query, parameters)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error al obtener datos: {e}")
            return []

    def close(self):
        """Cierra la conexión a la base de datos si está abierta."""
        if self._connection:
            self._connection.close()
            self._connection = None
            self.cursor = None
            print("Conexión a la base de datos cerrada.")