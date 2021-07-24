def triplets(a, b, c):
    triplets = 0
    
    for number in set(b):
        plessthanequalq = [value for value in a if value < number or value == number]
        qgreaterthanequalr = [value for value in c if number > value or number == value]
        print(plessthanequalq, qgreaterthanequalr, " ")
        triplets += len(plessthanequalq) * len(qgreaterthanequalr)
    return triplets