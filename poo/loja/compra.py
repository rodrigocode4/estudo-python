from .vendedor import Vendedor
from datetime import datetime

class Compra:
    def __init__(self, vendedor: Vendedor,data: datetime, valor: float):
        self.vendedor: Vendedor = vendedor
        self.data: datetime = data
        self.valor: float = valor
        