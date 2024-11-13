from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo7 import Ui_MainWindow



class ventana7(QMainWindow, Ui_MainWindow):
    def __init__(self, nombres_equipos):
        super().__init__()
        self.setupUi(self)