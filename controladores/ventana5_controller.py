from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo5 import Ui_MainWindow
from controladores.ventana6_controller import ventana6


class ventana5(QMainWindow, Ui_MainWindow):
    def __init__(self, texto="", nombres_equipos=None, ventana_anterior=None, ventana_principal=None):
        super().__init__()
        self.setupUi(self)
        self.label.setText(texto)  # Muestra el texto en el QLabel
        self.resize(650, 385)  # Tamaño inicial
        self.setFixedSize(self.size())
        self.ventana1 = ventana_principal  # Guarda la referencia de ventana1
        self.texto_torneo = texto  # Guarda el texto para pasarlo a ventana5



        self.ventana6 = None
        self.nombres_equipos = nombres_equipos
        self.ventana_anterior = ventana_anterior  # Guarda la referencia a ventana4
        # Conecta el botón `pushButton_2` para volver a `ventana4`
        self.pushButton_2.clicked.connect(self.Volver)

    def Volver(self):
        # Muestra ventana4 y cierra ventana5
        if self.ventana_anterior is not None:
            self.ventana_anterior.show()
        self.close()
        
    def siguiente(self):
        # Obtén los nombres actualizados de los equipos de ventana 4
        nombres_equipos_actualizados = [line_edit.text() for line_edit in self.ventana_anterior.line_edits]

        # Si ventana6 ya existe, actualiza los equipos
        if self.ventana6 is not None:
            self.ventana6.actualizar_equipos(nombres_equipos_actualizados)
        else:
            # Si ventana6 no existe, créala con los datos actuales
            self.ventana6 = ventana6(nombres_equipos_actualizados, self.ventana1, self.texto_torneo)
    
        self.ventana6.show()
        self.hide()  # Cierra la ventana actual
