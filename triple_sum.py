def triplets(a, b, c):
    triplets, plessthanequalq, qgreaterthanequalr = 0, 0, 0
    
    # Remove duplicates and sort
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))
    
    # Iterate through set b
    for value in b:
        while plessthanequalq < len(a) and a[plessthanequalq] <= value: # p <= q
            plessthanequalq += 1
        while qgreaterthanequalr < len(c) and c[qgreaterthanequalr] <= value: # r <= q
            qgreaterthanequalr += 1
        triplets += plessthanequalq * qgreaterthanequalr
    return triplets