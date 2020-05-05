from typing import List, Dict

pessoas: List[Dict[str, int]] = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]

menores: List[Dict[str, int]] = list(
    filter(
        lambda i: i['idade'] < 18,
        pessoas
    )
)

print(menores)

nome_maior_que_6_char: List[Dict[str, int]] = tuple(
    filter(
        lambda i: len(i['nome']) > 6,
        pessoas
    )
)

print(nome_maior_que_6_char)