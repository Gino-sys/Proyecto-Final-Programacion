from PyQt5.QtWidgets import QMainWindow
from interfaces.ui_archivo6 import Ui_MainWindow
from controladores.ventana7_controller import Ventana7

class ventana6(QMainWindow, Ui_MainWindow):
    def __init__(self, nombres_equipos, ventana_principal=None, texto=""):
        super().__init__()
        self.setupUi(self)
        self.ventana1 = ventana_principal  # Ventana principal que tiene la conexión serial
        self.texto_torneo = texto
        self.nombres_equipos = nombres_equipos

        # Actualiza las etiquetas con los equipos en la ventana 6
        labels = [
            self.label_2, self.label_3, self.label_4, self.label_5,
            self.label_6, self.label_7, self.label_8, self.label_9
        ]
        for i, nombre in enumerate(self.nombres_equipos):
            labels[i].setText(nombre)

        # Conecta el botón para avanzar
        self.pushButton.clicked.connect(self.sig)
        self.ventana7 = None

    def actualizar_equipos(self, nuevos_equipos):
        """Actualiza los nombres de los equipos en los labels de la ventana 6."""
        self.nombres_equipos = nuevos_equipos
        labels = [
            self.label_2, self.label_3, self.label_4, self.label_5,
            self.label_6, self.label_7, self.label_8, self.label_9
        ]
        for i, nombre in enumerate(self.nombres_equipos):
            labels[i].setText(nombre)

    def sig(self):
        # Generar los partidos en formato eliminatorio
        partidos = [
            f"{self.nombres_equipos[0]},{self.nombres_equipos[1]}",  # Partido 1
            f"{self.nombres_equipos[2]},{self.nombres_equipos[3]}",  # Partido 2
            f"{self.nombres_equipos[4]},{self.nombres_equipos[5]}",  # Partido 3
            f"{self.nombres_equipos[6]},{self.nombres_equipos[7]}"   # Partido 4
        ]

        
        # Enviar los partidos al Arduino
        if self.ventana1.ser and self.ventana1.ser.is_open:
            # Enviar la cadena de partidos con el formato adecuado
            comando = "partidos:" + ";".join(partidos) + "\n"
            self.ventana1.ser.write(comando.encode('utf-8'))
            print(f"Enviado al Arduino: {comando}")
        else:
            print("Error: La conexión serial no está abierta.")

        print(f"Comando enviado: {comando}")

        # Pasar los partidos a la ventana 7
        if self.ventana7 is None:
            self.ventana7 = Ventana7(self.nombres_equipos, self.ventana1, partidos)
        self.ventana7.show()
        self.hide()


