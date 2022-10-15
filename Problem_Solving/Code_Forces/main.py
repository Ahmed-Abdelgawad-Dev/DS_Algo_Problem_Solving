"""A. Mountain Scenery"""
n, k = map(int, input().split())
vals = list(map(int, input().split()))

for i in range(1, len(vals), 2):
    if k > 0 and vals[i] -1 > vals[i-1] and vals[i] -1 > vals[i+1]:
        vals[i] -= 1
        k -= 1
        if k == 0:
            break
if "__main__" == __name__:
    print(' '.join(map(str,vals)))