def Next_Permutation(nums):
    # start from second last index
    i = len(nums) - 2

    # find the pivot
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    # find next largest number from pivot
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # swap
        nums[i], nums[j] = nums[j], nums[i]

    # reverse the list after pivot index
    nums [i+1:]= reversed(nums[i+1:])

nums = [1, 4, 6, 5, 3, 2]
print(nums)
Next_Permutation(nums)
print(nums)