def Valid_Parenthesis(string):
    stack = []
    hashmap = {"(":")", "{":"}", "[":"]"}

    for char in string:
        if char in hashmap:
            stack.append(hashmap[char])
        elif len(stack) == 0 or stack.pop() != char:
            return False
        
    if len(stack) == 0:
        return True
    else:
        return False
    

print(Valid_Parenthesis("()"))
print(Valid_Parenthesis("()[]{}"))
print(Valid_Parenthesis(("()]")))