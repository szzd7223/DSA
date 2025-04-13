def Sqrt(x):
    if x < 2:
        return x # because square root of non negative number less than 2 is that number itself (1*1 = 1, 0*0 = 0)
    
    l = 1 # because integer part of square root of non negative integer greater than 2 would be more than or equal to 1
    r = x//2 # because integer part of square root of non negative integer greater than 2 less than or equal to x//2

    while l <= r:
        mid = (l+r)//2

        if mid*mid == x:
            return mid
        
        elif mid*mid < x:
            l = mid+1
        
        elif mid*mid > x:
            r = mid-1
        
    return r

print(Sqrt(17))