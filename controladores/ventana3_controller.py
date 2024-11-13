from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo3 import Ui_MainWindow


class ventana3(QMainWindow, Ui_MainWindow):
    def __init__(self, texto=""):
        super().__init__()
        self.setupUi(self)

        self.ventana2 = None
        
        # Muestra el texto recibido al iniciar la ventana
        self.mostrar_texto(texto)
        
    def mostrar_texto(self, texto):
        # Actualiza un QLabel o QTextEdit para mostrar el texto
        self.label.setText(texto)  # Asegúrate de que `label` sea el nombre del QLabel en tu UI

    def actualizar_texto(self, texto):
        # Método para actualizar el texto si la ventana ya está abierta
        self.mostrar_texto(texto)