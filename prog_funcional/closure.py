def multiplicar(x: int or float):
    def calcular(y: int or float):
        return x * y
    return calcular

if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)

    print(dobro)
    print(triplo)

    print(f'O dobro de 3 é {dobro(3)}')
    print(f'O triplo de 4 é {triplo(4)}')