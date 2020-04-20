#!/env/bin/python
from datetime import datetime, timedelta

class Tarefa:
    def __init__(self, descricao: str, vencimento: datetime = None) -> None:
        self.descricao: str = descricao
        self.feito: bool = False
        self.criacao: datetime = datetime.now()
        self.vencimento: datetime = vencimento

    def concluir(self) -> None:
        self.feito: bool = True
    
    def __str__(self) -> str:
        status = []
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')
        
        return f'{self.descricao} ' + ' '.join(status)

class Projeto:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.tarefas: list = []

    def __iter__(self) -> list:
        return self.tarefas.__iter__()

    def add(self, descricao: str, vencimento: datetime = None) -> None:
        self.tarefas.append(Tarefa(descricao, vencimento))
    
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
   casa.add('Passar roupa', datetime.now())
   casa.add('Lavar louça')
   casa.add('Compra tomate', datetime.now() + timedelta(days=3, minutes=12))

   print(casa)
   
   casa.procurar('lavar louça').concluir()

   print(casa.procurar('dad'))
   
   for tarefa in casa:
        print(tarefa)

   print(casa)
if __name__ == '__main__':
    main()