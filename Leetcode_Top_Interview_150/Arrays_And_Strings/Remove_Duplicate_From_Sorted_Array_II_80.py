def remDuplicatesII(nums):
    k = 0

    for num in nums:
        if k < 2 or num != nums[k-2]:
            nums[k] = num
            k += 1
    
    return k

print(remDuplicatesII([1,1,1,1,2,2,2,3,4]))