#!/usr/bin/python3


def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Manor de Idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade Inválida'


if __name__ == '__main__':
    idade = float(input('Informe a idade: '))
    print(f'Você é {faixa_etaria(idade)}')
