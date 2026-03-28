import csv
import os
from services.addProduct import addProduct
from services.showInv import showInv
from services.statistics import calculateStatistics
from services.delProduct import delproduct
from services.seacrh import searchProduct
from services.update import updateProduct

inventory = []
menu = ["1 - Add Product", 
        "2 - Show Inventory", 
        "3 - Calculate Statistics",
        "4 - Delete Product", 
        "5 - Search Product",
        "6 - Update Product", 
        "7 - EXIT"]

option = 0

while option != 7: 
    print("\n--- MAIN MENU ---")
    for item in menu:
        print(item)
    
    try:
        option = int(input("Select an option (1-7): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if option == 1:
        inventory = addProduct(inventory)
    elif option == 2:
        inventory = showInv(inventory)
    elif option == 3:
        calculateStatistics(inventory)
    elif option == 4:
        inventory = delproduct(inventory)
    elif option == 5:
        searchProduct(inventory)
    elif option == 6:
        inventory = updateProduct(inventory)
    elif option == 7:
        print("\nGOODBYE!")
    else:
        print("Invalid option. Please select between 1-7.")