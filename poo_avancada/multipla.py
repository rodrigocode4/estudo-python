class Aninal:
    @property
    def capacidades(self):
        return('dormir', 'comer', 'beber')


class Homem(Aninal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')


class Aranha(Aninal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + \
            ('bater em bandidos', 'atirar teia entre prédios')

if __name__ == '__main__':

    rodrigo = Homem()
    print(f'Rodrigo: {rodrigo.capacidades}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')
    
    peter = HomemAranha()
    print(f'Peter Parker: {peter.capacidades}')