magnets_count = int(input())
magnets = []
group = 1
for i in range(magnets_count):
    magnets.append(int(input()))
for j in range(len(magnets[:-1])):
    if magnets[j] != magnets[j+1]:
        group += 1
print(group)
