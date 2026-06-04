# ===================
# CONEXIÓN A BASE DE DATOS
# ===================

import pyodbc


class Conexion:

    @staticmethod
    def obtener_conexion():
        # Conexión directa a la base de datos del sistema
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "DATABASE=zona_fit_db;"
            "Trusted_Connection=yes;"
        )
        return conexion
