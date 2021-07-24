def pairs(k, arr):
    # Write your code here
    pairs = 0
    sortedlist = sorted(arr) # Sort the list in ascending order
    j = 1 # j will be an index one ahead of i, ensuring it is always the larger value
    # Iterate through the sorted list
    for i in range(len(sortedlist) - 1):
        # We will check each j against
        # the specific i then repeat
        while j < len(sortedlist):
            if sortedlist[j] - sortedlist[i] == k:
                pairs += 1
                j += 1
            # Here we break because the difference
            # is going to continue getting larger
            # since the list is sorted, it is 
            # monotonically increasing
            elif sortedlist[j] - sortedlist[i] > k:
                break
            elif sortedlist[j] - sortedlist[i] < k:
                j += 1
    return pairs