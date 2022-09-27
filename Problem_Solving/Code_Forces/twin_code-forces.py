"""Twin"""
b = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
c = 0
for i in range(b):
	c += a[i]
	if c > sum(a) / 2:
		print(i + 1)
		break
