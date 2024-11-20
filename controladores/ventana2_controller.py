import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from interfaces.ui_ventana2 import Ui_MainWindow
from controladores.ventana3_controller import ventana3  # Cambia 'archivo3' si usaste un nombre distinto

class Ventana2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Conectar la señal de texto del QLineEdit a la función que habilita el botón
        self.lineEdit.textChanged.connect(self.habilitar_boton)
        self.resize(790, 460)  # Tamaño inicial
        self.setFixedSize(self.size())
        
        
        # Deshabilitar el botón al iniciar
        self.pushButton.setEnabled(False)

        # Conectar el botón para cambiar de pestaña
        self.pushButton.clicked.connect(self.ir_a_siguiente_pestana)
        
        self.ventana3 = None
        self.animar_boton()
    
    def animar_boton(self):
        # Crear una animación para el botón torneo_button
        self.animation = QPropertyAnimation(self.pushButton, b"geometry")
        self.animation.setDuration(800)  # Duración total del rebote
        self.animation.setStartValue(self.pushButton.geometry())  # Posición inicial
        self.animation.setEndValue(self.pushButton.geometry().adjusted(0, 6, 0, 6))  # Mover ligeramente hacia abajo

        # Usar una curva de animación para el efecto de rebote
        self.animation.setEasingCurve(QEasingCurve.OutBounce)

        # Repetir indefinidamente
        self.animation.setLoopCount(-1)
        self.animation.start()    
        

    def habilitar_boton(self):
    
        text = self.lineEdit.text()  # Obtiene el texto directamente del QLineEdit
        self.pushButton.setEnabled(bool(text.strip()))  # Elimina espacios en blanco y verifica si tiene contenido
    
    def ir_a_siguiente_pestana(self):
        # Obtiene el texto del QLineEdit
        texto_para_mostrar = self.lineEdit.text()
        
        if self.ventana3 is None:
            # Pasa el texto como argumento al crear Ventana3
            self.ventana3 = ventana3(texto_para_mostrar)
        else:
            # Si la ventana ya está creada, solo actualiza el texto
            self.ventana3.actualizar_texto(texto_para_mostrar)
            
        self.ventana3.show()
        self.hide()