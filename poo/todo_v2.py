#!/env/bin/python
from datetime import datetime

class Tarefa:
    def __init__(self, descricao: str) -> None:
        self.descricao: str = descricao
        self.feito: bool = False
        self.criacao: datetime = datetime.now()
    
    def concluir(self) -> None:
        self.feito: bool = True
    
    def __str__(self) -> str:
        return self.descricao + (' (Concluida)' if self.feito else '')


class Projeto:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.tarefas: list = []

    def add(self, descricao: str) -> None:
        self.tarefas.append(Tarefa(descricao))
    
    def pendentes(self) -> list:
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao: str) -> Tarefa:
        try:
            return [tarefa for tarefa in self.tarefas 
                if str(tarefa.descricao).lower() == str(descricao).lower()][0]
        except IndexError:
            return Tarefa('Tarefa não encontrada')
    
    def __str__(self) -> str:
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendete(s)'


def main() -> None:
   casa = Projeto('Tarefas de Casa')
   casa.add('Passar roupa')
   casa.add('Lavar louça')

   print(casa)
   
   casa.procurar('lavar louça').concluir()

   tarefa = casa.procurar('passar roupa')

   tarefa.concluir()

   print(casa.procurar('dad'))
   
   for tarefa in casa.tarefas:
        print(tarefa)

   print(casa)
if __name__ == '__main__':
    main()