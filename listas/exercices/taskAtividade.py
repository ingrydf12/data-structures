# AgileCorp Contextualização
class Task:
    def __init__(self, id, descricao, prioridade, status):
        self.id = id
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return f"Tarefa {self.id}: {self.descricao} | Prioridade: {self.prioridade} | Status: {self.status}, próximo: [{self.proximo}], anterior: [{self.anterior}]"

class TaskMaster:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def adicionar_tarefa(self, id, descricao, prioridade, status):
        # Verifica se já existe uma tarefa com o mesmo id
        atual = self.head
        while atual:
            if atual.id == id:
                print(f"Já existe uma tarefa com o id {id}.")
                return
            atual = atual.proximo

        nova_tarefa = Task(id, descricao, prioridade, status)
        if not self.head:
            self.head = nova_tarefa
            self.tail = nova_tarefa
            return
        else:
            self.tail.proximo = nova_tarefa
            nova_tarefa.anterior = self.tail
            self.tail = nova_tarefa

        
