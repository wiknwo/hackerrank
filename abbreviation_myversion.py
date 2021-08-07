def abbreviation(a, b):
    # Write your code here
    new_string = ''
    for char in a:
        if char.islower() and char.upper() in b:
            new_string += char.upper()
        elif char.isupper() and char in b:
            new_string += char
        elif char.isupper() and char not in b:
            new_string += char
        elif char.islower() and char.upper() not in b:
            new_string += ''
        
    print(new_string)
    return 'YES' if new_string == b else "NO"