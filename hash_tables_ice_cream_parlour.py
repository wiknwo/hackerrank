def whatFlavors(cost, money):
    # Write your code here
    mydict = {}
    
    for index, value in enumerate(cost):
        if money - value in mydict:
            print(mydict.get(money - value) + 1, index + 1, " ")
        mydict[value] = index