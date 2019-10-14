# **kwargs

def resultado_f1(primeiro, segundo, terceiro):
    print(f' 1º {primeiro}')
    print(f' 2º {segundo}')
    print(f' 3º {terceiro}')


if __name__ == '__main__':
    podium = {
        'segundo' : 'Rubinho Barriquelo',
        'terceiro' : 'F. Massa',
        'primeiro' : 'Airton Senna'
    }
    resultado_f1(**podium)