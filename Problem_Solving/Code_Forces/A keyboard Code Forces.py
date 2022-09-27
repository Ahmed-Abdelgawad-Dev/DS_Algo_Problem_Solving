s = "qwertyuiopasdfghjkl;zxcvbnm,./"
s = [i for i in s]
direction = input().upper()
_input = input()
for i in _input:
	if direction == 'R':
		print(s[s.index(i) - 1], end='')
	if direction == 'L':
		print(s[s.index(i) + 1], end='')
