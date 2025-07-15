class Categoria:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

# Simulación de base de datos
categorias_db = [
    Categoria(1, "Boutique"),
    Categoria(2, "Ecohotel"),
    Categoria(3, "Familiar")
]
