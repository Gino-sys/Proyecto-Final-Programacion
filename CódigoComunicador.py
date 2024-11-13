import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def leer_datos():
    data = arduino.readline().decode('utf-8').strip()
    if data:
        # Actualiza el marcador en tu aplicación Qt
        goles_equipo1, goles_equipo2 = map(int, data.split(","))
        ventana4.actualizar_marcador(goles_equipo1, goles_equipo2)
