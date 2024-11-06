# Simulador de Torneo de Copa del Mundo

Este proyecto es una aplicación de simulación de torneos de copa del mundo, desarrollada en Python con PyQt para la interfaz gráfica y Arduino para la integración de hardware. Permite crear un torneo, agregar equipos, realizar cruces de partidos, registrar resultados y visualizar estadísticas, como el equipo ganador y el equipo más goleador. La información del torneo se guarda en archivos `.json` o `.csv` para su persistencia.

## Características

- **Crear y gestionar torneos**: Agregar el nombre del torneo y equipos participantes (hasta un máximo de 8 equipos por torneo).
- **Simulación de partidos**: A través de un sistema de cruces, el usuario puede simular cada partido y registrar los goles.
- **Interfaz gráfica con PyQt**: Muestra los cruces de equipos, los resultados de cada partido y permite la navegación entre diferentes secciones del torneo.
- **Integración con Arduino**: Controla el marcador de los partidos usando un display 20x4 y tres botones en el Arduino para sumar goles y finalizar el partido.
- **Estadísticas del torneo**: Al finalizar el torneo, se muestran el podio (primer, segundo y tercer lugar), el equipo con más goles y el equipo más goleado.
- **Persistencia de datos**: Los datos del torneo se guardan automáticamente en archivos `.json` o `.csv`, permitiendo su recuperación en futuras sesiones.
- **Búsqueda de equipos**: El usuario puede buscar un equipo específico y visualizar su historial de partidos y resultados.

## Requisitos

### Software
- **Python 3.x**
- **Librerías de Python**:
  - `PyQt5`: Para la interfaz gráfica.
  - `json` o `csv`: Para la persistencia de datos.
  - `serial`: Para la comunicación entre Python y Arduino.
- **IDE para Arduino**: Para programar el display y los botones.

### Hardware
- **Arduino Uno**
- **Display 20x4 I2C**
- **3 Botones**: Para registrar goles y finalizar partidos.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/usuario/simulador-torneo-copa-del-mundo.git
   cd simulador-torneo-copa-del-mundo

2. **Instalar las dependencias de python**
   pip install pyqt5 pyserial

3. **Configurar arduino**
     Conecta el Arduino a la computadora y carga el código arduino/display_controller.ino en el dispositivo.
     Asegúrate de que el display y los botones estén correctamente conectados al Arduino y configurados según el código.

## **Ejecutar la aplicación:**

bash
Copiar código
python src/main.py
## **Crear un nuevo torneo:**

En la ventana inicial, ingresa el nombre del torneo y agrega hasta 8 equipos participantes.
## **Simular partidos:**

La interfaz muestra los cruces en formato de eliminación directa.
Al seleccionar un partido, se abre una nueva ventana donde el usuario puede iniciar el partido y utilizar los botones de Arduino para registrar los goles de cada equipo.
Al finalizar el partido, los resultados se guardan automáticamente.
## **Ver estadísticas:**

Al finalizar el torneo, puedes ver el podio de ganadores y los equipos con más goles anotados y recibidos.
Usa la barra de búsqueda para encontrar un equipo específico y ver su historial de partidos.

## **Estructura del Proyecto**
  src/: Contiene el código fuente del proyecto en Python.
  arduino/: Incluye el código de Arduino para el display y los botones.
  data/: Carpeta para archivos de persistencia en formato .json o .csv.
  README.md: Descripción del proyecto, instrucciones de uso e instalación.

## **Contribuciones y Créditos**
Este proyecto fue desarrollado por:

**Gino Candiotto**

**Facundo Medina**

**Juan Ignacio Farah**


Este archivo `README.md` incluye toda la información necesaria para comprender, instalar y usar el proyecto.
