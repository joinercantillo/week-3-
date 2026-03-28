def showInv(list):
    import csv
    with open('inventory.csv', "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        listdat = list(reader)
    return list
myinventory = showInv('inventory.csv')
for i in myinventory:
    print(i)