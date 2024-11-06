import json

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.goles_a_favor = 0
        self.goles_en_contra = 0
    
    def agregar_goles_favor(self, goles):
        self.goles_a_favor += goles

    def agregar_goles_contra(self, goles):
        self.goles_en_contra += goles

class Partido:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0

    def registrar_gol(self, equipo):
        if equipo == self.equipo1:
            self.goles_equipo1 += 1
            equipo.agregar_goles_favor(1)
            self.equipo2.agregar_goles_contra(1)
        elif equipo == self.equipo2:
            self.goles_equipo2 += 1
            equipo.agregar_goles_favor(1)
            self.equipo1.agregar_goles_contra(1)

class Torneo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []
        self.partidos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)
    
    def generar_cruces(self):
        # Lógica para organizar los cruces de eliminación directa
        # Por simplicidad, aquí asumimos 8 equipos para un torneo de eliminación.
        for i in range(0, len(self.equipos), 2):
            partido = Partido(self.equipos[i], self.equipos[i+1])
            self.partidos.append(partido)
    
    def avanzar_fase(self):
        # Lógica para determinar ganadores y avanzar a la siguiente fase
        # Podría eliminar los equipos perdedores de `self.equipos`
        nuevos_partidos = []
        for partido in self.partidos:
            ganador = partido.jugar()
            nuevos_partidos.append(ganador)
        self.equipos = nuevos_partidos
        self.partidos = []
        if len(self.equipos) > 1:
            self.generar_cruces()
        else:
            print(f"El ganador del torneo {self.nombre} es {self.equipos[0]}")
    def guardar_datos(self, archivo='data/torneo.json'):
        datos = {
            "nombre": self.nombre,
            "equipos": [{ "nombre": e.nombre, "goles_a_favor": e.goles_a_favor, "goles_en_contra": e.goles_en_contra } for e in self.equipos]
        }
        with open(archivo, 'w') as f:
            json.dump(datos, f)

    def cargar_datos(self, archivo='data/torneo.json'):
        with open(archivo, 'r') as f:
            datos = json.load(f)
            self.nombre = datos["nombre"]
            self.equipos = [Equipo(e["nombre"]) for e in datos["equipos"]]
            for equipo, data in zip(self.equipos, datos["equipos"]):
                equipo.goles_a_favor = data["goles_a_favor"]
                equipo.goles_en_contra = data["goles_en_contra"]