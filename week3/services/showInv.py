def showInv(list):
    
    if not list:
        print("The list is empty")
    for p in list:
        print(f"- {p['product']}: ${p['cost']} (stock: {p['Quantity']})")
    return list             