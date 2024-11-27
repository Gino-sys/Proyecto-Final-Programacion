import json

class Torneo:
    def __init__(self, nombre=''):
        self.partidos = []  # Lista para almacenar los partidos y sus resultados
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

    def guardar_json(self, archivo_json):
        """
        Guarda los partidos en un archivo JSON.
        :param archivo_json: Ruta del archivo JSON donde se guardarán los partidos.
        """
        with open(archivo_json, 'w', encoding='utf-8') as archivo:
            json.dump(self.partidos, archivo, ensure_ascii=False, indent=4)

    def cargar_json(self, archivo_json):
        """
        Carga los partidos desde un archivo JSON.
        :param archivo_json: Ruta del archivo JSON desde donde se cargarán los partidos.
        """
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            self.partidos = json.load(archivo)

    def __str__(self):
        """
        Representación en texto del torneo, incluyendo su nombre y los partidos registrados.
        :return: Cadena con la información del torneo.
        """
        info_torneo = f"Torneo: {self.nombre}\nPartidos:"
        for partido in self.partidos:
            info_torneo += f"\n{partido['equipo1']} vs {partido['equipo2']} - Resultado: {partido['resultado']}"
        return info_torneo
