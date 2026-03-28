def calculateStatistics(inventory):
    if not inventory:
        print("The inventory is empty")
        return []
    
    total = sum(float(p['cost']) * int(p['quantity']) for p in inventory)
    max_cost = max(float(p['cost']) for p in inventory)
    max_product = max(inventory, key=lambda p: float(p['cost']) * int(p['quantity'])) if inventory else None
    print("\n=== STATISTICS ===")
    print(f"TOTAL PRODUCTS: {len(inventory)}")
    print(f"TOTAL COST: ${total:.2f}")
    print(f"MAXIMUM UNIT COST: ${max_cost:.2f}")
    if max_product:
        print(f"MOST EXPENSIVE PRODUCT: {max_product['product']} (${max_product['cost']})")
    return inventory