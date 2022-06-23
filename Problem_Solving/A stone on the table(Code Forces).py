stones = int(input())
colors = input().upper()
number=0
for i in range(len(colors)-1):
    if colors[i]==colors[i+1]:
        number+=1
print(number)

