#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

# def poisonousPlants(p):
    # Write your code here
# def poisonousPlants(p):
#     maxdays=0
#     s=[]
#     for i in range(len(p)):
#         alive=0
#         while s and p[i]<=s[-1][0]:
#             alive=max(alive,s.pop()[1])
#         if s:
#             alive=alive+1
#         else:
#             alive=0
#         maxdays=max(alive,maxdays)
#         s.append([p[i],alive])
#     return maxdays

def poisonousPlants(p):
    sl, d = [[p[0]]], 0
    for i, v in enumerate(p[1:], 1):
        if p[i - 1] < v: sl += [[v]]
        else: sl[-1] += [v]
    while len(sl) > 1:
        i = 1
        while i < len(sl):
            sl[i].pop(0)
            if not sl[i]: sl.pop(i)
            elif sl[i - 1][-1] >= sl[i][0]:
                sl[i - 1] += sl[i]
                sl.pop(i)
            else: i += 1
        d += 1
    return d