# Prova 1 - ED - Ingryd

class PaginaWeb:
    def __init__(self, url, titulo, timestamp):
        self.url = url
        self.titulo = titulo
        self.timestamp = timestamp
        self.anterior = None
        self.proximo = None

    def __str__(self):
        return f"Página: {self.titulo} / URL: {self.url} | Acesso: {self.timestamp}"

class GeminiBrowser:
    def __init__(self):
        self.head = None;
        self.tail = None;
        self.current = None;

    def visitar_nova_pagina(self, url, titulo, timestamp):
        nova_pag = PaginaWeb(url, titulo, timestamp)
        if not self.head:
            self.head = nova_pag
            self.tail = nova_pag
        else:
            self.tail.proximo = nova_pag
            nova_pag.anterior = self.tail
            self.tail = nova_pag
        self.current = nova_pag

    def voltar_pagina(self):
        if not self.current:
            print("Não existem páginas para voltar");
            return
        elif self.current.anterior is None:
            print("Não existe uma página próximo a sua atual.");
            return
        else:
            self.current.anterior = self.current
            print(f"Página atual foi para {self.current}");
            
    def voltar_pagina(self):
        if not self.current:
            print("Não existe uma página atual");
            return
        elif self.current.proximo is None:
            print("Não existe uma página próximo a sua atual.");
            return
        else:
            self.current.proximo = self.current
            print(f"Página atual foi para {self.current}");

    def buscar_historico(self, url):
        atual = self.head
        if not atual:
            print("Histórico está vazio. Navegue por algumas páginas antes.")
            return
        while atual and atual.url != url:
            atual = atual.proximo
            if atual.proximo is None:
                print("O histórico chegou ao fim e a página não foi encontrada.")
        if atual.url == url:
            print(f"Página encontrada no seu histórico: {atual.titulo} / URL: {atual.url} | Acesso em: {atual.timestamp}");

    def remover_pagina_historico(self, url):
        atual = self.head;
        while atual and atual.url != url:
            atual = atual.proximo
        if atual is None:
            print("Página não encontrada no seu histórico.");
            return
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        if atual == self.head:
            self.head = atual.proximo
        if atual == self.tail:
            self.tail = atual.anterior

def menu():
    browser = GeminiBrowser();

    while True:
        print("------ SITE DE PESQUISA GEMINI BROWSER ---------")
        print(f"Página atual: {browser.current}");
        print("1. Visitar nova página");
        print("2. Voltar a página anterior");
        print("3. Avançar para próxima página");
        print("4. Buscar no histórico");
        print("5. Remover página do histórico");
        print("6. Sair");

        try:
            escolha = int(input("Digite um número para chamar a ação: "))
        except ValueError:
            print("Esse número nao existe. Tente novamente");

        if escolha == 1:
            url = input("Digite a url do site: ");
            titulo = input("Digite o título do site: ");
            timestamp = int(input("Digite o horário de visita: "));
            browser.visitar_nova_pagina(url, titulo, timestamp);
        elif escolha == 2:
            browser.voltar_pagina();
        elif escolha == 3:
            browser.avancar_pagina();
        elif escolha == 4:
            url = input("Digite a url do site que deseja buscar: ");
            browser.buscar_historico(url);
        elif escolha == 5:
            url = input("Digite a url do site que deseja remover: ");
            browser.remover_pagina_historico(url);
        elif escolha == 6:
            print("Saindo...");
            break;
        else:
            print("Escolha inválida.");
            break;

if __name__ == "__main__":
    menu();
