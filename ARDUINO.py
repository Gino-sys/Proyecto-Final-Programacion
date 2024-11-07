import sys
import serial
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# Configuración de la comunicación serial (ajusta el puerto y velocidad según tu Arduino)
ser = serial.Serial('COM3', 9600)  # Cambia 'COM3' por el puerto que uses en tu sistema

class TeamInputApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingreso de Equipos")
        self.layout = QVBoxLayout()

        # Campos de entrada para los nombres de los equipos
        self.team_inputs = []
        for i in range(8):
            label = QLabel(f"Nombre del equipo {i+1}:")
            input_field = QLineEdit()
            self.layout.addWidget(label)
            self.layout.addWidget(input_field)
            self.team_inputs.append(input_field)
        
        # Botón para enviar equipos
        self.submit_button = QPushButton("Enviar Equipos a Arduino")
        self.submit_button.clicked.connect(self.send_teams_to_arduino)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def send_teams_to_arduino(self):
        teams = [input_field.text() for input_field in self.team_inputs]
        team_data = ",".join(teams)
        ser.write(team_data.encode())  # Enviar los nombres como cadena CSV
        print("Equipos enviados al Arduino:", team_data)

app = QApplication(sys.argv)
window = TeamInputApp()
window.show()
sys.exit(app.exec_())
