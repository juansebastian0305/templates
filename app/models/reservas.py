class Reserva:
    def __init__(self, id, cliente_id, habitacion_id, motivo, fecha_inicio, fecha_fin, precio, aplica_iva):
        self.id = id
        self.cliente_id = cliente_id
        self.habitacion_id = habitacion_id
        self.motivo = motivo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio = precio
        self.aplica_iva = aplica_iva

# Simulación de base de datos
reservas_db = []
