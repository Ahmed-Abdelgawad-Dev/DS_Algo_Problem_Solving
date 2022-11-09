n, answer = int(input()), 1000000000
directions, vals = [x for x in input()], [int(x) for x in input().split()]
for v in range(n-1):
    if directions[v] == 'R' and directions[v+1] == 'L':
        answer = min(answer, (vals[v+1] - vals[v]) // 2)
print(int('-1') if answer==1000000000 else answer)