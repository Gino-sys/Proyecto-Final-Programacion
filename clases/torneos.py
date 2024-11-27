from controladores.ventana2_controller import Ui_MainWindow

class Torneo:
    def __init__(self, nombre=''):
        self.partido = [] # Lista para almacenar los partidos y sus resultados
        self.nombre = nombre 
    def guardar_partido(self, equipo1, equipo2, resultado):
        """
        Guarda el resultado de un partido en la lista de partidos.
        :param equipo1: Nombre del equipo 1.
        :param equipo2: Nombre del equipo 2.
        :param resultado: Resultado del partido (por ejemplo, "3-2").
        """
        if not equipo1 or not equipo2 or not resultado:
            raise ValueError("Los datos del partido no pueden estar vacíos.")

        partido = {
            "equipo1": equipo1,
            "equipo2": equipo2,
            "resultado": resultado
        }
        self.partidos.append(partido)

    def obtener_partidos(self):
        """
        Devuelve la lista de todos los partidos registrados.
        :return: Lista de diccionarios con los datos de los partidos.
        """
        return self.partidos

    def __str__(self):
        """
        Representación en texto del torneo, incluyendo su nombre y los partidos registrados.
        :return: Cadena con la información del torneo.
        """
        info_torneo = f"Torneo: {self.nombre}\nPartidos:"
        for partido in self.partidos:
            info_torneo += f"\n{partido['equipo1']} vs {partido['equipo2']} - Resultado: {partido['resultado']}"
        return info_torneo
