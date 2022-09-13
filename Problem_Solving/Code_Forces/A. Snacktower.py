n = int(input())
sizes = list(map(str, input().split()))

que = []
for i in range(len(sizes)):
	if sizes[i] == max(sizes[i:]):
		if len(que) >= 1:
			if sizes[i] not in que:
				que.append(sizes[i])
				print(*que[::-1], sep=' ')
				que.clear()

		else:
			print(sizes[i])
	else:
		que.append(sizes[i])
		print()
