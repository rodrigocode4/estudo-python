#!/env/bin/python
from datetime import datetime, timedelta

class TarefaNaoEncontrada(Exception):
    pass

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


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias: int = dias
        self.dono: None = None
    
    def concluir(self) -> Tarefa:
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa

class Projeto:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.tarefas: list = []

    def __iter__(self) -> list:
        return self.tarefas.__iter__()
    
    def __iadd__(self, tarefa: Tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa: Tarefa, **kwargs: dict):
        self.tarefas.append(tarefa)
    
    def __add_nova_tarefa(self, descricao: str, **kwargs: dict):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa: Tarefa, vencimento: datetime = None, **kwargs: dict) -> None:
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self.__add_nova_tarefa
        kwargs['venciento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)
    def pendentes(self) -> list:
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao: str) -> Tarefa:
        try:
            return [tarefa for tarefa in self.tarefas 
                if str(tarefa.descricao).lower() == str(descricao).lower()][0]
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))
    
    def __str__(self) -> str:
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendete(s)'


def main() -> None:
   casa = Projeto('Tarefas de Casa')
   casa.add('Passar roupa', datetime.now())
   casa.add('Lavar louça')
   casa.add('Compra tomate', datetime.now() + timedelta(days=3, minutes=12))
   casa += TarefaRecorrente('Trocar lençóis', datetime.now(), 7)
   casa.procurar('trocar lençóis').concluir()

   print(casa)

   casa.procurar('lavar louça').concluir()

   try:
       print(casa.procurar('dad - erro'))
   except TarefaNaoEncontrada as e:
       print(f'Motivo do erro foi: "{str(e)}"')

   
   for tarefa in casa:
        print(tarefa)

   print(casa)
if __name__ == '__main__':
    main()