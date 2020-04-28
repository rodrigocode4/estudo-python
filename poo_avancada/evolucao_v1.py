
class Humano:

    especie = 'Homo Sapiens'

    def __init__(self, nome: str):
        self.nome: str = nome
    
    def das_cavernas(self):
        self.especie: str = 'Homo Neanderthalensis'
        return self

if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_cavernas()

    print(f'''
        Humano.especie: {Humano.especie}
        jose.especie: {jose.especie}
        grokn.especie: {grokn.especie}
    ''')