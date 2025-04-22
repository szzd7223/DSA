def Palindrome(x):
    rev = 0
    i = x

    while i > 0:
        digit = i % 10
        rev = rev*10 + digit
        i = i // 10

    if rev == x:
        return True
    

    return False


print(Palindrome(121))
print(Palindrome(234))