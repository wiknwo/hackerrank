def reverseShuffleMerge(s):
    # Write your code here
    character_count, required_characters, answer = {}, {}, []
    index, reversedstrings = 0, s[::-1]
    
    # Count characters in s
    for char in s:
        if char not in character_count:
            character_count[char] = 1
        elif char in character_count:
            character_count[char] += 1

    # Calculate required characters to form string A
    for char in character_count:
        required_characters[char] = character_count[char] / 2
    
    # Iterate through characters in s in reverse order and form string A
    while len(answer) < len(s) / 2:
        lexicographically_smallest_character_index = -1
        while True:
            char = reversedstrings[index]
            if required_characters[char] > 0 and (lexicographically_smallest_character_index < 0 or char < reversedstrings[lexicographically_smallest_character_index]):
                lexicographically_smallest_character_index = index
            character_count[char] -= 1
            if character_count[char] < required_characters[char]:
                break
            index += 1
        for j in range(lexicographically_smallest_character_index + 1, index + 1):
            character_count[reversedstrings[j]] += 1
        required_characters[reversedstrings[lexicographically_smallest_character_index]] -= 1
        answer.append(reversedstrings[lexicographically_smallest_character_index])
        index = lexicographically_smallest_character_index + 1
    return ''.join(answer)