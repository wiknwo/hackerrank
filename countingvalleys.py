def countingValleys(steps, path):
    # Write your code here
    current_level = 0 # Variable to keep track of altitude above or below sea level
    valleys = 0
    
    # Iterate over path
    for step in path:
        if step == 'U' and current_level == -1:
            valleys += 1
        if step == 'D':
            current_level = current_level - 1
        else:
            current_level = current_level + 1
    
    return valleys