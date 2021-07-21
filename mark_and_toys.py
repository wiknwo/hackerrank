def maximumToys(prices, k):
    # Write your code here
    sortedPrices = sorted(prices)
    maxToys = 0
    for i in range(len(sortedPrices)):
        if k - sortedPrices[i] >= 0:
            k -= sortedPrices[i]
            maxToys += 1
    return maxToys