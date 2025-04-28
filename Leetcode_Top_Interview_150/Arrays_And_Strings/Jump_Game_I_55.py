def jumpGame(nums):
    maxReach = 0
    
    for i in range(len(nums)):
        if i > maxReach:
            return False
        
        maxIndex = i + nums[i]
        maxReach = max(maxIndex, maxReach)

    return True


print(jumpGame([2,3,1,1,4]))
print(jumpGame([3,2,1,0,4]))