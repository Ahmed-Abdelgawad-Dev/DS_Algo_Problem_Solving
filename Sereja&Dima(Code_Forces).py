n = int(input())
numbers = list(map(int, input().split(' ')))
Sereja = Dima = 0
for i in range(n):
    # Sereja first
    if i % 2 == 0:
        # if leftmost >= rightmost
        if numbers[0] >= numbers[-1]:
            # sereja + value of leftmost
            Sereja += numbers.pop(0)
        else:
            # sereja + value of rightmost
            Sereja += numbers.pop()
    # Dima same conditions if i%2 != 0
    else:
        if numbers[0] >= numbers[-1]:
            Dima += numbers.pop(0)
        else:
            Dima += numbers.pop()
print(Sereja, Dima)
