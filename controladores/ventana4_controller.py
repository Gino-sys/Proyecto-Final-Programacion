import serial
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

        # Configuración del puerto serial (ajusta el puerto)
        try:
            self.ser = serial.Serial('/dev/ttyACM2', 9600)  # Reemplaza con tu puerto
        except Exception as e:
            QMessageBox.critical(self, "Error de conexión", f"No se pudo abrir el puerto serial: {e}")
            self.ser = None

    def verificar_campos(self):
        # Verifica si todos los QLineEdit tienen contenido
        todos_completos = all(line_edit.text().strip() for line_edit in self.line_edits)

        # Verifica si los nombres son únicos
        nombres = [line_edit.text().strip() for line_edit in self.line_edits]
        nombres_unicos = len(nombres) == len(set(nombres))

        # Habilita el botón solo si todas las condiciones se cumplen
        self.pushButton.setEnabled(todos_completos and nombres_unicos)

        # Opcional: Mostrar un mensaje si hay nombres duplicados
        if not nombres_unicos and todos_completos:
            QMessageBox.warning(self, "Nombres duplicados", "No se permiten nombres repetidos. Por favor, verifica los campos.")

    def siguiente(self):
        nombres_equipos = [line_edit.text() for line_edit in self.line_edits]
        # Agregar los equipos a la instancia de Equipos
        for nombre in nombres_equipos:
            self.equipos.agregar_equipo(nombre)

        # Enviar los nombres de los equipos al Arduino a través del puerto serial
        if self.ser and self.ser.is_open:
            try:
                mensaje = f"equipos:{','.join(nombres_equipos)}\n"  # Formato esperado por Arduino
                self.ser.write(mensaje.encode())  # Enviar al Arduino
                print(f"Enviado al Arduino: {mensaje}")  # Depuración
            except Exception as e:
                QMessageBox.critical(self, "Error de comunicación", f"No se pudo enviar los datos al Arduino: {e}")

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
    
    
        
