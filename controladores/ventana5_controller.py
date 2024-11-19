from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo5 import Ui_MainWindow
from controladores.ventana6_controller import ventana6


class ventana5(QMainWindow, Ui_MainWindow):
    def __init__(self, texto="", nombres_equipos=None, ventana_anterior=None):
        super().__init__()
        self.setupUi(self)
        self.label.setText(texto)  # Muestra el texto en el QLabel
        self.resize(685, 460)  # Tamaño inicial
        self.setFixedSize(self.size())



        self.ventana6 = None
        self.nombres_equipos = nombres_equipos
        self.ventana_anterior = ventana_anterior  # Guarda la referencia a ventana4
        # Conecta el botón `pushButton_2` para volver a `ventana4`
        self.pushButton_2.clicked.connect(self.Volver)

    def Volver(self):
        # Muestra ventana4 y cierra ventana5
        if self.ventana_anterior is not None:
            self.ventana_anterior.show()
        self.hide()
        
    def siguiente(self):
        if self.ventana6 is None:
            self.ventana6 = ventana6(self.nombres_equipos)  # Pasa el texto a ventana6
        self.ventana6.show()
        self.hide()  # Cierra la ventana actual