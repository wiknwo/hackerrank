def equalizeArray(arr):
	"""
	Determines minimum number of deletions to make for
	all values in list to be equal
	"""
    # Write your code here
    return len(arr) - max([arr.count(i) for i in arr])