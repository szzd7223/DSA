def Length_Of_Last_word(s):
    length = 0
    i = len(s) - 1

    while i >= 0 and s[i] == ' ':
        i -= 1
    
    while i >= 0 and s[i].isalpha():
        length += 1
        i -= 1

    return length


print(Length_Of_Last_word("   fly me   to   the moon  "))

print(Length_Of_Last_word("Hello World"))