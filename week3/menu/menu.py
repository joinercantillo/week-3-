def menu():
    menu =["1 - Add a product", 
        "2 - Show the inventory", 
        "3 - Calculate statistics",
            '4 - delete product', 
            '5 - search product',
            '6 - update product', 
            '7 - EXIT']
    option = 5 
    totalcost = 0
    while option != 7: 
        print("\n--- MENU---")
        for item in menu:
            print(item)
        
        option = int(input("Select an option (1-4): "))

        if option == 1:
            week3.services.addProduct(list)
        elif option == 2:
            week3.services.showInv(list)
        elif option == 3:
            week3.services.calculateStatistics(list)
        elif option == 4:
            print("DELETE PRODUCT")
            week3.services.delProduct(list)
        elif option == 5:
            print("SEARCH PRODUCT")
            week3.services.searchProduct(list)
        elif option == 6:
            print("UPDATE PRODUCT")
            week3.services.updateProduct(list)
        elif option == 7:
            print("GOOD BYE...")
    return list