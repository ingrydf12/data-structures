class Item:
    def __init__(self, id, name, price):
        self.id = id;
        self.name = name;
        self.price = price;
        self.proximo = None;

    def __str__(self):
        return f"Item {self.id}: {self.name} | {self.price}, próximo: [{self.proximo}]";


class Marketplace:
    def __init__(self):
        self.head = None;
        self.trail = None;

    def adicionar_item_marketplace(self, item_id, name, price):
        novo_item = Item(item_id, name, price);
        if not self.head:
            self.head = novo_item
            self.trail = novo_item
            return
        else:
            self.trail.proximo = novo_item
            self.trail = novo_item

    def verificar_item(self):
        atual = self.head
        print("Itens do mercado: ");
        while atual:
            print(atual);
            atual = atual.proximo;
            
    def contagem_itens(self):
        atual = self.head
        cont = 0;
        while atual:
            cont += 1;
            atual = atual.proximo
        return print(f"Quantidade de itens no Marketplace: {cont}");
        

mercado = Marketplace();
def main():
    print("MERCADO 1");
    print("1. Adicionar item")
    print("2. Ver itens no mercado")
    print("3. Contar itens");

    while True:
        try:
            escolha = int(input("Digite sua escolha: "))
        except ValueError:
            print("Entrada invÃ¡lida. Por favor, digite um nÃºmero.")
            continue

        if escolha == 1:
            item_id = input("Digite o ID: ")
            nome = input("Digite o nome do item: ")
            price = input("Digite um preço para o item: ")
            mercado.adicionar_item_marketplace(item_id, nome, price)
        elif escolha == 2:
            mercado.verificar_item();
        elif escolha == 3:
            mercado.contagem_itens();

if __name__ == "__main__":
    main()

