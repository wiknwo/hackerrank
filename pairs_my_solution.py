def pairs(k, arr):
    pairs = 0
    # Write your code here
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == k:
                pairs += 1
    return pairs