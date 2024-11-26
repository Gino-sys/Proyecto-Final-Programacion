from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
import json
from interfaces.ui_archivo9 import Ui_MainWindow


class ventana9(QMainWindow, Ui_MainWindow):
    def __init__(self, ventana_anterior=None):
        super().__init__()
        self.setupUi(self)
        self.resize(840, 495)  # Tamaño inicial
        self.setFixedSize(self.size())
        self.animar_boton()

        self.ventana_anterior = ventana_anterior  # Guarda la referencia a la ventana anterior
        self.archivo_json = "datos/historial.json"  # Ruta al archivo JSON
        self.cargar_datos_json()  # Carga los datos del JSON al iniciar

        # Conecta los botones
        self.pushButton.clicked.connect(self.buscar)  # Botón "BUSCAR"
        self.pushButton_2.clicked.connect(self.regresar)  # Botón "VOLVER"

    def cargar_datos_json(self):
        """Carga los datos del archivo JSON."""
        try:
            with open(self.archivo_json, "r") as archivo:
                self.datos = json.load(archivo)
        except FileNotFoundError:
            self.datos = []  # Si no existe el archivo, crea una lista vacía
        except json.JSONDecodeError:
            self.datos = []  # Si hay un error en el archivo JSON, crea una lista vacía

    def buscar(self):
        """Busca los datos de un equipo en el JSON y los muestra en el QListWidget."""
        nombre_equipo = self.lineEdit.text().strip()
        self.listWidget.clear()  # Limpia el listado antes de mostrar los resultados

        if not nombre_equipo:
            self.listWidget.addItem("Por favor, ingrese el nombre de un equipo.")
            return

        # Filtrar los partidos relacionados con el equipo buscado
        resultados = [partido for partido in self.datos if partido["equipo"] == nombre_equipo]

        if resultados:
            for partido in resultados:
                item = QListWidgetItem(
                    f"{partido['partido']} - Resultado: {partido['resultado']}"
                )
                self.listWidget.addItem(item)
        else:
            self.listWidget.addItem("No se encontraron resultados para el equipo ingresado.")

    def regresar(self):
        """Vuelve a la ventana anterior."""
        if self.ventana_anterior is not None:
            self.ventana_anterior.show()
        self.hide()
    def animar_boton(self):
        # Crear una animación para el botón torneo_button
        self.animation = QPropertyAnimation(self.pushButton, b"geometry")
        self.animation.setDuration(800)  # Duración total del rebote
        self.animation.setStartValue(self.pushButton.geometry())  # Posición inicial
        self.animation.setEndValue(self.pushButton.geometry().adjusted(6, 0, 6, 0))  # Mover ligeramente hacia abajo

        # Usar una curva de animación para el efecto de rebote
        self.animation.setEasingCurve(QEasingCurve.OutBounce)

        # Repetir indefinidamente
        self.animation.setLoopCount(-1)
        self.animation.start() 
    