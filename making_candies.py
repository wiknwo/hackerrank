def minimumPasses(m, w, p, n):
    # Write your code here
    candy = 0
    invest = 0
    spend = sys.maxsize
    while candy < n:
        # Calculate if enough candies to buy machines / workers 
        # (Otherwise price - candy becomes negative)
        # If not enough candies, we just add to the production 
        # with the current set up as many times as needed until 
        # can afford a new machine/worker
        passes = (p - candy) // (m * w)
        # if we can buy material, we do it (Greedy)
        if passes <= 0:
            # Number total of production power before acquiring 
            # machines or workers, we try have equal knowing 
            # that max x * y = Z, maximum is x , y = Z/2
            production = (candy // p) + m + w
            half = math.ceil(production / 2)
            # We add to the group with less resources 
            # until have a number equal to the production
            if m > w:
                m = max(m, half)
                w = production - m
            else:
                w = max(w, half)
                m = production - w
            # We save the remaining money
            candy %= p
            # In the next step, we will just add the new 
            # production for 1 pass when we buy
            passes = 1
        candy += passes * m * w
        invest += passes
        # Save the minimum between the current saving 
        # strategy (not buying new machine/worker) or 
        # using investment
        spend = min(spend, invest + math.ceil((n - candy) / (m * w)))
    return min(invest, spend)