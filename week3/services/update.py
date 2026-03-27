def updateProduct(list):
    print("UPDATE PRODUCT")
    name = input("Enter the name of the product to update: ")
    for product in list:
        if product['name'] == name:
            new_name = input("Enter the new name of the product: ")
            new_cost = float(input("Enter the new cost of the product: "))
            product['name'] = new_name
            product['cost'] = new_cost
            print("Product updated successfully.")
            break
    else:
        print("Product not found.")
    return list