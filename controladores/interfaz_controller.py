from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from interfaces.ui_interfaz import Ui_MainWindow
from controladores.ventana2_controller import Ventana2


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(790, 460)  # Tamaño inicial
        self.setFixedSize(self.size())

        self.torneo_button.clicked.connect(self.abrir)
        self.ventana2 = None

        # Agregar animación de rebote al botón
        self.animar_boton()

    def abrir(self):
        if self.ventana2 is None:
            self.ventana2 = Ventana2()
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


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
