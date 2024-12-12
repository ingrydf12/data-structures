/* Desafio 1: Inverter uma matriz
Crie uma função que imprima o conteúdo de uma matriz em ordem inversa. */ 

//Matriz genérica -> matriz (ou lista) de elementos do tipo genérico T
func invMatriz<T> (_ array: [T]) {
    var m = Stack<T>() // aqui cria uma pilha genérica (Stack)

//Itera os valores no array e envia pra pilha
    for value in array {
        m.push(value)
    }

//aqui ele desempilha os elementos da pilha e imprime o valor 
    while let value = m.pop() {
    print(value)
  }
}