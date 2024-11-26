
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QVBoxLayout, QPushButton, QLabel, QDialogButtonBox
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve, Qt
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QPushButton, QLabel, QDialogButtonBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve

from interfaces.ui_interfaz import Ui_MainWindow
from controladores.ventana2_controller import Ventana2
from clases.torneos import Torneo  # Importar la clase Torneo


class VentanaAyuda(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Instrucciones")
        self.setFixedSize(400, 300)  # Tamaño fijo de la ventana
        layout = QVBoxLayout()

        instrucciones = """Bienvenido a la aplicación de gestión de torneos.

        Paso 1: Ingrese el nombre del torneo en el campo correspondiente.
        Paso 2: Escriba los nombres de los 8 equipos en los campos de texto.
        Paso 3: Presione el botón para continuar y juegue su torneo.

        Después de jugar el torneo, podrá:
        - Ver la tabla de posiciones.
        - Filtrar por equipo y acceder a sus resultados.

        ¡Disfrute del torneo y que gane el mejor equipo!"""

        label_instrucciones = QLabel(instrucciones)
        label_instrucciones.setWordWrap(True)  # Permite que el texto se ajuste a varias líneas
        layout.addWidget(label_instrucciones)

        # Botón de cerrar
        boton_cerrar = QDialogButtonBox(QDialogButtonBox.Ok)
        boton_cerrar.accepted.connect(self.accept)
        layout.addWidget(boton_cerrar)

        self.setLayout(layout)

        # Centrar la ventana de ayuda en la pantalla
        self.centrar_ventana()

    def centrar_ventana(self):
        # Obtener el tamaño de la pantalla
        pantalla = QGuiApplication.primaryScreen().geometry()

        # Obtener el tamaño de la ventana
        size = self.geometry()

        # Calcular las coordenadas para centrar la ventana
        x = (pantalla.width() - size.width()) // 2
        y = (pantalla.height() - size.height()) // 2

        # Mover la ventana al centro de la pantalla
        self.move(x, y)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(790, 460)  # Tamaño inicial
        self.setFixedSize(self.size())

        # Crear una instancia de la clase Torneo
        self.torneo = Torneo()  # Asigna un nombre inicial

        # Conectar botones
        self.torneo_button.clicked.connect(self.abrir)
        self.ventana2 = None

        # Botón de ayuda
        self.ayuda_button = QPushButton("Ayuda", self)
        self.ayuda_button.setGeometry(650, 10, 100, 40)  # Posiciona el botón arriba a la derecha
        self.ayuda_button.clicked.connect(self.mostrar_ayuda)

        # Agregar animación de rebote al botón
        self.animar_boton()

    def abrir(self):
        if self.ventana2 is None:
            self.ventana2 = Ventana2(self)
        self.ventana2.show()
        self.hide()

    def animar_boton(self):
        # Crear una animación para el botón torneo_button
        self.animation = QPropertyAnimation(self.torneo_button, b"geometry")
        self.animation.setDuration(800)  # Duración total del rebote
        self.animation.setStartValue(self.torneo_button.geometry())  # Posición inicial
        self.animation.setEndValue(self.torneo_button.geometry().adjusted(0, 6, 0, 6))  # Mover ligeramente hacia abajo

        # Usar una curva de animación para el efecto de rebote
        self.animation.setEasingCurve(QEasingCurve.OutBounce)

        # Repetir indefinidamente
        self.animation.setLoopCount(-1)
        self.animation.start()

    def mostrar_ayuda(self):
        ventana_ayuda = VentanaAyuda()
        ventana_ayuda.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
