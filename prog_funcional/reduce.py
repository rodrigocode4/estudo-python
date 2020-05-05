from typing import List, Dict
from functools import reduce

pessoas: List[Dict[str, int]] = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]

soma_idades: int = reduce(lambda idades, i: idades + i['idade'],pessoas, 0)

print(soma_idades)