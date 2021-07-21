'''Two Strings

    Given two strings, determine if they share a common substring. 
    A substring may be as small as one character.
    
    William Ikenna-Nwosu (wiknwo)
'''
def twoStrings(s1, s2):
    # Write your code here
    stringone, stringtwo = set(s1), set(s2)
    return 'NO' if stringone.isdisjoint(stringtwo) else 'YES'