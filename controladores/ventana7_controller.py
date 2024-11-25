from PyQt5.QtWidgets import QMainWindow
from interfaces.ui_archivo7 import Ui_MainWindow
from controladores.ventana8_controller import ventana8
class ventana7(QMainWindow, Ui_MainWindow):
<<<<<<< HEAD
    def _init_(self, nombres_equipos, ventana_principal=None, torneo=None):
        super()._init_()
=======
    def __init__(self, nombres_equipos, ventana_principal=None, torneo=None):
        super().__init__()
>>>>>>> b76d7b7780ce1e39349639d2e884e2af2511fd68
        self.setupUi(self)
        self.ventana1 = ventana_principal
        self.torneo = torneo  # Recibe el objeto Torneo
        self.ventana8 = None

        labels = [
            self.label_2, self.label_3, self.label_4, self.label_5,
            self.label_6, self.label_7, self.label_8, self.label_9
        ]
        
        for i, nombre in enumerate(nombres_equipos):
            labels[i].setText(nombre)

        self.pushButton.clicked.connect(self.siguiente_pag)

    def siguiente_pag(self):
        """Pasa el torneo a la siguiente ventana."""
        if self.ventana8 is None:
            self.ventana8 = ventana8(self.torneo, self.ventana1)
        self.ventana8.show()
<<<<<<< HEAD
        self.hide()
=======
        self.hide()
>>>>>>> b76d7b7780ce1e39349639d2e884e2af2511fd68
