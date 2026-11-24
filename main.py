from funciones import (
    cargar_expedientes,
    registrar_expediente,
    eliminar_expediente,
    buscar_por_dni,
    buscar_por_codigo,
    buscar_por_area,
    mostrar_todos,
    ordenar_por_codigo
)

cargar_expedientes()

while True:

    print("\n================================")
    print("       MESA DE PARTES")
    print("       CENTRO MEDICO")
    print("================================")
    print("1. Registrar expediente")
    print("2. Eliminar expediente")
    print("3. Buscar por DNI")
    print("4. Buscar por codigo")
    print("5. Buscar por area")
    print("6. Mostrar todos los expedientes")
    print("7. Ordenar por codigo")
    print("8. Salir")
    print("================================")

    opcion = input("Seleccione una opcion: ")

    match opcion:

        case "1":
            registrar_expediente()

        case "2":
            eliminar_expediente()

        case "3":
            buscar_por_dni()

        case "4":
            buscar_por_codigo()

        case "5":
            buscar_por_area()

        case "6":
            mostrar_todos()

        case "7":
            ordenar_por_codigo()

        case "8":
            print("\nGracias por utilizar el sistema.")
            break

        case _:
            print("\nOpcion no valida. Intente nuevamente.")
