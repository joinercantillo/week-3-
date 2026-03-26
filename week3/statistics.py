def calculateStatistics(list):
    
    total = sum (p['cost'] for p in list)
    totalcost = total * len(list)
    print("CALCULATE STATISTICS")
    print(f"TOTAL COST ${totalcost}")
    return list