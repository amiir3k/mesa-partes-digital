# validaciones.py
# Funciones que piden un dato y lo repiten hasta que sea correcto.


def es_dni_valido(dni):
    """Devuelve True si el DNI tiene exactamente 8 números."""
    return dni.isdigit() and len(dni) == 8


def pedir_dni():
    """Pide el DNI hasta que sea válido y lo devuelve."""
    dni = input("DNI del ciudadano (8 dígitos): ").strip()

    while not es_dni_valido(dni):
        print("El DNI debe contener 8 números.")
        dni = input("DNI del ciudadano (8 dígitos): ").strip()

    return dni


def pedir_texto(mensaje):
    """Pide un texto obligatorio, sin el carácter ; y lo devuelve."""
    texto = input(mensaje).strip()

    while texto == "" or ";" in texto:
        print("Este dato es obligatorio y no puede contener ;")
        texto = input(mensaje).strip()

    return texto


def elegir_de_lista(titulo, opciones):
    """Muestra una lista numerada y devuelve el elemento elegido."""
    print(titulo)

    for i in range(len(opciones)):
        print("  " + str(i + 1) + ". " + opciones[i])

    numero = input("Elija un número: ").strip()

    while not numero.isdigit() or int(numero) < 1 or int(numero) > len(opciones):
        print("Elija un número entre 1 y " + str(len(opciones)) + ".")
        numero = input("Elija un número: ").strip()

    return opciones[int(numero) - 1]
