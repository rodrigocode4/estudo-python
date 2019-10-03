#!/usr/bin/python3

try:
    arquivo = open("pessoas.csv")

    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(*registro.strip().split(",")))
finally:
    print("executou o finally")
    arquivo.close()

if arquivo.closed:
    print('O arquivo foi fechado corretamente!')