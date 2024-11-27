from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from interfaces.ui_archivo8 import Ui_MainWindow
from controladores.ventana9_controller import ventana9
from clases.torneos import Torneo

class Ventana8(QMainWindow, Ui_MainWindow):
    def __init__(self, ventana_principal=None, texto=""):
        super().__init__()
        self.setupUi(self)
        self.resize(750, 485)
        self.setFixedSize(self.size())
        self.torneo = Torneo()  # Asigna un nombre inicial
        self.animar_boton()

        # Este texto es el que recibe de la ventana 7
        self.label_2.setText(texto)

        # Referencias
        self.ventana9 = None
        self.ventana1 = ventana_principal

        # Conexión de botones
        self.pushButton_2.clicked.connect(self.principio)
        self.pushButton.clicked.connect(self.next)

    def set_equipos(self, equipos):
        """Establece los equipos para la ventana 8."""
        self.equipos = equipos
        print(f"Equipos recibidos en ventana 8: {self.equipos}")

        # Actualiza los labels disponibles
        labels = [self.label_3, self.label_4, self.label_5]  # Lista de labels existentes
        for i, equipo in enumerate(self.equipos):
            if i < len(labels):  # Evita errores si hay más equipos que labels
                labels[i].setText(equipo)
            else:
                print(f"Advertencia: Más equipos que labels. Equipo '{equipo}' no asignado.")


    def next(self):
        """Método para avanzar a la ventana9."""
        if self.ventana9 is None:
            self.ventana9 = ventana9(self)
        self.ventana9.show()
        self.hide()

    def principio(self):
        """Método para volver al inicio."""
        self.close()

    def closeEvent(self, event):
        """Confirma el cierre de la ventana."""
        reply = QMessageBox.question(
            self, 'Confirmar Cierre', '¿Estás seguro de que deseas salir?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def animar_boton(self):
        """Animación del botón de la ventana 8."""
        self.animation = QPropertyAnimation(self.pushButton, b"geometry")
        self.animation.setDuration(800)
        self.animation.setStartValue(self.pushButton.geometry())
        self.animation.setEndValue(self.pushButton.geometry().adjusted(0, 6, 0, 6))
        self.animation.setEasingCurve(QEasingCurve.OutBounce)
        self.animation.setLoopCount(-1)
        self.animation.start()


