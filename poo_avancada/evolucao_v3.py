
class Humano:

    especie = 'Homo Sapiens'

    def __init__(self, nome: str):
        self.nome: str = nome
        self._idade = None
    
    def get_idade(self) -> int:
        return self._idade

    def set_idade(self, idade: int):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo')
        self._idade = idade
    
    def das_cavernas(self):
        self.especie: str = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies() -> tuple:
        objetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Autralopiteco', ) + tuple(f'Homo {obj}' for obj in objetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie: str = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie: str = Humano.especies()[-1]

if __name__ == '__main__':
    jose = HomoSapiens('José')
    jose.set_idade(30)
    print(f'Nome: {jose.nome}, Idade: {jose.get_idade()}')
