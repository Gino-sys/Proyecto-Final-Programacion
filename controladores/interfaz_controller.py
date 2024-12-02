import serial
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QVBoxLayout, QPushButton, QLabel, QDialogButtonBox
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve, Qt
from PyQt5.QtGui import QGuiApplication
from interfaces.ui_interfaz import Ui_MainWindow
from controladores.ventana2_controller import Ventana2
from clases.torneos import Torneo  # Importar la clase Torneo

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(790, 460)

        # Crear una instancia de la clase Torneo
        self.torneo = Torneo("Torneo de Fútbol")  # Nombre del torneo al crear la instancia

        # Conectar botones
        self.torneo_button.clicked.connect(self.abrir)
        self.ventana2 = None



        # Agregar la instancia serial para la comunicación con Arduino
        try:
            self.ser = serial.Serial('/dev/ttyACM2', 9600)  # Asegúrate de poner el puerto correcto
            print("Puerto serial abierto con éxito")
        except serial.SerialException as e:
            print(f"Error al abrir el puerto serial: {e}")
            self.ser = None  # Si hay un error, `ser` será `None` 
            # Mostrar un mensaje de advertencia si no se puede abrir el puerto serial
            QMessageBox.critical(self, "Error de Comunicación", "No se pudo abrir el puerto serial. Asegúrate de que el dispositivo esté conectado.")

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

        # Repetir 3 veces la animación
        self.animation.setLoopCount(3)
        self.animation.start()

    def mostrar_ayuda(self):
        ventana_ayuda = VentanaAyuda()
        ventana_ayuda.exec_()

    def closeEvent(self, event):
        # Cerrar el puerto serial correctamente cuando la aplicación se cierre
        if self.ser and self.ser.is_open:
            self.ser.close()
        event.accept()