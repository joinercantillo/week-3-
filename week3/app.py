import csv
import os
from services.addProduct import addProduct
from services.showInv import showInv
from services.statistics import calculateStatistics
from services.delProduct import delproduct
from services.seacrh import searchProduct
from services.update import updateProduct
list = []
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
    
    option = int(input("Select an option (1-7): "))

    if option == 1:
        addProduct(list)
    elif option == 2:
       showInv(list)
            
    elif option == 3:
       calculateStatistics(list)
    elif option == 4:
        print("DELETE PRODUCT")
    elif option == 5:
        print("SEARCH PRODUCT")
    elif option == 6:
        print("UPDATE PRODUCT")

    elif option == 7:
        print("GOOD BYE...")