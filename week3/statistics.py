def calculateStatistics(list):
    
    total = sum (p['cost'] for p in list)
    totalcost = total * len(list)
    max_cost = max(p['cost'] for p in list) if list else 0
    max_product = max(list, key=lambda p: p['cost']) if list else None
    print("CALCULATE STATISTICS")
    print(f"TOTAL PRODUCTS: {len(list)}")
    print(f"TOTAL COST ${totalcost}")
    print(f"MAXIMUM COST ${max_cost}")
    print(f"MAXIMUM PRODUCT: {max_product['name']}")
    return list