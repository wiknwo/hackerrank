def climbingLeaderboard(ranked, player):
	"""
	Returns player's rank after each new score in leaderboard
    
    Time Complexity: O(nlogn)
    Spsce Complexity(O(n)
	"""
    # Write your code here
    ranked = sorted(list(set(ranked)))
    rank = 0
    rank_list = []
    n = len(ranked)
    for i in player:
        while (n > rank and i >= ranked[rank]):
            rank += 1
        rank_list.append(n+1-rank) 
    return rank_list