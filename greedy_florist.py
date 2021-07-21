def getMinimumCost(k, c):
    sortedPrices = sorted(c, reverse=True)
    previous_purchase, minimum_cost = 0, 0
    
    for i in range(len(sortedPrices)):
        minimum_cost += (previous_purchase + 1) * sortedPrices[i]
        if (i + 1) % k == 0:
            previous_purchase += 1
    return minimum_cost