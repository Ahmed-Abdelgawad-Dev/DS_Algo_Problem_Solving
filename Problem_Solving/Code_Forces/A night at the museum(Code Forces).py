A = 'a'
root = 0
for c in input():
    temp = abs(ord(c) - ord(A))
    root += temp if temp <= 13 else (26-temp)
    init = c
print(root)
