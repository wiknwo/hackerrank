def miniMaxSum(arr):
    # Write your code here
    sortedlist = sorted(arr)
    print(sum(sortedlist[:4]),sum(sortedlist[1:]), " ")