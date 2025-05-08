def sumOfDigits(num):
    if num == 0:
        return 0

    else:
        return num%10 + sumOfDigits(num//10)

num = 123456
print(sumOfDigits(num))