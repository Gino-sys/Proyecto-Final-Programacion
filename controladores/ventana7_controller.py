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
        print(f"Ventana7 inicializada con los equipos: {self.nombres_equipos}")  # Depuración
        self.ventana_principal = ventana_principal
        self.ganadores = []  # Lista para almacenar ganadores
        self.partidos_jugados = 0  # Contador de partidos jugados
        self.ser = self.ventana_principal.ser
        self.lista_ya_enviada = False  # Inicializar el flag

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

    def enviar_lista(self):
        print("Función enviar_lista llamada")
        if not self.lista_ya_enviada:  # Verificar el flag
            print("Enviando lista:", self.lista)  # Depuración
            # Código para enviar la lista
            self.lista_ya_enviada = True  # Cambiar el flag después de enviar
        else:
            print("Intento de envío duplicado bloqueado.")

    def mostrar_equipos(self):
        """Muestra los nombres de los equipos en los labels 2 al 9"""
        labels = [
            self.label_2, self.label_3, self.label_4, self.label_5,
            self.label_6, self.label_7, self.label_8, self.label_9
        ]

        # Verifica si los nombres de equipos se pasaron correctamente
        print(f"Equipos recibidos para mostrar: {self.nombres_equipos}")  # Depuración
        
        for i, nombre in enumerate(self.nombres_equipos):
            if i < len(labels):
                print(f"Actualizando label {i+2} con el nombre: {nombre}")  # Depuración
                labels[i].setText(nombre)

    def guardar_partidos(self):
        """Guarda los partidos en el archivo JSON"""
        if len(self.nombres_equipos) >= 8:  # Asegúrate de tener al menos 8 equipos
            nuevos_partidos = [
                {"equipo1": self.nombres_equipos[0], "equipo2": self.nombres_equipos[1], "resultado": "0-0"},
                {"equipo1": self.nombres_equipos[2], "equipo2": self.nombres_equipos[3], "resultado": "0-0"},
                {"equipo1": self.nombres_equipos[4], "equipo2": self.nombres_equipos[5], "resultado": "0-0"},
                {"equipo1": self.nombres_equipos[6], "equipo2": self.nombres_equipos[7], "resultado": "0-0"}
            ]

            # Validar que self.partidos contiene diccionarios, si no, inicializar correctamente
            if not isinstance(self.partidos, list) or any(not isinstance(p, dict) for p in self.partidos):
                print("Corrigiendo formato de 'self.partidos', inicializando como lista de diccionarios vacía.")
                self.partidos = []

            # Evitar duplicados al agregar los nuevos partidos manualmente
            for nuevo_partido in nuevos_partidos:
                if not any(
                    p.get("equipo1") == nuevo_partido["equipo1"] and p.get("equipo2") == nuevo_partido["equipo2"]
                    for p in self.partidos
                ):
                    self.partidos.append(nuevo_partido)

            # Guardar partidos en el torneo y en JSON
            for nuevo_partido in nuevos_partidos:
                self.torneo.guardar_partido(nuevo_partido["equipo1"], nuevo_partido["equipo2"], nuevo_partido["resultado"])

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
            
            # Determinar el ganador del partido
            ganador = self.obtener_ganador(marcador, equipo1, equipo2)
            if ganador:
                self.registrar_ganador(ganador)
        except Exception as e:
            print(f"Error al procesar el resultado: {e}")

    def obtener_ganador(self, marcador, equipo1, equipo2):
        """Determina el ganador a partir del marcador"""
        goles_equipo1, goles_equipo2 = marcador.split("-")
        if int(goles_equipo1) > int(goles_equipo2):
            return equipo1
        elif int(goles_equipo1) < int(goles_equipo2):
            return equipo2
        return None  # Empate, no hay ganador

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
                json.dump(historial, archivo, indent=4)

            print("Historial actualizado en datos/historial.json")
        except Exception as e:
            print(f"Error al actualizar el historial: {e}")

    def siguiente_pag(self):
        """Método para avanzar a la Ventana8 y enviar los datos necesarios."""
        # Aseguramos que el archivo del torneo está actualizado
        self.torneo.guardar_json("torneo.json")

        # Creamos un texto combinando los ganadores para mostrar en la siguiente ventana
        texto_ganadores = ", ".join(self.ganadores) if self.ganadores else "Sin ganadores registrados"

        # Creamos la instancia de Ventana8, pasando nombres de equipos, ventana principal y ganadores
        self.ventana8 = Ventana8(self.nombres_equipos, self.ventana_principal, texto=texto_ganadores)
        self.ventana8.show()
        self.close()