n = int(input())
v = list(map(int, input().split()))
v = sorted(v)
stewards = 0
for i in v:
	if i > v[0] and i < v[-1]:
		stewards += 1
print(stewards)

