def Majority_Element(arr):
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


print(Majority_Element([2,2,2,3,4,4,5,2,4,5,4,4,2,2,2]))