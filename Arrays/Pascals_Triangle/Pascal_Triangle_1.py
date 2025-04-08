def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

def Pascal_Trinagle_1(r,c):
    n = r-1
    r = c-1
    res = 1
    for i in range(0,r):
        res = res * (n-i)
        res = res// (i + 1)

    return res

print(Pascal_Trinagle_1(5,3))