func bubbleSort(_ array: inout [Int]) {
    let n = array.count
    for i in 0..<n - 1 {
        for j in 0..<n - i - 1 {
            if array[j] > array[j + 1] {
                array.swapAt(j, j + 1)
            }
        }
    }
}

var array = [14, 21, 19]
bubbleSort(&array)
print("Array ordenado: \(array)")