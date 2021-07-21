def rotLeft(a, d):
    # Write your code here
    for i in range(d):
        item = a.pop(0)
        a.append(item)
    return a