
opcion = input("Elige tu fruto favorito: ")

match opcion.lower():
    case "manzana": 
        print("Elegiste manzana, excelente elección")
    case "durazno": 
        print("Elegiste durazno, excelente elección")
    case "mora": 
        print("Elegiste mora, excelente elección")
    case _: 
        print("Ninguna fruta elegida")
