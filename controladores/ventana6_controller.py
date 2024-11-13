from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo6 import Ui_MainWindow
from controladores.ventana7_controller import ventana7


class ventana6(QMainWindow, Ui_MainWindow):
    def __init__(self, nombres_equipos):
        super().__init__()
        self.setupUi(self)
        
        # Asigna los nombres de los equipos a los labels en orden
        labels = [
            self.label_2, self.label_3, self.label_4, self.label_5,
            self.label_6, self.label_7, self.label_8, self.label_9
        ]
        
        for i, nombre in enumerate(nombres_equipos):
            labels[i].setText(nombre)
            
    def sig(self):
        if self.ventana7 is None:
            self.ventana7 = ventana7()
        self.ventana7.show()
        self.hide()  # Cierra la ventana actual