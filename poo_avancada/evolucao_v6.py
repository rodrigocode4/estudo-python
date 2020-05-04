from abc import ABCMeta, abstractproperty

class Humano(metaclass=ABCMeta):

    especie = 'Homo Sapiens'

    def __init__(self, nome: str):
        self.nome: str = nome
        self._idade = None
    
    @abstractproperty
    def inteligente(self):
        pass

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade: int):
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

    @property
    def inteligente(self) -> bool:
        return False


class HomoSapiens(Humano):
    especie: str = Humano.especies()[-1]

    @property
    def inteligente(self) -> bool:
        return True

if __name__ == '__main__':

    """ try:
        anonimo = Humano('Jhon Doe')
        print(anonimo.inteligente)
    except TypeError:
        print('Classe abstrata') """

    jose = HomoSapiens('José')
    grokn = Neanderthal('Grokn')
    print(f'Nome: {jose.nome}, Classe: {jose.__class__.__name__}, Inteligente: {jose.inteligente}')
    print(f'Nome: {grokn.nome}, Classe: {grokn.__class__.__name__}, Inteligente: {grokn.inteligente}')
