from PyQt5.QtWidgets import QMainWindow, QMessageBox
from interfaces.ui_archivo5 import Ui_MainWindow
from controladores.ventana6_controller import ventana6
from clases.torneos import Torneo  # Importamos la clase Torneo


class ventana5(QMainWindow, Ui_MainWindow, Torneo):
    def __init__(self,texto="", nombres_equipos=None, ventana_anterior=None, ventana_principal=None):
        super().__init__()
        self.setupUi(self)

        self.nombres_equipos = nombres_equipos or []  # Lista de nombres de los equipos
        self.ventana_anterior = ventana_anterior  # Referencia a la ventana4
        self.ventana_principal = ventana_principal  # Referencia a la ventana principal
        self.ventana6 = None  # Inicialmente no existe ventana6
        self.texto_torneo = texto  # Guarda el texto para pasarlo a ventana5

        # Ajustes de la ventana
        self.label.setText(f"{self.texto_torneo}")  # Mostrar nombre del torneo
        self.resize(705, 402)  # Tamaño inicial
        self.setFixedSize(self.size())

        # Conecta los botones a sus respectivas funciones
        self.pushButton_2.clicked.connect(self.Volver)  # Botón para volver a ventana4
        self.pushButton.clicked.connect(self.siguiente)  # Botón para ir a ventana6

    def Volver(self):
        # Regresa a la ventana anterior (ventana4) para editar equipos
        if self.ventana_anterior is not None:
            self.ventana_anterior.show()
        self.close()

    def siguiente(self):
        # Obtén los nombres actualizados de los equipos desde ventana4
        if self.ventana_anterior is not None:
            self.nombres_equipos = [line_edit.text() for line_edit in self.ventana_anterior.line_edits]

        # Verifica si hay exactamente 8 equipos
        if len(self.nombres_equipos) != 8:
            QMessageBox.warning(self, "Error", "Debes ingresar exactamente 8 equipos.")
            return

        # Si ventana6 ya existe, actualiza los equipos
        if self.ventana6 is not None:
            self.ventana6.actualizar_equipos(self.nombres_equipos)
        else:
            # Crea ventana6 con los datos actuales
            self.ventana6 = ventana6(self.nombres_equipos, self.ventana_principal, self.texto_torneo)
        
        self.ventana6.show()
        self.hide()  # Oculta la ventana actual
