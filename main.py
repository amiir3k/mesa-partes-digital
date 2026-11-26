# main.py
# Mesa de Partes Digital - menú principal.
from datos import cargar_expedientes, expedientes
from tramites import registrar_expediente, buscar_y_consultar, actualizar_estado, listar_y_ordenar
from reportes import estadisticas

cargar_expedientes()
print("Expedientes cargados:", len(expedientes))

while True:
    print("\n================================")
    print("   MESA DE PARTES DIGITAL")
    print("================================")
    print("1. Registrar expediente")
    print("2. Buscar y consultar expediente")
    print("3. Actualizar estado de trámite")
    print("4. Listar y ordenar expedientes")
    print("5. Estadísticas de expedientes")
    print("6. Salir")
    print("================================")

    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        case "1":
            registrar_expediente()
        case "2":
            buscar_y_consultar()
        case "3":
            actualizar_estado()
        case "4":
            listar_y_ordenar()
        case "5":
            estadisticas()
        case "6":
            print("\nGracias por utilizar el sistema.")
            break
        case _:
            print("\nOpción no válida. Intente nuevamente.")
