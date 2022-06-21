words = str(input().split(' '))
capital, small = [], []
for i in words[2:-2]:
    if i.islower():
        small.append(i)
    if i.isupper():
        capital.append(i)
if len(capital) > len(small):
    print(words[2:-2].upper(), end='')
else:
    print(words[2:-2].lower(), end='')
