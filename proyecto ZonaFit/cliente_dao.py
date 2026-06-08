from cliente import Cliente
from conexionDB import Conexion


class ClienteDAO:

    SELECCIONAR = "SELECT * FROM cliente"

    INSERTAR = """
    INSERT INTO cliente
    (id_cliente, nombre, apellido, telefono, correo,
     membresia, fecha_inscripcion, fecha_vencimiento, estado)
    VALUES (?,?,?,?,?,?,?,?,?)
    """

    ACTUALIZAR = """
    UPDATE cliente
    SET nombre=?,
        apellido=?,
        telefono=?,
        correo=?,
        membresia=?,
        fecha_inscripcion=?,
        fecha_vencimiento=?,
        estado=?
    WHERE id_cliente=?
    """

    ELIMINAR = "DELETE FROM cliente WHERE id_cliente=?"

    @classmethod
    def seleccionar(cls):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)

            registros = cursor.fetchall()
            clientes = []

            for registro in registros:
                cliente = Cliente(
                    registro[0],  # id_cliente
                    registro[1],  # nombre
                    registro[2],  # apellido
                    registro[3],  # telefono
                    registro[4],  # correo
                    registro[5],  # membresia
                    registro[6],  # fecha_inscripcion
                    registro[7],  # fecha_vencimiento
                    registro[8],  # estado
                )

                clientes.append(cliente)

            return clientes

        except Exception as e:
            print(f"Ocurrió un error al seleccionar clientes: {e}")

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valores = (
                cliente.id_cliente,
                cliente.nombre,
                cliente.apellido,
                cliente.telefono,
                cliente.correo,
                cliente.membresia,
                cliente.fecha_inscripcion,
                cliente.fecha_vencimiento,
                cliente.estado,
            )

            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"Ocurrió un error al insertar clientes: {e}")

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valores = (
                cliente.nombre,
                cliente.apellido,
                cliente.telefono,
                cliente.correo,
                cliente.membresia,
                cliente.fecha_inscripcion,
                cliente.fecha_vencimiento,
                cliente.estado,
                cliente.id_cliente,
            )

            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"Ocurrió un error al actualizar clientes: {e}")

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valor = (cliente.id_cliente,)

            cursor.execute(cls.ELIMINAR, valor)
            conexion.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"Ocurrió un error al eliminar clientes: {e}")

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()


"""
if __name__ == "__main__":
    clientes = ClienteDAO.seleccionar()

    for cliente in clientes:
        print(cliente)
        
if __name__ == "__main__":

    cliente1 = Cliente(
        71795830,
        "Jorge",
        "Mosquera",
        "3001234567",
        "jorge@gmail.com",
        "Premium",
        "2026-06-01",
        "2026-07-01",
        "Activo"
    )

    registros_insertados = ClienteDAO.insertar(cliente1)

    print(f"Registros insertados: {registros_insertados}")
    
    
    
    # Actualizar
    if __name__ == "__main__":

    cliente_actualizado = Cliente(
        71795830,
        "Jorge Andres",
        "Mosquera",
        "3119876543",
        "jorge@gmail.com",
        "VIP",
        "2026-06-01",
        "2026-08-01",
        "Activo"
    )

    registros_actualizados = ClienteDAO.actualizar(cliente_actualizado)

    print(f"Registros actualizados: {registros_actualizados}")



if __name__ == "__main__":

    cliente_eliminar = Cliente(
        id_cliente=71795830
    )

    registros_eliminados = ClienteDAO.eliminar(cliente_eliminar)

    print(f"Registros eliminados: {registros_eliminados}")
"""
