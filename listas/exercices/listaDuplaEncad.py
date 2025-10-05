# https://docs.python.org/pt-br/3.13/tutorial/classes.html

class Produto:
    def __init__(self, id, nome, preco):
        self.id = id;
        self.nome = nome;
        self.preco = preco;
        self.proximo = None;
        self.anterior = None;

    def __str__(self):
        return f"Produto: {self.id} | {self.nome} / {self.preco}";

class Mercado:
    def __init__(self):
        self.head = None;
        self.tail = None;

    def adicionar_produto(self, item_id, nome, preco):
        novo_prod = Produto(item_id, nome, preco);
        if not self.head:
            self.head = novo_prod;
            self.tail  = novo_prod;
            return
        else:
            # Self.trail é o anterior (ultimo) -> referencia de proximo que era None vira o novo_prod
            self.tail.proximo = novo_prod
            novo_prod.anterior = self.tail
        self.tail = novo_prod;

    def remover_produto(self, id):
        atual = self.head;
        while atual and atual.id != id:
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

    def exibir_produtos(self):
        produtos = []
        atual = self.head
        while atual:
            produtos.append(atual)
            print(atual)
            atual = atual.proximo
        return produtos

    def contar_produtos(self):
        atual = self.head;
        cont = 0;
        while atual:
            atual = atual.proximo
            cont +=1;
        print(f"Contagem total de produtos: {cont}");

    def inverter_lista_dupla(self):
        # verificar se esta vazia ou se só tem um elemento (que não precisam inverter sem sentido)
        if not self.head:
            print("Lista vazia");
            return
        
        atual = self.head
        temp_node = None # vai guardar a ref do anterior sempre
        # inverte as referências (o proximo vira o anterior, o anterior com auxilio do temp_node vira o proximo
        while atual:
            temp_node = atual.anterior
            atual.anterior = atual.proximo
            atual.proximo = temp_node
            atual = atual.anterior
        # precisa atualizar o head e o tail -> muda pra outra linguagem (isso so py)
        self.head, self.tail = self.tail, self.head
        print("A ordem da lista foi invertida.");

    # inserção baseado na ordenacao
    def insercao_ordenada_preco_crescente(self, item_id, nome, preco):
        novo_prod = Produto(item_id, nome, preco);
        if not self.head:
            self.head = novo_prod;
            self.tail  = novo_prod;
            return

        # caso 2: no inicio (antes do head)
        if novo_prod.preco <= self.head.preco:
            novo_prod.proximo = self.head
            self.head.anterior = novo_prod
            self.head = novo_prod
            return
        
        # caso 3: no meio da lista
        atual = self.head
        while atual.proximo and atual.proximo.preco < novo_prod.preco:
            atual = atual.proximo

        # chegou a condição
        # caso 4: chegou ao final da lista
        if not atual.proximo:
            # se não tem proximo, chegou ao final (tail)
            self.tail.proximo = novo_prod
            novo_prod.anterior = self.tail
            self.tail = novo_prod
        else: #insere ao meio
            novo_prod.proximo = atual.proximo
            atual.proximo.anterior = novo_prod
            atual.proximo = novo_prod
            novo_prod.anterior = atual

    # ordernar por preço
    

class MercadoDoHenrique(Mercado):
    def teste(self):
        print("Teste");
        return


def juntar_e_ordenar_mercados(mercado1, mercado2):
    mercado_ordenado = Mercado()

    # Percorre o primeiro mercado
    atual = mercado1.head
    while atual:
        mercado_ordenado.insercao_ordenada_preco_crescente(atual.id, atual.nome, float(atual.preco))
        atual = atual.proximo

    # Percorre o segundo mercado
    atual = mercado2.head
    while atual:
        mercado_ordenado.insercao_ordenada_preco_crescente(atual.id, atual.nome, float(atual.preco))
        atual = atual.proximo

    return mercado_ordenado

def main():    
    while True:
        print("\nMercado duplamente encadeado")
        print("1. Listar todos os produtos")
        print("2. Adicionar produto")
        print("3. Remover produto por ID")
        print("4. Contar produtos");
        print("5. Inverter lista (último na frente)");
        print("6. Ordenar os produtos dos marketplaces disponíveis por preço")
        print("7. Sair");

        try:
            escolha = int(input("Digite sua escolha: "));
        except ValueError:
            print("Entrada inválida");
            continue

        if escolha == 1:
            choice = int(input("Digite um número para qual mercado ver produtos: "));
            if choice == 1:
                mercado.exibir_produtos();
            elif choice == 2:
                mercado_sec.exibir_produtos();
            else:
                print("Escolha inválida");
        elif escolha == 2:
            novo_id = int(input("Digite o ID: "))
            novo_nome = input("Digite o nome: ")
            novo_preco = input("Digite o preço: ")

            choice = int(input("Digite um número para qual mercado deseja adicionar"));
            if choice == 1:
                mercado.adicionar_produto(novo_id, novo_nome, novo_preco);
            elif choice == 2:
                mercado_sec.adicionar_produto(novo_id, novo_nome, novo_preco);
            else:
                print("Escolha inválida");
        elif escolha == 3:
            remove_id = int(input("Digite o ID do produto a ser removido: "));
            mercado.remover_produto(remove_id);
        elif escolha == 4:
            mercado.contar_produtos();
        elif escolha == 5:
            mercado.inverter_lista_dupla();
        elif escolha == 6:
            # puxar as ordenações e juntar em um só
            mercado_ordenado = juntar_e_ordenar_mercados(mercado, mercado_sec)
            mercado_ordenado.exibir_produtos()
        elif escolha == 7:
            break;

if __name__ == "__main__":
    mercado = Mercado();
    mercado_sec = MercadoDoHenrique();
    main()