#!/usr/bin/python3
def tag_bloco(conteudo, classe = 'success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class={classe}>{conteudo}</{tag}>'

def tag_list(*items):
    lista = ''.join((f'<li>{item}</li>' for item in items))
    return f'<ul>{lista}</ul>'

if __name__ == '__main__':
    print(tag_bloco('Sucesso!!!'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('Falhou!!!', classe='error'))
    print(tag_bloco(classe='error',conteudo='Falhou!!!'))

    print(tag_bloco(conteudo=tag_list('Item 1', 'Item 2', 'Item 3'), classe='default'))
