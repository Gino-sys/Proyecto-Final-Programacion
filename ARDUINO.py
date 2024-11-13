from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo4 import Ui_MainWindow
from controladores.ventana5_controller import ventana5

class ventana4(QMainWindow, Ui_MainWindow):
    def __init__(self, texto_torneo=""):
        super().__init__()
        self.setupUi(self)
        
        self.texto_torneo = texto_torneo
        self.line_edits = [
            self.lineEdit_1, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4,
            self.lineEdit_5, self.lineEdit_6, self.lineEdit_7, self.lineEdit_8
        ]
        
        self.pushButton.setEnabled(False)
        for line_edit in self.line_edits:
            line_edit.textChanged.connect(self.verificar_campos)
        
        self.pushButton.clicked.connect(self.siguiente)
        
        # Listas para equipos y resultados
        self.equipos = []
        self.fixture = []
        self.ganadores = []
        self.partido_actual = 0
        
        self.ventana5 = None

    def verificar_campos(self):
        todos_completos = all(line_edit.text().strip() for line_edit in self.line_edits)
        self.pushButton.setEnabled(todos_completos)

    def siguiente(self):
        if self.ventana5 is None:
            self.equipos = [line_edit.text() for line_edit in self.line_edits]
            self.fixture = [(self.equipos[i], self.equipos[i+1]) for i in range(0, 8, 2)]
            self.mostrar_fixture()
            self.ventana5 = ventana5(self.texto_torneo, self)
        self.ventana5.show()
        self.hide()

    def actualizar_marcador(self, equipo1_goles, equipo2_goles):
        equipo1, equipo2 = self.fixture[self.partido_actual]
        if equipo1_goles > equipo2_goles:
            self.ganadores.append(equipo1)
        else:
            self.ganadores.append(equipo2)
        
        # Pasar al siguiente partido o a la siguiente ronda
        self.partido_actual += 1
        if self.partido_actual >= len(self.fixture):
            self.partido_actual = 0
            self.fixture = [(self.ganadores[i], self.ganadores[i+1]) for i in range(0, len(self.ganadores), 2)]
            self.ganadores = []
        self.mostrar_fixture()

    def mostrar_fixture(self):
        # Aquí se actualiza la interfaz para mostrar los partidos del fixture y los ganadores.
        pass
