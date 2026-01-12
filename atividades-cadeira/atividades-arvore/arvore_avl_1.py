class Branch:
    def __init__(self, value):
        self.value = value;
        self.height = 1
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f"Nó de valor {self.value} / Parente: {self.parent}"

class Arvore:
    def __init__(self):
        self.root = None
        self.current_branch = None

    # balanceamento -> fator de balanceamento
    # diferença (esq - dir) > | 1 |
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if not root:
            return Branch(value)

        if value < root.value:
            root.left = self._insert(root.left, value)
            root.left.parent = root
        else:
            root.right = self._insert(root.right, value)
            root.right.parent = root

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        # Esquerda-Esquerda
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Direita-Direita
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Esquerda-Direita
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Direita-Esquerda
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
	# o balanceamento positivo, inclinado mais para um lado
	# mais para esquerda -> balanco mais positivo (direita, os maiores)
        #if balance > 1 and self.get_balance(root.left) >= 0:
	#	return self.right_rotate(root)
	# mais para direita -> balanco mais negativo (esquerda, os menores)
	#if balance < -1 and self.get_balance(root.right) <= 0:
	#	return self.left_rotate(root)
	#if balance > 1 and self.get_balance(root.left) < 0:
	#	root.left = self.left_rotate(root.left)

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self._remove(root.left, value)
        elif value > root.value:
            root.right = self._remove(root.right, value)
        else:
            # nó com 0 ou 1 filho
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # nó com dois filhos
            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self._remove(root.right, temp.value)

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        # balanceamentos
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def in_order(self):
        elements = []
        self._in_order(self.root, elements)
        return elements

    def _in_order(self, node, elements):
        if node:
            self._in_order(node.left, elements)
            elements.append(node.value)
            self._in_order(node.right, elements)


    # Rotação a esquerda -> para balancear
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        if T2:
            T2.parent = z

        y.parent = z.parent
        z.parent = y

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        if T3:
            T3.parent = z

        y.parent = z.parent
        z.parent = y

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        return root.height if root else 0

    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current