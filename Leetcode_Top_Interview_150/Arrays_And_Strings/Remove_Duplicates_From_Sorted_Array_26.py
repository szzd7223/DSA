def Remove_Duplicates_From_Sorted_Array(nums):
    if not nums:
        return 0
    
    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1

    return k

print(Remove_Duplicates_From_Sorted_Array([1,1,2]))