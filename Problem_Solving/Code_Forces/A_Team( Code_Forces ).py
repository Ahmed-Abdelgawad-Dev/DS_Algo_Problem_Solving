problems = int(input())
result = 0
for i in range(problems):
    Petya, Vasya, Tonya = map(int, input().split())
    if int(Petya+Vasya+Tonya) >= 2:
        result += 1
print(result)
