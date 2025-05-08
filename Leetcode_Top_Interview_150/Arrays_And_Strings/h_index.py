def h_index(citations):
    n = len(citations)
    for i in range(n):
        if citations[i] >= n-i:
            return n-i
    return 0
    

print(h_index([3,0,6,1,5]))