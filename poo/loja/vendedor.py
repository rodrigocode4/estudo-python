from .pessoa import Pessoa

class Vendedor(Pessoa):
    def __init__(self, nome: str, idade: int, salario: float):
        super().__init__(nome, idade)
        self.salario: float = salario