import math
x = input().split()
n, k = int(x[0]), int(x[1])
v = math.ceil(n/2)

if k <= v:
    print(2*k - 1)
else:
    print(2*(k - v))
