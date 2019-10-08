#!/usr/bin/python3

import csv

#!/usr/bin/python3

def read(path):
    with open(path, 'rb') as arquivo_ibge:
        print(' ================= Lendo CSV... =============================')
        dados = arquivo_ibge.read().decode('latin1')
        print(' ================= Leitura completa do CSV... ============================')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')

if __name__ == '__main__':
    read('desafio-ibge.csv')