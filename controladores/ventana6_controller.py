from PyQt5.QtWidgets import QMainWindow
from interfaces.ui_archivo6 import Ui_MainWindow
<<<<<<< HEAD
from controladores.ventana7_controller import Ventana7
=======
from controladores.ventana7_controller import ventana7
from clases.equipos import Equipos  # Importamos la clase Equipos
>>>>>>> b76d7b7780ce1e39349639d2e884e2af2511fd68

class ventana6(QMainWindow, Ui_MainWindow):
    def __init__(self, nombres_equipos, ventana_principal=None, texto=""):
        super().__init__()
        self.setupUi(self)
        self.resize(870, 600)  # Tamaño inicial
        self.setFixedSize(self.size())
        self.ventana1 = ventana_principal  # Guarda la referencia de ventana1
        self.texto_torneo = texto  # Guarda el texto para pasarlo a ventana5
        self.nombres_equipos = nombres_equipos  # Asigna los equipos

        # Asigna los nombres de los equipos a los labels en orden
        labels = [
            self.label_2, self.label_3, self.label_4, self.label_5,
            self.label_6, self.label_7, self.label_8, self.label_9
        ]
        for i, nombre in enumerate(nombres_equipos):
            labels[i].setText(nombre)

        # Asegúrate de que el botón esté conectado a la función sig
        self.pushButton.clicked.connect(self.sig)

        self.ventana7 = None

    def sig(self):
        # Aquí pasa los nombres de los equipos a la ventana7
        if self.ventana7 is None:
            self.ventana7 = ventana7(self.nombres_equipos, self.ventana1, self.texto_torneo)
        self.ventana7.show()
        self.hide()  # Cierra la ventana actual

    def actualizar_equipos(self, nombres_equipos):
        # Actualiza los nombres internamente
        self.nombres_equipos = nombres_equipos  
        labels = [
            self.label_2, self.label_3, self.label_4, self.label_5,
            self.label_6, self.label_7, self.label_8, self.label_9
        ]
        for i, nombre in enumerate(self.nombres_equipos):
            labels[i].setText(nombre)
<<<<<<< HEAD

=======
>>>>>>> b76d7b7780ce1e39349639d2e884e2af2511fd68
