def myPow(x,n):
    ans = 1
    nn = abs(n)

    while nn > 0:
        if nn % 2 == 1:
            ans = ans*x
            nn -= 1
        else:
            x = x*x
            nn = nn//2
        
    if n < 0:
        ans = 1 / ans
    
    return ans

print(myPow(2,10))