from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo4 import Ui_MainWindow
from controladores.ventana5_controller import ventana5


class ventana4(QMainWindow, Ui_MainWindow):
    def __init__(self, texto_torneo="", ventana_principal=None):
        super().__init__()
        self.setupUi(self)
        self.resize(685, 460)  # Tamaño inicial
        self.setFixedSize(self.size())
        self.ventana1 = ventana_principal  # Guarda la referencia de ventana1
        
        self.texto_torneo = texto_torneo  # Guarda el texto para pasarlo a ventana5
        # Suponiendo que los nombres de los QLineEdit en la interfaz son lineEdit1, lineEdit2, etc.
        self.line_edits = [
            self.lineEdit_1, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4,
            self.lineEdit_5, self.lineEdit_6, self.lineEdit_7, self.lineEdit_8
        ]
        
        # Conecta cada QLineEdit a la función que verifica el contenido
        for line_edit in self.line_edits:
            line_edit.textChanged.connect(self.verificar_campos)
        
        # Deshabilita el botón al iniciar
        self.pushButton.setEnabled(False)
        
        # Conecta el botón para abrir la siguiente ventana y cerrar esta
        self.pushButton.clicked.connect(self.siguiente)
        
        self.ventana5 = None

    def verificar_campos(self):
        # Verifica si todos los QLineEdit tienen contenido
        todos_completos = all(line_edit.text().strip() for line_edit in self.line_edits)
        self.pushButton.setEnabled(todos_completos)

    def siguiente(self):
    
        nombres_equipos = [line_edit.text().strip() for line_edit in self.line_edits]   
        if self.ventana5 is None:
            self.ventana5 = ventana5(self.texto_torneo, nombres_equipos, self, self.ventana1)  # Pasa el texto a ventana5
        self.ventana5.show()
        self.hide()  # Cierra la ventana actual