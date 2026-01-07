"""inserir novos clientes, remover clientes existentes, realizar balanceamento após cada
inserção/remoção e buscar clientes pelo nome, exibindo todas as informações
pertencentes a eles."""

import time

class Cliente:
    def __init__(self, nmr_corrente, nome, saldo, valor_credito):
        self.nmr_corrente = nmr_corrente
        self.nome = nome
        self.saldo = saldo
        self.valor_credito = valor_credito

class Sistema:
    # Baseado em árvore AVL
    def __init__(self):
        self.root = None