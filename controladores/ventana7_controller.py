from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
from interfaces.ui_archivo7 import Ui_MainWindow
from controladores.ventana8_controller import Ventana8
from clases.torneos import Torneo  # Importamos la clase Torneo
import json

class Ventana7(QMainWindow, Ui_MainWindow):
    def __init__(self, nombres_equipos, ventana_principal=None, partidos=None):
        super().__init__()
        self.setupUi(self)
        self.nombres_equipos = nombres_equipos  # Recibe los nombres de los equipos
        self.ventana_principal = ventana_principal
        self.ganadores = []  # Lista para almacenar ganadores
        self.partidos_jugados = 0  # Contador de partidos jugados
        self.ser = self.ventana_principal.ser

        # Si no se pasan partidos, por defecto está vacío
        self.partidos = partidos if partidos is not None else []

        # Crear una instancia del Torneo
        self.torneo = Torneo("Torneo de Fútbol")  # Asignamos un nombre al torneo

        # Mostrar equipos en los labels 2 a 9
        self.mostrar_equipos()

        # Conexión del botón "siguiente"
        self.pushButton.clicked.connect(self.siguiente_pag)

        # Iniciar escucha de datos desde Arduino
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.listen_for_data)
        self.timer.start(100)  # Comprobar cada 100 ms

    def mostrar_equipos(self):
        """Muestra los nombres de los equipos en los labels 2 al 9"""
        labels = [
            self.label_2, self.label_3, self.label_4, self.label_5,
            self.label_6, self.label_7, self.label_8, self.label_9
        ]
        
        for i, nombre in enumerate(self.nombres_equipos):
            if i < len(labels):
                labels[i].setText(nombre)

        # Guardar los partidos en el JSON
        self.guardar_partidos()

    def guardar_partidos(self):
        """Guarda los partidos en el archivo JSON"""
        if len(self.nombres_equipos) >= 4:
            # Crear partidos basados en los equipos
            partidos = [
                (self.nombres_equipos[0], self.nombres_equipos[1]),
                (self.nombres_equipos[2], self.nombres_equipos[3]),
            ]
            for partido in partidos:
                self.torneo.guardar_partido(partido[0], partido[1], "0-0")  # Inicializa con marcador "0-0"

            # Guardamos los partidos en el archivo JSON
            self.torneo.guardar_json("torneo.json")
            print("Partidos guardados en torneo.json")

        # Además, actualizamos el archivo historial.json
        self.actualizar_historial(partidos)

    def actualizar_historial(self, partidos):
        """Actualiza el historial de partidos en el archivo JSON"""
        try:
            # Intentamos cargar el archivo actual para agregar los nuevos partidos
            with open("datos/historial.json", "r") as archivo:
                historial = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            historial = []  # Si no existe el archivo, o hay error, creamos una lista vacía

        # Añadir los nuevos partidos al historial
        for partido in partidos:
            historial.append({
                "equipo": partido[0],
                "partido": f"{partido[0]} vs {partido[1]}",
                "resultado": "0-0"  # Resultado inicial
            })

        # Guardar el historial actualizado en el archivo JSON
        with open("datos/historial.json", "w") as archivo:
            json.dump(historial, archivo, indent=4, ensure_ascii=False)
            print("Historial actualizado en historial.json")

    def listen_for_data(self):
        """Escucha los datos enviados desde Arduino periódicamente"""
        if self.ser and self.ser.is_open:
            while self.ser.in_waiting > 0:  # Mientras haya datos disponibles
                linea = self.ser.readline().decode('utf-8').strip()
                if linea.startswith("ganador:"):
                    ganador = linea.split(":")[1]
                    self.registrar_ganador(ganador)

    def registrar_ganador(self, ganador):
        """Registra el ganador y actualiza la interfaz"""
        labels = [
            self.label_10, self.label_11, self.label_12, 
            self.label_13, self.label_14, self.label_15, self.label_16
        ]

        if self.partidos_jugados < len(labels):
            labels[self.partidos_jugados].setText(ganador)
            self.ganadores.append(ganador)
            self.partidos_jugados += 1

            print(f"Ganador registrado: {ganador}")
        else:
            print("No se pueden registrar más ganadores. Límite de etiquetas alcanzado.")

    def siguiente_pag(self):
        """Método para avanzar a la ventana 8"""
        # Cargar los partidos desde el archivo JSON
        self.torneo.cargar_json("torneo.json")
        
        # Pasamos los equipos y partidos a la ventana 8
        texto = " - ".join(self.ganadores)  # Combina los ganadores en un texto
        self.ventana8 = Ventana8(self.ventana_principal, texto)
        self.ventana8.set_equipos(self.nombres_equipos)  # Enviamos los equipos a la ventana 8
        self.ventana8.show()
        self.hide()
