def addProduct(list):
    import csv
    import os
    validation = int(input("Do you wanna add any product? (si=1/no=0): "))
    inventor = []   
    while validation == 1:
        base_dir = os.path.dirname(os.path.abspath(__file__))

        ruta_csv = os.path.join(base_dir, '..', 'data', 'inventory.csv')


        name = input(str("Name that product: "))
        cost = float(input("Cost: "))
        quantity = int(input("Quantity: "))
            
        
        list.append({'product': name, 'cost':cost, 'quantity':quantity})
        with open('inventory.csv', 'w', newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["product", "cost","quantity"])
            writer.writeheader()
            writer.writerows(list) 
        
        
        validation = int(input("¿Añadir otro? (si=1/no=0): "))
        if validation == 0:
            print("Return to main menu...")
    return list