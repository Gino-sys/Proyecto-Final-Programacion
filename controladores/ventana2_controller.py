import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from interfaces.ui_ventana2 import Ui_MainWindow
from controladores.ventana3_controller import ventana3
from clases.torneos import Torneo  # Importar la clase Torneo

class Ventana2(QMainWindow, Ui_MainWindow):
    def __init__(self, ventana_principal=None):
        super().__init__()
        self.setupUi(self)
        
        self.resize(790, 460)  # Tamaño inicial
        self.setFixedSize(self.size())
        
        # Referencia a la ventana principal
        self.ventana1 = ventana_principal

        # Instancia de Torneo
        self.torneo = Torneo()

        # Conectar la señal de texto del QLineEdit a la función que habilita el botón
        self.lineEdit.textChanged.connect(self.habilitar_boton)

        # Deshabilitar el botón al iniciar
        self.pushButton.setEnabled(False)

        # Conectar el botón para cambiar de pestaña
        self.pushButton.clicked.connect(self.ir_a_siguiente_pestana)

        # Inicializar la referencia a ventana3
        self.ventana3 = None

        # Agregar animación al botón
        self.animar_boton()
    
    def animar_boton(self):
        # Crear una animación para el botón pushButton
        self.animation = QPropertyAnimation(self.pushButton, b"geometry")
        self.animation.setDuration(800)  # Duración total del rebote
        self.animation.setStartValue(self.pushButton.geometry())  # Posición inicial
        self.animation.setEndValue(self.pushButton.geometry().adjusted(0, 6, 0, 6))  # Mover ligeramente hacia abajo
        self.animation.setEasingCurve(QEasingCurve.OutBounce)  # Efecto rebote
        self.animation.setLoopCount(-1)  # Repetir indefinidamente
        self.animation.start()

    def habilitar_boton(self):
        # Habilitar el botón solo si el texto no está vacío
        text = self.lineEdit.text()
        self.pushButton.setEnabled(bool(text.strip()))

    def ir_a_siguiente_pestana(self):
    # Obtiene el texto del QLineEdit
        texto_para_mostrar = self.lineEdit.text()

        if self.ventana3 is None:
        # Pasa la instancia de torneo y la ventana1 a ventana3
            self.ventana3 = ventana3(texto_para_mostrar, self.ventana1, self.torneo)  # Pasa la instancia del torneo
        else:
        # Si la ventana ya está creada, solo actualiza el texto
            self.ventana3.actualizar_texto(texto_para_mostrar)
    
        self.ventana3.show()
        self.hide()