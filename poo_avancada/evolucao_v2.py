
class Humano:

    especie = 'Homo Sapiens'

    def __init__(self, nome: str):
        self.nome: str = nome
    
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
    grokn = Neanderthal('Grokn')

    print(f'''
    Evolução a partir da classe: {', '.join(HomoSapiens.especies())}
    Evolução a partir da instancia: {', '.join(jose.especies())}
    Homo Sapiens evoluído? : {HomoSapiens.is_evoluido()}
    Neanderthal evoluído? : {Neanderthal.is_evoluido()}
    José evoluído? : {jose.is_evoluido()}
    Grokn evoluído? : {grokn.is_evoluido()}
    ''')