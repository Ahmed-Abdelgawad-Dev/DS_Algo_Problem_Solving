m = []
for _ in range(4):
    m.append(list(input()))

for i in range(3):
    for j in range(3):
        t = m[i][j] + m[i][j+1] + m[i+1][j] + m[i+1][j+1]
        if t.count('#') >= 3 or t.count('.') >= 3:
            print("YES")
            exit()
print("NO")
