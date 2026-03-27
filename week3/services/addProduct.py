def addProduct(list):
    
    validation = int(input("Do you wanna add any product? (si=1/no=0): "))
        
    while validation == 1:
        name = input(str("Name that product: "))
        cost = float(input("Cost: "))
        quantity = int(input("Quantity: "))
            
        products = {'product': name, 
                        'cost': cost, 
                        'Quantity': quantity}
        list.append(products)
            
        
        
        validation = int(input("¿Añadir otro? (si=1/no=0): "))
        print("Return to main menu...")
    return list