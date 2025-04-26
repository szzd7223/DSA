def threeSum(nums):
    n = len(nums)
    res = []
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i+1
        r = n-1

        while l < r:
            total = nums[i] + nums[l] + nums[r]

            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])

                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1

                l += 1
                r -= 1
        
    return res


print(threeSum([-1,0,1,2,-1,-4]))