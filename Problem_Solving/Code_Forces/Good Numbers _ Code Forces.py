"""Good Number (Code_Forces)"""
n, k = [int(x) for x in input().split()]
result = 0
for i in range(0, n):
    _input = input()
    if set(map(int, _input)).issuperset(set(range(0, k+1))):
        result += 1
print(result)
