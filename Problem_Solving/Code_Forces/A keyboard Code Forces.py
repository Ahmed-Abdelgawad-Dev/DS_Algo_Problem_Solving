s = "qwertyuiopasdfghjkl;zxcvbnm,./"
string = [i for i in s]
direction = input().upper()       #"R"
_input = input()                  #"s;;upimrrfod;pbr"
for i in _input:
	if i in string:
		if direction == 'R':
			pos = string.index(i) - 1
			print(string[pos], end='')
		if direction == 'L':
			pos = string.index(i) + 1
			print(string[pos], end='')