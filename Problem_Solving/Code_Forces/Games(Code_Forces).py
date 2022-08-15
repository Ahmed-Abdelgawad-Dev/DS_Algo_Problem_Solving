teams = int(input())
counter = 0
arr, arr2 = [], []
for i in range(teams):
    matches = list(map(int, input().split()))
    arr.append(matches[0])
    arr2.append(matches[1])
# One loop only i/of 2
for x in arr:
    if x in arr2:
        counter += arr2.count(x)
print(counter)
