def countTriplets(arr, r):
    tripletscount = 0
    before_dict, after_dict = {}, {}
    
    # Initialise after dictionary
    for element in arr:
        if element not in after_dict:
            after_dict[element] = 1
        elif element in after_dict:
            after_dict[element] += 1
    
    # Calculate triplets
    for element in arr:
        after_dict[element] -= 1 # This is our current element, no longer in after_dict
        if element // r in before_dict and element % r == 0 and element * r in after_dict:
            tripletscount += before_dict[element // r] * after_dict[element * r]
        if element in before_dict:
            before_dict[element] += 1
        elif element not in before_dict:
            before_dict[element] = 1
    return tripletscount