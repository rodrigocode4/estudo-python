PALAVRAS_PROIBIDAS = ['futebol', 'política', 'religião']

textos = [
    'João gosta de futebol e política',
    'A praia foi boa no fim de semana'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('O texto possui ao menos uma palavra proibida:', palavra)
            break
    else:
        print('Texto autorizado:', texto)
