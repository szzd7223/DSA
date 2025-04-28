def minPlatforms(arr, dep):
    arr.sort()
    dep.sort()

    cnt = 0
    maxcnt  = 0

    i = 0
    j = 0

    while i < len(arr):
        if arr[i] <= dep[j]:
            cnt += 1
            i += 1
        else:
            cnt -= 1
            j += 1
        
        maxcnt = max(maxcnt, cnt)

    return maxcnt