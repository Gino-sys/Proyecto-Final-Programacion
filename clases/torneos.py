class Torneo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidos = []  # Lista de partidos, donde cada partido es un diccionario

    def guardar_partido(self, equipo1, equipo2, resultado="0-0"):
        """Guarda un partido con su resultado (goles)"""
        partido = {
            "equipo1": equipo1,
            "equipo2": equipo2,
            "resultado": resultado  # Guardar el marcador de goles
        }
        self.partidos.append(partido)

    def guardar_json(self, ruta):
        """Guarda los partidos en un archivo JSON"""
        try:
            with open(ruta, "w") as archivo:
                json.dump(self.partidos, archivo, indent=4, ensure_ascii=False)
            print(f"Datos guardados correctamente en {ruta}")
        except Exception as e:
            print(f"Error al guardar el archivo JSON: {e}")

    def cargar_json(self, ruta):
        """Carga los datos de un archivo JSON"""
        try:
            with open(ruta, "r") as archivo:
                self.partidos = json.load(archivo)
            print(f"Datos cargados correctamente desde {ruta}")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {e}")
    
    def obtener_resultados(self):
        """Devuelve los resultados de los partidos"""
        return self.partidos

    def actualizar_resultado(self, equipo1, equipo2, goles_equipo1, goles_equipo2):
        """Actualiza el resultado de un partido dado con los goles"""
        resultado = f"{goles_equipo1}-{goles_equipo2}"

        for partido in self.partidos:
            if (partido["equipo1"] == equipo1 and partido["equipo2"] == equipo2) or \
               (partido["equipo1"] == equipo2 and partido["equipo2"] == equipo1):
                partido["resultado"] = resultado
                print(f"Resultado actualizado: {equipo1} vs {equipo2} = {resultado}")
                break
        else:
            print("Partido no encontrado para actualizar.")

    def reiniciar_json(self, ruta):
        """Reinicia el archivo JSON, borrando todos los datos del torneo"""
        try:
            # Sobrescribir el archivo JSON con una lista vacía
            with open(ruta, "w") as archivo:
                json.dump([], archivo, indent=4, ensure_ascii=False)
            print("El archivo JSON ha sido reiniciado.")
        except Exception as e:
            print(f"Error al reiniciar el archivo JSON: {e}")
