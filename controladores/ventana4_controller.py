from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo4 import Ui_MainWindow



class ventana4(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


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
        
        self.ventana_siguiente = None

    def verificar_campos(self):
        # Verifica si todos los QLineEdit tienen contenido
        todos_completos = all(line_edit.text().strip() for line_edit in self.line_edits)
        self.pushButton.setEnabled(todos_completos)

    def siguiente(self):
        if self.ventana_siguiente is None:
            self.ventana_siguiente = Ventana5()  # Cambia `Ventana5` por el nombre de la siguiente ventana
        self.ventana_siguiente.show()
        self.hide()  # Cierra la ventana actual