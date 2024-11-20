from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo9 import Ui_MainWindow



class ventana9(QMainWindow, Ui_MainWindow):
    def __init__(self, ventana_anterior = None):
        super().__init__()
        self.setupUi(self)
        self.resize(685, 460)  # Tamaño inicial
        self.setFixedSize(self.size())

        self.ventana_anterior = ventana_anterior  # Guarda la referencia a ventana4
        # Conecta el botón `pushButton_2` para volver a `ventana4`
        self.pushButton_2.clicked.connect(self.regresar)
    def buscar(self):
        return
    
    def regresar(self):
        # Muestra ventana4 y cierra ventana5
        if self.ventana_anterior is not None:
            self.ventana_anterior.show()
        self.hide()    
