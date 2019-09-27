
def get_dia_semana(dia):
    dias = {
        1: 'Dom',
        2: 'Seg',
        3: 'Ter',
        4: 'Qua',
        5: 'Qui',
        6: 'Sex',
        7: 'Sab'
    }
    return dias.get(dia, ' DIA INVÁLIDO!!!')

if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia} : {get_dia_semana(dia)}')