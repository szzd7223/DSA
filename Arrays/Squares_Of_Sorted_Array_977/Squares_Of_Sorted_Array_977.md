# Squares of a Sorted Array

## Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, return an array of the squares of each number **sorted** in non-decreasing order.

### Example 1:

**Input:**
```python
nums = [-4,-1,0,3,10]
```
**Output:**
```python
[0,1,9,16,100]
```

### Example 2:

**Input:**
```python
nums = [-7,-3,2,3,11]
```
**Output:**
```python
[4,9,9,49,121]
```

## Constraints:

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in **non-decreasing order**.

## Approach

### Two-Pointer Approach

1. **Use Two Pointers:** Start from both ends of the array (`l = 0`, `r = len(nums) - 1`).
2. **Compare Absolute Values:** Square both elements and place the larger square at the end of the result array.
3. **Move Pointers:** Move the left or right pointer inward based on the comparison.
4. **Repeat Until Done:** Fill the result array from back to front.

## Time and Space Complexity

- **Time Complexity:** `O(N)`, where `N` is the length of `nums`.
- **Space Complexity:** `O(N)`, since we store the result separately.

## Conclusion

The two-pointer technique is an efficient way to handle this problem, avoiding unnecessary sorting and achieving `O(N)` complexity.

