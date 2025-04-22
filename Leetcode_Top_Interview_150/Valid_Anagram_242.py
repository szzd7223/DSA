def isAnagram(s, t) :
        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        # Subtract counts using characters in t
        for char in t:
            if char in count:
                count[char] -= 1
                if count[char] < 0:
                    return False
            else:
                return False

        return True


print(isAnagram("abcd", "bdac"))