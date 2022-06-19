matrix = []
for i in range(5):
    array = map(int, input().split(' '))
    matrix.append(list(array))
answer = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            answer = abs(2-i) + abs(2-j)
print(answer)
