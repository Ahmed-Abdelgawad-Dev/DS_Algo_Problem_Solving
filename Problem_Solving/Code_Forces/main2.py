N = int(input())
Ds = [x for x in input()]
Cs = [int(x) for x in input().split()]
Ans = int(1e9)
for i in range(N-1):
    if Ds[i] == 'R' and Ds[i+1] == 'L':
        Ans = min(Ans, (Cs[i+1] - Cs[i]) // 2)
if Ans == int(1e9):
    print(-1)
else:
    print(Ans)
