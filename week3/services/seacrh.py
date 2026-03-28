def searchProduct(list):
    print("SEARCH PRODUCT")
    name = input("Enter the name of the product to search: ")
    found_products = [p for p in list if p['name'].lower() == name.lower()]
    base_dir = os.path.dirname(os.path.abspath(__file__))

    ruta_csv = os.path.join(base_dir, '..', 'data', 'inventory.csv')

    if found_products:
        print("Product(s) found:")
        for product in found_products:
            print(f"Name: {product['name']}, Cost: {product['cost']}")
    else:
        print("No products found with that name.")
    return(list)