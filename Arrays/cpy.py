from collections import defaultdict

freq = defaultdict(int)
print(freq['a'])
freq['a'] = 1
print(freq['a'])

freq['a'] -= 1  # Now freq['a'] becomes 0

if freq['a'] == 0:
    del freq['a']  # Deletes 'a' from freq

print(freq['a'])  # KeyError: 'a'
