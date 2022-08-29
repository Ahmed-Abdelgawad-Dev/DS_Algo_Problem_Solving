"""
A. Presents

4
# 1 2 3 4
  2 3 4 1   
-------
  4 1 2 3
"""
n = int(input())
friends = [int(x) for x in input().split()]
obj = {}
for i in range(n):
    obj[friends[i]] = i+1

for key in sorted(obj.keys()):
    print(obj[key], end=' ')