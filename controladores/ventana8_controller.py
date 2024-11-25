from PyQt5.QtWidgets import QMainWindow, QMessageBox
from interfaces.ui_archivo8 import Ui_MainWindow
from controladores.ventana9_controller import ventana9
from clases.torneos import Torneo

class ventana8(QMainWindow, Ui_MainWindow):
    def __init__(self, torneo: Torneo, ventana_principal=None):
        super().__init__()
        self.setupUi(self)
        self.resize(750, 485)  # Tamaño inicial
        self.setFixedSize(self.size())

        # Referencias
        self.ventana9 = None
        self.torneo = torneo
        self.ventana1 = ventana_principal

<<<<<<< Updated upstream
=======
        # Actualiza el label con el nombre del torneo
        if self.torneo and hasattr(self.torneo, 'nombre'):
            self.label_2.setText(self.torneo.nombre)
        else:
            self.label_2.setText("Torneo no definido")
        
>>>>>>> Stashed changes
        self.pushButton_2.clicked.connect(self.principio)

    def next(self):
        """Método para avanzar a la ventana9."""
        if self.ventana9 is None:
            self.ventana9 = ventana9(self)
        self.ventana9.show()
        self.hide()

    def principio(self):
<<<<<<< Updated upstream
        QApplication.quit()  # Cierra toda la aplicación
=======
        """Regresa a la ventana principal."""
        self.close()

    def closeEvent(self, event):
        """Confirma antes de cerrar la ventana."""
        reply = QMessageBox.question(
            self,
            'Confirmar Cierre',
            '¿Estás seguro de que deseas salir?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
>>>>>>> Stashed changes
