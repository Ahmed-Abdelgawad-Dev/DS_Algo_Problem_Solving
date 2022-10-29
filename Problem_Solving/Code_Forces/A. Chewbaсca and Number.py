"A. Chewbaсca and Number"
x = str(input())
l = []
for i in x:
    if (9 - int(i)) == 0 or (9 - int(i)) > int(i):
        l.append(i)
    else:
        l.append(str(9-int(i)))
print(''.join(str(j) for j in l))

