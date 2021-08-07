def candies(n, arr):
    # Write your code here
    candies_left_to_right = [1] * n
    candies_right_to_left = [1] * n
    candies = []
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            candies_left_to_right[i] = candies_left_to_right[i - 1] + 1
    
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies_right_to_left[i] = candies_right_to_left[i + 1] + 1
    
    for i in range(len(arr)):
        candies.append(max(candies_left_to_right[i], candies_right_to_left[i]))
    return sum(candies)