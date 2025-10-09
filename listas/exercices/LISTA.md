# Lista de Exercícios

## Lista 1
A - Simples
	•	Inserir um novo item no início do marketplace.
	•	Inserir um novo item no final do marketplace.
	•	Remover um item do marketplace pelo nome.
	•	Verificar se um item está disponível no marketplace.
B - Intermediárias
	•	Contar quantos itens estão cadastrados no marketplace.
	•	Inverter a ordem dos itens no marketplace (último vira o primeiro).
	•	Inserir item no marketplace mantendo a ordem crescente de preço.
C - Difícil
	•	Mesclar dois marketplaces ordenados por preço em um único marketplace ordenado.	


## Lista 2

Contextualização:

Você faz parte da equipe de desenvolvimento da "AgileCorp", uma startup que estÃ¡ criando um software de gerenciamento de projetos chamado TaskMaster. O coração do sistema Ã© a lista de tarefas (backlog) de um projeto. Sua função é implementar a lógica principal que permite aos usuários manipular essa lista de tarefas de forma eficiente.

Objetivo:

Aplicar os conceitos de manipulação de listas (seja usando arranjos dinÃ¢micos ou listas ligadas) para implementar as funcionalidades centrais de um sistema de gerenciamento de tarefas.

Ferramentas:

Estrutura de Dados: O foco Ã© a utilizaÃ§Ã£o de uma estrutura de lista duplamente encadeada.

Estrutura de Dados Base:

Primeiro, defina uma classe para representar uma Tarefa. Ela deve conter, no mÃ­nimo, os seguintes atributos:

- id (inteiro, único para cada tarefa)
- descricao (texto)
- prioridade (inteiro, ex: 1 para alta, 2 para mÃ©dia, 3 para baixa)
- status (texto, ex: "A Fazer", "Em Andamento", "ConcluÃ­da")

Requisitos da Atividade:

VocÃª deve criar um programa principal que gerencia uma Ãºnica lista de tarefas e implemente as seguintes funções:

1. Adicionar Tarefa no Fim da Lista:

Crie uma função adicionar_tarefa(tarefa) que insere uma nova tarefa no final da lista de pendências. Esta Ã© a forma padrão de adicionar novos itens ao backlog.

2. Adicionar Tarefa Urgente no InÃ­cio da Lista:

Crie uma função adicionar_tarefa_urgente(tarefa) que insere uma nova tarefa no inÃ­cio da lista. Isso Ã© Ãºtil para tarefas crÃ­ticas que precisam ser vistas primeiro.

3. Inserir tarefa em Posição Especí­fica:

Crie uma função inserir_tarefa_apos(id_referencia, nova_tarefa). Esta função deve encontrar a tarefa com o id_referencia e inserir a nova_tarefa imediatamente apÃ³s ela na lista. Se o ID de referência nÃ£o for encontrado, a nova tarefa não deve ser inserida e uma mensagem de erro deve ser exibida.

4. Remover Tarefa:

Crie uma função remover_tarefa(id) que busca uma tarefa pelo seu id e a remove da lista. Se a tarefa não for encontrada, exiba uma mensagem informativa.

5. Procurar Tarefa:

Crie uma função procurar_tarefa(id) que busca uma tarefa pelo seu id. Se encontrada, a funÃ§Ã£o deve retornar (e exibir na tela) todos os detalhes da tarefa. Caso contrÃ¡rio, deve informar que a tarefa nÃ£o foi encontrada.

6. QuestÃ£o EspecÃ­fica: Organizar por Prioridade:

Crie uma função organizar_por_prioridade(). Esta função não deve usar um algoritmo de ordenaÃ§Ã£o completo (como Bubble Sort, Quick Sort, etc.). Em vez disso, ela deve percorrer a lista uma única vez e mover todas as tarefas com prioridade == 1 (alta) para o inÃ­cio da lista, mantendo a ordem relativa entre elas e entre as demais tarefas.

Exemplo:

Lista inicial: [id:1, P:2], [id:2, P:1], [id:3, P:3], [id:4, P:1]

Lista final: [id:2, P:1], [id:4, P:1], [id:1, P:2], [id:3, P:3]