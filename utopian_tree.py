def utopianTree(n):
    # Write your code here
    count, height = 0, 1
    while count < n:
        if count % 2 == 0:
            height *= 2
        else:
            height += 1
        count += 1
    return height