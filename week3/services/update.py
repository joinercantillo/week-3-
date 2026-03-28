def updateProduct(inventory):
    import csv
    import os
    print("\n=== UPDATE PRODUCT ===")
    name = input("Enter the product name to update: ")
    found = False
    
    for product in inventory:
        if product['product'].lower() == name.lower():
            new_name = input("Enter the new product name (press Enter to keep current): ")
            new_cost = input("Enter the new cost (press Enter to keep current): ")
            new_quantity = input("Enter the new quantity (press Enter to keep current): ")
            
            try:
                if new_name:
                    product['product'] = new_name
                if new_cost:
                    product['cost'] = float(new_cost)
                if new_quantity:
                    product['quantity'] = int(new_quantity)
                
                print("\nProduct updated successfully.")
                found = True
            except ValueError:
                print("Error: Cost must be a number, quantity must be an integer.")
                return inventory
            break
    
    if not found:
        print(f"Product '{name}' not found.")
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, 'data', 'inventory.csv')
        try:
            with open(csv_path, 'w', newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["product", "cost", "quantity"])
                writer.writeheader()
                writer.writerows(inventory)
        except FileNotFoundError as e:
            print(f"Error saving: {e}")
    
    return inventory