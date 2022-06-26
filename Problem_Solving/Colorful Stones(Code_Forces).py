one = input()
two = input()
position = 1
for i in two:
    if i == one[position-1]:
        position += 1
print(position)
