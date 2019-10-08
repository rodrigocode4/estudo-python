def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2,7)): 'Dia de semana'
    }
    dia_escolhido = (tipo for index, tipo in dias.items() if dia in index)
    return next(dia_escolhido, '** Dia inválido **')

if __name__ == '__main__':
    for dia in range(0,9):
        print(f'{dia}: {get_tipo_dia(dia)}')