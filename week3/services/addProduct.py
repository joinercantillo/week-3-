def addProduct(inventory):
    import csv
    import os
    validation = int(input("Do you want to add products? (yes=1/no=0): "))
    while validation == 1:
        try:
            name = input("Product name: ")
            cost = float(input("Cost: "))
            quantity = int(input("Quantity: "))
            
            inventory.append({'product': name, 'cost': cost, 'quantity': quantity})
            
            # Get the correct CSV file path
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            csv_path = os.path.join(base_dir, 'data', 'inventory.csv')
            
            with open(csv_path, 'w', newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["product", "cost", "quantity"])
                writer.writeheader()
                writer.writerows(inventory)
            
            print(f"Product '{name}' added successfully.")
            validation = int(input("Add another product? (yes=1/no=0): "))
            if validation == 0:
                print("Returning to main menu...")
        except FileNotFoundError as e:
            print(f"Error: CSV file path not found. {e}")
            break
        except ValueError:
            print("Error: Enter valid values (cost must be a number, quantity must be an integer)")
    return inventory