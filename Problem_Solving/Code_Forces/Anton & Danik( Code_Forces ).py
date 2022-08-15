matche_nums = int(input())
strings = list(input())
Anton, Danik = 0, 0
if (1 <= matche_nums and matche_nums <= 100000):
    for i in range(len(strings)):
        if strings[i] == 'D':
            Danik += 1
        else:
            Anton += 1
    if Anton > Danik:
        print("Anton")
    elif Danik > Anton:
        print("Danik")
    else:
        print("Friendship")
