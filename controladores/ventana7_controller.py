from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo7 import Ui_MainWindow
from controladores.ventana8_controller import ventana8


class ventana7(QMainWindow, Ui_MainWindow):
    def __init__(self, nombres_equipos, ventana_principal=None, texto=""):
        super().__init__()
        self.setupUi(self)
        self.resize(850, 650)  # Tamaño inicial
        self.setFixedSize(self.size())
        self.ventana1 = ventana_principal  # Guarda la referencia de ventana1
        self.texto_torneo = texto  # Guarda el texto para pasarlo a ventana5
        
        self.ventana8 = None
        
        labels = [
            self.label_2, self.label_3, self.label_4, self.label_5,
            self.label_6, self.label_7, self.label_8, self.label_9
        ]
        
        for i, nombre in enumerate(nombres_equipos):
            labels[i].setText(nombre)
        
    def siguiente_pag(self):
        if self.ventana8 is None:
            self.ventana8 = ventana8(self.ventana1, self.texto_torneo)
        self.ventana8.show()
        self.hide()  # Cierra la ventana actual
        
