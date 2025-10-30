# Fila -> FIFO

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
        self.head = None
        self.tail = None
        self.current = None
        
    def visitar_nova_pag(url, titulo, timestamp):
        nova_pag = PaginaWeb(url, titulo, timestamp)
        if not self.head:
            self.head = self.tail = nova_pag
        else:
            # Adiciona no final e atualiza o ponteiro fim
            self.tail.proximo = nova_pag
            self.tail = nova_pag
        self.current = nova_pag
        print(f"Nova página adicionada à fila: {nova_pag}")
        
    def voltar_pagina(self):
        if not self.current:
            print("Nenhuma página para voltar.")
            return

        print(f"Voltando de: {self.topo}")
        self.current = self.current.proximo
        if self.current:
            print(f"Página atual: {self.current}")
        else:
            print("Histórico vazio.")
        
    def avancar_pagina(self):
        if not self.current or not self.current.proximo:
            print("Não há página seguinte para avançar.")
            return
    
        self.current = self.current.proximo
        print(f"Avançando para: {self.current}")
        
    def buscar_historico(self, url):
        if not self.head:
            print("Histórico vazio.")
            return

        pagina = self.head
        while pagina:
            if pagina.url == url:
                print(f"Página encontrada: {pagina}")
                return pagina
            pagina = pagina.proximo

        print("Página não encontrada no histórico.")
        
    def remover_pagina_historico(self, url):
        if not self.head:
            print("Histórico vazio.")
            return

        anterior = None
        pagina = self.head

        while pagina:
            if pagina.url == url:
                if anterior is None:
                    self.head = pagina.proximo
                    if not self.head:
                        self.tail = None
                else:
                    anterior.proximo = pagina.proximo
                    if pagina == self.tail:
                        self.tail = anterior
                print(f"Página removida do histórico: {url}")
                return
            anterior = pagina
            pagina = pagina.proximo

        print("Página não encontrada para remoção.")
        
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