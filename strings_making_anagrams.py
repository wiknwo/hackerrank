def makeAnagram(a, b):
    # Write your code here
    a_char_freq = [0] * 26
    b_char_freq = [0] * 26
    deletions = 0
    
    for i in range(len(a)):
        a_char_freq[ord(a[i]) - ord('a')] += 1
        
    for i in range(len(b)):
        b_char_freq[ord(b[i]) - ord('a')] += 1
        
    for i in range(26):
        deletions += abs(a_char_freq[i] - b_char_freq[i])
    
    return deletions