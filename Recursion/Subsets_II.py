def subsetWithDuplicates(nums):
    res = []

    nums.sort()

    subset = []

    def dfs(i):
        if i > len(nums):
            res.append(subset.copy())
            return
        
        # Decision to include nums[i]
        subset.append(nums[i])
        dfs(i+1) # Go 1 level deeper

        # Decision to NOT include nums[i]
        subset.pop
        # Skip duplicates
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        dfs(i+1) # Go 1 level deeper

    dfs(0)

    return res