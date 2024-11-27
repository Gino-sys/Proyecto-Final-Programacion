from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget, QHBoxLayout
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt
import json
from interfaces.ui_archivo9 import Ui_MainWindow


class ventana9(QMainWindow, Ui_MainWindow):
    def __init__(self, ventana_anterior=None):
        super().__init__()
        self.setupUi(self)
        self.resize(765, 490)  # Tamaño inicial
        self.setFixedSize(self.size())
        self.animar_boton()
        self.animar_boton_2()

        self.ventana_anterior = ventana_anterior  # Guarda la referencia a la ventana anterior
        self.archivo_json = "datos/historial.json"  # Ruta al archivo JSON
        self.cargar_datos_json()  # Carga los datos del JSON al iniciar

        # Conecta los botones
        self.pushButton.clicked.connect(self.buscar)  # Botón "BUSCAR"
        self.pushButton_2.clicked.connect(self.regresar)  # Botón "VOLVER"
    
    def animar_boton(self):
        # Crear una animación para el botón torneo_button
        self.animation = QPropertyAnimation(self.pushButton, b"geometry")
        self.animation.setDuration(800)  # Duración total del rebote
        self.animation.setStartValue(self.pushButton.geometry())  # Posición inicial
        self.animation.setEndValue(self.pushButton.geometry().adjusted(1, 7, 1, 7))  # Mover ligeramente hacia abajo

        # Usar una curva de animación para el efecto de rebote
        self.animation.setEasingCurve(QEasingCurve.OutBounce)

        # Repetir indefinidamente
        self.animation.setLoopCount(-1)
        self.animation.start()

    def animar_boton_2(self):
        # Crear una animación para el botón torneo_button
        self.animation2 = QPropertyAnimation(self.pushButton_2, b"geometry")
        self.animation2.setDuration(800)  # Duración total del rebote
        self.animation2.setStartValue(self.pushButton_2.geometry())  # Posición inicial
        self.animation2.setEndValue(self.pushButton_2.geometry().adjusted(1, 7, 1, 7))  # Mover ligeramente hacia abajo

        # Usar una curva de animación para el efecto de rebote
        self.animation2.setEasingCurve(QEasingCurve.OutBounce)

        # Repetir indefinidamente
        self.animation2.setLoopCount(-1)
        self.animation2.start()    




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
        label_partido.setFont(QFont("Cooper Black", 14))  # Cambiado a Cooper Black
        label_partido.setStyleSheet("color: #2C3E50;")
        layout_item.addWidget(label_partido, alignment=Qt.AlignLeft)

        # Analizar el resultado
        try:
            equipo1_goles, equipo2_goles = map(int, resultado.split("-"))
            if equipo1_goles > equipo2_goles:
                estado = "Ganador"
                color_estado = "#16A085"  # Verde para ganador
            elif equipo1_goles < equipo2_goles:
                estado = "Perdedor"
                color_estado = "#E74C3C"  # Rojo para perdedor
            else:
                estado = "Empate"
                color_estado = "#7F8C8D"  # Gris para empate
        except ValueError:
            estado = "Resultado inválido"
            color_estado = "#7F8C8D"  # Gris para errores

        # Etiqueta para el resultado
        label_resultado = QLabel(f"{resultado} ({estado})", self)
        label_resultado.setFont(QFont("Cooper Black", 14, QFont.Bold))  # Cambiado a Cooper Black
        label_resultado.setStyleSheet(f"color: {color_estado};")
        layout_item.addWidget(label_resultado, alignment=Qt.AlignRight)

        # Crear un QListWidgetItem para asociar con el widget personalizado
        list_item = QListWidgetItem(self.listWidget)
        list_item.setSizeHint(widget_item.sizeHint())
        self.listWidget.addItem(list_item)
        self.listWidget.setItemWidget(list_item, widget_item)

    def regresar(self):
        """Vuelve a la ventana anterior y resetea el contenido."""
        if self.ventana_anterior is not None:
            self.ventana_anterior.show()
        # Limpiar el QListWidget y el QLineEdit
        self.listWidget.clear()
        self.lineEdit.clear()
        self.hide()
