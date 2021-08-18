def breakingRecords(scores):
	"""
	Return number of times player breaks record for 
	minimum points and maximum points
	
	Time Complexity: O(n)
	Space Complexity: O(1)
	
	n is the number of scores
	"""
    # Write your code here
    min_score, max_score, min_count, max_count = sys.maxsize, -sys.maxsize, -1, -1
    # Iterate through scores
    for score in scores:
        if score > max_score:
            max_score = score
            max_count += 1
        if score < min_score:
            min_score = score
            min_count += 1
    return [max_count, min_count]