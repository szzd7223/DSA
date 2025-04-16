# Better Aproach O(n) + O(log(n))
 
def searchMatrix(matrix, target):
        # Binary Search on 2D Matrix
        def bs(arr, k):
            low = 0
            high = n-1

            while low <= high:
                mid = (low+high)//2

                if arr[mid] == target:
                    return True
                elif arr[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                for j in range(n):
                    if bs(matrix[i], target) == True:
                        return True
                    else:
                        return False

        return False

# Optimal Approach using binary search O(log(n))

def searchMatrix(matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        
        low = 0
        high = (m*n) - 1

        while low <= high:
            mid = (low+high)//2
            r = mid // n
            c = mid % n

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] >= target:
                high = mid - 1
            else:
                low = mid + 1
            
        return False