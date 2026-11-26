import json
import os
from datetime import datetime


expedientes = []

ARCHIVO = "expedientes.json"

ESTADOS = ["Recibido", "En proceso", "Atendido", "Archivado"]


def cargar_expedientes():
    global expedientes

    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

                if isinstance(datos, list):
                    expedientes = datos

                    for expediente in expedientes:
                        if "estado" not in expediente:
                            expediente["estado"] = "Recibido"

        except json.JSONDecodeError:
            print("El archivo está vacío o contiene datos inválidos.")


def guardar_expedientes():
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(expedientes, archivo, ensure_ascii=False, indent=4)


def registrar_expediente():
    print("\n--- REGISTRO DE EXPEDIENTE ---")

    codigo = input("Ingrese el código del expediente: ").strip().upper()

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print("El código ya se encuentra registrado.")
            return

    dni = input("Ingrese el DNI del paciente: ").strip()

    if not dni.isdigit() or len(dni) != 8:
        print("El DNI debe contener 8 números.")
        return

    nombre = input("Ingrese el nombre del paciente: ").strip()
    area = input("Ingrese el área médica: ").strip()
    asunto = input("Ingrese el asunto del expediente: ").strip()

    if not all([codigo, nombre, area, asunto]):
        print("Todos los campos son obligatorios.")
        return

    nuevo_expediente = {
        "codigo": codigo,
        "dni": dni,
        "nombre": nombre,
        "area": area,
        "asunto": asunto,
        "fecha": datetime.now().strftime("%d/%m/%Y"),
        "estado": "Recibido"
    }

    expedientes.append(nuevo_expediente)
    guardar_expedientes()

    print("\n¡Expediente registrado correctamente!")
    print("Estado inicial: Recibido")


def eliminar_expediente():
    print("\n--- ELIMINAR EXPEDIENTE ---")

    codigo = input("Ingrese el código del expediente: ").strip().upper()

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            expedientes.remove(expediente)
            guardar_expedientes()

            print("Expediente eliminado correctamente.")
            return

    print("No se encontró el expediente.")


def mostrar_expediente(expediente):
    print("\n------------------------------")
    print("Código:", expediente["codigo"])
    print("DNI:", expediente["dni"])
    print("Paciente:", expediente["nombre"])
    print("Área:", expediente["area"])
    print("Asunto:", expediente["asunto"])
    print("Fecha:", expediente["fecha"])
    print("Estado:", expediente["estado"])
    print("------------------------------")


def buscar_por_dni():
    print("\n--- BUSCAR POR DNI ---")

    dni = input("Ingrese el DNI: ").strip()
    encontrado = False

    for expediente in expedientes:
        if expediente["dni"] == dni:
            mostrar_expediente(expediente)
            encontrado = True

    if not encontrado:
        print("No se encontraron expedientes con ese DNI.")


def buscar_por_codigo():
    print("\n--- BUSCAR POR CÓDIGO ---")

    codigo = input("Ingrese el código: ").strip().upper()

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            mostrar_expediente(expediente)
            return

    print("No se encontró el expediente.")


def buscar_por_area():
    print("\n--- BUSCAR POR ÁREA ---")

    area = input("Ingrese el área médica: ").strip().lower()
    encontrado = False

    for expediente in expedientes:
        if expediente["area"].lower() == area:
            mostrar_expediente(expediente)
            encontrado = True

    if not encontrado:
        print("No se encontraron expedientes en esa área.")


def mostrar_todos():
    print("\n--- LISTA DE EXPEDIENTES ---")

    if not expedientes:
        print("No hay expedientes registrados.")
        return

    for expediente in expedientes:
        mostrar_expediente(expediente)


def ordenar_por_codigo():
    print("\n--- ORDENAR POR CÓDIGO ---")

    if not expedientes:
        print("No hay expedientes registrados.")
        return

    n = len(expedientes)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if expedientes[j]["codigo"] > expedientes[j + 1]["codigo"]:
                expedientes[j], expedientes[j + 1] = expedientes[j + 1], expedientes[j]

    guardar_expedientes()

    print("Expedientes ordenados por código:")
    for expediente in expedientes:
        print(expediente["codigo"], "-", expediente["nombre"])


def buscar_y_consultar():
    print("\n--- BUSCAR Y CONSULTAR ---")
    print("1. Buscar por código")
    print("2. Buscar por DNI")
    print("3. Buscar por área")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        buscar_por_codigo()
    elif opcion == "2":
        buscar_por_dni()
    elif opcion == "3":
        buscar_por_area()
    else:
        print("Opcion no valida.")


def cambiar_estado():
    print("\n--- CAMBIAR ESTADO DEL TRÁMITE ---")

    codigo = input("Ingrese el código del expediente: ").strip().upper()

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print("Paciente:", expediente["nombre"])
            print("Estado actual:", expediente["estado"])

            for i in range(len(ESTADOS)):
                print(str(i + 1) + ". " + ESTADOS[i])

            opcion = input("Elija el nuevo estado (1-" + str(len(ESTADOS)) + "): ").strip()

            if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(ESTADOS):
                print("Estado no válido.")
                return

            nuevo_estado = ESTADOS[int(opcion) - 1]

            if nuevo_estado == expediente["estado"]:
                print("El expediente ya tiene ese estado.")
                return

            expediente["estado"] = nuevo_estado
            guardar_expedientes()

            print("Estado actualizado a:", nuevo_estado)
            return

    print("No se encontró el expediente.")


def actualizar_tramite():
    print("\n--- ACTUALIZAR TRÁMITE ---")
    print("1. Cambiar estado del trámite")
    print("2. Eliminar expediente (registrado por error)")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        cambiar_estado()
    elif opcion == "2":
        eliminar_expediente()
    else:
        print("Opcion no valida.")


def listar_por_estado():
    print("\n--- LISTAR POR ESTADO ---")

    for i in range(len(ESTADOS)):
        print(str(i + 1) + ". " + ESTADOS[i])

    opcion = input("Elija el estado (1-" + str(len(ESTADOS)) + "): ").strip()

    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(ESTADOS):
        print("Estado no válido.")
        return

    estado = ESTADOS[int(opcion) - 1]
    cantidad = 0

    for expediente in expedientes:
        if expediente["estado"] == estado:
            print(expediente["codigo"], "-", expediente["nombre"], "-", expediente["area"])
            cantidad = cantidad + 1

    print("Total en estado", estado + ":", cantidad)


def listar_y_ordenar():
    print("\n--- LISTAR Y ORDENAR ---")
    print("1. Mostrar todos los expedientes")
    print("2. Ordenar por código")
    print("3. Listar por estado")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        mostrar_todos()
    elif opcion == "2":
        ordenar_por_codigo()
    elif opcion == "3":
        listar_por_estado()
    else:
        print("Opcion no valida.")


def estadisticas():
    print("\n--- ESTADÍSTICAS DE EXPEDIENTES ---")

    total = len(expedientes)

    if total == 0:
        print("No hay expedientes registrados.")
        return

    # Arreglos paralelos: areas[i] tiene sus conteos en matriz[i]
    # Matriz (arreglo bidimensional): una fila por área, una columna por estado
    areas = []
    matriz = []

    for expediente in expedientes:
        area = expediente["area"].strip().title()

        if area not in areas:
            areas.append(area)
            matriz.append([0] * len(ESTADOS))

        fila = areas.index(area)
        columna = ESTADOS.index(expediente["estado"])
        matriz[fila][columna] = matriz[fila][columna] + 1

    hoy = datetime.now().strftime("%d/%m/%Y")
    registrados_hoy = 0
    pendientes = 0

    for expediente in expedientes:
        if expediente["fecha"] == hoy:
            registrados_hoy = registrados_hoy + 1
        if expediente["estado"] == "Recibido" or expediente["estado"] == "En proceso":
            pendientes = pendientes + 1

    print("Total de trámites:", total)
    print("Registrados hoy:", registrados_hoy)
    print("Pendientes (Recibido o En proceso):", pendientes)

    print("\nTrámites por estado:")
    for j in range(len(ESTADOS)):
        cantidad = 0
        for i in range(len(areas)):
            cantidad = cantidad + matriz[i][j]

        porcentaje = cantidad * 100 / total
        print(ESTADOS[j].ljust(12), str(cantidad).rjust(3), (str(round(porcentaje, 1)) + " %").rjust(8), "#" * cantidad)

    print("\nTrámites por área:")
    mayor = 0

    for i in range(len(areas)):
        cantidad = sum(matriz[i])
        porcentaje = cantidad * 100 / total
        print(areas[i].ljust(18), str(cantidad).rjust(3), (str(round(porcentaje, 1)) + " %").rjust(8), "#" * cantidad)

        if cantidad > sum(matriz[mayor]):
            mayor = i

    print("\nÁrea con más trámites:", areas[mayor])

    print("\nCuadro área x estado:")
    encabezado = "Área".ljust(18)
    for estado in ESTADOS:
        encabezado = encabezado + estado[:10].rjust(11)
    print(encabezado)

    for i in range(len(areas)):
        linea = areas[i].ljust(18)
        for j in range(len(ESTADOS)):
            linea = linea + str(matriz[i][j]).rjust(11)
        print(linea)
