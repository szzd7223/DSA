def Pascal_Triangle_3(n):
    ans = []
    for i in range(n):
        val = 1
        templist = []
        for j in range(i+1):
            templist.append(val)
            val = val*(i-j)//(j+1)
        
        ans.append(templist)
    
    return ans

print(Pascal_Triangle_3(5))
        
