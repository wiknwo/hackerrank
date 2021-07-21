def isValid(s):
    # Write your code here
    freq_dict, is_valid = {}, False
    
    # Calculate frequencies of characters
    for char in s:
        if char not in freq_dict:
            freq_dict[char] = 1
        elif char in freq_dict:
            freq_dict[char] += 1
    
    # Determine if string is valid
    frequency_values = list(freq_dict.values())
    is_valid = all(x == frequency_values[0] for x in frequency_values)
    if is_valid:
        return "YES"
    else:
        highest_frequency_character = max(freq_dict, key=freq_dict.get)
        freq_dict[highest_frequency_character] -= 1
        frequency_values = list(freq_dict.values())
        is_valid = all(x == frequency_values[0] for x in frequency_values)
        return "YES" if is_valid else "NO"