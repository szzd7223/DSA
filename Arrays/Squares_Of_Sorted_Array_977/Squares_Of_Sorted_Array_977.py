def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)

        nums = [x ** 2 for x in nums]
        
        l = 0
        r = len(nums) - 1

        for pos in range(len(nums)-1, -1, -1):
            if nums[l] > nums[r]:
                result[pos] = nums[l]
                l += 1
            else:
                result[pos] = nums[r]
                r -= 1
        
        return result