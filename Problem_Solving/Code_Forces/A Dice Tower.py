n = int(input())
top = int(input())
l = [top, 7 - top]
flag = True
for i in range(n):
	x = input().split()
	if int(x[0]) in l or int(x[1]) in l:
		print('NO')
		flag = False
		break
	else:
		flag = True
if flag:
	print('YES')
