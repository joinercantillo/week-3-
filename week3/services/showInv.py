def showInv(inventory):
    import csv
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'data', 'inventory.csv')
    try:
        with open(csv_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            listdat = list(reader)
            if listdat:
                print("\n=== INVENTORY ===")
                for row in listdat:
                    print(f"Product: {row['product']}, Cost: ${row['cost']}, Quantity: {row['quantity']}")
            else:
                print("The inventory is empty.")
            return listdat
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
        return []