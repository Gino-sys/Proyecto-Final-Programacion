from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo5 import Ui_MainWindow



class ventana5(QMainWindow, Ui_MainWindow):
    def __init__(self, texto="", ventana_anterior=None):
        super().__init__()
        self.setupUi(self)
        self.label.setText(texto)  # Muestra el texto en el QLabel

        self.ventana_anterior = ventana_anterior  # Guarda la referencia a ventana4

        # Conecta el botón `pushButton_2` para volver a `ventana4`
        self.pushButton_2.clicked.connect(self.volver)

    def volver(self):
        # Muestra ventana4 y cierra ventana5
        if self.ventana_anterior is not None:
            self.ventana_anterior.show()
        self.close()