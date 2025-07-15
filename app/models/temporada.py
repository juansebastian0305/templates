class Temporada:
    def __init__(self, id, nombre, fecha_inicio, fecha_fin):
        self.id = id
        self.nombre = nombre  # alta, media, baja
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

# Simulación de base de datos
temporadas_db = []
