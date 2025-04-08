def Pascal_Triangle_2(r):
    row = []
    val = 1

    for i in range(r+1):
        row.append(val)
        val = val*(r-i)//(i+1)
    
    return row

print(Pascal_Triangle_2(5))