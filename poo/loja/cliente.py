from .pessoa import Pessoa
from .vendedor import Vendedor
from .compra import Compra
from datetime import datetime, timedelta

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.compras: list = []

    def registrar_compra(self, compra: Compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self) -> datetime:
        return self.compras[-1].data
    
    def total_compras(self):
        return sum([valor_compra.valor for valor_compra in self.compras])
