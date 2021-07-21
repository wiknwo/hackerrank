def sockMerchant(n, ar):
    # Write your code here
    sock_dict = {} # Dictionary to keep track of pairs of socks
    pair_count = 0
    
    # Iterate over socks and add them to the sock_dict
    for sock in ar:
        if sock not in sock_dict:
            sock_dict[sock] = 1
        elif sock in sock_dict:
            sock_dict[sock] += 1
    
    for key in sock_dict:
        number_of_socks = sock_dict[key]
        while number_of_socks >= 2:
            number_of_socks -= 2
            pair_count += 1
    
    return pair_count