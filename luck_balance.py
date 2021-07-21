def luckBalance(k, contests):
    # Write your code here
    luck = 0
    sortedContests = sorted(contests, key=lambda x: x[0], reverse=True)
    for i in range(len(sortedContests)):
        contest_luck_balance = sortedContests[i][0]
        importance_rating = sortedContests[i][1]
        
        # Can lose a contest if it is not important
        if importance_rating == 0:
            luck += contest_luck_balance
        
        # Can lose up to k important contests
        elif importance_rating == 1 and k > 0:
            luck += contest_luck_balance
            k -= 1
        
            # Must win remaining n-k contests
        elif importance_rating == 1 and k == 0:
            luck -= contest_luck_balance
    return luck