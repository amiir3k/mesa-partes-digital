# reportes.py
# Estadísticas con arreglos paralelos y una matriz (arreglo bidimensional).
from datetime import datetime

from datos import expedientes, ESTADOS, AREAS


def porcentaje(parte, total):
    """Devuelve el porcentaje redondeado a 1 decimal."""
    return round(parte * 100 / total, 1)


def barra(cantidad):
    """Devuelve una barra de # para dibujar en la consola."""
    return "#" * cantidad


def estadisticas():
    print("\n--- ESTADÍSTICAS DE EXPEDIENTES ---")

    total = len(expedientes)

    if total == 0:
        print("No hay expedientes registrados.")
        return

    # Arreglos paralelos: AREAS[i] <-> por_area[i]  y  ESTADOS[j] <-> por_estado[j]
    por_area = [0] * len(AREAS)
    por_estado = [0] * len(ESTADOS)

    # Matriz: una fila por área y una columna por estado
    matriz = []
    for i in range(len(AREAS)):
        matriz.append([0] * len(ESTADOS))

    hoy = datetime.now().strftime("%d/%m/%Y")
    registrados_hoy = 0

    for expediente in expedientes:
        i = AREAS.index(expediente["area"])
        j = ESTADOS.index(expediente["estado"])

        por_area[i] = por_area[i] + 1
        por_estado[j] = por_estado[j] + 1
        matriz[i][j] = matriz[i][j] + 1

        if expediente["fecha"] == hoy:
            registrados_hoy = registrados_hoy + 1

    pendientes = por_estado[0] + por_estado[1]

    print("Total de trámites      :", total)
    print("Registrados hoy        :", registrados_hoy)
    print("Pendientes             :", pendientes, "(" + str(porcentaje(pendientes, total)) + " %)")

    print("\nPor estado:")
    for j in range(len(ESTADOS)):
        print("  " + ESTADOS[j].ljust(18) + str(por_estado[j]).rjust(3)
              + (str(porcentaje(por_estado[j], total)) + " %").rjust(9) + "  " + barra(por_estado[j]))

    print("\nPor área:")
    mayor = 0
    for i in range(len(AREAS)):
        print("  " + AREAS[i].ljust(18) + str(por_area[i]).rjust(3)
              + (str(porcentaje(por_area[i], total)) + " %").rjust(9) + "  " + barra(por_area[i]))

        if por_area[i] > por_area[mayor]:
            mayor = i

    print("\nÁrea con más trámites:", AREAS[mayor], "(" + str(por_area[mayor]) + ")")

    print("\nCuadro área x estado:")
    encabezado = "  " + "Área".ljust(18)
    for estado in ESTADOS:
        encabezado = encabezado + estado.rjust(11)
    print(encabezado)

    for i in range(len(AREAS)):
        linea = "  " + AREAS[i].ljust(18)
        for j in range(len(ESTADOS)):
            linea = linea + str(matriz[i][j]).rjust(11)
        print(linea)
