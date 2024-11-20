from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interfaces.ui_archivo8 import Ui_MainWindow
from controladores.ventana9_controller import ventana9


class ventana8(QMainWindow, Ui_MainWindow):
    def __init__(self, ventana_principal=None, texto=""):
        super().__init__()
        self.setupUi(self)
        self.resize(750, 485)  # Tamaño inicial
        self.setFixedSize(self.size())
        self.label_2.setText(texto)  # Muestra el texto en el QLabel
        self.ventana9 = None
        self.ventana1 = ventana_principal
        
        self.pushButton_2.clicked.connect(self.principio)

    def next(self):
        if self.ventana9 is None:
            self.ventana9 = ventana9(self)
        self.ventana9.show()
        self.hide()
    
    def principio(self):
        # Llamar al método de confirmación de cierre (lo vamos a manejar en closeEvent)
        self.close()

    def closeEvent(self, event):
        # Crear la ventana de confirmación
        reply = QMessageBox.question(self, 'Confirmar Cierre', '¿Estás seguro de que deseas salir?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # Si el usuario selecciona "Sí", cerrar la ventana
        if reply == QMessageBox.Yes:
            event.accept()  # Permite que se cierre la ventana
        else:
            event.ignore()  # No permite el cierre de la ventana
