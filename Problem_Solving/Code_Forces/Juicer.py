n, b, d = map(int, input().split())
oranges = list(map(int, input().split()))

count, total = 0, 0

for orange in oranges:
    if orange <= b:
        total += orange
        if total > d:
            count+=1
            total=0
print(count)