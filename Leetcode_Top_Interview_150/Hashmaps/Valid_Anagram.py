def validAnagram(s, t):
    if len(s) != len(t):
        return False
    
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char in t:
        if char in count:
            count[char] -= 1
            if count[char] < 0:
                return False
        else:
            return False
        
    return True


print(validAnagram('anagram', 'agamarn'))