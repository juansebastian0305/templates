class Cliente:
    def __init__(self, id, nombre, documento, tipo_cliente, es_agencia):
        self.id = id
        self.nombre = nombre
        self.documento = documento
        self.tipo_cliente = tipo_cliente  # nacional o extranjero
        self.es_agencia = es_agencia      # True = agencia, False = persona

# Simulación de base de datos
clientes_db = []
