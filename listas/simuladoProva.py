class Cliente:
    def __init__(self, nome, cpf, valor_gasto):
        self.nome = nome
        self.cpf = cpf
        self.valor_gasto = valor_gasto
        self.anterior = None
        self.proximo = None

    def __str__(self):
        return f"Cliente: {self.nome} / {self.cpf} | Valor gasto: {self.valor_gasto}"

class PostoGasolina:
    def __init__(self):
        self.head = None;
        self.tail = None;

    def adicionar_cliente(self, nome, cpf, valor_gasto):
        novo_cliente = Cliente(nome, cpf, valor_gasto)
        if not self.head:
            self.head = novo_cliente
            self.tail = novo_cliente
        else:
            self.tail.proximo = novo_cliente
            novo_cliente.anterior = self.tail
            self.tail = novo_cliente
        print("Cliente adicionado")

    def adicionar_cliente_ao_inicio(self, nome, cpf, valor_gasto):
        novo_cliente = Cliente(nome, cpf, valor_gasto)
        if not self.head:
            self.head = novo_cliente
            self.tail = novo_cliente
        else:
            self.head.anterior = novo_cliente
            novo_cliente.proximo = self.head
            self.head = novo_cliente
        print("Cliente adicionado ao início da lista")

    def remover_cliente(self, cpf):
        atual = self.head;
        while atual and atual.cpf != cpf:
            print(f"{atual}");
            atual = atual.proximo
        if atual is None:
            print("Produto não encontrado.");
            return
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        # EXTREMIDADES
        # Se o atual for o head, o head se torna o proximo do atual
        if atual == self.head:
            self.head = atual.proximo
        # se o atual for o último (trail), o ultimo vira o anterior ao atual
        if atual == self.tail:
            self.tail = atual.anterior

    def mostrar_clientes(self):
        atual = self.head
        while atual:
            print(atual)
            atual = atual.proximo

    def ordernar_por_cpf(self):
        if not self.head or not self.head.proximo:
            print("A lista não precisa ser ordenada.");
            return

        houve_troca = True
        while houve_troca:
            houve_troca = False
            no_atual = self.head
            while no_atual.proximo is not None:
                if no_atual.valor_gasto > no_atual.proximo.valor_gasto:
                    # nós temporários
                    no1 = no_atual
                    # guarda o valor do proximo do proximo
                    no2 = no_atual.proximo
                    # atualiza o proximo do atual como o proximo do proximo
                    no1.proximo = no2.proximo
                    if no2.proximo:
                        no2.proximo.anterior = no1
                    
                    no2.anterior = no1.anterior
                    if no1.anterior:
                        no1.anterior.proximo = no2
                    
                    no2.proximo = no1
                    no1.anterior = no2

                    if self.head == no1:
                        self.head = no2
                    if self.tail == no2:
                        self.tail = no1
                    
                    houve_troca = True
                else:
                    no_atual = no_atual.proximo

        print("Lista ordenada por valor crescente de gasto");
        self.mostrar_clientes();
                    

    def abastecer_cliente(self, cpf, valor_gasto):
        atual = self.head;
        while atual and atual.cpf != cpf:
            print(f"{atual}");
            atual = atual.proximo
        if atual is None:
            print("O CPF não existe nessa base de dados.");
            return
        if atual.cpf == cpf:
            atual.valor_gasto += valor_gasto
            return
        

def menu():
    posto = PostoGasolina();

    while True:
        print("Bem-vindo ao Posto Gasolina")
        print("1. Adicionar um novo cliente ao final");
        print("2. Adicionar um novo cliente ao início");
        print("3. Remover um cliente com base no CPF");
        print("4. Mostrar todos os clientes");
        print("5. Ordenar clientes pelo CPF");
        print("6. Abastecer cliente");

        try:
            escolha = int(input("Digite um número para chamar a ação: "))
        except ValueError:
            print("Esse número nao existe. Tente novamente");

        if escolha == 1:
            nome = input("Digite o nome para cliente: ");
            cpf = input("Insira o CPF do cliente: ");
            valor_gasto = int(input("Insira o valor gasto pelo cliente: "));
            posto.adicionar_cliente(nome, cpf, valor_gasto);
        elif escolha == 2:
            nome = input("Digite o nome para cliente: ");
            cpf = input("Insira o CPF do cliente: ");
            valor_gasto = int(input("Insira o valor gasto pelo cliente: "));
            posto.adicionar_cliente_ao_inicio(nome, cpf, valor_gasto);
        elif escolha == 3:
            cpf = input("Digite o CPF do cliente a ser removido: ")
            posto.remover_cliente(cpf)
        elif escolha == 4:
            posto.mostrar_clientes();
        elif escolha == 5:
            posto.ordernar_por_cpf();
        elif escolha == 6:
            cpf = input("Digite o CPF do cliente que quer abastecer: ");
            valor_gasto = int(input("Digite o valor gasto pelo cliente: "));
            posto.abastecer_cliente(cpf, valor_gasto);
        else:
            print("Escolha inválida");
            break;

if __name__ == "__main__":
    menu();
