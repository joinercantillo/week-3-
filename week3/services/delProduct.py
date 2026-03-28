def delproduct(inventory):
    import csv
    import os
    print("\n=== DELETE PRODUCT ===")
    name = input("Enter the product name to delete: ")
    found = False
    for p in inventory:
        if p['product'].lower() == name.lower():
            inventory.remove(p)
            print(f"Product '{name}' has been deleted.")
            found = True
            break
    
    if not found:
        print(f"Product '{name}' not found in inventory.")
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