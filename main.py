<<<<<<< HEAD

=======
>>>>>>> d4355f32c5f19f27d03011aa719b14fc01994607
import time
import sys
from controladores.interfaz_controller import MainWindow # Importa el controlador
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot



if __name__ == "__main__": #checkea si el script está siendo ejecutado como el prog principal (no importado como un modulo).
    app = QApplication(sys.argv)    # Crea un Qt widget, la cual va ser nuestra ventana.
    window = MainWindow()  
    window.show()
    sys.exit(app.exec_()) 

