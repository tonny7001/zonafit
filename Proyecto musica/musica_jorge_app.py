# menu de opciones
from genero import Genero
from genero_dao import GeneroDAO

while True:
    print("\n========================")
    print("   SISTEMA DE MUSICA")
    print("========================")

    print("1. Gestion de Generos")
    print("2. Gestion de Artistas")
    print("3. Gestion de Albums")
    print("4. Gestion de Canciones")
    print("0. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        menu_genero = None

        while menu_genero != "5":

            print("""
Menu Genero:
1. Mostrar Generos.
2. Agregar Genero.
3. Modificar un Genero.
4. Eliminar Genero.
5. Salir.
""")

            menu_genero = input("Seleccione una opcion: ")

            if menu_genero == "1":

                generos = GeneroDAO.seleccionar()

                if not generos:
                    print("No hay géneros registrados.")
                else:
                    for genero in generos:
                        print(genero)

            elif menu_genero == "2":

                nombre_genero = input("Ingrese el nombre del género: ")

                genero = Genero(nombre=nombre_genero)

                registros = GeneroDAO.insertar(genero)

                if registros and registros > 0:
                    print("Género agregado correctamente.")
                else:
                    print("No se pudo agregar el género.")

            elif menu_genero == "3":
                print("Opción Modificar Género pendiente de implementar.")

            elif menu_genero == "4":
                print("Opción Eliminar Género pendiente de implementar.")

            elif menu_genero == "5":
                print("Saliendo del menú de géneros...")

            else:
                print("Opción no válida.")

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida.")
