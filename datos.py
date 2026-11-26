# datos.py
# Datos del sistema y lectura/escritura del archivo.
import json
import os

ARCHIVO = "expedientes.json"
RESPALDO = "expedientes_respaldo.json"

# Catálogos (arreglos unidimensionales)
ESTADOS = ["Recibido", "En proceso", "Atendido", "Archivado"]
AREAS = ["Triaje", "Medicina General", "Laboratorio", "Obstetricia", "Pediatría", "Odontología"]

# Lista principal: un diccionario por expediente
expedientes = []


def cargar_expedientes():
    """Lee el archivo JSON y llena la lista expedientes."""
    if not os.path.exists(ARCHIVO):
        return

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        for expediente in datos:
            expedientes.append(expediente)

    except json.JSONDecodeError:
        print("El archivo está dañado. Se usará el respaldo si existe.")

        if os.path.exists(RESPALDO):
            with open(RESPALDO, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            for expediente in datos:
                expedientes.append(expediente)

            print("Se recuperaron", len(expedientes), "expedientes del respaldo.")


def guardar_expedientes():
    """Guarda la lista en el archivo y deja una copia de respaldo."""
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(expedientes, archivo, ensure_ascii=False, indent=4)

    with open(RESPALDO, "w", encoding="utf-8") as archivo:
        json.dump(expedientes, archivo, ensure_ascii=False, indent=4)
