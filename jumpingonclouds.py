def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    index = 0
    
    while index < len(c) - 1:
        if index + 2 < len(c) and c[index + 2] == 0:
            index += 2
            jumps += 1
        elif index + 1 < len(c) and c[index + 1] == 0:
            index += 1
            jumps += 1
    return jumps