def delproduct(list):
    print("DELETE PRODUCT")
    name = input(str("Enter the name of the product to delete: "))
    for p in list:
        if p['name'] == name:
            list.remove(p)
            print(f"Product '{name}' has been deleted.")
            break
    else:
        print(f"Product '{name}' not found in the inventory.")
    return list