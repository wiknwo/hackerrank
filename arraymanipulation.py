def arrayManipulation(n, queries):
    # Write your code here
    my_list = [0 for i in range(n)] # List containing n zeroes
    
    # Iterate through rows in queries 
    # and apply each one row by row to 
    # the list
    for i in range(len(queries)):
        for j in range(queries[i][0] - 1, queries[i][1]):
            my_list[j] += queries[i][2]
    
    return max(my_list)