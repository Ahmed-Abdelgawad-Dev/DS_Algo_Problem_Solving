n, x = map(int, input().split())
total = int(x)
kid = 0
for line in range(n):
    val = input().split()
    if val[0] == '+':
        total += int(val[1])

    if val[0] == '-':
        if total - int(val[1]) >= 0:
            total -= int(val[1])
        else:
            kid += 1
print(total, kid)
