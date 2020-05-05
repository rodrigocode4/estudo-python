from typing import List, Dict

lista1: List[int] = [1, 2, 3]

dobro: map = map(lambda x: x * 2, lista1)
print(list(dobro))


lista2: List[Dict[str, int]] = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]

so_nomes: List[str] = list(map(lambda n: n['nome'], lista2))
print(so_nomes)

so_idades: List[int] = list(map(lambda i: i['idade'], lista2))
print(so_idades)


# Desafio: usuando map, retorne a frase: '<Nome> tem <idade> anos.'

frases: List[str] = list(
    map(
        lambda f: f"{f['nome']} tem {f['idade']} anos.",
        lista2
    )
)
print(frases)
