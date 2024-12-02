from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
from interfaces.ui_archivo7 import Ui_MainWindow
from controladores.ventana8_controller import Ventana8
from clases.torneos import Torneo  # Importamos la clase Torneo
import json

class Ventana7(QMainWindow, Ui_MainWindow):
    def __init__(self, nombres_equipos, ventana_principal=None, partidos=None):
        super().__init__()
        self.setupUi(self)
        self.nombres_equipos = nombres_equipos  # Recibe los nombres de los equipos
        self.ventana_principal = ventana_principal
        self.ganadores = []  # Lista para almacenar ganadores
        self.partidos_jugados = 0  # Contador de partidos jugados
        self.ser = self.ventana_principal.ser

        # Si no se pasan partidos, por defecto está vacío
        self.partidos = partidos if partidos is not None else []

        # Crear una instancia del Torneo
        self.torneo = Torneo("Torneo de Fútbol")  # Asignamos un nombre al torneo

        # Mostrar equipos en los labels 2 a 9
        self.mostrar_equipos()

        # Guardar los partidos en el JSON
        self.guardar_partidos()  # <-- Ahora está dentro del método __init__

        # Conexión del botón "siguiente"
        self.pushButton.clicked.connect(self.siguiente_pag)

        # Iniciar escucha de datos desde Arduino
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.listen_for_data)
        self.timer.start(100)  # Comprobar cada 100 ms

    def mostrar_equipos(self):
        """Muestra los nombres de los equipos en los labels 2 al 9"""
        labels = [
            self.label_2, self.label_3, self.label_4, self.label_5,
            self.label_6, self.label_7, self.label_8, self.label_9
        ]
    
        for i, nombre in enumerate(self.nombres_equipos):
            if i < len(labels):
                labels[i].setText(nombre)

    def guardar_partidos(self):
        """Guarda los partidos en el archivo JSON"""
        if len(self.nombres_equipos) >= 4:
            nuevos_partidos = [
                {"equipo1": self.nombres_equipos[0], "equipo2": self.nombres_equipos[1], "resultado": "0-0"},
                {"equipo1": self.nombres_equipos[2], "equipo2": self.nombres_equipos[3], "resultado": "0-0"},
            ]

            # Validar que self.partidos contiene diccionarios, si no, inicializar correctamente
            if not isinstance(self.partidos, list) or any(not isinstance(p, dict) for p in self.partidos):
                print("Corrigiendo formato de 'self.partidos', inicializando como lista de diccionarios vacía.")
                self.partidos = []

            # Evitar duplicados al agregar los nuevos partidos
            for nuevo_partido in nuevos_partidos:
                if not any(
                    isinstance(p, dict) and  # Validar que p sea un diccionario
                    p.get("equipo1") == nuevo_partido["equipo1"] and 
                    p.get("equipo2") == nuevo_partido["equipo2"]
                    for p in self.partidos
                ):
                    self.partidos.append(nuevo_partido)

            # Guardar partidos en el torneo y en JSON
            for partido in nuevos_partidos:
                self.torneo.guardar_partido(partido["equipo1"], partido["equipo2"], partido["resultado"])

            self.torneo.guardar_json("torneo.json")
            print("Partidos guardados en torneo.json")

            # Actualizar el historial
            self.actualizar_historial(self.partidos)


    def listen_for_data(self):
        """Escucha los datos enviados desde Arduino periódicamente"""
        if self.ser and self.ser.is_open:
            while self.ser.in_waiting > 0:  # Mientras haya datos disponibles
                linea = self.ser.readline().decode('utf-8').strip()
                print(f"Dato recibido: {linea}")  # Debug: mostrar lo que llega desde Arduino
                if linea.startswith("resultado:"):
                    # Procesar el resultado enviado por Arduino
                    self.procesar_resultado(linea)

    def procesar_resultado(self, linea):
        """Procesa el resultado del partido y lo guarda en el archivo JSON"""
        try:
            # Validar formato de la línea
            if not linea.startswith("resultado:"):
                print(f"Línea no válida: {linea}")
                return
        
            # Separar los datos después de "resultado:"
            partes = linea[len("resultado:"):].strip().split(" ")
            if len(partes) < 3:
                print(f"Formato inválido en la línea: {linea}")
                return
        
            equipo1, marcador, equipo2 = partes[0], partes[1], partes[2]

            # Crear un nuevo partido
            nuevo_partido = {"equipo1": equipo1, "equipo2": equipo2, "resultado": marcador}

            # Buscar si el partido ya existe para actualizarlo
            partido_actualizado = False
            for partido in self.partidos:
                if partido["equipo1"] == equipo1 and partido["equipo2"] == equipo2:
                    partido["resultado"] = marcador
                    partido_actualizado = True
                    break

            if not partido_actualizado:
                # Si el partido no existe, añadirlo
                self.partidos.append(nuevo_partido)
                print(f"Nuevo partido añadido: {nuevo_partido}")

            # Actualizar el historial y guardar en JSON
            self.actualizar_historial(self.partidos)
        except Exception as e:
            print(f"Error al procesar el resultado: {e}")

    def actualizar_historial(self, partidos):
        """Actualiza el historial de partidos en el archivo JSON"""
        try:
            # Cargar el historial existente
            try:
                with open("datos/historial.json", "r") as archivo:
                    historial = json.load(archivo)
            except (FileNotFoundError, json.JSONDecodeError):
                historial = []

            # Validar que el historial sea una lista de diccionarios
            if not isinstance(historial, list) or any(not isinstance(h, dict) for h in historial):
                print("El historial no está en el formato esperado. Se inicializará como una lista vacía.")
                historial = []

            # Actualizar o agregar nuevos partidos
            for partido in partidos:
                if not isinstance(partido, dict):
                    print(f"Partido inválido ignorado: {partido}")
                    continue

                existe = False
                for h_partido in historial:
                    if (
                        h_partido.get("equipo1") == partido["equipo1"] and 
                        h_partido.get("equipo2") == partido["equipo2"]
                    ):
                        h_partido["resultado"] = partido["resultado"]
                        existe = True
                        break
                if not existe:
                    historial.append(partido)

            # Guardar el historial actualizado
            with open("datos/historial.json", "w") as archivo:
                json.dump(historial, archivo, indent=4, ensure_ascii=False)
                print("Historial actualizado en historial.json")
        except Exception as e:
            print(f"Error al actualizar el historial: {e}")


    def registrar_ganador(self, ganador):
        """Registra el ganador y actualiza la interfaz"""
        labels = [
            self.label_10, self.label_11, self.label_12, 
            self.label_13, self.label_14, self.label_15, self.label_16
        ]

        if self.partidos_jugados < len(labels):
            labels[self.partidos_jugados].setText(ganador)
            self.ganadores.append(ganador)
            self.partidos_jugados += 1

            print(f"Ganador registrado: {ganador}")
        else:
            print("No se pueden registrar más ganadores. Límite de etiquetas alcanzado.")

    def siguiente_pag(self):
        """Método para avanzar a la ventana 8"""
        # Cargar los partidos desde el archivo JSON
        self.torneo.cargar_json("torneo.json")
        
        # Pasamos los equipos y partidos a la ventana 8
        texto = " - ".join(self.ganadores)  # Combina los ganadores en un texto
        self.ventana8 = Ventana8(self.ventana_principal, texto)
        self.ventana8.set_equipos(self.nombres_equipos)  # Enviamos los equipos a la ventana 8
        self.ventana8.show()
        self.hide()

