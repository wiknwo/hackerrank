def stockmax(prices):
    # Write your code here
    profit = 0
    current_max = prices[-1]
    for i in range(len(prices)-1, -1, -1):
        if prices[i] >= current_max:
            current_max = prices[i]

        profit += current_max - prices[i]
    return profit