"""Buy  A SHOVEL - Code Forces"""
n = input().split()
answer = 1
while True:
    if (int(n[0]) * answer) % 10 == 0:
        break
    if ((int(n[0]) * answer) % 10) - int(n[1]) == 0:
        break
    answer += 1
print(answer)
