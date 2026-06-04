from conexionDB import Conexion
from genero import Genero


class GeneroDAO:

    # ======================
    # CONSULTAS SQL
    # ======================

    SELECCIONAR = "SELECT * FROM generos"

    INSERTAR = """
    INSERT INTO generos(nombre)
    VALUES(?)
    """

    ACTUALIZAR = """
    UPDATE generos
    SET nombre = ?
    WHERE id = ?
    """

    ELIMINAR = """
    DELETE FROM generos
    WHERE id = ?
    """

    # ======================
    # SELECT
    # ======================

    @classmethod
    def seleccionar(cls):

        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()

            generos = []

            for registro in registros:
                genero = Genero(registro[0], registro[1])
                generos.append(genero)

            return generos

        except Exception as e:
            print(f"Error al seleccionar géneros: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    # ======================
    # INSERTAR
    # ======================

    @classmethod
    def insertar(cls, genero):

        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valores = (genero.nombre,)

            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"Error al insertar género: {e}")

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    # ======================
    # ACTUALIZAR
    # ======================

    @classmethod
    def actualizar(cls, genero):

        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valores = (genero.nombre, genero.id)

            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"Error al actualizar género: {e}")

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    # ======================
    # ELIMINAR
    # ======================

    @classmethod
    def eliminar(cls, genero):

        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valores = (genero.id,)

            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"Error al eliminar género: {e}")

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
