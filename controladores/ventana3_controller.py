from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from interfaces.ui_archivo3 import Ui_MainWindow
from controladores.ventana4_controller import ventana4
from clases.torneos import Torneo  # Importar la clase Torneo


class ventana3(QMainWindow, Ui_MainWindow):
    def __init__(self,texto="", ventana_principal=None, torneo=None):
        super().__init__()
        self.setupUi(self)
        self.resize(700, 495)  # Tamaño inicial
        self.setFixedSize(self.size())
        self.animar_boton()
        self.ventana4 = None
        self.ventana1 = ventana_principal  # Guarda la referencia de ventana1
        self.texto_torneo = texto  # Guarda el texto para pasarlo a la siguiente ventana


    def mostrar_texto(self, texto):
        # Actualiza un QLabel o QTextEdit para mostrar el texto
        self.label.setText(texto)  # Asegúrate de que 'label' sea el nombre del QLabel en tu UI

    def actualizar_texto(self, texto):
        # Método para actualizar el texto si la ventana ya está abierta
        self.mostrar_texto(texto)

    def otra(self):
        if self.ventana4 is None:
            self.ventana4 = ventana4(self.texto_torneo, self.ventana1)  # Pasa el torneo a ventana4
        self.ventana4.show()
        self.hide()
    
    def animar_boton(self):
        # Crear una animación para el botón torneo_button
        self.animation = QPropertyAnimation(self.pushButton, b"geometry")
        self.animation.setDuration(800)  # Duración total del rebote
        self.animation.setStartValue(self.pushButton.geometry())  # Posición inicial
        self.animation.setEndValue(self.pushButton.geometry().adjusted(0, 6, 0, 6))  # Mover ligeramente hacia abajo

        # Usar una curva de animación para el efecto de rebote
        self.animation.setEasingCurve(QEasingCurve.OutBounce)

        # Repetir indefinidamente
        self.animation.setLoopCount(-1)
        self.animation.start()