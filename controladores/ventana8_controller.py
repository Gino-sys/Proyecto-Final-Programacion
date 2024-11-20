from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo8 import Ui_MainWindow
from controladores.ventana9_controller import ventana9


class ventana8(QMainWindow, Ui_MainWindow):
    def __init__(self, ventana1 = None, ventana_principal=None):
        super().__init__()
        self.setupUi(self,)
        self.resize(685, 460)  # Tamaño inicial
        self.setFixedSize(self.size())
        self.ventana1 = ventana_principal  # Guarda la referencia de ventana1
        
        
        
        self.ventana9 = None
        self.ventana1 = ventana1


        self.pushButton_2.clicked.connect(self.principio)
    def next(self):
        if self.ventana9 is None:
            self.ventana9 = ventana9()
        self.ventana9.show()
        self.hide()     

    def principio (self):
        if self.ventana1 is not None:
            self.ventana1.show()
        self.hide()




