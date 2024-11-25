from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from interfaces.ui_archivo4 import Ui_MainWindow
from controladores.ventana5_controller import ventana5
from clases.equipos import Equipos


class ventana4(QMainWindow, Ui_MainWindow):
    def __init__(self, texto_torneo="", ventana_principal=None):
        super().__init__()
        self.setupUi(self)
        self.resize(685, 460)  # Tamaño inicial
        self.setFixedSize(self.size())
        self.ventana1 = ventana_principal  # Guarda la referencia de ventana1
        self.animar_boton()
    
        self.texto_torneo = texto_torneo  # Guarda el texto para pasarlo a ventana5
        
        # Conecta los QLineEdit para los nombres de los equipos
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
        self.equipos = Equipos()  # Instancia de la clase Equipos

    def verificar_campos(self):
        # Verifica si todos los QLineEdit tienen contenido
        todos_completos = all(line_edit.text().strip() for line_edit in self.line_edits)
        self.pushButton.setEnabled(todos_completos)

    def siguiente(self):
<<<<<<< Updated upstream
    
        nombres_equipos = [line_edit.text() for line_edit in self.line_edits]
=======
        # Recoge los nombres de los equipos
        nombres_equipos = [line_edit.text().strip() for line_edit in self.line_edits]
>>>>>>> Stashed changes
        
        # Agregar los equipos a la instancia de Equipos
        for nombre in nombres_equipos:
            self.equipos.agregar_equipo(nombre)
        
        # Pasamos el texto del torneo y los equipos a la siguiente ventana (ventana 5)
        if self.ventana5 is None:
            self.ventana5 = ventana5(self.texto_torneo, self.equipos, self, self.ventana1)
        self.ventana5.show()
        self.hide()  # Cierra la ventana actual
    
    def animar_boton(self):
        # Crear una animación para el botón torneo_button
        self.animation = QPropertyAnimation(self.pushButton, b"geometry")
        self.animation.setDuration(800)  # Duración total del rebote
        self.animation.setStartValue(self.pushButton.geometry())  # Posición inicial
        self.animation.setEndValue(self.pushButton.geometry().adjusted(6, 0, 6, 0))  # Mover ligeramente hacia abajo

        # Usar una curva de animación para el efecto de rebote
        self.animation.setEasingCurve(QEasingCurve.OutBounce)

        # Repetir indefinidamente
        self.animation.setLoopCount(-1)
        self.animation.start()     
    
        
