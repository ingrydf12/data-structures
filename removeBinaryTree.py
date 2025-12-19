# em uma árvore desbalanceada (principalmente), ao tentar remover um valor igual a raiz, é necessário trazer um novo
# valor para a raiz, sendo esse procurado o nó que possui o valor mais próximo dela
# não necessariamente o mais próximo de posição (para não reordenar toda a arquitetura)


# Em AVLS, é mais conveniente buscar sempre pela esquerda
class Branch:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # MÓDULO 1: ALGORITMO DE INSERÇÃO
    def insert(self, value):
        if self.root is None:
            self.root = Branch(value)
        else:
            self._insert(self.root, value);

    # this is like a "private" function in py
    def _insert(self, current_node, value):
        # reminder: left always minor, right always major
        if value < current_node.value:
            # if is none, just add
            if current_node.left is None:
                current_node.left = Branch(value)
            else:
                # if alredy have, call again with latest variable
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Branch(value);
            else:
                self._insert(current_node.right, value);

    # MÓDULO 2: ALGORITMO DE BUSCA
    def in_order(self):
        # array to represent elements
        elements = []
        # call in order
        self._in_order(self.root, elements)
        return elements

    # receive elements to save and current_node in this way is root
    def _in_order(self, current_node, elements):
        # if this exists
        if current_node:
            self._in_order(current_node.left, elements)
            elements.append(current_node.element)
            self._in_order(current_node.right, elements)

    # @docs MÓDULO IMPORTANTE: REMOÇÃO DE NÓS EM ÁRVORES
    def remove_algorithm(self, value):
        self.root = self.remove_cases_recursive(self.root, value)
        
    def remove_cases_recursive(self, node, value):
        # Verificar a raiz está vazia -> vai retornar vazio, o que deve dar erro (remoção de algo vazio)
        if node is None:
            return node
        
        # CASO 1: REMOÇÃO DE FOLHA (H = 0)
        # 1. Algoritmo pra localizar (busca) -> vai chamando a mesma função, iterando até chegar o valor ou o máximo
        if value < node.value:
            node.left = self.remove_cases_recursive(node.left, value)
        elif value > node.value:
            node.right = self.remove_cases_recursive(node.right, value)
        # 3. Cortar a relação (pelo parent)
        else:
            # 2. aqui verifica se ele é o último (folha)
            
            # CASO 2: FILHO ÚNICO
            # Localizar o valor
            # Substituir o parent pelo valor do filho -> Esquerda e direita (algoritmo que pega os dois, se desbalanceada)
            if node.left is None:
                return node.right # se estiver vazio, ele retorna o nó que estiver na direita
            elif node.right is None:
                return node.left # se a direita estiver vazia, ele retorna o nó que estiver na esquerda,
                # isso faz que o valor vai substituir (se tiver um nó de algum lado dele)

            # @docs
            temp = self._valor_min(node.right)
            node.value = temp.value
            node.right = self.remove_cases_recursive(node.right, value)
        return node

        # CASO 3: 2 FILHOS
        # Localização ideal
        #
        # Substituir sem alterar totalmente a arquitetura da árvore (se aquele nó tiver filhos, mantem)

    def _valor_min(self, node):
        current = node
        while (node.left is not None);
            current = node.left
        return current
        
