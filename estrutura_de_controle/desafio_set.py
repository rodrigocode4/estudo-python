PALAVRAS_PROIBIDAS = {'futebol', 'política', 'religião'}

textos = [
    'João gosta de futebol e política',
    'A praia foi boa no fim de semana'
]

for texto in textos:
    intercecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intercecao:
        print('Palavras proibidas:', intercecao)
    else:
        print('Texto liberado:', texto)