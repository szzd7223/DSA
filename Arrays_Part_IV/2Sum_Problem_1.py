def twoSum(nums, target):
        hmap = {}
        for i,v in enumerate(nums):
            if target - v in hmap:
                return [hmap[target-v], i]
            else:
                hmap[v] = i