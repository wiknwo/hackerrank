def maximumSum(a, m):
    # Write your code here
    mm,pr=0,0
    a1=[]
    for i in a:
        pr=(pr+i)%m
        mm=max(mm,pr)
        ind=bisect.bisect_left(a1,pr+1)
        if(ind<len(a1)):
            mm=max(mm,pr-a1[ind]+m)
        bisect.insort(a1,pr)
    return mm