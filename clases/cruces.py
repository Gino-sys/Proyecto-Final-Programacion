import random


class Cruces:
    def __init__(self, equipos):
        self.equipos = equipos  # Lista inicial de equipos
        self.enfrentamientos = []  # Lista de cruces de cada ronda
        self.campeon = None  # Campeón del torneo
        self.generar_cruces_iniciales()  # Genera los cruces de la primera ronda

    def generar_cruces_iniciales(self):
        """Baraja los equipos y genera los enfrentamientos iniciales."""
        equipos_barajados = random.sample(self.equipos, len(self.equipos))
        self.enfrentamientos = [(equipos_barajados[i], equipos_barajados[i + 1]) for i in range(0, len(equipos_barajados), 2)]

    def generar_siguiente_ronda(self):
        """Genera los enfrentamientos de la siguiente ronda."""
        if not self.enfrentamientos:  # Si no hay más enfrentamientos, termina el torneo
            return

        # Obtén los ganadores de los enfrentamientos actuales
        ganadores = [self.obtener_ganador(equipo1, equipo2) for equipo1, equipo2 in self.enfrentamientos]
        self.enfrentamientos = [(ganadores[i], ganadores[i + 1]) for i in range(0, len(ganadores), 2)] if len(ganadores) > 1 else []

        # Si solo queda un ganador, es el campeón
        if len(ganadores) == 1:
            self.campeon = ganadores[0]

    def obtener_ganador(self, equipo1, equipo2):
        """Simula el ganador entre dos equipos."""
        return random.choice([equipo1, equipo2])  # Escoge un ganador aleatorio
