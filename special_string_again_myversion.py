def checkAllCharactersSame(s):
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            return False
    return True

def checkAllCharactersSameExceptMiddleChar(s):
    if len(s) % 2 == 1:
        middle_character_index = len(s) // 2
        newstr = s[:middle_character_index] + s[middle_character_index + 1:]
        return checkAllCharactersSame(newstr)
        
# Complete the substrCount function below.
def substrCount(n, s):
    special_string_count = 0
    for i in range(n):
        for substrlen in range(i + 1, n + 1):
            substring = s[i: substrlen]
            if checkAllCharactersSame(substring) or checkAllCharactersSameExceptMiddleChar(substring):
                special_string_count += 1
                print(substring)
    return special_string_count
