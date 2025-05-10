def productExceptSelf(nums):
    n = len(nums)

    left = [1]*n
    right = [1]*n

    # Build left array
    for i in range(1,n):
        left[i] = left[i-1] * nums[i-1]
    
    # Build right array
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]

    # Build answer array
    ans = [1]*n

    for i in range(n):
        ans[i] = left[i]*right[i]
    
    return ans


print(productExceptSelf([1,2,3,4]))