from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo3 import Ui_MainWindow
from controladores.ventana4_controller import ventana4

class ventana3(QMainWindow, Ui_MainWindow):
    def __init__(self, texto=""):
        super().__init__()
        self.setupUi(self)

        self.ventana4 = None
        self.texto_torneo = texto  # Guarda el texto para pasarlo a la siguiente ventana

        # Muestra el texto recibido al iniciar la ventana
        self.mostrar_texto(texto)
        
    def mostrar_texto(self, texto):
        # Actualiza un QLabel o QTextEdit para mostrar el texto
        self.label.setText(texto)  # Asegúrate de que `label` sea el nombre del QLabel en tu UI

    def actualizar_texto(self, texto):
        # Método para actualizar el texto si la ventana ya está abierta
        self.mostrar_texto(texto)
        
    def otra(self):
        if self.ventana4 is None:
            self.ventana4 = ventana4(self.texto_torneo)
        self.ventana4.show()
        self.hide()