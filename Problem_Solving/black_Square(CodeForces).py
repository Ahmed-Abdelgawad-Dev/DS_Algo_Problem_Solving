lost_calories_per_strip = list(map(int, input().split(' ')))
strip_touch_sequence = input()
answer = sum(lost_calories_per_strip[int(i) - 1] for i in strip_touch_sequence)
print(answer)
