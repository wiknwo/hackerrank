def minimumAbsoluteDifference(arr):
    # Write your code here
    min_abs_diff = sys.maxsize
    sortedlist = sorted(arr)
    for i in range(len(sortedlist) - 1):
        min_abs_diff = min(abs(sortedlist[i] - sortedlist[i + 1]), min_abs_diff)
    return min_abs_diff