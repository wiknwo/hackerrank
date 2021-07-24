def birthdayCakeCandles(candles):
    # Write your code here
    mydict = {}
    # Fill dictionary
    for candle in candles:
        if candle not in mydict:
            mydict[candle] = 1
        elif candle in mydict:
            mydict[candle] += 1
    return mydict[max(mydict, key=mydict.get)]