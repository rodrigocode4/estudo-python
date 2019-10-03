#!/usr/bin/python3

import csv

with open("pessoas.csv") as arquivo:
    for registro in csv.reader(arquivo):
        print("Nome: {}, Idade: {}".format(*registro))
