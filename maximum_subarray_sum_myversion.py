def maximumSum(a, m):
    # Write your code here
    substrings_of_length_k, sub_array_sum_modulo_m_dict = [], {}
    # Iterate through integer array and generate all substrings
    for i in range(1, len(a)):
        substrings_of_length_k = calculateSubstringsLengthK(a, i)
        for substring in substrings_of_length_k:
            string_of_digits = ''.join(str(val) for val in substring)
            if string_of_digits not in sub_array_sum_modulo_m_dict:
                sub_array_sum_modulo_m_dict[string_of_digits] = sum(substring) % m
            elif string_of_digits in sub_array_sum_modulo_m_dict:
                pass
    
    # Calculate max subarray sum modulo m
    max_sub_array_key = max(sub_array_sum_modulo_m_dict, key=sub_array_sum_modulo_m_dict.get)
    return sub_array_sum_modulo_m_dict[max_sub_array_key]