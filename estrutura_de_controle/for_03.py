produto = {
    'nome': 'Notebook',
    'marca': 'Asus',
    'modelo': 'Vivobook X510UR',
    'preço': 2800
}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)
