x = list(map(int, input().split()))
result = 0
for i in range(x[0]):
    vals = list(map(int, input().split()))
    result += vals[1] - vals[0] + 1
print(x[1] - (result % x[1]) if result % x[1] != 0 else result % x[1])
