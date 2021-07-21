def hourglassSum(arr):
    # Write your code here
    maximum_hourglass_sum = -sys.maxsize
    current_hourglass_sum = 0
    top, middle, bottom = 0, 0, 0
    
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            top = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            middle = arr[i + 1][j + 1]
            bottom = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            current_hourglass_sum = top + middle + bottom
            maximum_hourglass_sum = max(maximum_hourglass_sum, current_hourglass_sum)
    return maximum_hourglass_sum