n = int(input())
cities = list(map(int, input().split()))
result = []
for i in range(n):
	# Maximum value in all cases except 2 cases ({first & last} elements of array)
	maxi = max(abs(cities[i] - cities[0]), abs(cities[i] - cities[-1]))
	# Exception One -> i==First index of array
	if i == 0:
		mini = abs(cities[i] - cities[1])
	# Exception Two -> i==last index of array
	if i == n - 1:
		mini = abs(cities[i] - cities[-2])
	else:
		# Minimum value in all cases except 2 cases ({first & last} elements of array)
		mini = min(abs(cities[i] - cities[i - 1]), abs(cities[i] - cities[i + 1]))
	result.append([mini, maxi])
for x in result:
	print(*x)
