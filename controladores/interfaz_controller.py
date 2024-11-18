from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
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
        
    def abrir(self):
        if self.ventana2 is None:
            self.ventana2 = Ventana2()
        self.ventana2.show()
        self.hide()