int(input())
letters = list(set(list(input().lower())))
print('YES') if len(letters) == 26 else print('NO')
