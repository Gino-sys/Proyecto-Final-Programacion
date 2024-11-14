from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo7 import Ui_MainWindow



class ventana7(QMainWindow, Ui_MainWindow):
    def __init__(self, nombres_equipos):
        super().__init__()
        self.setupUi(self)
        
        labels = [
            self.label_2, self.label_3, self.label_4, self.label_5,
            self.label_6, self.label_7, self.label_8, self.label_9
        ]
        
        for i, nombre in enumerate(nombres_equipos):
            labels[i].setText(nombre)
        