# Mesa de Partes Digital – WawaRed

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Estado](https://img.shields.io/badge/estado-prototipo%20acad%C3%A9mico-155E6B)
![Licencia](https://img.shields.io/badge/licencia-MIT-green)

Prototipo de consola en Python que digitaliza el registro de expedientes de la mesa de partes del área de **Admisión** de un centro de salud del MINSA. Permite **registrar, validar, buscar, ordenar, eliminar y guardar** expedientes en un archivo JSON, sin bases de datos ni librerías externas (solo módulos estándar de Python).

Proyecto del desafío **«Del archivador al algoritmo: un prototipo para la mesa de partes digital»**, curso *Fundamentos de Programación (CIIN1205P)*, Universidad Privada del Norte.

---

## Contenido

- [Contexto y problema](#contexto-y-problema)
- [Funcionalidades](#funcionalidades)
- [Demostración](#demostración)
- [Instalación y uso](#instalación-y-uso)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Formato de los datos](#formato-de-los-datos)
- [Diseño del algoritmo](#diseño-del-algoritmo)
- [Pruebas](#pruebas)
- [Limitaciones y trabajo futuro](#limitaciones-y-trabajo-futuro)
- [Equipo](#equipo)
- [Licencia](#licencia)

---

## Contexto y problema

La **Ley N.° 31170** obliga a las entidades del Estado a implementar mesas de partes digitales. En el área de Admisión del **Centro de Salud Tupac Amaru (MINSA, categoría I-3)** se observó, el 03/10/2026, que:

- Se atienden **20 a 30 historias por día**.
- La historia clínica se busca **a mano en archivadores** ordenados por número.
- Los problemas frecuentes son la **pérdida** y la **duplicidad** de historias.

![Proceso actual](docs/img/proceso-actual.png)

El diagrama de Ishikawa resume las causas del problema en seis categorías (6M):

![Diagrama de Ishikawa](docs/img/ishikawa.png)

**Solución:** un registro digital propio, con código único, validaciones y búsqueda inmediata, que se guarda en un archivo para no perder ningún trámite.

![Proceso propuesto](docs/img/proceso-propuesto.png)

> El prototipo solo guarda **datos administrativos** del trámite (código, DNI, nombre, área, asunto y fecha). No guarda diagnósticos ni información clínica, y todos los datos de ejemplo son **ficticios**.

---

## Funcionalidades

| Opción | Función | Qué hace |
|:-:|---|---|
| 1 | `registrar_expediente()` | Registra un expediente con la fecha del día. Valida código único, DNI de 8 dígitos y campos obligatorios |
| 2 | `eliminar_expediente()` | Elimina un expediente por su código |
| 3 | `buscar_por_dni()` | Muestra todos los expedientes de un DNI |
| 4 | `buscar_por_codigo()` | Muestra el expediente con ese código |
| 5 | `buscar_por_area()` | Muestra los expedientes de un área (sin importar mayúsculas) |
| 6 | `mostrar_todos()` | Lista todos los expedientes |
| 7 | `ordenar_por_codigo()` | Ordena por código con el método burbuja y guarda el resultado |
| 8 | — | Sale del sistema |

Cada cambio se guarda automáticamente en `expedientes.json`, y al iniciar el programa se cargan los expedientes guardados.

---

## Demostración

| Registro y búsqueda tras reiniciar | Validaciones |
|:-:|:-:|
| ![Registro](docs/img/demo-registro.png) | ![Validaciones](docs/img/demo-validaciones.png) |

---

## Instalación y uso

**Requisitos:** Python 3.10 o superior. No necesita instalar librerías.

```bash
git clone https://github.com/amiir3k/mesa-partes-digital.git
cd mesa-partes-digital
python3 main.py
```

En Windows usa `python main.py`. Se necesita Python 3.10 o superior porque el menú usa `match/case`.

---

## Estructura del repositorio

```
mesa-partes-digital/
├── main.py            # Menú del sistema (while True + match/case)
├── funciones.py       # Lógica: registrar, eliminar, buscar, ordenar, cargar y guardar
├── expedientes.json   # Datos de ejemplo (ficticios); se crea al registrar el primero
├── docs/img/          # Diagramas y capturas usados en este README
├── .gitignore
├── LICENSE
└── README.md
```

---

## Formato de los datos

`expedientes.json` guarda una **lista de diccionarios**, uno por expediente:

```json
[
    {
        "codigo": "EXP-2026-0007",
        "dni": "45871236",
        "nombre": "Rosa Quispe Mamani",
        "area": "Triaje",
        "asunto": "Apertura de historia clínica",
        "fecha": "02/11/2026"
    }
]
```

- Al iniciar, `cargar_expedientes()` lo lee con `json.load`; después de cada cambio, `guardar_expedientes()` lo reescribe con `json.dump(..., ensure_ascii=False, indent=4)` para conservar tildes y ñ.
- Si el archivo está dañado, el programa avisa y arranca con la lista vacía.

---

## Diseño del algoritmo

### Organización modular

![Módulos](docs/img/modulos.png)

### Flujo del programa principal

```mermaid
flowchart TD
    A([Inicio]) --> B[cargar_expedientes]
    B --> C[/Mostrar menú y leer opción/]
    C --> D{match opción}
    D -- 1 --> E[registrar_expediente]
    D -- 2 --> F[eliminar_expediente]
    D -- 3 --> G[buscar_por_dni]
    D -- 4 --> H[buscar_por_codigo]
    D -- 5 --> I[buscar_por_area]
    D -- 6 --> J[mostrar_todos]
    D -- case _ --> L[/Opción no válida/]
    D -- 7 --> K[ordenar_por_codigo]
    D -- 8 --> Z([Fin])
    E & F & G & H & I & J & K & L --> C
```

### Registro y ordenamiento

| Registro | Ordenamiento burbuja |
|:-:|:-:|
| ![Flujo registrar](docs/img/flujo-registrar.png) | ![Flujo ordenar](docs/img/flujo-ordenar.png) |

### Conceptos aplicados

| Concepto | Dónde |
|---|---|
| Estructuras de control | `while True` y `match/case` del menú, `if` en validaciones, `for` en búsquedas y dos `for` anidados en la burbuja |
| Funciones | 10 funciones en `funciones.py`; `mostrar_expediente(expediente)` recibe un parámetro |
| Listas (arreglos) | Lista `expedientes` de diccionarios: `append`, `remove` e intercambio por índice |
| Cadenas | `strip()`, `upper()`, `lower()`, `isdigit()`, `len()` y fecha con `strftime("%d/%m/%Y")` |
| Archivos | `open()` en modo `"r"` y `"w"` con `encoding="utf-8"`, `json.load` / `json.dump`, `os.path.exists` |
| Manejo de errores | `try/except json.JSONDecodeError` al cargar |

### Eficiencia

| Expedientes (n) | Búsqueda lineal (comparaciones) | Burbuja n(n−1)/2 (comparaciones) | Guardar JSON |
|---|---|---|---|
| 25 (un día) | 25 | 300 | 0,3 ms |
| 660 (un mes) | 660 | 217 470 (31 ms) | 3 ms |
| 7 920 (un año) | 7 920 | 31 359 240 (4,4 s) | 33 ms |

La búsqueda lineal y el archivo JSON son suficientes incluso para un año de datos. La burbuja conviene para volúmenes diarios o mensuales.

---

## Pruebas

Se ejecutaron **17 casos de prueba** y todos dan el resultado esperado.

| Grupo | Casos |
|---|---|
| Registro y persistencia | Registro válido; el expediente sigue al reiniciar |
| Validaciones | Código repetido, DNI de 7 dígitos, DNI con letra, campo vacío, opción inválida |
| Búsquedas | Por DNI (con y sin resultados), por código inexistente, por área en minúsculas y área sin registros |
| Ordenamiento y eliminación | Orden en pantalla y en `expedientes.json`; eliminar existente e inexistente |
| Robustez | Archivo JSON dañado (avisa y sigue); código en minúsculas (`exp-2026-0007`) detectado como repetido |

---

## Limitaciones y trabajo futuro

- [ ] Copia de respaldo (`expedientes.bak`) antes de guardar, para no perder datos si el JSON se daña
- [ ] Generar el código `EXP-AAAA-NNNN` automáticamente
- [ ] Volver a pedir solo el dato incorrecto, en lugar de cancelar el registro
- [ ] Elegir el área de un catálogo numerado
- [ ] Reemplazar la burbuja por `sorted()` cuando haya miles de expedientes
- [ ] Migrar a una base de datos (SQLite) para varios usuarios

---

## Equipo

**Grupo 05** – Fundamentos de Programación (CIIN1205P), Facultad de Ingeniería, UPN
Docente: Ing. Jorge Chicana Aspajo

| Integrante | GitHub |
|---|---|
| Olivares Torres, Amir Alim | [amiir3k](https://github.com/amiir3k) |
| Pari Benites, Edgar Genaro | [EdgarPari2025](https://github.com/EdgarPari2025) |
| Castro Delgado, Yanilka Carla | [yamilka-cd](https://github.com/yamilka-cd) |
| Montoya Orccosupa, Renato Sebastian | [Renato123j](https://github.com/Renato123j) |
| Toboada Quispe, Cristian Alvaro | [Cristian2703-boop](https://github.com/Cristian2703-boop) |

---

## Licencia

Distribuido bajo la licencia MIT. Ver [LICENSE](LICENSE).
