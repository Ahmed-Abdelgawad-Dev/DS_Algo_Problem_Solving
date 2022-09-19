import string

print('----------Solution One')
letters = [x for x in string.ascii_lowercase]
x = int(input())
inputs = str(input()).lower()
num = 0
for i in letters:
	if i in inputs:
		num += 1
print('YES') if num == 26 else print('NO')
print()
print('----------Solution Two')
int(input())
letters = list(set(list(input().lower())))
print('YES') if len(letters) == 26 else print('NO')
