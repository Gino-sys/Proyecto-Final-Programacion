import serial
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QVBoxLayout, QPushButton, QLabel, QDialogButtonBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QGuiApplication
from interfaces.ui_interfaz import Ui_MainWindow
from controladores.ventana2_controller import Ventana2
from clases.torneos import Torneo  # Importar la clase Torneo

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(790, 460)

        # Crear una instancia de la clase Torneo con el nombre
        self.torneo = Torneo("Torneo Inicial")  # Nombre del torneo al crear la instancia

        # Conectar botones
        self.torneo_button.clicked.connect(self.abrir)
        self.ventana2 = None
        # Agregar animación de rebote al botón
        self.animar_boton()

          # Agregar la instancia serial para la comunicación con Arduino
        try:
            self.ser = serial.Serial('/dev/ttyACM5', 9600)  # Asegúrate de poner el puerto correcto
            print("Puerto serial abierto con éxito")
        except serial.SerialException as e:
            print(f"Error al abrir el puerto serial: {e}")
            self.ser = None  # Si hay un error, ser será None
            # Mostrar un mensaje de advertencia si no se puede abrir el puerto serial
            QMessageBox.critical(self, "Error de Comunicación", "No se pudo abrir el puerto serial. Asegúrate de que el dispositivo esté conectado.")


    def abrir(self):
        if self.ventana2 is None:
            # Pasar la instancia de Torneo a Ventana2
            self.ventana2 = Ventana2(self, self.torneo)
        self.ventana2.show()
        self.hide()

    def animar_boton(self):
        self.animation = QPropertyAnimation(self.torneo_button, b"geometry")
        self.animation.setDuration(800)
        self.animation.setStartValue(self.torneo_button.geometry())
        self.animation.setEndValue(self.torneo_button.geometry().adjusted(0, 6, 0, 6))
        self.animation.setEasingCurve(QEasingCurve.OutBounce)
        self.animation.setLoopCount(-1)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
