def getMax(arr):
    maximum = -sys.maxsize
    runningsum = 0
    for i in range(len(arr)):
        runningsum += arr[i]
        maximum = max(maximum, runningsum)
    return maximum

def arrayManipulation(n, queries):
    # Write your code here
    my_list = [0 for i in range(n + 2)] # List containing n zeroes
    
    # Iterate through rows in queries 
    # and apply each one row by row to 
    # the list
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        my_list[a] += k
        my_list[b + 1] -= k
    return getMax(my_list)