def searchProduct(inventory):
    import os
    import csv
    print("\n=== SEARCH PRODUCT ===")
    name = input("Enter the product name to search: ")
    found_products = [p for p in inventory if p['product'].lower() == name.lower()]
    
    if found_products:
        print("\nProduct(s) found:")
        for product in found_products:
            print(f"  Name: {product['product']}, Cost: ${product['cost']}, Quantity: {product['quantity']}")
    else:
        print(f"No products found with the name '{name}'.")
    
    return inventory