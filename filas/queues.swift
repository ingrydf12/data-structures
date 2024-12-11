//MARK: - Filas em swift
struct Fila<T> {
    // Lista genérica
    var list = [T]()
    
    // Adiciona um elemento à fila
    mutating func enqueue(_ element: T) {
        list.append(element)
    }
    
    // Remove e retorna o primeiro elemento da fila
    mutating func dequeue() -> T? {
        if !list.isEmpty {
            return list.removeFirst()
        } else {
            return nil
        }
    }
    
    // Retorna o primeiro elemento da fila sem removê-lo
    func pega() -> T? {
        if !list.isEmpty {
            return list[0]
        } else {
            return nil
        }
    }
    
    // Propriedade para verificar se a fila está vazia
    var isEmpty: Bool {
        return list.isEmpty
    }
}