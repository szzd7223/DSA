def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer until it points to an alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer until it points to an alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (in lowercase)
        if s[left].lower() != s[right].lower():
            return False
        
        # Move both pointers inward
        left += 1
        right -= 1

    return True
