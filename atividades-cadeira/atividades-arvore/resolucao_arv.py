# Resoluçao de provas antigas
class Robo:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return f"Robo {self.id}: {self.nome}"

class Gerenciador:
    def __init__(self):
        self.root = None

    def insert(self, id, nome):
        self.root = self._insert(self.root, id, nome)

    def _insert(self, root, id, nome):
        # Se não tiver nada na árvore, vai ser criado o Robô direto
        if not root:
            return Robo(id, nome)

        # lado esquerdo é sempre menor que a raiz
        if id < root.id:
            # passa de novo a função até chegar a folha
            root.left = self._insert(root.left, id, nome)
            root.left.parent = root
        else:
            root.right = self._insert(root.right, id, nome)
            root.right.parent = root

        # Altura e balanceamento (nivel)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and id < root.left.id:
            return self.right_rotate(root)

        # Direita-Direita
        if balance < -1 and id > root.right.id:
            return self.left_rotate(root)

        # Esquerda-Direita
        if balance > 1 and id > root.left.id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Direita-Esquerda
        if balance < -1 and id < root.right.id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # MARK: - Remove por ID
    def remove(self, id):
        self.root = self._remove(self.root, id)

    def _remove(self, root, id):
        if not root:
            return root

        if id < root.id:
            root.left = self._remove(root.left, id)
        elif id > root.id:
            root.right = self._remove(root.right, id)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.get_min_value(root)
            root.id = temp.id
            root.nome = temp.nome
            root.right = self._remove(root.right, temp.id)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # LL - Esquerda-Esquerda
        # Ta maior na esquerda do filho esquerdo
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR - Esquerda-Direita
        # Ta maior na direita do filho esquerdo
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR - Direita-Direita
        # Cresceu a direita do filho direito
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL - Direita-Esquerda
        # Cresceu a esquerda da direita, a balança ta pesada pra DIREITA (negativo) e o nó pesado pra ESQUERDA (positivo)
        if balance < -1 and self.get_balance(root.right) > 0:
            # Passa o nó pra direita
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # MARK: - Buscas
    def buscar_por_nome(self, nome):
        return self._buscar_por_nome(self.root, nome)
    
    def _buscar_por_nome(self, root, nome):
        if not root:
            return root
        
        if root.nome == nome:
            return root
        
        findName = self._buscar_por_nome(root.left, nome)
        if findName:
            return findName
            
        return self._buscar_por_nome(root.right, nome)
    
    def buscar_por_id(self, id):
        return self._buscar_por_id(self.root, id);
    
    def _buscar_por_id(self, root, id):
        if not root:
            return root;
        
        if root.id == id:
            return root;
        
        findById = self._buscar_por_id(root.left, id);
        if findById:
            return findById;
        
        return self._buscar_por_id(root.right, id);
            
    # Usa quando a árvore está pesada pra direita (NEGATIVO)
    # O node é o nó desbalanceado -> Pra direita
    def left_rotate(self, node):
        # Pega o valor do nó da direita dele e a sub-arvore da esquerda desse nó
        novo_root = node.right
        subarvore = novo_root.left

        novo_root.left = node
        novo_root.right = subarvore

        # ALterando as referëncias de parent
        novo_root.parent = node.parent
        node.parent = novo_root

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        novo_root.height = 1 + max(
            self.get_height(novo_root.left), self.get_height(novo_root.right)
        )

        return novo_root

    # Usa quando a árvore está pesada pra esquerda (POSITIVO)
    # O node é o nó desbalanceado -> Pra esquerda
    def right_rotate(self, node):
        novo_root = node.left
        subarvore = novo_root.right

        novo_root.right = node
        novo_root.left = subarvore

        # Parents - Node e Node.right
        novo_root.parent = node.parent
        node.parent = novo_root

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        novo_root.height = 1 + max(
            self.get_height(novo_root.left), self.get_height(novo_root.right)
        )

        return novo_root

    # Itera até o valor mais baixo da arvore - Folha da subarvore esquerda
    def get_min_value(self, data):
        current = data
        while current.left:
            current = data.left
        return current

    # Se nao tiver um root, a altura é 0
    def get_height(self, root):
        return root.height if root else 0

    # Balanceamento da árvore é sempre ESQ - DIREITA > | 1 |
    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right)
