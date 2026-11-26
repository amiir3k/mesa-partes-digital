from funciones import (
    cargar_expedientes,
    registrar_expediente,
    buscar_y_consultar,
    actualizar_tramite,
    listar_y_ordenar,
    estadisticas
)

cargar_expedientes()

while True:

    print("\n================================")
    print("       MESA DE PARTES")
    print("       CENTRO MEDICO")
    print("================================")
    print("1. Registrar expediente")
    print("2. Buscar y consultar expediente")
    print("3. Actualizar estado de tramite")
    print("4. Listar y ordenar expedientes")
    print("5. Estadisticas de expedientes")
    print("6. Salir")
    print("================================")

    opcion = input("Seleccione una opcion: ")

    match opcion:

        case "1":
            registrar_expediente()

        case "2":
            buscar_y_consultar()

        case "3":
            actualizar_tramite()

        case "4":
            listar_y_ordenar()

        case "5":
            estadisticas()

        case "6":
            print("\nGracias por utilizar el sistema.")
            break

        case _:
            print("\nOpcion no valida. Intente nuevamente.")
