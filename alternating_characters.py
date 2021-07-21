def alternatingCharacters(s):
    # Write your code here
    deletions = 0
    for i in range(len(s) - 1):
        if s[i] == 'A' and s[i + 1] == 'A':
            deletions += 1
        elif s[i] == 'B' and s[i + 1] == 'B':
            deletions += 1
    return deletions