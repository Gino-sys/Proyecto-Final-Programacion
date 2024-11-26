from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget, QHBoxLayout
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt
import json
from interfaces.ui_archivo9 import Ui_MainWindow


class ventana9(QMainWindow, Ui_MainWindow):
    def __init__(self, ventana_anterior=None):
        super().__init__()
        self.setupUi(self)
        self.resize(765, 440)  # Tamaño inicial
        self.setFixedSize(self.size())

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
                self.agregar_item_personalizado(partido['partido'], partido['resultado'])
        else:
            self.listWidget.addItem("No se encontraron resultados para el equipo ingresado.")

    def agregar_item_personalizado(self, partido, resultado):
        """Crea un elemento personalizado para el QListWidget."""
        # Crear un widget personalizado
        widget_item = QWidget(self)
        layout_item = QHBoxLayout(widget_item)
        layout_item.setContentsMargins(10, 5, 10, 5)

        # Etiqueta para el nombre del partido
        label_partido = QLabel(partido, self)
        label_partido.setFont(QFont("Cooper Black", 14, QFont.Bold))
        label_partido.setStyleSheet("color: #2C3E50;")
        layout_item.addWidget(label_partido, alignment=Qt.AlignLeft)

        # Etiqueta para el resultado
        label_resultado = QLabel(resultado, self)
        label_resultado.setFont(QFont("Cooper Black", 10, QFont.Bold))
        label_resultado.setStyleSheet("color: #16A085;")
        layout_item.addWidget(label_resultado, alignment=Qt.AlignRight)

        # Crear un QListWidgetItem para asociar con el widget personalizado
        list_item = QListWidgetItem(self.listWidget)
        list_item.setSizeHint(widget_item.sizeHint())
        self.listWidget.addItem(list_item)
        self.listWidget.setItemWidget(list_item, widget_item)

    def regresar(self):
        """Vuelve a la ventana anterior."""
        if self.ventana_anterior is not None:
            self.ventana_anterior.show()
        self.hide()
