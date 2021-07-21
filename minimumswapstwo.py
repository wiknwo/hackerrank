def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr) - 1):
        while arr[i] != i + 1:
            tmp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = tmp
            swaps += 1
    return swaps