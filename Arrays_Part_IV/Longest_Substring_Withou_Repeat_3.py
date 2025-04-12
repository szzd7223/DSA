def Longest_Substring_Without_Repeat(s):
    l = 0
    r = 0
    maxlen = 0
    hashmap = {chr(i): -1 for i in range(256)}

    while r < len(s):
        if hashmap[s[r]] != -1:
            if hashmap[s[r]] >= l:
                l = hashmap[s[r]] + 1
        
        hashmap[s[r]] = r

        maxlen = max(maxlen, r-l+1)

        r += 1

    return maxlen


print(Longest_Substring_Without_Repeat("abcabcddd"))