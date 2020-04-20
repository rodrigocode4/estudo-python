class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome: str = nome
        self.idade: str = idade

    def __str__(self) -> str:
        return f'{self.nome}'

    def is_adulto(self) -> bool:
        return (self.idade or 0) >= 18
