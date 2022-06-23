n = input()
free = untreated = 0
for x in map(int, input().split()):
    free += x
    if free < 0:
        free = 0
        untreated += 1
print(untreated)
