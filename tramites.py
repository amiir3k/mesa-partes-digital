# tramites.py
# Registrar, buscar, actualizar estado, listar y ordenar expedientes.
from datetime import datetime

from datos import expedientes, ESTADOS, AREAS, guardar_expedientes
from validaciones import pedir_dni, pedir_texto, elegir_de_lista


# ---------- funciones de apoyo (con retorno) ----------

def generar_codigo():
    """Crea el siguiente código EXP-AAAA-NNNN según el último registrado del año."""
    anio = datetime.now().strftime("%Y")
    mayor = 0

    for expediente in expedientes:
        partes = expediente["codigo"].split("-")      # "EXP-2026-0007" -> ["EXP", "2026", "0007"]

        if partes[1] == anio and int(partes[2]) > mayor:
            mayor = int(partes[2])

    return "EXP-" + anio + "-" + str(mayor + 1).zfill(4)


def buscar_indice(codigo):
    """Búsqueda lineal: devuelve la posición del expediente o -1 si no existe."""
    for i in range(len(expedientes)):
        if expedientes[i]["codigo"] == codigo:
            return i

    return -1


def clave_fecha(fecha):
    """Convierte "dd/mm/aaaa" en "aaaa/mm/dd" para poder ordenar por fecha."""
    partes = fecha.split("/")
    return partes[2] + "/" + partes[1] + "/" + partes[0]


def mostrar_expediente(expediente):
    """Imprime la ficha de un expediente (recibe un parámetro)."""
    print("------------------------------")
    print("Código :", expediente["codigo"])
    print("DNI    :", expediente["dni"])
    print("Nombre :", expediente["nombre"])
    print("Área   :", expediente["area"])
    print("Asunto :", expediente["asunto"])
    print("Fecha  :", expediente["fecha"])
    print("Estado :", expediente["estado"])
    print("------------------------------")


def mostrar_tabla(lista):
    """Imprime varios expedientes en forma de tabla."""
    print("CÓDIGO".ljust(15) + "NOMBRE".ljust(24) + "ÁREA".ljust(18) + "FECHA".ljust(12) + "ESTADO")
    print("-" * 80)

    for expediente in lista:
        print(expediente["codigo"].ljust(15) + expediente["nombre"][:22].ljust(24)
              + expediente["area"].ljust(18) + expediente["fecha"].ljust(12) + expediente["estado"])


def guardar_cargo(expediente):
    """Escribe el cargo de recepción en un archivo de texto."""
    nombre_archivo = "cargo_" + expediente["codigo"] + ".txt"

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("CARGO DE RECEPCIÓN - MESA DE PARTES\n")
        archivo.write("Código : " + expediente["codigo"] + "\n")
        archivo.write("Nombre : " + expediente["nombre"] + "\n")
        archivo.write("DNI    : " + expediente["dni"] + "\n")
        archivo.write("Área   : " + expediente["area"] + "\n")
        archivo.write("Asunto : " + expediente["asunto"] + "\n")
        archivo.write("Fecha  : " + expediente["fecha"] + "\n")

    return nombre_archivo


# ---------- opción 1: registrar ----------

def registrar_expediente():
    print("\n--- REGISTRAR EXPEDIENTE ---")

    dni = pedir_dni()

    # Control de duplicidad: avisar si el DNI ya tiene un trámite pendiente
    for expediente in expedientes:
        if expediente["dni"] == dni and (expediente["estado"] == "Recibido" or expediente["estado"] == "En proceso"):
            print("Atención: este DNI ya tiene un trámite pendiente:")
            mostrar_expediente(expediente)
            respuesta = input("¿Registrar de todas formas? (s/n): ").strip().lower()

            if respuesta != "s":
                print("Registro cancelado.")
                return

    nombre = pedir_texto("Nombre completo: ").title()
    area = elegir_de_lista("Área de destino:", AREAS)
    asunto = pedir_texto("Asunto del trámite: ")

    nuevo = {
        "codigo": generar_codigo(),
        "dni": dni,
        "nombre": nombre,
        "area": area,
        "asunto": asunto,
        "fecha": datetime.now().strftime("%d/%m/%Y"),
        "estado": "Recibido"
    }

    expedientes.append(nuevo)
    guardar_expedientes()
    archivo_cargo = guardar_cargo(nuevo)

    print("\n¡Expediente registrado correctamente!")
    mostrar_expediente(nuevo)
    print("Cargo guardado en:", archivo_cargo)


# ---------- opción 2: buscar y consultar ----------

def buscar_y_consultar():
    print("\n--- BUSCAR Y CONSULTAR ---")
    criterio = elegir_de_lista("Buscar por:", ["Código", "DNI", "Nombre", "Área"])

    if criterio == "Código":
        codigo = input("Código (EXP-AAAA-NNNN): ").strip().upper()
        posicion = buscar_indice(codigo)

        if posicion == -1:
            print("No se encontró el expediente.")
        else:
            mostrar_expediente(expedientes[posicion])
        return

    if criterio == "DNI":
        dni = pedir_dni()
    elif criterio == "Nombre":
        texto = pedir_texto("Nombre o parte del nombre: ").lower()
    else:
        area = elegir_de_lista("Área:", AREAS)

    encontrados = []

    for expediente in expedientes:
        if criterio == "DNI" and expediente["dni"] == dni:
            encontrados.append(expediente)
        elif criterio == "Nombre" and texto in expediente["nombre"].lower():
            encontrados.append(expediente)
        elif criterio == "Área" and expediente["area"] == area:
            encontrados.append(expediente)

    if len(encontrados) == 0:
        print("No se encontraron expedientes.")
    else:
        mostrar_tabla(encontrados)
        print("Encontrados:", len(encontrados))


# ---------- opción 3: actualizar estado ----------

def actualizar_estado():
    print("\n--- ACTUALIZAR ESTADO DEL TRÁMITE ---")

    codigo = input("Código del expediente: ").strip().upper()
    posicion = buscar_indice(codigo)

    if posicion == -1:
        print("No se encontró el expediente.")
        return

    expediente = expedientes[posicion]
    actual = ESTADOS.index(expediente["estado"])

    if actual == len(ESTADOS) - 1:
        print("El expediente ya está archivado. No se puede cambiar.")
        return

    print("Estado actual:", expediente["estado"])
    siguientes = ESTADOS[actual + 1:]                # solo se puede avanzar
    nuevo_estado = elegir_de_lista("Nuevo estado:", siguientes)

    expediente["estado"] = nuevo_estado
    guardar_expedientes()

    print("Estado actualizado:", ESTADOS[actual], "->", nuevo_estado)


# ---------- opción 4: listar y ordenar ----------

def ordenar_burbuja(campo):
    """Ordena la lista por "codigo", "nombre" o "fecha" con el método burbuja."""
    n = len(expedientes)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            a = expedientes[j][campo]
            b = expedientes[j + 1][campo]

            if campo == "fecha":
                a = clave_fecha(a)
                b = clave_fecha(b)

            if a > b:
                expedientes[j], expedientes[j + 1] = expedientes[j + 1], expedientes[j]


def listar_y_ordenar():
    print("\n--- LISTAR Y ORDENAR ---")

    if len(expedientes) == 0:
        print("No hay expedientes registrados.")
        return

    opcion = elegir_de_lista("¿Qué desea hacer?", ["Listar todos", "Ordenar por código",
                             "Ordenar por nombre", "Ordenar por fecha", "Listar por estado"])

    if opcion == "Listar todos":
        mostrar_tabla(expedientes)
    elif opcion == "Listar por estado":
        estado = elegir_de_lista("Estado:", ESTADOS)
        lista = []

        for expediente in expedientes:
            if expediente["estado"] == estado:
                lista.append(expediente)

        mostrar_tabla(lista)
        print("Total en estado", estado + ":", len(lista))
    else:
        if opcion == "Ordenar por código":
            ordenar_burbuja("codigo")
        elif opcion == "Ordenar por nombre":
            ordenar_burbuja("nombre")
        else:
            ordenar_burbuja("fecha")

        guardar_expedientes()
        mostrar_tabla(expedientes)
