class HtmlToStringMixin:
    def __str__(self) -> str:
        #conversão pra HTML
        html = super().__str__() \
            .replace('(', '<strong>') \
            .replace(')', '</strong>')

        return f'<span>{html}</span>'

    def pai(self):
        return f'PAI: {super().__str__()}'


class Pessoa:
    def __init__(self, nome: str):
        self.nome: str = nome
    
    def __str__(self) -> str:
        return self.nome


class Animal:
    def __init__(self, nome: str, pet: bool = True):
        self.nome: str = nome
        self.pet: bool = pet
    
    def __str__(self) -> str:
        return self.nome + ('', ' (pet)')[self.pet]


class PessoaHTML(HtmlToStringMixin, Pessoa):
    pass


class AnimalHTML(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    p1 = Pessoa('Edson Oliveira')
    print(p1)

    p2 = PessoaHTML('Rodrigo Oliveira')
    print(p2)

    p3 = PessoaHTML('Edson (Rodrigo) de Oliveira')
    print(p3)

    a1 = Animal('Doginho')
    print(a1)

    a2 = AnimalHTML('Doginho')
    print(a2)

    a3 = AnimalHTML('Doginho', pet=False)
    print(a3)

    mix = HtmlToStringMixin()
    print(mix.pai())