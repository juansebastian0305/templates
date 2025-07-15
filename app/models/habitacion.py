class Habitacion:
    def __init__(self, id, numero, piso, tipo, estado, hotel_id):
        self.id = id
        self.numero = numero
        self.piso = piso
        self.tipo = tipo
        self.estado = estado  # disponible / ocupada
        self.hotel_id = hotel_id

# Simulación de base de datos
habitaciones_db = []
