class Data:

    def __init__(self, dia: int=1, mes: int=1, ano: int=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self) -> str:
        return f'{self.dia}/{self.mes}/{self.ano}'
    
    def to_str(self) -> str:
        return  f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(18, 4, 2020)
#d1.dia = 18
#d1.mes = 4
#d1.ano = 2020
print(d1)
print(d1.to_str())

d2 = Data(mes=2)
d2.dia = 3
print(d2)
print(d2.to_str())
