"""
A - Next Round:
	n>= index{5}=7  -> result => 6 nominees
	n=8       5=7
	|1 |2|3|4|5|6|7|8|
	|10|9|8|7|7|7|5|5|
"""
ent1 = input().split()
n = int(ent1[0])
k = int(ent1[1])
ent2 = input().split()
result = 0
for i in range(0, len(ent2)):
	if int(ent2[i]) >= int(ent2[k-1]) and int(ent2[i]) > 0:
		result += 1
print(result)
