#!/env/bin/python
from datetime import datetime

class Tarefa:
    def __init__(self, descricao: str) -> None:
        self.descricao: str = descricao
        self.feito: bool = False
        self.criacao = datetime.now()
    
    def concluir(self) -> None:
        self.feito: bool = True
    
    def __str__(self) -> str:
        return self.descricao + (' (Concluida)' if self.feito else '')


def main() -> None:
    casa: list = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))

    # Desafio -> concluir() se Tarefa for 'Lavar prato'
    """
    for task in casa:
        if task.descricao == 'Lavar prato':
            task.concluir()
        print(task)
    """
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']
    for tarefa in casa:
        print(f'- {tarefa}')

if __name__ == '__main__':
    main()