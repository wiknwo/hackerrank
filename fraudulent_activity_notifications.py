def computeMedian(a_list):
    median_index = len(a_list) // 2
    if len(a_list) % 2 == 0:
        return sum(a_list[median_index - 1:median_index + 1]) / 2
    else:
        return a_list[median_index]
    
def activityNotifications(expenditure, d):
    # Write your code here
    trailing_expenditures = expenditure[:d]
    notices = 0
    trailing_expenditures = sorted(trailing_expenditures)
    
    for i in range(d, len(expenditure)):
        if expenditure[i] >= 2 * computeMedian(trailing_expenditures):
            notices += 1
        del trailing_expenditures[bisect.bisect_left(trailing_expenditures, expenditure[i - d])]
        bisect.insort(trailing_expenditures, expenditure[i])
    return notices