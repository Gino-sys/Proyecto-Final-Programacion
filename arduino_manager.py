import serial
import time

class ArduinoManager:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial = None

    def connect(self):
        """Establece la conexión serial con Arduino."""
        self.serial = serial.Serial(self.port, self.baudrate, timeout=1)
        time.sleep(2)  # Esperar a que Arduino esté listo

    def send_data(self, data):
        """Envía datos a Arduino."""
        if self.serial and self.serial.is_open:
            self.serial.write(data.encode())

    def read_data(self):
        """Lee datos desde Arduino."""
        if self.serial and self.serial.is_open:
            return self.serial.readline().decode().strip()
        return None

    def close(self):
        """Cierra la conexión serial."""
        if self.serial and self.serial.is_open:
            self.serial.close()

