def maxSubsetSum(arr):
    dp = [0] * len(arr) # List to hold dynamic programming sub values
    dp[0] = arr[0] # Max at position 0 is arr[0]
    dp[1] = max(arr[1], dp[0]) # Max at position 1 is either arr[1] or value at 0
    for i in range(2, len(arr)):
        # Max of position dp[i] is either:
        # arr[i]: current value at that position
        # dp[i - 1]: max value found so far
        # arr[i] + dp[i - 2]: Max value from 2 positions ack plus current value
        dp[i] = max(arr[i], dp[i - 1], arr[i] + dp[i - 2])
    return dp[-1]
