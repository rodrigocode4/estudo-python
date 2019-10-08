#!/usr/bin/python3
def tag_bloco(texto, classe = 'success'):
    return f'<div class={classe}>{texto}</div>'

if __name__ == '__main__':
    assert tag_bloco('Sucesso!!!') == '<div class=success>Sucesso!!!</div>'
    assert tag_bloco('Error!!!', 'erro') == '<div class=erro>Error!!!</div>'
    assert tag_bloco('Aviso!!!', 'warning') == '<div class=warning>Aviso!!!</div>'