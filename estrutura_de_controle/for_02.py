name = 'Rodrigo'

for letra in name:
    print(letra, end=',')
print('FIM')

aprovados = ['Rodrigo', 'Edson', 'Paola', 'Maria']

for aluno in aprovados:
    print(aluno)

for i, nome in enumerate(aprovados):
    print(f'{i + 1})', nome)

dias_semana = ('Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab')

for dia in dias_semana:
    print(dia)

for num in {1, 2, 3, 2, 4, 5, 6, 6, 6, 6, 6}:
    print(num)
