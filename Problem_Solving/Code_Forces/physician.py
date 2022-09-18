x, y, z = 0, 0, 0
for i in range(int(input())):
	val = list(map(int, input().split()))
	x += val[0]
	y += val[1]
	z += val[2]
if x == 0 and y == 0 and z == 0:
	print('YES')
else:
	print('NO')
