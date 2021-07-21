'''Hash Tables: Ransom Note

    Harold is a kidnapper who wrote a ransom note, but now he 
    is worried it will be traced back to him through his 
    handwriting. He found a magazine and wants to know if he can 
    cut out whole words from it and use them to create an 
    untraceable replica of his ransom note. The words in his note 
    are case-sensitive and he must use only whole words available 
    in the magazine. He cannot use substrings or concatenation to 
    create the words he needs.

    Given the words in the magazine and the words in the ransom 
    note, print Yes if he can replicate his ransom note exactly 
    using whole words from the magazine; otherwise, print No.

    William Ikenna-Nwosu (wiknwo)
'''
def checkMagazine(magazine, note):
    # Write your code here
    magazine_dict, constructedstr = {}, []
    
    # Iterate through magazine and count number
    # number of occurences of words
    for word in magazine:
        if word not in magazine_dict:
            magazine_dict[word] = 1
        elif word in magazine_dict:
            magazine_dict[word] += 1
    
    for word in note:
        if word in magazine_dict:
            constructedstr.append(word)
            magazine_dict[word] = magazine_dict[word] - 1
            if magazine_dict[word] == 0:
                del magazine_dict[word]
        elif word not in magazine_dict:
            print('No')
            return
            
    if constructedstr == note:
        print('Yes')
        return    