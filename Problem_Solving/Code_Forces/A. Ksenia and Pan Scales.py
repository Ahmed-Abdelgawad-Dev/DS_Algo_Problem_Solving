"""A. Ksenia and Pan Scales"""
left, right = input().split('|')
for i in input():
    if len(left) < len(right):
        left += i
    else:
        right += i
    print(f'{left}|{right}' if len(left) == len(right) else 'Impossible')
