#!/usr/bin/python3

with open("pessoas.csv") as arquivo:
    with open("pessoas.txt", "w") as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(",")
            print("Nome: {}, Idade: {}".format(*pessoa), file=saida)

if arquivo.closed:
    print("O arquivo foi fechado corretamente!")

if saida.closed:
    print("O aquivo de saída foi fechado corretamente!") 