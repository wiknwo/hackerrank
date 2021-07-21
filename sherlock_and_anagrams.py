def calculateSubstringsLengthK(s, k):
    substrings, index = [], 0
    while index + k <= len(s):
        substrings.append(s[index:index + k])
        index += 1
    return substrings

def sherlockAndAnagrams(s):
    substrings_of_length_k, anagarams_dict = [], {}
    anagrammatic_pairs_count = 0
    
    # Write your code here
    for i in range(1, len(s)):
        substrings_of_length_k = calculateSubstringsLengthK(s, i)
        for substring in substrings_of_length_k:
            sortedstring = ''.join(sorted(substring))
            if sortedstring not in anagarams_dict:
                anagarams_dict[sortedstring] = 1
            elif sortedstring in anagarams_dict:
                anagarams_dict[sortedstring] += 1
    
    # Calculate pairs of anagrams
    for key, value in anagarams_dict.items():
        anagrammatic_pairs_count += (value * (value - 1)) // 2
    
    return anagrammatic_pairs_count