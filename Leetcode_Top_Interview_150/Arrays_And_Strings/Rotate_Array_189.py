def rotateArray(nums, k):
    n = len(nums)

    k = k % n

    def rev(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    rev(nums, 0, n-1)

    rev(nums, 0, k-1)

    rev(nums, k, n-1)

    return nums


print(rotateArray([1,2,3,4,5,6,7], 3))