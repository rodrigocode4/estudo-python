compras = (
    {'quantidade': 2, 'preco': 20},
    {'quantidade': 3, 'preco': 30},
    {'quantidade': 4, 'preco': 40}
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)


if __name__ == '__main__':

    print(f'Preços totais: {totais}')
    print(f'Preço geral: {sum(totais)}')
