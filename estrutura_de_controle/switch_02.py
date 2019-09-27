
def is_fim_de_semana(dia):
    dias = {
        1: 'Dom',
        2: 'Seg',
        3: 'Ter',
        4: 'Qua',
        5: 'Qui',
        6: 'Sex',
        7: 'Sab'
    }

    if dias.get(dia) == dias[1] or dias.get(dia) == dias[len(dias)]:
        return f'{dias.get(dia)}: Fim de Semana'
    elif dia not in dias.keys():
        return 'Dia Inválido'
    else:
        return f'{dias.get(dia)}: Dia de semana'


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia} : {is_fim_de_semana(dia)}')
