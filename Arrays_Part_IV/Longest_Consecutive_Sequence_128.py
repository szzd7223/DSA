def Longest_Consecutive_Sequence(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current = num
            streak = 1

            while current + 1 in nums_set:
                current += 1
                streak += 1
            
            longest =  max(longest, streak)

    return longest


print(Longest_Consecutive_Sequence([2,4,5,1,6,7,8]))