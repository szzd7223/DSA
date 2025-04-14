def Find_The_Duplicate_Number(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast:
            break

    slow = nums[0]

    while slow != fast:
        fast = nums[fast]
        slow = nums[slow]

    return slow


print(Find_The_Duplicate_Number([1,2,3,7,4,4,6,5]))