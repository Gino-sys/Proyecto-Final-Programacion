class Equipos:
    def __init__(self):
        # Inicializamos una lista vacía para los 8 equipos
        self.equipos = []

    def agregar_equipo(self, nombre_equipo):
        if len(self.equipos) < 8:
            self.equipos.append(nombre_equipo)

    def obtener_equipos(self):
        # Retorna la lista de equipos
        return self.equipos
