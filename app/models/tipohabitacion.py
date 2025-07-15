class TipoHabitacion:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

# Simulación de base de datos
tipos_db = [
    TipoHabitacion(1, "Suite", "Habitación amplia con sala y jacuzzi"),
    TipoHabitacion(2, "Doble", "Para 2 personas con dos camas"),
    TipoHabitacion(3, "Individual", "Para una persona"),
    TipoHabitacion(4, "Familiar", "Ideal para familias con niños")
]
