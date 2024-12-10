//Swift Struct
struct Bicycle {
    var name: String
    var brand: String
    var weight: Double
}

var touringBike = Bicycle(name: "Bicicleta", brand: "Oakley", weight: 65.2) //Associando valores

let bikeMessage = "My \(touringBike.brand) bicycle weights \(touringBike.weight) pounds." //Return