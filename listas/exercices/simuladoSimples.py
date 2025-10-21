class Cliente:
    def __init__(self, nome, cpf, valor_gasto):
        self.nome = nome
        self.cpf = cpf
        self.valor_gasto = valor_gasto
        self.proximo = None  # ponteiro para o próximo cliente

    def __str__(self):
        return f"Nome: {self.nome} | CPF: {self.cpf} | Valor gasto: R$ {self.valor_gasto:.2f}"


class ListaClientes:
    def __init__(self):
        self.inicio = None  # referência para o primeiro cliente

    # 1. Adicionar cliente no fim da lista
    def adicionar_fim(self, nome, cpf, valor_gasto):
        novo = Cliente(nome, cpf, valor_gasto)
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        print(f"Cliente {nome} adicionado ao fim da lista.")

    # 2. Adicionar cliente no início da lista
    def adicionar_inicio(self, nome, cpf, valor_gasto):
        novo = Cliente(nome, cpf, valor_gasto)
        novo.proximo = self.inicio
        self.inicio = novo
        print(f"Cliente {nome} adicionado ao início da lista.")

    # 3. Remover cliente por CPF
    def remover_por_cpf(self, cpf):
        if self.inicio is None:
            print("A lista está vazia.")
            return

        if self.inicio.cpf == cpf:
            removido = self.inicio
            self.inicio = self.inicio.proximo
            print(f"Cliente {removido.nome} removido.")
            return

        anterior = self.inicio
        atual = self.inicio.proximo

        while atual:
            if atual.cpf == cpf:
                anterior.proximo = atual.proximo
                print(f"Cliente {atual.nome} removido.")
                return
            anterior = atual
            atual = atual.proximo

        print(f"Nenhum cliente encontrado com CPF {cpf}.")

    # 4. Mostrar todos os clientes
    def mostrar(self):
        if self.inicio is None:
            print("A lista está vazia.")
            return

        print("\n--- Clientes na lista ---")
        atual = self.inicio
        while atual:
            print(atual)
            atual = atual.proximo
        print("-------------------------")

    # 5. Reordenar a lista por CPF (ordem crescente)
    def ordenar_por_cpf(self):
        if self.inicio is None or self.inicio.proximo is None:
            return  # lista vazia ou com um elemento

        trocou = True
        while trocou:
            trocou = False
            atual = self.inicio
            while atual.proximo:
                if atual.cpf > atual.proximo.cpf:
                    # troca os dados dos nós
                    atual.nome, atual.proximo.nome = atual.proximo.nome, atual.nome
                    atual.cpf, atual.proximo.cpf = atual.proximo.cpf, atual.cpf
                    atual.valor_gasto, atual.proximo.valor_gasto = atual.proximo.valor_gasto, atual.valor_gasto
                    trocou = True
                atual = atual.proximo
        print("Lista reordenada por CPF.")

    # 6. Abastecer cliente (aumentar valor gasto)
    def abastecer_cliente(self, cpf, valor):
        atual = self.inicio
        while atual:
            if atual.cpf == cpf:
                atual.valor_gasto += valor
                print(f"Cliente {atual.nome} abasteceu R$ {valor:.2f}. Total: R$ {atual.valor_gasto:.2f}")
                return
            atual = atual.proximo
        print(f"Nenhum cliente encontrado com CPF {cpf}.")
